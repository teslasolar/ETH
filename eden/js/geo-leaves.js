// clump of 4–7 flattened green spheres at a branch tip
function createLeaves(size) {
  const group = new THREE.Group();
  const count = 4 + Math.floor(Math.random() * 4);

  for (let i = 0; i < count; i++) {
    const leaf = new THREE.Mesh(
      new THREE.SphereGeometry(
        size * (0.4 + Math.random() * 0.4), 6, 4
      ),
      new THREE.MeshPhongMaterial({ color: 0x3a5a30 })
    );
    leaf.scale.y = 0.5;
    leaf.position.set(
      (Math.random() - 0.5) * size * 2,
      (Math.random() - 0.5) * size,
      (Math.random() - 0.5) * size * 2
    );
    group.add(leaf);
  }
  return group;
}
