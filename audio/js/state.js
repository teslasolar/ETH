// shared mutable state
const S = {
  ac:       null,   // AudioContext
  analyser: null,   // AnalyserNode
  source:   null,   // MediaStreamAudioSourceNode
  stream:   null,   // captured tab audio stream
  freqData: null,   // Uint8Array · frequency bins
  timeData: null,   // Uint8Array · time-domain samples
  running:  false,  // animation loop flag
  bpm:      null,   // last BPM estimate
  bpmBuffer: [],    // envelope history for autocorrelation
};
