// UI element events · input · buttons · keys
document.getElementById('repo-btn').onclick = () => {
  const v = document.getElementById('repo-input').value.trim();
  if (v) loadInput(v);
};
document.getElementById('repo-input').onkeypress = e => {
  if (e.key === 'Enter') document.getElementById('repo-btn').click();
};
document.getElementById('file-close').onclick = () =>
  document.getElementById('file-panel').classList.remove('visible');
document.querySelectorAll('#file-tabs .tab').forEach(
  t => t.onclick = () => switchTab(t.dataset.tab)
);
document.getElementById('ai-send').onclick = () => {
  const v = document.getElementById('ai-input').value.trim();
  if (v) {
    sendToAI(v);
    document.getElementById('ai-input').value = '';
  }
};
document.getElementById('ai-input').onkeypress = e => {
  if (e.key === 'Enter') document.getElementById('ai-send').click();
};
document.querySelectorAll('#ai-actions button').forEach(
  b => b.onclick = () => sendToAI(null, b.dataset.action)
);
document.onkeydown = e => {
  if (e.key === 'Escape')
    document.getElementById('file-panel').classList.remove('visible');
};
