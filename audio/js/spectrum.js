// log-frequency spectrum · colored by ring band
function drawSpectrum() {
  const cv = document.getElementById('spectrum');
  const ctx = cv.getContext('2d');
  const W = cv.width, H = cv.height;
  ctx.fillStyle = '#050308';
  ctx.fillRect(0, 0, W, H);

  if (!S.analyser) {
    ctx.fillStyle = '#fff8e7'; ctx.globalAlpha = 0.3;
    ctx.font = '11px Monaco,Menlo,monospace';
    ctx.fillText('no stream · click Capture tab audio', 12, 20);
    ctx.globalAlpha = 1;
    return;
  }

  // log scale: 20 Hz → nyquist
  const nyquist = S.ac.sampleRate / 2;
  const loHz = 20, hiHz = Math.min(20000, nyquist);
  const logLo = Math.log(loHz), logHi = Math.log(hiHz);
  const bins = S.analyser.frequencyBinCount;
  const barW = 2;

  for (let x = 0; x < W; x += barW) {
    const f = Math.exp(logLo + (x / W) * (logHi - logLo));
    const bin = Math.round(f / nyquist * bins);
    const v = S.freqData[bin] / 255;
    const h = v * H;

    // color by which ring band the frequency falls in
    let col = '#888';
    for (const b of RING_BANDS) {
      if (f >= b.lo && f < b.hi) { col = b.color; break; }
    }
    ctx.fillStyle = col;
    ctx.fillRect(x, H - h, barW - 0.5, h);
  }
}
