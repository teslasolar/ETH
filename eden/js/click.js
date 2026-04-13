// click on a flower → open the file panel
function onClick(e) {
  if (isDragging) return;

  mouse.x = (e.clientX / innerWidth) * 2 - 1;
  mouse.y = -(e.clientY / innerHeight) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);

  for (const flower of state.clickables) {
    const intersects = raycaster.intersectObject(flower, true);
    if (intersects.length > 0) {
      openFilePanel(flower.userData);
      return;
    }
  }
}
