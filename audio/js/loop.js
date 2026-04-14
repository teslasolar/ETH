// rAF driver · pulls freq data, pushes every meter
function startLoop() {
  function tick() {
    if (!S.running) return;
    S.analyser.getByteFrequencyData(S.freqData);
    drawSpectrum();
    updateBands();
    updateRMS();
    updatePitch();
    updateBPM();
    requestAnimationFrame(tick);
  }
  tick();
}
