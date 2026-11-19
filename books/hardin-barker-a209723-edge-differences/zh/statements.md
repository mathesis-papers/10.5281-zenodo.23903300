# 精确陈述与证明

以下沿用原文的定义。$N(n,k)$ 是满足局部条件的、有标号的 $(n+1)\times(k+1)$ 数组数，$n,k\geq1$，每个数属于 $\{0,1,2\}$。对小方格 $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，局部条件是 $b-a,d-b,c-d,a-c$ 为两两不同的整数。令 $T=N/4$，并定义

$$
\begin{aligned}
b(2m+1)&=2^{m+1},\\
b(2m+2)&=3\cdot2^m\qquad(m\geq0).
\end{aligned}
$$

先陈述主要答案，再依次证明局部分类、图分解与计数，最后给出两个推论。各书面证明据 Haobo Ma 与 Wenlin Zhang 第 2 版原文展开。

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.theorem #rectangular-count title="长方形计数公式" mathesis="collected:hardin-barker-a209723-edge-differences:2:s1" status="written-proof" proof="pf-rectangular-count" doi="10.5281/zenodo.23903301" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/223"}
对所有 $n,k\geq1$，

$$
T(n,k)=b(n)+b(k)-2.
$$

特别地，$a(n)=T(n,4)$ 满足

$$
\begin{aligned}
a(2m+1)&=2^{m+1}+4,\\
a(2m+2)&=3\cdot2^m+4\qquad(m\geq0),
\end{aligned}
$$

且作为形式幂级数，

$$
\sum_{n\geq1}a(n)x^n=\frac{x(6+x-11x^2)}{(1-x)(1-2x^2)}.
$$
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

## 八种小方格

四个不同的差取自 $\{-2,-1,0,1,2\}$，且和为零，所以必为 $\{-2,-1,1,2\}$。差 $+2$ 与 $-2$ 不能在对边：例如上边差为 $2$、下边顺时针差为 $-2$ 时，上下两行都为 $02$，另外两个差同为零；其他方向由旋转得到。因此这两条边相邻，在其公共顶点取得极端值 $0$ 或 $2$。剩余顶点必须是 $1$，才会产生差 $1$ 与 $-1$。这恰好得到以下八个 $(a,b,c,d)$：

$$
\begin{aligned}
&(0,1,2,0),\ (0,2,1,0),\\
&(0,2,2,1),\ (1,0,0,2),\\
&(1,2,2,0),\ (2,0,0,1),\\
&(2,0,1,2),\ (2,1,0,2).
\end{aligned}
$$

逐项相减也验证每个都合格，从而同时证明必要性与充分性。两列卡片相邻的图正是

$$
\begin{aligned}
02&\longleftrightarrow\{10,21\},\\
20&\longleftrightarrow\{01,12\}.
\end{aligned}
$$

注意每张卡片的不同邻居的上端数字不同。

## 行图的结构

$H_k$ 的点为长度 $k+1$ 的所有行；两行可叠放时相邻。交换上下两行只会置换各差并取负，所以相邻关系对称。同一行不能与自己相邻，因为会出现两个为零的竖直差。于是这是一个无自环的无向图。数组与带指定起点的 $n$ 步走法一一对应；走法可以重复经过边和点。

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.lemma #row-structure title="行相容图的分解" mathesis="collected:hardin-barker-a209723-edge-differences:2:s2" status="written-proof" proof="pf-row-structure" doi="10.5281/zenodo.23903301" source="Lemma 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/222"}
对每个 $k\geq1$，$H_k$ 的非孤立部分由两个 $K_{1,2}$ 与 $2b(k)-4$ 个 $K_2$ 不交组成。
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-row-structure}
记 $R_{uv}=uvuvu\cdots$，截取长度 $k+1$。直接利用卡片图可得

$$
\begin{aligned}
R_{02}&\longleftrightarrow\{R_{10},R_{21}\},\\
R_{20}&\longleftrightarrow\{R_{01},R_{12}\}.
\end{aligned}
$$

例如上行为 $R_{02}$，首列卡片只能为 $01$ 或 $02$。前者的下一张卡片被迫为 $20$；后者在上端数字为 $2$ 的要求下被迫接 $21$。反复如此即得两个下行。交换 $0,2$ 得第二颗星。由于 $k+1\geq2$，这六行互不相同。

任取有邻居的行 $s$。由八种小方格，相邻数字不等。若不含 $1$，它必为 $R_{02}$ 或 $R_{20}$。否则，因长度至少为二，存在涉及 $1$ 的相邻对。从清单可见，上端对 $01,10,12,21$ 各只有一个下端对，分别为 $20,02,20,02$。该对一旦确定，向两边每次延伸时，下一个卡片的上端数字已经指定，而当前卡片至多有一个具有该上端数字的邻居。因此整行邻居至多一个。显示的四个叶子确有邻居，所以度恰为一；除两颗星外，任何非孤立分量都是 $K_2$。

数这些分量：一颗 $K_{1,2}$ 在 $2m$ 步时，三个起点各有 $2^m$ 条走法，总计 $3\cdot2^m$；在 $2m+1$ 步时，中心有 $2^{m+1}$ 条，两个叶子各有 $2^m$ 条，总计 $4\cdot2^m$。两颗星在每个正步数 $k$ 时合计 $4b(k)$ 条走法。

同一两行数组，按行读对应 $H_k$ 的有方向边，按列读对应卡片图中的 $k$ 步走法。这是一一对应，所以 $H_k$ 有 $4b(k)$ 条有方向边。两颗星占八条，余下每个 $K_2$ 占两条，故共有 $(4b(k)-8)/2=2b(k)-4$ 个。$k=1$ 时该数为零，论证仍成立。
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## 主公式的证明


::: {.proof #pf-rectangular-count}
利用 [@row-structure]。$n\geq1$ 时孤立点无贡献，两颗星贡献 $4b(n)$ 条走法，每个 $K_2$ 从任一端出发都只有一条走法，贡献二。因此

$$
\begin{aligned}
N(n,k)&=4b(n)+2(2b(k)-4),\\
T(n,k)&=b(n)+b(k)-2.
\end{aligned}
$$

取 $k=4$，$b(4)=6$，即得奇偶公式。为求生成函数，分别对两个奇偶子列求几何级数：

$$
B(x):=\sum_{n\geq1}b(n)x^n=\frac{2x+3x^2}{1-2x^2}.
$$

于是 $A(x)=B(x)+4x/(1-x)$。通分后分子为 $(2x+3x^2)(1-x)+4x(1-2x^2)=6x+x^2-11x^3$，得到所述结果。分母的常数项均为一，因此在形式幂级数环中可逆，无须解析收敛假设。
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

## 五列情形的精确形式化范围

下述结论是 [@rectangular-count] 的五列特例，加上原文 §3 的递推式；它不是任意宽度的形式化。

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.theorem #five-column title="五列的奇偶、递推与形式级数" mathesis="collected:hardin-barker-a209723-edge-differences:2:s1" lean="D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result"}
令 $a(n)=N(n,4)/4$，其值视为有理数。对每个 $m\geq0$，

$$
\begin{aligned}
a(2m+1)&=2^{m+1}+4,\\
a(2m+2)&=3\cdot2^m+4.
\end{aligned}
$$

对所有 $n\geq4$，

$$
a(n)=a(n-1)+2a(n-2)-2a(n-3).
$$

存在 $A\in\mathbb Q[[x]]$，其常数项为零，且对 $n\geq1$，$x^n$ 的系数为 $a(n)$。每个这样的 $A$ 都满足

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
奇偶公式来自 $a(n)=b(n)+4$。由 $b(n+2)=2b(n)$ 得 $a(n+2)=2a(n)-4$（$n\geq1$），再将相邻两式相减，得到 $a(n+3)-a(n+2)=2a(n+1)-2a(n)$，即所述递推。生成函数的系数构造给出存在性，前面的通分计算给出恒等式。此处的 Lean 链接直接陈述以上全部结论；$m+4$ 与 $n\geq4$ 是相同的索引范围。Lean 虽对所有自然数定义计数函数，但级数的零次系数是另行指定的零，并不等于在 $n=0$ 计算的数组数除以四。
:::

## 三列与整数三角形

为避免与五列的 $a(n)$ 混淆，本小节记 $u(n)=T(n,2)$；原文 Corollary 1 在此处使用符号 $a(n)$。

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #beck-peterson title="三列计数与三角形" mathesis="collected:hardin-barker-a209723-edge-differences:2:s3" status="written-proof" proof="pf-beck-peterson" doi="10.5281/zenodo.23903301" source="Corollary 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/224"}
对 $n\geq1$，三列数列 A209721 满足

$$
u(n)=\mathrm{A029744}(n+1)+1.
$$

对 $n\geq3$，

$$
u(n)=2u(n-2)-1.
$$

此外，$n\geq3$ 时，$u(n)$ 等于两条指定边长为 $u(n-1),u(n-2)$ 的非退化整数三角形的数量，即第三边的正整数取值数。
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-beck-peterson}
取 [@rectangular-count] 中的 $k=2$，利用 $b(2)=3$，得 $u(n)=b(n)+1$。A029744 的定义给出 $b(n)=\mathrm{A029744}(n+1)$，即 Beck 的第一个猜想。由 $b(n)=2b(n-2)$（$n\geq3$），得 $u(n)=2(u(n-2)-1)+1=2u(n-2)-1$，即 Peterson 的递推式。

奇偶公式说明数列严格递增：$b(2m+2)-b(2m+1)=2^m>0$，$b(2m+3)-b(2m+2)=2^m>0$。令 $A=u(n-1)>B=u(n-2)>0$。第三边 $c$ 满足严格三角形不等式恰等价于 $A-B<c<A+B$。因此 $c$ 可取从 $A-B+1$ 到 $A+B-1$ 的每个整数，共 $2B-1=u(n)$ 个。端点对应退化情形，不能计入。最小索引 $n=3$ 时两条边是 $4,3$，第三边为 $2,3,4,5,6$，共有 $5=u(3)$ 种。
:::

## 方形网格

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #diagonal title="方形网格的对角数列" mathesis="collected:hardin-barker-a209723-edge-differences:2:s4" status="written-proof" proof="pf-diagonal" doi="10.5281/zenodo.23903301" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/223"}
对所有 $n\geq1$，A209727 的对角线满足

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
在 [@rectangular-count] 中取 $k=n$ 即得 $T(n,n)=2b(n)-2$。偶数索引 $n=2m\geq2$ 时，这等于 $3\cdot2^m-2$；奇数索引 $n=2m+1\geq1$ 时，等于 $2^{m+2}-2$。这正是 A027383 的奇偶定义。数组对角线从 $n=1$ 起为 $2,4,6,10,14,\ldots$；A027383 虽有零索引项，此处没有移位，也未断言 $T(0,0)$。
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## 每个宽度的递推、生成函数与增长率

这些是 [@rectangular-count] 的直接代入计算（原文 §3）。令 $C_k=b(k)-2$，$A_k(x)=\sum_{n\geq1}T(n,k)x^n$。对固定的 $k\geq1$，

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

因此 $T(n+2,k)=2T(n,k)-C_k$（$n\geq1$）。相邻两式相减给出

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

$k=1$ 时 $C_1=0$，于是有更强的两步递推 $T(n,1)=2T(n-2,1)$（$n\geq3$）。此外

$$
A_k(x)=\frac{x\bigl((C_k+2)+x-(2C_k+3)x^2\bigr)}{(1-x)(1-2x^2)}.
$$

<section hidden="hidden">

```{=typst}
]
```

</section>

证明只需将 $A_k=B+C_kx/(1-x)$ 通分，分子为 $(2x+3x^2)(1-x)+C_kx(1-2x^2)$。$k=2,3,4,5,6,7$ 分别给出常数 $C_k=1,2,4,6,10,14$，对应 A209721–A209726；第一列是 $b(n)=\mathrm{A029744}(n+1)$。

对每个固定 $k\geq1$，还有 $T(n,k)^{1/n}\to\sqrt2$。具体说，奇数 $n$ 时 $b(n)/2^{n/2}=\sqrt2$，偶数时该比值为 $3/2$。所以 $\sqrt2\,2^{n/2}\leq T(n,k)\leq(3/2+C_k)2^{n/2}$，因 $C_k\geq0$。两端取 $n$ 次方根，常数的 $n$ 次方根趋于一，夹逼即得极限。这是固定宽度的结论，不涉及宽度随 $n$ 增长的情形。
