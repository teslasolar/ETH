// pentagonal flower · amber center + 5 colored petals
function createFlower(size, hue) {
  const group = new THREE.Group();
  const color = new THREE.Color().setHSL(hue, 0.7, 0.6);

  // amber center · clickable hitbox
  const center = new THREE.Mesh(
    new THREE.SphereGeometry(size * 0.35, 8, 8),
    new THREE.MeshPhongMaterial({ color: 0xffdd44 })
  );
  group.add(center);

  // 5 petals on a unit ring
  for (let i = 0; i < 5; i++) {
    const petal = new THREE.Mesh(
      new THREE.SphereGeometry(size * 0.4, 6, 6),
      new THREE.MeshPhongMaterial({
        color, transparent: true, opacity: 0.9
      })
    );
    petal.scale.set(1, 0.3, 0.6);
    const a = (i / 5) * τ;
    petal.position.set(
      Math.cos(a) * size * 0.4, 0, Math.sin(a) * size * 0.4
    );
    petal.rotation.y = -a;
    petal.rotation.z = -0.5;
    group.add(petal);
  }

  return group;
}
