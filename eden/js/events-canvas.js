// canvas-level input · drag · scroll · click
canvas.addEventListener('mousedown', e => {
  isDragging = true;
  dragStart = { x: e.clientX, y: e.clientY };
});
window.addEventListener('mouseup', () => { isDragging = false; });
window.addEventListener('mousemove', onMouseMove);
canvas.addEventListener('click', onClick);
canvas.addEventListener('wheel', e => {
  camDist = Math.max(15, Math.min(200, camDist + e.deltaY * 0.05));
});
