'use strict';

function titleLine(text, alpha = 1) {
  txt(text, W / 2, 274, {size: 54, fam: F.orb, align: 'center', w: 700, c: C.white, a: alpha});
}

function mathLine(text, vertical, alpha = 1, color = C.white, size = 42) {
  txt(text, W / 2, vertical, {size, fam: F.mono, align: 'center', c: color, a: alpha});
}

SCENES.window = scene => {
  titleLine('A three-remainder sequence', at(scene, 0, 0.45));
  const values = [0, 1, 1, 2, 0, 1, 1, 2, 0];
  values.forEach((value, index) => {
    const alpha = index < 2 ? at(scene, 0, 0.4) : at(scene, 1, 0.4, (index - 2) * 0.22);
    const left = 365 + index * 137;
    const color = value === 0 ? C.now : C.cyan;
    chip(left, 444, 96, 90, String(value), color, alpha, 46);
    txt(String(index + 1), left + 48, 570, {size: 28, align: 'center', a: alpha});
  });
  mathLine('Admissible start 5  ────────  end 9', 694, at(scene, 2, 0.55), C.now);
};

SCENES.orbit = scene => {
  titleLine('The orbit closes at lag 61', at(scene, 0, 0.45));
  panel(240, 344, 1440, 180, at(scene, 0, 0.5), C.cyan, 'FIRST REPEATED WINDOW');
  mathLine('S₀  →  …  →  S₇₃₉  →  …  →  S₉₆₈₄', 456, at(scene, 0, 0.6));
  mathLine('S₉₆₈₄  →  S₇₃₉     |     8,946 windows in the loop', 594, at(scene, 1, 0.55), C.cyan, 36);
  mathLine('10 gaps: 1 matching window     11 gaps: none', 726, at(scene, 2, 0.55), C.now, 36);
};

SCENES.capture = scene => {
  titleLine('Which zero can end a run?', at(scene, 0, 0.45));
  mathLine('L = μ + 2 − k       μ = last disagreement, for k ≥ 3', 361, at(scene, 0, 0.6), C.white, 32);
  panel(252, 422, 1416, 216, at(scene, 1, 0.45), C.cyan, 'ENDPOINT μ + 2');
  mathLine('k ≡ 2: extra zero at L−1   |   k ≡ 3: nonzero start', 545, at(scene, 1, 0.6), C.white, 32);
  mathLine('μ + 6 works for k ≥ 3     |     k = 2: z = 9, μ = 0', 752, at(scene, 2, 0.5), C.now, 34);
};

SCENES.scope = scene => {
  titleLine('An upper bound is not a witness', at(scene, 0, 0.6));
  mathLine('The cycle can start before a run certifies it.', 453, at(scene, 0, 0.65), C.cyan, 35);
  mathLine('Ma and Zhang · version 3', 674, at(scene, 0, 0.55, 4), C.white, 33);
};

FILM.poster = () => {
  titleLine('Zero runs and four-cycle capture');
  mathLine('0    1    2    2    0', 484, 1, C.now, 80);
  mathLine('One closed orbit. Two candidate endpoints.', 691, 1, C.cyan, 37);
};
