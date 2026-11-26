# Permuted rotor loops beyond Jenzer (2026): resolving Remark 5.5 (arXiv:2610.21593v1, p. 19)

**Authors:** Haobo Ma, Wenlin Zhang

Extending Jenzer's (2026) same-order and star-family proofs, we resolve his Remark 5.5 (arXiv:2610.21593v1, p. 19): every return permutation satisfies the rotor-loop subset formula for every anticommuting unit bivector family, without the star condition. Conjugation eliminates every off-diagonal scalar contribution except possibly complementary subsets when the family size is odd. Their total vanishes because a balanced product in an exterior algebra has even degree. Corollaries give mixed-sign compact and zero formulas, the exact chain correction, and the range and separability of every return order. For at most three factors the loop has only scalar and simple bivector parts, and every scalar power is a Chebyshev polynomial of its scalar part.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24404942](https://doi.org/10.5281/zenodo.24404942)
- Concept DOI: [https://doi.org/10.5281/zenodo.24404941](https://doi.org/10.5281/zenodo.24404941)
- License: CC-BY-4.0
- Version: 5
- Mathesis record: [jen2610-permuted-rotor-loops](https://mathesis-omega-research.apps.chrono-ai.fun/papers/jen2610-permuted-rotor-loops?version=5)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Permuted rotor loops beyond Jenzer (2026): resolving Remark 5.5 (arXiv:2610.21593v1, p. 19). Mathesis, version 5. https://doi.org/10.5281/zenodo.24404942

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Lemma (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/jen2610-permuted-rotor-loops/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/jen2610-permuted-rotor-loops/jen2610-permuted-rotor-loops/zh/) · [Read in English](https://papers.trureturing.org/jen2610-permuted-rotor-loops/jen2610-permuted-rotor-loops/en/)

[Slides](https://papers.trureturing.org/jen2610-permuted-rotor-loops/jen2610-permuted-rotor-loops/slides/) ([sources](books/jen2610-permuted-rotor-loops/slides/)) · [Videos](https://papers.trureturing.org/jen2610-permuted-rotor-loops/jen2610-permuted-rotor-loops/films/) ([sources](books/jen2610-permuted-rotor-loops/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/jen2610-permuted-rotor-loops/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `chain-correction` | variant | `D5/S3/QuadraticForms/JenzerPermutedRotorLoopAlgebra.tracial_subset_vanishing` |
| `loop-formula` | same | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |
| `mixed-loop` | special case | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |
| `odd-cancellation` | special case | `D5/S3/QuadraticForms/JenzerPermutedRotorLoopWords.signed_top_sum_zero` |
| `order-graph` | variant | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |
| `polar-zero` | variant | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |
| `three-factor-powers` | variant | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |
| `trace-support` | special case | `D5/S3/QuadraticForms/JenzerPermutedRotorLoopAlgebra.tracial_subset_vanishing` |
| `tracial-loop` | variant | `D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/jen2610-permuted-rotor-loops/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
