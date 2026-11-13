# OEIS A209723: Barker's conjectures on clockwise edge differences

Authors: Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).
License: Creative Commons Attribution 4.0 International (CC BY 4.0).

## Result and coverage

For `n,k >= 1`, the normalized labelled-array count is
`T(n,k) = b(n) + b(k) - 2`, with
`b(2m+1) = 2^(m+1)` and `b(2m+2) = 3*2^m`.
The PDF supplies the complete graph-decomposition proof and a source-coverage
map. Consequences include Barker's A209723 formulas, the A209721–A209726
companion formulas, Beck's first A209721 conjecture, Peterson's recurrence
and integer-triangle interpretation, and the column recurrences and diagonal
identification `T(n,n) = A027383(n)` for `n >= 1` in A209727.
Beck's second A209721 zero-position conjecture and Reverter i Bigas's
A209724 divisor/minimality conjecture are not covered.

## Build

The main source is `note.tex`; the bibliography is embedded and there are no
external figures or TeX inputs. Use Tectonic **0.17.0**:

```sh
tectonic --untrusted note.tex
```

Alternatively, use a standard LaTeX installation with Latin Modern,
`amsmath`, `amsthm`, `booktabs`, `tabularx`, `geometry`, and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

No BibTeX pass is required.

## Finite checks

Python 3.8 or later and its standard library suffice:

```sh
python3 verify.py
```

The script checks all 81 local tiles, independently constructs row graphs
for widths 2–6, checks component decompositions through width 12, and counts
walks of lengths 1–60 (1–210 for widths 3 and 5). It also directly enumerates
seven whole-array sizes through 3 by 4, checks the five-column recurrence
and generating-function coefficients through degree 210, and checks the
Beck, Peterson and diagonal identities through index 210. Triangle counts
are independently enumerated for indices 3–16.

Optional OEIS comparisons use two public tables:

```sh
mkdir -p .checks/data
curl -fLsS https://oeis.org/A209723/b209723.txt -o .checks/data/b209723.txt
curl -fLsS https://oeis.org/A209727/b209727.txt -o .checks/data/b209727.txt
python3 verify.py --data .checks/data --output .checks/verification.json
```

These compare 210 A209723 values and 1512 A209727 values. If OEIS search-JSON
snapshots named `A209721.json` through `A209726.json`, `A029744.json`, and
`A027383.json` are present in that directory, their displayed prefixes are
also compared. `reproduction.json` records input and output hashes.
The mathematical results for arbitrary dimensions have written proofs;
the Python computations cover the explicitly stated finite ranges.

## Attribution and Lean scope

Hardin defined the array counts, and Barker supplied the conjectured
formulas. Andrew's Math Stack Exchange answer 4995628, dated
November 8, 2024, 00:07:06 UTC, supplies an earlier four-column proof outline.
The note cites that answer and Stanley's transfer-matrix framework.

The PDF links the exact Lean file at commit
`cdafeab0d44da2b6840cfc802535d2f94a146fad`:

https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.lean

Its declaration
`D5.S3.Combinatorics.Graph.Pressure.HardinBarkerA209723EdgeDifferences.result`
formalizes the five-column (`k=4`) parity formulas, recurrence from index 4,
existence of the zero-constant generating series, and its denominator identity.
The all-width theorem and added corollaries have written proofs in the note.
