# From one square to every rectangle

<style>pre:has(> code[class*="typst"]) { display: none; }</style>

Fill a rectangular grid with $0,1,2$. In every adjacent $2\times2$ square, go clockwise and subtract consecutive entries. Require the four signed differences to be different. How many fillings work? Haobo Ma and Wenlin Zhang give an exact answer for every rectangle with at least two rows and two columns. The mechanism is surprisingly small: two three-vertex stars and a collection of separate edges.

For $n+1$ rows and $k+1$ columns, with $n,k\geq1$, let $N(n,k)$ be the actual number of fillings and use the OEIS normalization $T(n,k)=N(n,k)/4$. Then

$$
T(n,k)=b(n)+b(k)-2,
$$

where $b(1),b(2),b(3),\ldots=2,3,4,6,8,12,\ldots$: every other term doubles. Height and width contribute separately, by addition. The purpose of this chapter is to explain why.

This reading explains version 2 of the paper. [Precise statements and proofs](statements.md) supplies the complete argument; [Sources and further work](sources.md) gives the references and formalization contribution route. The original authors are Haobo Ma and Wenlin Zhang.

## Subtraction has a direction

```{=typst}
#block(breakable: false)[
```

Start with a single square:

$$
\begin{pmatrix}0&1\\2&0\end{pmatrix}.
$$

```{=typst}
]
```

Starting at the upper left and going clockwise gives

$$
\begin{aligned}
1-0&=1,&0-1&=-1,\\
2-0&=2,&0-2&=-2.
\end{aligned}
$$

These four numbers differ, so the square is allowed. They are signed integer differences, rather than absolute differences or subtraction modulo $3$. A square filled entirely with zero fails: every difference is zero.

Why are allowed squares rare? A difference can only be $-2,-1,0,1,2$. The four differences add to zero because a trip around the square returns to the starting value. The five possible differences also add to zero, so the omitted value must be zero. Every allowed square therefore uses exactly $-2,-1,1,2$. This restriction reduces the $3^4=81$ possible local fillings to eight.

The division by four is a numerical normalization in the problem. We count fillings of labelled positions; we do not identify rotations, reflections or renamed symbols. For example, a $2\times2$ grid has eight allowed fillings, giving $T(1,1)=2$. The formula agrees: $2+2-2=2$.

## Read two rows vertically: the first two stars

Treat a column as a little card: $02$ means zero above two. Two cards may stand next to one another exactly when their square is allowed. The eight allowed squares give just these connections:

$$
\begin{aligned}
10&\longleftrightarrow02\longleftrightarrow21,\\
01&\longleftrightarrow20\longleftrightarrow12.
\end{aligned}
$$

Each line is a three-vertex star: one center with two leaves. The remaining cards $00,11,22$ have no connections. An allowed two-row strip is a walk on these two stars. Each step adds a column, so $k$ steps give $k+1$ columns. Walking back along an edge and revisiting a card are allowed. The starting card is part of the choice.

From a star's center, two steps mean “choose a leaf, then return to the center”: two choices. From a specified leaf, two steps mean “return to the center, then choose a leaf”: again two choices. Thus a walk of $2m$ steps has $3\cdot2^m$ possibilities across the three starting vertices. For $2m+1$ steps, the center contributes $2^{m+1}$ walks and each leaf contributes $2^m$, totaling $4\cdot2^m$.

For every positive length $r$, the two stars together contribute $4b(r)$ walks, where

$$
\begin{aligned}
b(2m+1)&=2^{m+1},\\
b(2m+2)&=3\cdot2^m\qquad(m\geq0).
\end{aligned}
$$

## Make a whole row a vertex: wider grids add no branching

Fix the width $k+1$. Now a vertex is a complete row. Join two vertices when those rows may be stacked without violating any square. Call this the row-compatibility graph $H_k$. A whole grid is a walk of $n$ steps: its start gives the first row and each step adds a row. Turning local restrictions into walks is the idea behind the transfer-matrix method.

The decisive observation is that only two rows can branch, however wide the grid is. They alternate zeros and twos: at width five, they are $02020$ and $20202$. The first can meet $10101$ or $21212$; the second can meet $01010$ or $12121$. The two stars survive.

Any other row with a neighbor contains a $1$. Some adjacent pair therefore involves $1$, and the eight allowed squares uniquely determine the two entries beneath that pair. Extend left and right. Every new column has at most one choice: in the card graph above, a card's neighbors have different upper entries. Once a small piece of the next row is fixed, the whole next row is forced. Every vertex other than the two star centers has at most one neighbor. Outside the stars, the usable graph consists of separate edges.

How many separate edges? A two-row grid read horizontally is a directed edge of $H_k$; the same grid read vertically is a $k$-step walk in the card graph. There are $4b(k)$ directed edges altogether. The two stars use eight, and each separate edge uses two. There are therefore $2b(k)-4$ separate edges.

The film follows this same square, card and walk construction.

::: {.film src="001-two-stars"}
Two stars count the grids: how a local restriction determines a whole rectangle. English narration with aligned Chinese and English subtitles.
:::

## Add the two contributions

For $n\geq1$, isolated vertices contribute no walks. The two stars contribute $4b(n)$ walks of length $n$. Each separate edge contributes exactly two walks of any positive length, one from each end. Consequently,

$$
\begin{aligned}
N(n,k)&=4b(n)+2\bigl(2b(k)-4\bigr),\\
T(n,k)&=b(n)+b(k)-2.
\end{aligned}
$$

At five columns, $k=4$ and $b(4)=6$, so there are eight separate edges. Two rows and five columns have $4b(1)+16=24$ actual fillings, giving normalized count $6$. Three rows and five columns have $4b(2)+16=28$, giving $7$. Continuing produces OEIS A209723: $6,7,8,10,12,16,\ldots$.

## Read more information from the same formula

For five columns write $a(n)=T(n,4)$. Since $a(n)=b(n)+4$,

$$
\begin{aligned}
a(2m+1)&=2^{m+1}+4,\\
a(2m+2)&=3\cdot2^m+4\qquad(m\geq0).
\end{aligned}
$$

```{=typst}
#block(breakable: false)[
```

The identity $b(n+2)=2b(n)$ gives $a(n+2)=2a(n)-4$ for $n\geq1$. Subtract this identity at consecutive indices to eliminate the constant and obtain Hardin's recurrence:

$$
\begin{gathered}
a(n)=a(n-1)+2a(n-2)-2a(n-3),\\
n\geq4.
\end{gathered}
$$

```{=typst}
]
```

We can also store the sequence in a formal expression $A(x)=6x+7x^2+8x^3+\cdots$: the coefficient of $x^n$ records $a(n)$. This is a generating function. Doubling every other term gives the denominator $1-2x^2$, and adding four each time gives $4x/(1-x)$. Together these yield

$$
A(x)=\frac{x(6+x-11x^2)}{(1-x)(1-2x^2)}.
$$

This is an identity of formal power series: no real value of $x$ or convergence assumption is needed. Its constant term is deliberately zero; this does not extend the array formula to $n=0$.

The rectangle formula also gives $u(n)=T(n,2)=b(n)+1$ for three columns, so $u(n)=2u(n-2)-1$ for $n\geq3$. At these indices, if two triangle sides are specified as $u(n-1)$ and $u(n-2)$, there are exactly $u(n)$ positive integer choices for the third side: the strict triangle inequalities give an interval containing $2u(n-2)-1$ integers. Square grids give $T(n,n)=2b(n)-2$. The next chapter proves these connections with their index ranges.

The academic presentation follows the square–card–row–count progression and includes a technical appendix and speaker notes.

::: {.slides src="seminar"}
From squares to two stars: aligned Chinese and English academic presentations.
:::

R. H. Hardin posed these OEIS counting problems, and Colin Barker conjectured the five-column parity formulas and generating function. Andrew gave a tile-based proof outline for four columns in 2024. This paper treats all widths through the graph decomposition. The five-column parity formulas, recurrence and formal series have a direct [Lean source](lean:D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result); this reading supplies the manuscript's written proofs for arbitrary width and the consequences above. The paper does not address Beck's second conjecture concerning zero positions in A309019 minus A002487, or Reverter i Bigas's smallest-integer/divisor conjecture in A209724.
