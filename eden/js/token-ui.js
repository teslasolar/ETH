// small UI for pasting a GitHub Personal Access Token.
// click "🔑" link, paste, saved to localStorage.
function promptForToken() {
  const current = GH.token ? '(token set)' : '';
  const v = prompt(
    'GitHub Personal Access Token (increases API limit from '
    + '60/hr → 5000/hr). Leave blank to remove. ' + current,
    GH.token || ''
  );
  if (v === null) return;
  if (v.trim() === '') {
    localStorage.removeItem('eden_gh_token');
    GH.token = null;
  } else {
    localStorage.setItem('eden_gh_token', v.trim());
    GH.token = v.trim();
  }
  renderRateStatus();
}

// wire the 🔑 icon next to the rate status
document.addEventListener('DOMContentLoaded', () => {
  const link = document.getElementById('token-link');
  if (link) link.addEventListener('click', promptForToken);
});
