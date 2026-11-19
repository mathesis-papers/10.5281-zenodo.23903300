# Precise statements and proofs

Use the manuscript's definitions. For $n,k\geq1$, $N(n,k)$ counts labelled $(n+1)\times(k+1)$ arrays over $\{0,1,2\}$. In each adjacent square $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$, the integers $b-a,d-b,c-d,a-c$ must be pairwise distinct. Put $T=N/4$ and define

$$
\begin{aligned}
b(2m+1)&=2^{m+1},\\
b(2m+2)&=3\cdot2^m\qquad(m\geq0).
\end{aligned}
$$

We state the main answer first, prove the local classification, graph decomposition and count in that order, and finish with two consequences. The written proofs below expand the arguments in Haobo Ma and Wenlin Zhang's version 2 manuscript.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.theorem #rectangular-count title="The rectangular count" mathesis="collected:hardin-barker-a209723-edge-differences:2:s1" status="written-proof" proof="pf-rectangular-count" doi="10.5281/zenodo.23903301" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/223"}
For all $n,k\geq1$,

$$
T(n,k)=b(n)+b(k)-2.
$$

In particular, $a(n)=T(n,4)$ satisfies

$$
\begin{aligned}
a(2m+1)&=2^{m+1}+4,\\
a(2m+2)&=3\cdot2^m+4\qquad(m\geq0),
\end{aligned}
$$

and, as a formal power series,

$$
\sum_{n\geq1}a(n)x^n=\frac{x(6+x-11x^2)}{(1-x)(1-2x^2)}.
$$
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

## The eight squares

Four distinct differences from $\{-2,-1,0,1,2\}$ sum to zero, so they must be $\{-2,-1,1,2\}$. The $+2$ and $-2$ edges cannot be opposite. For example, if the top edge is $+2$ and the clockwise bottom edge is $-2$, both rows are $02$ and the remaining differences are both zero; rotations cover the other positions. These edges must therefore meet at an extreme entry, $0$ or $2$. The remaining vertex must be $1$ to supply differences $1$ and $-1$. This gives exactly eight tuples $(a,b,c,d)$:

$$
\begin{aligned}
&(0,1,2,0),\ (0,2,1,0),\\
&(0,2,2,1),\ (1,0,0,2),\\
&(1,2,2,0),\ (2,0,0,1),\\
&(2,0,1,2),\ (2,1,0,2).
\end{aligned}
$$

Direct subtraction verifies every listed square, proving sufficiency as well as necessity. The adjacency graph of column cards is exactly

$$
\begin{aligned}
02&\longleftrightarrow\{10,21\},\\
20&\longleftrightarrow\{01,12\}.
\end{aligned}
$$

In particular, different neighbors of a card have different upper entries.

## Structure of the row graph

The vertices of $H_k$ are all rows of length $k+1$; two are adjacent if they can be stacked. Interchanging the rows permutes and negates the differences, so adjacency is symmetric. A repeated row would have two zero vertical differences, ruling out loops. An array corresponds bijectively to a walk of length $n$ with specified starting vertex. Walks may repeat edges and vertices.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.lemma #row-structure title="Decomposition of the row graph" mathesis="collected:hardin-barker-a209723-edge-differences:2:s2" status="written-proof" proof="pf-row-structure" doi="10.5281/zenodo.23903301" source="Lemma 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/222"}
For every $k\geq1$, the nonisolated part of $H_k$ is the disjoint union of two copies of $K_{1,2}$ and $2b(k)-4$ copies of $K_2$.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-row-structure}
Write $R_{uv}=uvuvu\cdots$, truncated to length $k+1$. The card graph gives

$$
\begin{aligned}
R_{02}&\longleftrightarrow\{R_{10},R_{21}\},\\
R_{20}&\longleftrightarrow\{R_{01},R_{12}\}.
\end{aligned}
$$

For example, with $R_{02}$ as the upper row the first column card can only be $01$ or $02$. The former forces the next card to be $20$; the latter forces $21$ because its upper entry must be $2$. Continuing determines the two possible lower rows. Interchanging $0,2$ gives the other star. All six rows are distinct since $k+1\geq2$.

Take any row $s$ with a neighbor. Its adjacent entries are unequal by the eight-square list. If it has no $1$, it must be $R_{02}$ or $R_{20}$. Otherwise an adjacent pair involves $1$, as the row has at least two entries. In the list, upper pairs $01,10,12,21$ have unique lower pairs $20,02,20,02$, respectively. Once that pair is fixed, extend in either direction. The next card's upper entry is prescribed, and the current card has at most one neighbor with that upper entry. Thus the entire neighboring row is unique whenever it exists. The four displayed leaves do have neighbors, hence have degree one. Outside these stars, every nonisolated component is $K_2$.

To count them, a single $K_{1,2}$ has $3\cdot2^m$ walks of length $2m$: $2^m$ from each starting vertex. At length $2m+1$, the center contributes $2^{m+1}$ and each leaf $2^m$, totaling $4\cdot2^m$. Thus two stars have $4b(k)$ walks of every positive length $k$.

Reading the same two-row array by rows gives a directed edge of $H_k$; reading it by columns gives a $k$-step walk in the card graph. This is a bijection, so $H_k$ has $4b(k)$ directed edges. Its two stars account for eight; each remaining $K_2$ accounts for two. There are $(4b(k)-8)/2=2b(k)-4$ such components. At $k=1$ this number is zero, and the argument still applies.
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## Proof of the main formula


::: {.proof #pf-rectangular-count}
Apply [@row-structure]. For $n\geq1$ isolated vertices contribute nothing, the two stars contribute $4b(n)$ walks, and each $K_2$ contributes two, one from each starting end. Hence

$$
\begin{aligned}
N(n,k)&=4b(n)+2(2b(k)-4),\\
T(n,k)&=b(n)+b(k)-2.
\end{aligned}
$$

Set $k=4$, so $b(4)=6$, to obtain the parity formulas. Summing the odd and even geometric series gives

$$
B(x):=\sum_{n\geq1}b(n)x^n=\frac{2x+3x^2}{1-2x^2}.
$$

Thus $A(x)=B(x)+4x/(1-x)$. The common numerator is $(2x+3x^2)(1-x)+4x(1-2x^2)=6x+x^2-11x^3$, as asserted. Both denominator factors have constant term one and are invertible in the formal power-series ring; no analytic convergence assumption is required.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

## Exact formal scope for five columns

The following is the five-column specialization of [@rectangular-count], together with the recurrence in manuscript §3. It does not assert arbitrary-width formalization.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.theorem #five-column title="Five-column parity, recurrence and formal series" mathesis="collected:hardin-barker-a209723-edge-differences:2:s1" lean="D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result"}
Let $a(n)=N(n,4)/4$, valued in the rationals. For every $m\geq0$,

$$
\begin{aligned}
a(2m+1)&=2^{m+1}+4,\\
a(2m+2)&=3\cdot2^m+4.
\end{aligned}
$$

For every $n\geq4$,

$$
a(n)=a(n-1)+2a(n-2)-2a(n-3).
$$

There exists $A\in\mathbb Q[[x]]$ with constant coefficient zero and coefficient $a(n)$ at $x^n$ for every $n\geq1$. Every such $A$ satisfies

$$
A(1-x)(1-2x^2)=x(6+x-11x^2).
$$
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-five-column}
The parity formulas follow from $a(n)=b(n)+4$. The identity $b(n+2)=2b(n)$ gives $a(n+2)=2a(n)-4$ for $n\geq1$. Subtract consecutive instances to obtain $a(n+3)-a(n+2)=2a(n+1)-2a(n)$, which is the stated recurrence. Constructing the series by its coefficients gives existence, and the common-denominator calculation above gives its identity. The linked Lean theorem states all these clauses directly; its recurrence index $m+4$ is the same range as $n\geq4$. Although Lean defines its count for every natural input, the series constant coefficient is specified separately as zero; it is not the array count at $n=0$ divided by four.
:::

## Three columns and integer triangles

Write $u(n)=T(n,2)$ here to distinguish it from the five-column $a(n)$. Manuscript Corollary 1 calls this three-column sequence $a(n)$.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #beck-peterson title="Three-column counts and triangles" mathesis="collected:hardin-barker-a209723-edge-differences:2:s3" status="written-proof" proof="pf-beck-peterson" doi="10.5281/zenodo.23903301" source="Corollary 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/224"}
For $n\geq1$, the three-column sequence A209721 satisfies

$$
u(n)=\mathrm{A029744}(n+1)+1.
$$

For $n\geq3$,

$$
u(n)=2u(n-2)-1.
$$

For $n\geq3$, $u(n)$ also counts nondegenerate integer triangles with two specified side lengths $u(n-1),u(n-2)$, meaning the number of positive integer choices for the third side.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-beck-peterson}
Set $k=2$ in [@rectangular-count]. Since $b(2)=3$, $u(n)=b(n)+1$. The defining sequence A029744 gives $b(n)=\mathrm{A029744}(n+1)$, proving Beck's first conjecture. Since $b(n)=2b(n-2)$ for $n\geq3$, we obtain $u(n)=2(u(n-2)-1)+1=2u(n-2)-1$, Peterson's recurrence.

The parity formulas make the sequence strictly increasing: $b(2m+2)-b(2m+1)=2^m>0$ and $b(2m+3)-b(2m+2)=2^m>0$. Put $A=u(n-1)>B=u(n-2)>0$. The strict triangle inequalities for the third side $c$ are equivalent to $A-B<c<A+B$. Hence $c$ ranges over all integers from $A-B+1$ through $A+B-1$, giving $2B-1=u(n)$ choices. The endpoints would be degenerate and are excluded. At the first index $n=3$, the specified sides are $4,3$ and the third side can be $2,3,4,5,6$: five choices, agreeing with $u(3)=5$.
:::

## Square grids

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #diagonal title="The square-grid diagonal" mathesis="collected:hardin-barker-a209723-edge-differences:2:s4" status="written-proof" proof="pf-diagonal" doi="10.5281/zenodo.23903301" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/223"}
For every $n\geq1$, the diagonal of A209727 satisfies

$$
T(n,n)=2b(n)-2=\mathrm{A027383}(n).
$$
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-diagonal}
Set $k=n$ in [@rectangular-count] to obtain $T(n,n)=2b(n)-2$. At even indices $n=2m\geq2$ this is $3\cdot2^m-2$; at odd indices $n=2m+1\geq1$ it is $2^{m+2}-2$. These are the defining parity formulas of A027383. The array diagonal starts at $n=1$ with $2,4,6,10,14,\ldots$. Although A027383 also has an index-zero term, there is no shift here and no assertion about $T(0,0)$.
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## Recurrences, series and growth at every width

These are direct substitutions in [@rectangular-count], as in manuscript §3. Put $C_k=b(k)-2$ and $A_k(x)=\sum_{n\geq1}T(n,k)x^n$. For fixed $k\geq1$,

$$
\begin{aligned}
T(2m+1,k)&=2^{m+1}+C_k,\\
T(2m+2,k)&=3\cdot2^m+C_k\qquad(m\geq0).
\end{aligned}
$$

<section hidden="hidden">

```{=typst}
]
```

</section>

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

Thus $T(n+2,k)=2T(n,k)-C_k$ for $n\geq1$. Subtract consecutive instances to obtain

$$
\begin{gathered}
\begin{aligned}
T(n,k)&=T(n-1,k)+2T(n-2,k)\\
&\qquad-2T(n-3,k),
\end{aligned}\\
n\geq4.
\end{gathered}
$$

<section hidden="hidden">

```{=typst}
]
```

</section>

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

At $k=1$, $C_1=0$, giving the stronger recurrence $T(n,1)=2T(n-2,1)$ for $n\geq3$. Also,

$$
A_k(x)=\frac{x\bigl((C_k+2)+x-(2C_k+3)x^2\bigr)}{(1-x)(1-2x^2)}.
$$

<section hidden="hidden">

```{=typst}
]
```

</section>

Indeed, put $A_k=B+C_kx/(1-x)$ over a common denominator: the numerator is $(2x+3x^2)(1-x)+C_kx(1-2x^2)$. Width parameters $k=2,3,4,5,6,7$ give constants $C_k=1,2,4,6,10,14$, corresponding to A209721–A209726. The first column of the counting table is $b(n)=\mathrm{A029744}(n+1)$.

For every fixed $k\geq1$, $T(n,k)^{1/n}\to\sqrt2$. In detail, $b(n)/2^{n/2}$ is $\sqrt2$ for odd $n$ and $3/2$ for even $n$. As $C_k\geq0$, we have $\sqrt2\,2^{n/2}\leq T(n,k)\leq(3/2+C_k)2^{n/2}$. Taking $n$th roots, the constant factors tend to one, and squeezing proves the limit. The width is fixed; this is not a claim about widths growing with $n$.
