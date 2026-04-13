// three-light setup · ambient + sun + secondary
const ambient = new THREE.AmbientLight(0x404060, 0.6);
scene.add(ambient);

const sun = new THREE.DirectionalLight(0xffeedd, 0.8);
sun.position.set(50, 80, 50);
scene.add(sun);

scene.add(
  new THREE.DirectionalLight(0x8899cc, 0.2)
    .translateX(-30).translateY(40).translateZ(-30)
);
