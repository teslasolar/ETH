// global mutable state · shared by all modules
const state = {
  trees: [],
  clickables: [],      // every flower · { userData:{file, repo} }
  currentRepo: null,
};
