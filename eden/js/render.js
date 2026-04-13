// animate loop · camera orbit · gentle sway · render
let time = 0;

function animate() {
  requestAnimationFrame(animate);
  time++;

  camera.position.set(
    Math.sin(camAngle) * Math.cos(camPitch) * camDist,
    Math.sin(camPitch) * camDist + 10,
    Math.cos(camAngle) * Math.cos(camPitch) * camDist
  );
  camera.lookAt(0, 8, 0);

  // gentle sway on every tree
  state.trees.forEach((tree, i) => {
    tree.rotation.z = Math.sin(time * 0.001 + i) * 0.01;
  });

  renderer.render(scene, camera);
}

window.onresize = () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
};

// Init
document.getElementById('loading').classList.add('hidden');
animate();
