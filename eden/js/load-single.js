// load one repo → single central tree, deeper detail
async function loadSingleRepo(repoPath) {
  const status = document.getElementById('load-status');
  const overlay = document.getElementById('loading');
  status.textContent = `Loading ${repoPath}...`;
  overlay.classList.remove('hidden');

  state.trees.forEach(t => scene.remove(t));
  state.trees = [];
  state.clickables = [];
  state.currentRepo = repoPath;

  try {
    let data = null;
    for (const branch of ['main', 'master']) {
      const res = await fetch(
        `https://api.github.com/repos/${repoPath}`
        + `/git/trees/${branch}?recursive=1`
      );
      if (res.ok) { data = await res.json(); break; }
    }
    if (!data?.tree) throw new Error('Could not load repo');

    const files = data.tree
      .filter(f => f.type === 'blob'
        && !f.path.includes('node_modules')
        && !f.path.startsWith('.'))
      .slice(0, 200)
      .map(f => ({
        path: f.path,
        name: f.path.split('/').pop(),
        size: f.size || 100,
      }));

    const height = Math.min(40, 15 + files.length * 0.1);
    const radius = Math.min(3, 1 + files.length * 0.005);

    createTree(0, 0, height, radius, files, repoPath);
    updateUI(repoPath, 1, files.length);
    overlay.classList.add('hidden');
  } catch (e) {
    status.textContent = `Error: ${e.message}`;
    setTimeout(() => overlay.classList.add('hidden'), 2000);
  }
}
