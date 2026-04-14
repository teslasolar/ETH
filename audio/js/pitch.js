// dominant-pitch estimate · argmax over the voice band
// good enough for speech/music peak · not YIN-quality
function updatePitch() {
  if (!S.analyser) return;
  const lo = binForHz(60);
  const hi = binForHz(1500);
  let maxBin = lo, maxVal = 0;
  for (let i = lo; i <= hi; i++) {
    if (S.freqData[i] > maxVal) { maxVal = S.freqData[i]; maxBin = i; }
  }
  if (maxVal < 40) {
    document.getElementById('pitch-val').textContent = '—';
    return;
  }
  const nyquist = S.ac.sampleRate / 2;
  const hz = maxBin / S.analyser.frequencyBinCount * nyquist;
  document.getElementById('pitch-val').textContent =
    hz.toFixed(0) + ' Hz · ' + hzToNote(hz);
}

// rough Hz → note name (equal-tempered, A4=440)
function hzToNote(hz) {
  const names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  const n = Math.round(12 * Math.log2(hz / 440)) + 57;  // offset to C0
  return names[((n % 12) + 12) % 12] + Math.floor(n / 12);
}
