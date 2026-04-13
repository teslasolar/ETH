// populate the bottom-right info panel + counters
function updateUI(name, treeCount, fileCount) {
  document.getElementById('repo-name').textContent = name;
  document.getElementById('tree-count').textContent = treeCount;
  document.getElementById('file-count').textContent =
    fileCount || state.clickables.length;
  document.getElementById('repo-stats').innerHTML =
    `${state.clickables.length} flowers`;
}
