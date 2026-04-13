// oriented cylinder · start → end
function createBranch(start, end, radius) {
  const dir = new THREE.Vector3().subVectors(end, start);
  const len = dir.length();
  const geo = new THREE.CylinderGeometry(
    radius * 0.3, radius, len, 6
  );
  const mesh = new THREE.Mesh(
    geo,
    new THREE.MeshPhongMaterial({ color: 0x5a4030 })
  );

  mesh.position.copy(start).add(end).multiplyScalar(0.5);
  mesh.quaternion.setFromUnitVectors(
    new THREE.Vector3(0, 1, 0),
    dir.normalize()
  );

  return mesh;
}
