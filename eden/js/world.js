// sky dome + ground disc
const skyGeo = new THREE.SphereGeometry(400, 32, 24);
const skyMat = new THREE.MeshBasicMaterial({
  color: 0x1a1a2e,
  side: THREE.BackSide,
});
scene.add(new THREE.Mesh(skyGeo, skyMat));

const ground = new THREE.Mesh(
  new THREE.CircleGeometry(300, 64),
  new THREE.MeshPhongMaterial({ color: 0x0d0a08 })
);
ground.rotation.x = -Math.PI / 2;
ground.position.y = -0.1;
scene.add(ground);
