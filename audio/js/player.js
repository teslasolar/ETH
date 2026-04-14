// YouTube iframe embed · accepts full URL or raw 11-char video ID
function ytIdFromInput(input) {
  const s = input.trim();
  // raw video id
  if (/^[a-zA-Z0-9_-]{11}$/.test(s)) return s;
  // youtu.be/<id>
  let m = s.match(/youtu\.be\/([a-zA-Z0-9_-]{11})/);
  if (m) return m[1];
  // youtube.com/watch?v=<id>
  m = s.match(/[?&]v=([a-zA-Z0-9_-]{11})/);
  if (m) return m[1];
  // youtube.com/embed/<id>
  m = s.match(/embed\/([a-zA-Z0-9_-]{11})/);
  if (m) return m[1];
  // shorts/<id>
  m = s.match(/shorts\/([a-zA-Z0-9_-]{11})/);
  if (m) return m[1];
  return null;
}

function loadVideo() {
  const input = document.getElementById('yt-url').value;
  const id = ytIdFromInput(input);
  const iframe = document.getElementById('player');
  if (!id) {
    iframe.src = '';
    alert('Could not parse a YouTube video ID from that input.');
    return;
  }
  iframe.src =
    `https://www.youtube.com/embed/${id}?autoplay=0&modestbranding=1`;
}
