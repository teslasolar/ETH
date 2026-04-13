// open modal · fetch source · render meta + code + preview
async function openFilePanel(data) {
  const file = data.file;
  const repo = data.repo;
  currentFile = { ...file, repo };
  chatHistory = [];

  const ext = file.name.split('.').pop().toLowerCase();
  const isPreviewable = ['html', 'htm', 'svg'].includes(ext);

  document.getElementById('file-title').textContent = file.path;
  document.getElementById('file-meta').innerHTML =
    `<span>${file.size} B</span><span>${ext.toUpperCase()}</span>`
    + `<span>${repo}</span>`;
  document.getElementById('file-code').textContent = 'Loading...';
  document.getElementById('ai-messages').innerHTML = '';

  document.querySelector('[data-tab="preview"]').style.display =
    isPreviewable ? '' : 'none';
  switchTab('code');
  document.getElementById('file-panel').classList.add('visible');

  try {
    let res = await fetch(
      `https://raw.githubusercontent.com/${repo}/main/${file.path}`
    );
    if (!res.ok) res = await fetch(
      `https://raw.githubusercontent.com/${repo}/master/${file.path}`
    );
    const text = await res.text();
    currentFile.content = text;
    document.getElementById('file-code').textContent =
      text.substring(0, 8000);

    if (isPreviewable) {
      const iframe = document.getElementById('file-iframe');
      iframe.srcdoc = ext === 'svg'
        ? text
        : text.replace('<head>',
            `<head><base href="https://raw.githubusercontent.com/`
            + `${repo}/main/">`);
    }
  } catch (e) {
    document.getElementById('file-code').textContent = '// Could not load';
  }
}

function switchTab(name) {
  document.querySelectorAll('#file-tabs .tab').forEach(
    t => t.classList.toggle('active', t.dataset.tab === name)
  );
  document.querySelectorAll('.tab-content').forEach(
    c => c.classList.toggle('active', c.id === `tab-${name}`)
  );
}
