# 来源与继续工作

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## 论文与先前工作

本书的数学来源为 Haobo Ma、Wenlin Zhang，*OEIS A209723: Barker's conjectures on distinct clockwise edge differences*，第 2 版（2026），[版本 DOI：10.5281/zenodo.23903301](https://doi.org/10.5281/zenodo.23903301)。许可为 CC BY 4.0。[概念 DOI](https://doi.org/10.5281/zenodo.23903300) 汇集各版；这里的引用指向第 2 版。原文 Theorem 1 在 §1 陈述，Lemma 1 与主定理证明在 §2，Corollaries 1–2 与配套计算在 §3。

<section hidden="hidden">

```{=typst}
]
```

</section>

- R. H. Hardin：[A209723](https://oeis.org/A209723)，五列计数问题，2012 年 3 月 12 日；Colin Barker，2018 年 7 月 12 日的奇偶公式与生成函数猜想。
- R. H. Hardin：[A209727](https://oeis.org/A209727)，所有长方形尺寸的计数表；归一化为实际填法数的四分之一。
- [A209721](https://oeis.org/A209721)：三列情形，Barker 的生成函数、Beck 的第一个猜想以及 Peterson 的递推式与三角形解释。
- [A209722](https://oeis.org/A209722)、[A209724](https://oeis.org/A209724)、[A209725](https://oeis.org/A209725)、[A209726](https://oeis.org/A209726)：四列及六至八列的配套公式。
- N. J. A. Sloane：[A029744](https://oeis.org/A029744)，两条交错翻倍的基本数列；R. K. Guy：[A027383](https://oeis.org/A027383)，方形网格的对角数列。
- Andrew，Math Stack Exchange 回答 [4995628](https://math.stackexchange.com/a/4995628)，2024 年 11 月 8 日：四列情形的方块证明提纲。
- R. P. Stanley，*Enumerative Combinatorics, Volume 1*，第 2 版，2012，§4.7，[DOI：10.1017/CBO9781139058520](https://doi.org/10.1017/CBO9781139058520)：转移矩阵法背景。本书直接给出所需走法计数，不要求读者预先学习矩阵。

## 哪些陈述已有直接的形式证明？

[@five-column] 直接对应[五列 Lean 定理](lean:D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209723EdgeDifferences.result)：数字先转成整数再相减，按原始有标号数组数除以四，奇偶公式覆盖所有正索引，递推从四开始，形式级数存在且常数项为零。任意宽度的 [@rectangular-count]、图分解 [@row-structure]、三角形推论 [@beck-peterson] 和对角推论 [@diagonal] 的书面证明均在上一章。

另有[三列 Lean 定理](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Combinatorics/Graph/Pressure/HardinBarkerA209721EdgeDifferences.lean#L150)，证明三列的三阶递推与形式生成函数。它可供三角形推论的形式化复用，但没有直接陈述该推论的全部结论。

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

## 参与形式化

待补的是形式证明，数学论证已经在论文中给出。使用同一组公共协作问题，避免为不同语言另开任务：

- [任意宽度的行图分解](https://github.com/the-omega-institute/trureturing-requests/issues/222)：证明两颗星及独立边的分解，供一般计数使用。
- [长方形计数与对角推论](https://github.com/the-omega-institute/trureturing-requests/issues/223)：复用分解得到一般公式；对角线由代入得到，与主结果共用该任务。
- [Beck–Peterson 恒等式与三角形解释](https://github.com/the-omega-institute/trureturing-requests/issues/224)：复用一般公式的三列特例，或已有三列形式证明，完成两步递推、数列识别与第三边计数。

<section hidden="hidden">

```{=typst}
]
```

</section>

贡献者先在相应问题说明准确范围与分支，再从自己的 fork 向 [trureturing 的 dev 分支](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) 提交聚焦的 PR，遵守现有证明准入、评审与 CI 规则。接纳后须核对冻结声明与完整书面陈述再更新引用；GitHub 合并不自动改变 Mathesis 的独立验证记录或积分。


<section hidden="hidden">

```{=typst}
#pagebreak(weak: true)
```

</section>
