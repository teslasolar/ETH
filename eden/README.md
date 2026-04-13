# 🌳 EDEN · repo → forest

A GitHub repository rendered as a living tree — **files are flowers,
branches are directory paths, trunk is the repo.** Enter an
`owner/repo` for a single tree, or just an `owner` for a forest of
their repositories arranged on a Fibonacci spiral.

## How to run

```bash
cd eden
python3 -m http.server
# open http://localhost:8000
```

## Layout

```
eden/
├── index.html            thin entry point · loads css/ + js/
├── README.md             this file
├── css/                  7 stylesheets, each sub-250-token
│   ├── base.css           reset + body + canvas + .panel + status/controls
│   ├── input.css          the "Grow" input panel
│   ├── tooltip.css        hover-over file hint
│   ├── file.css           file viewer modal shell
│   ├── tabs.css           Code / Preview / AI tab group
│   ├── ai.css             AI chat styling
│   └── loading.css        splash screen
└── js/                   ~22 modules, each sub-250-token
    ├── const.js           τ, φ, goldenAngle
    ├── scene.js           Three.js scene + camera + renderer
    ├── lighting.js        three lights
    ├── world.js           sky dome + ground disc
    ├── state.js           trees[] · clickables[] · currentRepo
    ├── geo-trunk.js       createTrunk
    ├── geo-branch.js      createBranch
    ├── geo-flower.js      createFlower
    ├── geo-leaves.js      createLeaves
    ├── colors.js          hue-by-extension mapping
    ├── tree.js            createTree · composes branch/flower/leaves
    ├── forest.js          getForestPosition (golden-angle spiral)
    ├── load-forest.js     loadForest (multi-repo)
    ├── load-single.js     loadSingleRepo
    ├── loader.js          loadInput dispatcher
    ├── ui.js              updateUI
    ├── raycaster.js       raycaster + mouse + tooltip state
    ├── mouse.js           onMouseMove (hover + drag)
    ├── click.js           onClick
    ├── file-panel.js      openFilePanel · switchTab
    ├── ai.js              sendToAI · renderChat
    ├── camera.js          orbit + zoom
    ├── events.js          wire all UI events
    └── render.js          animate loop + resize + init
```

## Design

Flowers at branch tips are clickable. Color is derived from the file
extension (JS → amber, Python → green, TypeScript → blue, ...).
Flower size scales with file byte-size. The file panel has three
tabs: raw code, HTML preview (for `.html`/`.svg`), and an AI chat
pane scaffolded for a `/v1/messages` endpoint.

Every file under 250 tokens. Refactor-friendly.

🌳 · 和
