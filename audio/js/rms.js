// RMS volume from the time-domain buffer · normalized 0..1
function updateRMS() {
  if (!S.analyser) return;
  S.analyser.getByteTimeDomainData(S.timeData);
  let sum = 0;
  for (let i = 0; i < S.timeData.length; i++) {
    // byte values center around 128; subtract to get ±
    const v = (S.timeData[i] - 128) / 128;
    sum += v * v;
  }
  const rms = Math.sqrt(sum / S.timeData.length);
  const pct = Math.min(1, rms * 3) * 100;     // 3× gain for headroom
  document.getElementById('rms-bar').style.width = pct.toFixed(1) + '%';
  document.getElementById('rms-val').textContent =
    (20 * Math.log10(Math.max(1e-6, rms))).toFixed(1) + ' dB';
}
