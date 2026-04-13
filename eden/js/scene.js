// Three.js scene · camera · renderer
const canvas = document.getElementById('canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  50, innerWidth / innerHeight, 0.1, 1000
);
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });

renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setClearColor(0x050308);
