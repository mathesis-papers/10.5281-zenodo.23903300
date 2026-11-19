# OEIS A209723: Barker's conjectures on distinct clockwise edge differences

**Authors:** Haobo Ma, Wenlin Zhang

We prove the Conjectures of Colin Barker in the FORMULA section of OEIS A209723, dated July 12, 2018: the parity formulas and ordinary generating function for ternary arrays with distinct clockwise edge differences. We also prove Hardin's empirical recurrence. A decomposition of the row-compatibility graph into two three-vertex stars and isolated edges gives a formula for every rectangular size. Its corollaries include the companion formulas in A209721–A209726, Beck's first A209721 conjecture, Peterson's A209721 recurrence and triangle interpretation, and the column recurrences and diagonal identification in A209727.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23903301](https://doi.org/10.5281/zenodo.23903301)
- Concept DOI: [https://doi.org/10.5281/zenodo.23903300](https://doi.org/10.5281/zenodo.23903300)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [hardin-barker-a209723-edge-differences](https://mathesis-omega-research.apps.chrono-ai.fun/papers/hardin-barker-a209723-edge-differences?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). OEIS A209723: Barker's conjectures on distinct clockwise edge differences. Mathesis, version 2. https://doi.org/10.5281/zenodo.23903301

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.lean) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23903300/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23903300/hardin-barker-a209723-edge-differences/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23903300/hardin-barker-a209723-edge-differences/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23903300/hardin-barker-a209723-edge-differences/slides/) ([sources](books/hardin-barker-a209723-edge-differences/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23903300/hardin-barker-a209723-edge-differences/films/) ([sources](books/hardin-barker-a209723-edge-differences/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23903300/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `rectangular-count` | special case | `D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result` |
| `row-structure` | none | — |
| `five-column` | same | `D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result` |
| `beck-peterson` | variant | `D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209721EdgeDifferences.result` |
| `diagonal` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/hardin-barker-a209723-edge-differences/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
