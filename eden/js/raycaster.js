// shared raycaster · mouse vector · tooltip + file-panel state
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
const tooltip = document.getElementById('tooltip');

let currentFile = null;
let chatHistory = [];
let isDragging = false;
let dragStart = { x: 0, y: 0 };
