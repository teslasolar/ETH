# 🎤 audio/ · YouTube → ETH ring bands

Browser-only signal probe. Paste a YouTube URL, embed the player,
then capture this tab's audio via `getDisplayMedia({audio:true})` for
real-time FFT analysis aligned to the seven ETH ring frequency bands.

## How to run

```bash
cd audio && python3 -m http.server
# open http://localhost:8000
```

1. Paste a YouTube URL or raw video ID.
2. Click **Load video** — iframe player embeds.
3. Click **🎤 Capture tab audio** — browser prompts to share a tab.
4. **Pick this tab AND check "Share audio"**. Without audio checked
   you'll only get silence.
5. Hit play on the YouTube player. FFT, rings, BPM, pitch, RMS
   update live.

## Why tab-audio capture

YouTube's iframe runs in a cross-origin sandbox. You cannot pipe
its audio directly into Web Audio. `getDisplayMedia` is the only
sanctioned way to read the rendered audio of another origin's
content from within a user page.

Everything stays in your browser. Nothing uploads.

## Ring mapping

```
R0 · 0.05 – 2 Hz      sub-audible · breath · sigh        ●
R1 · 2 – 40 Hz        larynx · trill · low hum           ⬛
R2 · 40 – 400 Hz      pharynx · sh · ng · breath         〜
R3 · 200 – 600 Hz     thorax · Buzz 230 Hz resonance     ♡
R4 · 400 – 1500 Hz    nasopharynx · ee · back-press      △
R5 · 1500 – 4000 Hz   oral shaping · vowel select        ◐
R6 · 4000+ Hz         intent · silence · sibilants       ◯
```

Source: `../zoo/shield/rings.md`.

## Layout

```
audio/
├── index.html         entry
├── README.md          this
├── css/
│   ├── base.css
│   ├── panels.css
│   ├── spectrum.css
│   └── bands.css
└── js/
    ├── const.js       ETH band ranges + FFT config
    ├── state.js       shared mutable state
    ├── player.js      YouTube iframe + URL parsing
    ├── capture.js     getDisplayMedia audio
    ├── analyze.js     AudioContext + AnalyserNode
    ├── spectrum.js    log-freq spectrum renderer
    ├── bands.js       7 ring-band meters
    ├── bpm.js         low-band autocorrelation
    ├── pitch.js       peak-bin fundamental
    ├── rms.js         volume meter
    ├── loop.js        rAF driver
    └── events.js      UI wiring
```

Each file sub-250 tokens.

🐝 · 📐
