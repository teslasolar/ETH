// Fibonacci-spiral placement · natural forest distribution
function getForestPosition(index, total) {
  const angle = index * goldenAngle;
  const r = 8 + Math.sqrt(index) * 10;
  const wobble = Math.sin(index * 0.7) * 3;
  return {
    x: Math.cos(angle) * r + wobble,
    z: Math.sin(angle) * r + wobble * 0.5,
  };
}
