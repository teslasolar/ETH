// dispatch · "owner/repo" → one tree · "owner" → forest
async function loadInput(input) {
  if (input.includes('/')) {
    await loadSingleRepo(input);
  } else {
    await loadForest(input);
  }
}
