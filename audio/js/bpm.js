// cheap BPM estimator · low-band envelope autocorrelation
// sampled roughly 30 Hz by the rAF loop · we look for lags
// between 400 ms (150 bpm) and 1200 ms (50 bpm).
function updateBPM() {
  if (!S.analyser) return;
  const e = bandEnergy(40, 200);              // kick-drum band
  S.bpmBuffer.push(e);
  if (S.bpmBuffer.length > 256) S.bpmBuffer.shift();
  if (S.bpmBuffer.length < 128) return;

  // autocorrelation — lag in "frames", ~60 frames/sec assumed
  const N = S.bpmBuffer.length;
  const lagMin = 30;    // ~500 ms @ 60 fps → 120 bpm
  const lagMax = 72;    // ~1200 ms         → 50 bpm
  let bestLag = 0, bestR = 0;
  for (let lag = lagMin; lag <= lagMax; lag++) {
    let r = 0;
    for (let i = 0; i < N - lag; i++) r += S.bpmBuffer[i] * S.bpmBuffer[i + lag];
    if (r > bestR) { bestR = r; bestLag = lag; }
  }
  if (bestLag > 0) {
    const bpm = Math.round(60 * 60 / bestLag);
    S.bpm = bpm;
    document.getElementById('bpm-val').textContent = bpm + ' bpm';
  }
}
