# Permuted rotor loops beyond Jenzer (2026): resolving Remark 5.5 (arXiv:2610.21593v1, p. 19)

Extending Nik Jenzer's (2026) same-order and star-family proofs, the note resolves Remark 5.5,
arXiv:2610.21593v1, page 19 (source TeX label `remark:5-7`): every return
permutation satisfies the subset formula without the star condition.
It also proves the arbitrary-permutation mixed-sign extension, mixed-sign
compact and zero formulas, and an exact scalar chain formula. The subset
identity also holds in any unital real algebra with a normalized tracial
linear functional, without a grading or involution. For at most
three factors, the loop is scalar plus a simple bivector and every scalar
power is a Chebyshev polynomial. These settle the three-factor observations
in Section 8.4, OF 2 and OF 3. A four-factor example gives equal scalar parts
but different scalar parts of their squares. The permutation graph determines the
exact range and the finest factorization into disjoint variable blocks.

## Contents

- `note.tex`: complete proofs, bibliography, source coverage and formal statement links.
- `note.pdf`: typeset note.
- `verify.py`: Python 3 standard-library exact polynomial checks.
- `verification.txt`: deterministic output of those finite checks.
- `metadata.json`: bibliographic metadata and statement coverage.
- `LICENSE`: CC BY 4.0 notice.

## Build

Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error note.tex`
twice. The bibliography is embedded; BibTeX and external figures are unnecessary.
The source archive contains everything needed to typeset the note; the rendered
PDF is supplied separately.

## Exact finite checks

```sh
python3 verify.py
```

The output must match `verification.txt`. The formal Clifford-generator
checks cover all 873 permutations for `1 <= k <= 6`; the mixed-sign
checks cover all 442 choices of signature and return order for `1 <= k <= 4`.
These compare coefficients in independent `c_i,s_i`, including the odd
full-support coefficient that a tracial functional could retain.
The geometric checks cover the six return orders for a non-star triangle
and a rationally rotated triangle. Finite checks do not replace the
universal written proofs.

Additional exact checks cover 378 mixed-sign compact cases through six
factors; 873 permutation graphs and their 50,362 vertex coefficients;
210 normalized geometric loops with at most three factors, all signatures
and return orders in the stated star samples, plus two non-star triangle
families; and 1,890 scalar powers with exponents 0 through 8. The four-factor
example has scalar -1/4 and its square has scalar part -1/4, whereas the corresponding
Chebyshev value is -7/8. These are finite rational checks, not universal
parameter proofs.
The identity-order equal-half-weight sequence is OEIS A009545 shifted by
one: `2**k * F_id(1/2,...,1/2) = A009545(k+1)`. The checker compares
65 signed binomial sums with its classical recurrence, for `0 <= k <= 64`.

## Scientific sources and formal statements

- Posing source: https://arxiv.org/abs/2610.21593v1, Theorem 5.5 and Remark 5.5, pages 18–19.
- Earlier star-family chain and same-order formulas: Nik Jenzer, 6 August 2026, https://doi.org/10.5281/zenodo.20769239, Sections 3.1–3.2, S5.10–S5.11, pages 18–19.
- Trace-support antecedent: Shirokov, https://arxiv.org/abs/1412.0246v2, Theorem 3.2.
- Odd exterior coefficients: Diehl–Reizenstein, https://arxiv.org/abs/1801.06104v2, Lemma 22; determinant antecedent de Bruijn (1955), Section 4.
- Graph coefficient separability: Hein–Eisert–Briegel, https://arxiv.org/abs/quant-ph/0307130v1, Proposition 3, Eq. (42).
- Clifford conventions: https://arxiv.org/abs/0907.5356v1, Section 2.3.
- Equal-half-weight sequence: https://oeis.org/A009545, its imaginary-power formula and recurrence.
- Square-minus-one formula: https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoop.lean, declaration `D5.S3.QuadraticForms.JenzerPermutedRotorLoop.result`.
- Scalar cyclicity and trace support: https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoopAlgebra.lean.
- Odd complementary-subset cancellation: https://github.com/the-omega-institute/trureturing/blob/3bedf2870aacc6e7f17353444aadaa49fb73157c/D5/S3/QuadraticForms/JenzerPermutedRotorLoopWords.lean, declaration `ExteriorSum.signed_top_sum_zero` in that module's namespace.

The linked Lean declarations cover the square-minus-one formula and its
scalar-cyclicity, trace-support and odd-coefficient ingredients.
The mixed-sign formula, compact and zero expressions, chain refinement,
three-factor simplicity and powers, and permutation-graph factorization
have written proofs in the note. The listed main Lean declaration concerns
the square-minus-one subset formula for bivector families in
finite-dimensional nondegenerate real Clifford algebras. The companion
declarations supply scalar cyclicity, trace support and odd exterior
coefficient cancellation, as specified in the note.

## Coverage limits

The coverage table in the PDF names the exact posing locators and separates
proved extensions, corrected endpoints, prior proofs and uncovered questions.
The geometric classification in OF 1, general higher-grade formulas in OF 2,
and general four-or-more-factor powers and other longer words in OF 3 are
not covered. The identity-order special cases are attributed to Jenzer;
there is no priority claim. Only the established problem ID `jen2610`
appears in the metadata.

## Creators and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`), https://creativecommons.org/licenses/by/4.0/.
