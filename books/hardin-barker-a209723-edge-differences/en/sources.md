# Sources and further work

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## Paper and earlier work

The mathematical source is Haobo Ma and Wenlin Zhang, *OEIS A209723: Barker's conjectures on distinct clockwise edge differences*, version 2 (2026), [version DOI: 10.5281/zenodo.23903301](https://doi.org/10.5281/zenodo.23903301), licensed CC BY 4.0. The [concept DOI](https://doi.org/10.5281/zenodo.23903300) groups the versions; citations here identify version 2. Manuscript Theorem 1 is stated in §1; Lemma 1 and the main proof are in §2; Corollaries 1–2 and the companion calculations are in §3.

<section hidden="hidden">

```{=typst}
]
```

</section>

- R. H. Hardin, [A209723](https://oeis.org/A209723), the five-column problem, March 12, 2012; Colin Barker's parity and generating-function conjectures, July 12, 2018.
- R. H. Hardin, [A209727](https://oeis.org/A209727), the rectangular counting table, normalized as one quarter of the actual number of fillings.
- [A209721](https://oeis.org/A209721), three columns: Barker's generating function, Beck's first conjecture, and Peterson's recurrence and triangle interpretation.
- [A209722](https://oeis.org/A209722), [A209724](https://oeis.org/A209724), [A209725](https://oeis.org/A209725), [A209726](https://oeis.org/A209726), companion formulas for four and six through eight columns.
- N. J. A. Sloane, [A029744](https://oeis.org/A029744), the interlaced doubling sequence; R. K. Guy, [A027383](https://oeis.org/A027383), the square-grid diagonal.
- Andrew, Math Stack Exchange answer [4995628](https://math.stackexchange.com/a/4995628), November 8, 2024: a tile-based proof outline for four columns.
- R. P. Stanley, *Enumerative Combinatorics, Volume 1*, second edition, 2012, §4.7, [DOI: 10.1017/CBO9781139058520](https://doi.org/10.1017/CBO9781139058520), for the transfer-matrix method. This reading gives the needed walk count directly and assumes no matrix theory.

## Which statements have a direct formal proof?

[@five-column] corresponds directly to the [five-column Lean theorem](lean:D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result): entries are converted to integers before subtraction; the literal labelled-array count is divided by four; parity covers every positive index; the recurrence starts at four; and a formal source series exists with constant coefficient zero. The preceding chapter gives the manuscript's written proofs of the arbitrary-width [@rectangular-count], decomposition [@row-structure], triangle consequence [@beck-peterson], and diagonal [@diagonal].

A separate [three-column Lean theorem](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209721EdgeDifferences.lean#L150) proves the order-three recurrence and formal generating function at that width. It offers reusable prerequisites for the triangle consequence, but does not directly state all its conclusions.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## Contribute a formalization

The remaining work is formalization of arguments already proved in the paper. Use these shared public coordination issues; translations do not need separate tasks:

- [Arbitrary-width row-graph decomposition](https://github.com/the-omega-institute/trureturing-requests/issues/222): establish the two stars and separate edges, providing the structure for the general count.
- [Rectangular count and diagonal consequence](https://github.com/the-omega-institute/trureturing-requests/issues/223): reuse the decomposition to prove the general count; obtain the diagonal by substitution in the same contribution.
- [Beck–Peterson identities and triangle interpretation](https://github.com/the-omega-institute/trureturing-requests/issues/224): reuse the general formula at three columns, or the existing three-column formal proof, for the two-step recurrence, sequence identification and third-side count.

<section hidden="hidden">

```{=typst}
]
```

</section>

State the exact intended scope and branch in the relevant issue, then submit a focused PR from your contributor fork directly to [trureturing's dev branch](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md), following existing proof admission, review and CI rules. After acceptance, compare the frozen declaration with the complete written statement before updating citations. GitHub merge does not automatically alter independent Mathesis verification records or award platform points.


<section hidden="hidden">

```{=typst}
#pagebreak(weak: true)
```

</section>
