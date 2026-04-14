// build the Web Audio graph once a stream is captured
function initAnalyser(stream) {
  S.ac = new (window.AudioContext || window.webkitAudioContext)();
  S.source = S.ac.createMediaStreamSource(stream);
  S.analyser = S.ac.createAnalyser();
  S.analyser.fftSize = FFT_SIZE;
  S.analyser.smoothingTimeConstant = SMOOTHING;
  S.source.connect(S.analyser);
  // intentionally NOT connecting to destination — we don't want
  // to re-echo the tab audio into the user's output
  S.freqData = new Uint8Array(S.analyser.frequencyBinCount);
  S.timeData = new Uint8Array(S.analyser.fftSize);

  S.running = true;
  startLoop();
}

// bin index for a given frequency in Hz
function binForHz(hz) {
  if (!S.ac) return 0;
  const nyquist = S.ac.sampleRate / 2;
  return Math.min(
    S.analyser.frequencyBinCount - 1,
    Math.max(0, Math.round(hz / nyquist * S.analyser.frequencyBinCount))
  );
}

// mean dB magnitude over a frequency range (returns 0..1)
function bandEnergy(loHz, hiHz) {
  const a = binForHz(loHz), b = binForHz(hiHz);
  let sum = 0;
  for (let i = a; i <= b; i++) sum += S.freqData[i];
  const bins = Math.max(1, b - a + 1);
  return (sum / bins) / 255;
}
