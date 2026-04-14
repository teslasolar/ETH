// wire UI events · render the static band list on load
document.addEventListener('DOMContentLoaded', () => {
  renderBands();
  drawSpectrum();  // draws the "no stream" hint

  document.getElementById('load-btn')
    .addEventListener('click', loadVideo);
  document.getElementById('yt-url')
    .addEventListener('keypress', e => {
      if (e.key === 'Enter') loadVideo();
    });
  document.getElementById('capture-btn')
    .addEventListener('click', () => {
      if (S.stream) stopCapture();
      else startCapture();
    });
});
