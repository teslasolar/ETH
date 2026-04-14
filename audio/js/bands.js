// 7 ring meters · DOM-built once, filled on each tick
function renderBands() {
  const container = document.getElementById('bands');
  if (container.children.length === 0) {
    RING_BANDS.forEach(b => {
      const div = document.createElement('div');
      div.className = 'band';
      div.dataset.ring = b.ring;
      div.innerHTML = `
        <span class="glyph" style="color:${b.color}">${b.glyph}</span>
        <span>${b.ring} · <span class="range">${b.lo}–${b.hi} Hz</span></span>
        <span class="meter"><span class="fill" id="fill-${b.ring}"></span></span>
        <span class="val" id="val-${b.ring}">—</span>
      `;
      container.appendChild(div);
    });
  }
}

function updateBands() {
  RING_BANDS.forEach(b => {
    const e = S.analyser ? bandEnergy(b.lo, b.hi) : 0;
    // gentle gamma so low-amplitude signals still move the bar
    const pct = Math.min(1, Math.pow(e, 0.6)) * 100;
    const fill = document.getElementById('fill-' + b.ring);
    const val  = document.getElementById('val-' + b.ring);
    if (fill) fill.style.width = pct.toFixed(1) + '%';
    if (val) val.textContent = (pct).toFixed(0) + '%';
  });
}
