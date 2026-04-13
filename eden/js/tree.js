// compose one full tree · trunk + branches + leaves + flowers
function createTree(x, z, height, radius, files, repoName) {
  const group = new THREE.Group();
  group.position.set(x, 0, z);
  group.add(createTrunk(height, radius));

  const branchCount = Math.min(12, 4 + Math.floor(files.length / 5));
  let fileIdx = 0;

  for (let i = 0; i < branchCount; i++) {
    const angle = i * goldenAngle;
    const h = height * (0.25 + (i / branchCount) * 0.55);
    const len = 2 + Math.random() * (height * 0.3);

    const start = new THREE.Vector3(
      Math.cos(angle) * radius * 0.3, h, Math.sin(angle) * radius * 0.3
    );
    const end = new THREE.Vector3(
      Math.cos(angle) * (radius + len),
      h + len * 0.25,
      Math.sin(angle) * (radius + len)
    );

    group.add(createBranch(start, end, 0.15));
    const leaves = createLeaves(1 + Math.random());
    leaves.position.copy(end);
    group.add(leaves);

    const flowersOnBranch = Math.min(
      4,
      Math.ceil((files.length - fileIdx) / (branchCount - i))
    );
    for (let j = 0; j < flowersOnBranch && fileIdx < files.length; j++) {
      const file = files[fileIdx++];
      const t = 0.25 + (j / flowersOnBranch) * 0.65;
      const pos = start.clone().lerp(end, t);
      pos.x += (Math.random() - 0.5) * 0.8;
      pos.y += (Math.random() - 0.5) * 0.5;
      pos.z += (Math.random() - 0.5) * 0.8;

      const hue = getHueForFile(file.name);
      const size = 0.3 + Math.min(0.7, (file.size || 100) / 5000);
      const flower = createFlower(size, hue);
      flower.position.copy(pos);
      flower.userData = { file, repo: repoName };
      group.add(flower);
      state.clickables.push(flower);
    }
  }

  scene.add(group);
  state.trees.push(group);
  return group;
}
