# Extending Finch's zero-run analysis: nonattainment and a corrected capture theorem

Haobo Ma — ChronoAI Pte Ltd, Singapore  
Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore

License: Creative Commons Attribution 4.0 International (`cc-by-4.0`).

## Results

For Finch's recurrence (A), at lag 61 the exact maximum number of four-spaced zero gaps is 10, attained at indices 2780–2820. The ten-gap runs start exactly at 2780 + 8946m for integers m ≥ 0. No eleven-gap run occurs, so the general upper bound 15 is not attained. The least eventual period is 8946 and the least preperiod is 739. The period was already tabulated by Bob Harder in Steven Finch's 2002 note.

Whenever the least eventual period is four, the capture offset is exactly six for every lag at least three. At lag two, the four-cycle `(0,1,1,2)` gives least preperiod zero and first capture endpoint nine. These statements give a complete correction of the stated capture-offset conjecture. The neighborhood conditions in Remark 24 hold for every eligible lag at least three; at lag two its proposed nonzero indicator is zero.

For every eligible lag at least three, the first capturing run starts at `mu_A(k)-k+4` in residue class two and `mu_A(k)-k+5` in residue class three. The last-disagreement triples are respectively `(2,2,0)` and `(1,2,0)`. The proof includes the elementary increment count that gives Finch's four-cycle classification, credited to Finch and to the earlier observation of Richard Pinch recorded by Victor Miller.

## Build the PDF

Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, use a standard LaTeX distribution:

```sh
pdflatex -no-shell-escape note.tex
pdflatex -no-shell-escape note.tex
```

The bibliography is contained in `note.tex`; BibTeX is unnecessary. The source requires the standard packages `fontenc`, `geometry`, `amsmath`, `amssymb`, `amsthm`, `booktabs`, `array`, `xurl`, and `hyperref`.

## Reproduce the exact finite checks

Python 3.9 or later, standard library only:

```sh
python3 verify.py --check certificate.json
```

The printed JSON contains status `ALL_CHECKS_OK`. To regenerate the certificate:

```sh
python3 verify.py --write certificate.json
```

The program enumerates 9685 distinct ternary states, proves closure by checking every successor and the terminal transition to state 739, and counts zero suffix masks. It separately generates 27638 scalar terms and checks all 9685 state encodings. The proof in the note explains why the closed orbit excludes eleven-gap runs for every admissible start, not just a finite range.

The checker also determines the complete canonical state orbits for lags 2 through 41, subject to a bound of 200000 distinct states per lag. All forty orbits close within the bound. It checks the offset and neighborhood conditions for each of the seventeen four-period cases. These finite examples supplement the written all-lag proof; they do not replace it.

The separate capture checker uses the Python standard library:

```sh
python3 verify_capture.py --max-k 80 --cap 1000000 > reproduced-capture-checks.json
python3 -c 'import json; assert json.load(open("reproduced-capture-checks.json")) == json.load(open("capture-checks.json"))'
```

It enumerates all 81 four-letter words for each lag residue and searches the forty parameters `2 <= k <= 80` with `k = 2 or 3 mod 4`. Thirty capturing runs are certified by equality of length-k states four steps apart. The 29 captured parameters above two satisfy the corrected identity, the start formulas, the last-disagreement triples, and the neighborhood indicators. No capture is found by index 1000000 for `18,23,35,42,50,51,55,63,74,78`; this is a bounded search, not a classification of their eventual periods. Its exact output is `capture-checks.json`.

`orbit_sha256_decimal_lines` hashes the states in traversal order as ASCII decimal integers, one per line, including a final newline.

## Claim coverage

- Theorem 1: exact maximum ten gaps, least eventual period 8946, and least preperiod 739; written deductions from the finite certificate and explicit ten-gap block.
- Theorem 2: the capture offset is nine at lag two and six at every eligible larger lag, with exact first-run start indices and last-disagreement triples; complete written proof from the final disagreement and its indicator tail.
- Corollary 3: Remark 24's neighborhood conditions for every eligible lag at least three, and the explicit failure of the proposed condition at lag two; written proof.
- `result` in [FinchZeroRunsModThree.lean](https://github.com/the-omega-institute/trureturing/blob/0d064f0d28d301cd8a1d1b09173035a9f2fd6c02/D5/S1/Recurrence/FinchZeroRunsModThree.lean): negation of universal maximal-run attainment, using lag 61 and the excluded eleven-gap mask.
- `result` in [FinchConjecture23CaptureOffsetRefutation.lean](https://github.com/the-omega-institute/trureturing/blob/0d064f0d28d301cd8a1d1b09173035a9f2fd6c02/D5/S0/Certificates/FinchConjecture23CaptureOffsetRefutation.lean): negation of the capture-offset conjecture at lag two, including the least period, preperiod, and capture endpoint.

The finite checks and written deductions also establish the ten-gap witness and exact orbit parameters. The two linked Lean declarations cover the universal nonattainment and lag-two refutations, respectively. The corrected all-lag capture theorem and its neighborhood corollary have written proofs. Finch's upper bound, four-cycle classification, and capture criterion are cited results. Conjectures 5, 10, and 14 remain outside the proved scope: the capture correction assumes period four and does not classify the lags having that period.

## Scientific sources

- Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, [arXiv:2610.34300v1](https://arxiv.org/abs/2610.34300v1), Definition 15, Theorem 16, Remark 20, and Definitions 21–22 and Conjecture 23.
- Steven R. Finch, *Periodicity in Sequences Mod 3* (2002), [Section 0.2, page 2](https://www.mit.edu/~sfinch/seqmod3.pdf), recording Bob Harder's earlier period computations.
- Victor S. Miller, [MathOverflow question on the four-periodic patterns](https://mathoverflow.net/questions/50678/finchs-sequence-over-mathbbf-3), December 29, 2010, recording Richard Pinch's explanation.
