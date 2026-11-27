# Extending Finch's zero-run analysis: nonattainment and a corrected capture theorem

**Authors:** Haobo Ma, Wenlin Zhang

Extending Finch's analysis of the zero-run question in Three Quadratic Recurrences Modulo 3, arXiv:2610.34300v1, Section 6, Remark 20, page 8, we answer universal attainment negatively: a closed ternary-state orbit proves that the maximum at lag 61 is ten gaps rather than the upper bound fifteen. The ten-gap starts are exactly 2780+8946m for m >= 0, and the least preperiod is 739; Harder's earlier period value 8946 is recovered. We also correct Finch's capture-offset Conjecture 23 (Section 7, page 9): whenever the eventual period is four, the offset is six for every lag k >= 3, and nine at k=2.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24408308](https://doi.org/10.5281/zenodo.24408308)
- Concept DOI: [https://doi.org/10.5281/zenodo.24408307](https://doi.org/10.5281/zenodo.24408307)
- License: CC-BY-4.0
- Version: 3
- Mathesis record: [finch-zero-runs](https://mathesis-omega-research.apps.chrono-ai.fun/papers/finch-zero-runs?version=3)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Extending Finch's zero-run analysis: nonattainment and a corrected capture theorem. Mathesis, version 3. https://doi.org/10.5281/zenodo.24408308

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0d064f0d28d301cd8a1d1b09173035a9f2fd6c02/D5/S1/Recurrence/FinchZeroRunsModThree.lean) | No public receipt |
| Theorem (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0d064f0d28d301cd8a1d1b09173035a9f2fd6c02/D5/S1/Recurrence/FinchZeroRunsModThree.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0d064f0d28d301cd8a1d1b09173035a9f2fd6c02/D5/S1/Recurrence/FinchZeroRunsModThree.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/finch-zero-runs/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/finch-zero-runs/finch-zero-runs/zh/) · [Read in English](https://papers.trureturing.org/finch-zero-runs/finch-zero-runs/en/)

[Slides](https://papers.trureturing.org/finch-zero-runs/finch-zero-runs/slides/) ([sources](books/finch-zero-runs/slides/)) · [Videos](https://papers.trureturing.org/finch-zero-runs/finch-zero-runs/films/) ([sources](books/finch-zero-runs/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/finch-zero-runs/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `lag-61` | variant | `D5/S1/Recurrence/FinchZeroRunsModThree.D5.S1.Recurrence.FinchZeroRunsModThree.result` |
| `capture` | variant | `D5/S0/Certificates/FinchConjecture23CaptureOffsetRefutation.Trureturing.OpenProblems.FinchConjecture23CaptureOffset.result` |
| `neighborhood` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/finch-zero-runs/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
