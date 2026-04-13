/* L∞.12 · reference implementation · bloom ↔ integer
   per-ring prime · Mersenne shield · BUZZYBLOOM predicate
   stdlib-only · BigInt for exact arithmetic above R0=30 or so */

const P = [2, 3, 5, 7, 11, 13, 17];                    // prime per ring
const M = [
  127n, 8191n, 131071n, 524287n,
  2147483647n,
  2305843009213693951n,
  170141183460469231731687303715884105727n,
];
const PHI = (1 + Math.sqrt(5)) / 2;
const PRIMORIAL = 510510n;                              // fold({1,1,1,1,1,1,1})

/* bloom (R0..R6) → integer */
const fold = B => B.reduce(
  (a, r, k) => a * BigInt(P[k]) ** BigInt(r), 1n
);

/* integer → bloom (R0..R6) */
const unfold = n => P.map(p => {
  let e = 0n, x = n;
  const pp = BigInt(p);
  while (x % pp === 0n) { x /= pp; e++; }
  return Number(e);
});

/* BUZZYBLOOM predicates */
const safe = (B1, B2, tau = 4) =>
  B1.every((_, k) => Math.max(B1[k], B2[k]) >= tau);

const phiCoh = B => {
  let s = 0;
  for (let k = 0; k < 6; k++) {
    const r = B[k + 1] / (B[k] || 1);
    s += Math.max(0, 1 - Math.abs(r - PHI));
  }
  return s / 6;
};

const happy = (B1, B2, phiMin = 0.3) =>
  phiCoh(B1.map((_, k) => Math.max(B1[k], B2[k]))) > phiMin;

const buzzy = (B1, B2) => safe(B1, B2) && happy(B1, B2);

/* 127-shield · one integer comparison */
const shield = (B, ring = 6) => fold(B) < M[ring];

/* cross-bloom anti-prime pollination */
const antiPrime = (src, tgt, k) =>
  src[k] > tgt[k]
    ? tgt.map((v, i) => i === k ? Math.min(src[k], v + 1) : v)
    : tgt;

/* canonical example — Thomas × John */
const Thomas = [2, 8, 3, 7, 15, 6, 12];
const John   = [7, 9, 5, 12, 6, 8, 4];

if (typeof module !== 'undefined') {
  module.exports = { P, M, PHI, PRIMORIAL, fold, unfold,
                     safe, happy, buzzy, shield, antiPrime,
                     Thomas, John };
}
