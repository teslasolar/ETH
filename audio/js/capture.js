// capture tab audio via getDisplayMedia · connect to AnalyserNode
async function startCapture() {
  const status = document.getElementById('cap-status');
  status.classList.remove('-live', '-error');
  try {
    // request display media with audio. User must pick a tab
    // and TICK "Share audio" in the browser dialog.
    const stream = await navigator.mediaDevices.getDisplayMedia({
      video: true, // some browsers require video:true + we ignore it
      audio: true,
    });
    const audioTracks = stream.getAudioTracks();
    if (audioTracks.length === 0) {
      stream.getTracks().forEach(t => t.stop());
      throw new Error(
        'no audio track — did you tick "Share audio" in the dialog?'
      );
    }
    // video track is unused; stop it immediately to save bandwidth
    stream.getVideoTracks().forEach(t => t.stop());

    S.stream = stream;
    initAnalyser(stream);
    status.textContent = 'capturing · live';
    status.classList.add('-live');

    stream.getAudioTracks()[0].addEventListener('ended', () => {
      stopCapture();
      status.textContent = 'capture ended';
    });
  } catch (e) {
    status.textContent = 'error: ' + e.message;
    status.classList.add('-error');
  }
}

function stopCapture() {
  if (S.stream) S.stream.getTracks().forEach(t => t.stop());
  S.stream = null; S.running = false;
  if (S.ac) S.ac.close();
  S.ac = null; S.analyser = null;
}
