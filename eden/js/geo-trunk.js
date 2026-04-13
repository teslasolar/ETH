// tapered cylinder, base-to-top
function createTrunk(height, radius) {
  const geo = new THREE.CylinderGeometry(
    radius * 0.4, radius, height, 8
  );
  geo.translate(0, height / 2, 0);
  return new THREE.Mesh(
    geo,
    new THREE.MeshPhongMaterial({ color: 0x4a3020 })
  );
}
