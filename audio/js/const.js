// ETH ring frequency bands · derived from zoo/shield/rings.md
const RING_BANDS = [
  { ring:'R0', glyph:'●', name:'breath · sigh',          lo:0.05, hi:2,     color:'#993366' },
  { ring:'R1', glyph:'⬛', name:'larynx · trill',         lo:2,    hi:40,    color:'#00aadd' },
  { ring:'R2', glyph:'〜', name:'pharynx · breath',       lo:40,   hi:400,   color:'#ffaa00' },
  { ring:'R3', glyph:'♡', name:'thorax · 230 Hz Buzz',   lo:200,  hi:600,   color:'#ff4444' },
  { ring:'R4', glyph:'△', name:'nasopharynx · ee',        lo:400,  hi:1500,  color:'#44aa44' },
  { ring:'R5', glyph:'◐', name:'oral · vowel select',     lo:1500, hi:4000,  color:'#aa44ff' },
  { ring:'R6', glyph:'◯', name:'intent · sibilants',      lo:4000, hi:16000, color:'#eeeeee' },
];

const FFT_SIZE = 2048;       // AnalyserNode fftSize · 1024 freq bins
const SMOOTHING = 0.75;      // Web Audio smoothingTimeConstant
