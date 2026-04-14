// load up to 50 repos for a user → forest of trees
async function loadForest(username) {
  const status = document.getElementById('load-status');
  const overlay = document.getElementById('loading');
  status.textContent = `Loading ${username}...`;
  overlay.classList.remove('hidden');

  state.trees.forEach(t => scene.remove(t));
  state.trees = [];
  state.clickables = [];

  try {
    const res = await gh(
      `https://api.github.com/users/${username}/repos?per_page=100&sort=pushed`
    );
    if (!res.ok) throw new Error('User not found');
    const repos = await res.json();
    if (!repos.length) throw new Error('No repos');

    status.textContent = `Growing ${repos.length} trees...`;
    const batch = repos.slice(0, 50);
    let loaded = 0;

    for (let i = 0; i < batch.length; i++) {
      const repo = batch[i];
      const pos = getForestPosition(i, batch.length);
      const sizeFactor = Math.sqrt(repo.size || 100) * 0.02;
      const height = Math.max(6, Math.min(30, 8 + sizeFactor));
      const radius = Math.max(0.4, Math.min(2, 0.5 + sizeFactor * 0.1));

      try {
        let data = null;
        for (const branch of ['main', 'master']) {
          const r = await gh(
            `https://api.github.com/repos/${username}/${repo.name}`
            + `/git/trees/${branch}?recursive=1`
          );
          if (r.ok) { data = await r.json(); break; }
        }
        if (data?.tree) {
          const files = data.tree
            .filter(f => f.type === 'blob'
              && !f.path.includes('node_modules')
              && !f.path.startsWith('.'))
            .slice(0, 50)
            .map(f => ({
              path: f.path,
              name: f.path.split('/').pop(),
              size: f.size || 100,
            }));
          if (files.length) {
            createTree(pos.x, pos.z, height, radius, files,
              `${username}/${repo.name}`);
            loaded++;
          }
        }
      } catch (e) { /* skip failed repo */ }

      status.textContent = `Growing... ${loaded}/${i + 1}`;
      if (i % 5 === 4) await new Promise(r => setTimeout(r, 100));
    }

    updateUI(username, loaded);
    overlay.classList.add('hidden');
  } catch (e) {
    status.textContent = `Error: ${e.message}`;
    setTimeout(() => overlay.classList.add('hidden'), 2000);
  }
}
