// GitHub API wrapper · rate-limit aware · optional PAT
// stored at localStorage.eden_gh_token (no server round-trip)
const GH = {
  remaining: null,
  limit: null,
  resetsAt: null,
  token: localStorage.getItem('eden_gh_token') || null,
};

async function gh(url) {
  const headers = { 'Accept': 'application/vnd.github+json' };
  if (GH.token) headers['Authorization'] = `Bearer ${GH.token}`;

  const res = await fetch(url, { headers });
  // rate-limit headers present on every api.github.com response
  const rem = res.headers.get('X-RateLimit-Remaining');
  const lim = res.headers.get('X-RateLimit-Limit');
  const rst = res.headers.get('X-RateLimit-Reset');
  if (rem !== null) GH.remaining = parseInt(rem, 10);
  if (lim !== null) GH.limit     = parseInt(lim, 10);
  if (rst !== null) GH.resetsAt  = parseInt(rst, 10) * 1000;
  renderRateStatus();

  if (res.status === 403 && GH.remaining === 0) {
    const mins = Math.ceil((GH.resetsAt - Date.now()) / 60000);
    throw new Error(`Rate limit reached. Resets in ${mins} min. `
      + `Paste a GitHub token in the input panel to raise the cap.`);
  }
  return res;
}

function renderRateStatus() {
  const el = document.getElementById('rate-status');
  if (!el || GH.remaining === null) return;
  const mins = GH.resetsAt
    ? Math.max(0, Math.ceil((GH.resetsAt - Date.now()) / 60000))
    : 0;
  const pct = GH.limit ? Math.round(GH.remaining * 100 / GH.limit) : 0;
  const color = pct > 25 ? '#6c6' : pct > 10 ? '#fa4' : '#f44';
  el.innerHTML = `<span style="color:${color}">`
    + `${GH.remaining}/${GH.limit}</span>`
    + ` · resets ${mins}m` + (GH.token ? ' · 🔑' : '');
}
