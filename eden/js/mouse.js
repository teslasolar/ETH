// hover · drag · raycast flowers · show tooltip
function onMouseMove(e) {
  if (isDragging) {
    const dx = e.clientX - dragStart.x;
    const dy = e.clientY - dragStart.y;
    camAngle += dx * 0.005;
    camPitch = Math.max(0.1, Math.min(1.3, camPitch + dy * 0.003));
    dragStart.x = e.clientX;
    dragStart.y = e.clientY;
    tooltip.classList.remove('visible');
    return;
  }

  mouse.x = (e.clientX / innerWidth) * 2 - 1;
  mouse.y = -(e.clientY / innerHeight) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);

  let hit = null;
  for (const flower of state.clickables) {
    const intersects = raycaster.intersectObject(flower, true);
    if (intersects.length > 0) { hit = flower; break; }
  }

  if (hit) {
    canvas.style.cursor = 'pointer';
    const data = hit.userData;
    document.getElementById('tooltip-path').textContent = data.file.path;
    document.getElementById('tooltip-meta').innerHTML =
      `${data.file.size} bytes<br>`
      + `<span style="color:#ffd700">${data.repo}</span>`;
    tooltip.style.left = (e.clientX + 15) + 'px';
    tooltip.style.top = (e.clientY + 15) + 'px';
    tooltip.classList.add('visible');
  } else {
    canvas.style.cursor = 'default';
    tooltip.classList.remove('visible');
  }
}
