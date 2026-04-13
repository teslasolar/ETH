// extension → HSL hue (0..1) · the flower's petal color
function getHueForFile(filename) {
  if (/\.(js|jsx|mjs)$/i.test(filename)) return 0.12;  // amber
  if (/\.(ts|tsx)$/i.test(filename))     return 0.58;  // blue
  if (/\.py$/i.test(filename))           return 0.35;  // green
  if (/\.(html|htm)$/i.test(filename))   return 0.02;  // red
  if (/\.css$/i.test(filename))          return 0.75;  // violet
  if (/\.(md|txt)$/i.test(filename))     return 0.85;  // magenta
  if (/\.(json|yaml|yml)$/i.test(filename)) return 0.15; // gold
  if (/\.(go|rs)$/i.test(filename))      return 0.48;  // cyan
  return 0.33;                                          // default green
}
