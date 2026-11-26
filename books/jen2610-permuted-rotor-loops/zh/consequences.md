# 进一步的结论

这里沿用前文的 $I,\tau,t,U_i$；$B_S$ 始终按递增编号相乘，空积为 $1$。编号沿用[源论文第 5 版](https://doi.org/10.5281/zenodo.24404942)，而不是本书的显示编号。

::: {.lemma #trace-support mathesis="collected:jen2610-permuted-rotor-loops:5:s2" status="written-proof" proof="pf-trace-support" doi="10.5281/zenodo.24404942" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/545"}
**原文引理 2。** 在有限维实 Clifford 代数（非退化二次型）中，设 $k\ge1$，双向量 $B_i$ 两两反交换，且 $B_i^2=\varepsilon_i\in\{-1,1\}$。对每个非空 $D\subseteq I$，除非 $D=I$ 且 $k$ 为奇数，否则 $t(B_D)=0$。例外中也不保证非零。
:::

::: {.proof #pf-trace-support}
以 $B_j$ 共轭，因 $B_j^{-1}=\varepsilon_j B_j$，符号论证与平方为 $-1$ 时相同。非空偶数个编号选内部的 $j$，未用完的奇数个编号选外部的 $j$。标量部分不变而乘积变号，故标量部分为零。
:::

::: {.remark #odd-cancellation mathesis="collected:jen2610-permuted-rotor-loops:5:s3"}
**原文引理 3。** 在以 $e_1,\dots,e_k$ 为基的实外代数中，对任意排列 $\tau$，$(1+e_1)\cdots(1+e_k)(1-e_{\tau(1)})\cdots(1-e_{\tau(k)})$ 没有奇次分量。这是对每个奇次基系数的陈述，不仅是最高次系数。取该基的任意奇数个下标即可读出对应的系数结论。
:::

::: {.corollary #mixed-loop mathesis="collected:jen2610-permuted-rotor-loops:5:s4" status="written-proof" proof="pf-mixed-loop" doi="10.5281/zenodo.24404942" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/546"}
**原文推论 4。** 取引理 2 的双向量及任意实数 $c_i,s_i$，不要求归一化。对任意回程次序，
$$
t(\Theta_k(\tau))=\sum_{S\subseteq I}(-1)^{|S|(|S|+1)/2+\iota(\tau,S)}\prod_{i\in S}(\varepsilon_i s_i^2)\prod_{i\notin S}c_i^2.
$$
:::

::: {.proof #pf-mixed-loop}
引理 2 与引理 3 原样消去不同子集的总贡献。同子集配对时，$m=|S|$ 个双向量的乘积平方为 $(-1)^{m(m-1)/2}\prod_{i\in S}\varepsilon_i$。回程另给 $(-1)^{m+\iota(\tau,S)}$，相乘即所求。
:::

::: {.corollary #tracial-loop mathesis="collected:jen2610-permuted-rotor-loops:5:s5" status="written-proof" proof="pf-tracial-loop" doi="10.5281/zenodo.24404942" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/547"}
**原文推论 5。** 在任意有单位元的实结合代数中，设 $t$ 为线性泛函，$t(1)=1$ 且 $t(xy)=t(yx)$。取 $k\ge1$ 个两两反交换的元素，$B_i^2=\varepsilon_i1$，$\varepsilon_i=\pm1$。任取实数 $c_i,s_i$ 和 $\tau$；对先乘 $(c_i+s_iB_i)$、再按 $\tau$ 乘 $(c_i-s_iB_i)$ 的积应用 $t$，结果仍为推论 4 的公式。不需要分次、有限维数或反演。
:::

::: {.proof #pf-tracial-loop}
循环性给出共轭不变性，$\varepsilon_iB_i$ 仍是逆元。不同子集的符号计算可照搬，因为奇次外代数抵消只涉及形式记号，而与所取代数无关。同子集计算只用平方和 $t(1)=1$。
:::

::: {.corollary #polar-zero mathesis="collected:jen2610-permuted-rotor-loops:5:s6" status="written-proof" proof="pf-polar-zero" doi="10.5281/zenodo.24404942" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/548"}
**原文推论 6。** 在推论 4 中取同序回程与 $c_i^2-\varepsilon_i s_i^2=1$。设 $z_i=1+\varepsilon_i w_i+\mathrm i\varepsilon_i w_i$、$\rho_i=|z_i|$，并以 $\alpha_i=\operatorname{atan2}(\varepsilon_iw_i,1+\varepsilon_i w_i)$ 取角。标量部分为 $\operatorname{Re}[(1+\mathrm i)\prod_i z_i]=\sqrt2(\prod_i\rho_i)\cos(\pi/4+\sum_i\alpha_i)$。它恰在 $\sum_i\alpha_i\in\pi/4+\pi\mathbb Z$ 时为零；固定平方符号后，有能使它为零的参数当且仅当至少两个符号相同。两因子平方异号时，结果为 $1+2w_1w_2$，永不为零。
:::

::: {.proof #pf-polar-zero}
用 $\operatorname{Re}[(1+\mathrm i)\mathrm i^m]=(-1)^{m(m+1)/2}$ 识别同序子集和为复数乘积。所有 $z_i$ 非零，故余弦决定零点。其余参数置零时，两个负平方因子可各取角 $-3\pi/8$，两个正平方因子可各取 $\pi/8$；对应角分别在允许的 $[-\pi/2,0]$ 和 $[0,\pi/4)$。若所有符号相异，只有单因子或一正一负；前者标量为 1，后者由子集和得 $1+2w_1w_2$。
:::

::: {.corollary #chain-correction mathesis="collected:jen2610-permuted-rotor-loops:5:s7" status="written-proof" proof="pf-chain-correction" doi="10.5281/zenodo.24404942" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/549"}
**原文推论 7。** 在推论 4 的假设下，$t(U_1\cdots U_k)$ 对偶数 $k$ 为 $\prod_i c_i$；对奇数 $k$ 为 $\prod_i c_i+t(B_I)\prod_i s_i$。除 $k\equiv3\pmod4$ 外星条件自动成立；该例外中它等价于 $t(B_I)=0$。
:::

::: {.proof #pf-chain-correction}
展开单程积后应用引理 2。对奇数 $k$，反演将 $B_I$ 乘以 $(-1)^{k(k+1)/2}$，却不改变标量部分；当 $k\equiv1\pmod4$ 时因此也消失。
:::

::: {.corollary #three-factor-powers mathesis="collected:jen2610-permuted-rotor-loops:5:s8" status="written-proof" proof="pf-three-factor-powers" doi="10.5281/zenodo.24404942" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/550"}
**原文推论 8。** 在推论 4 中限制 $1\le k\le3$ 并假设 $c_i^2-\varepsilon_i s_i^2=1$。任意回程下令 $R=\Theta_k(\tau)$、$a=t(R)$，则 $R=a+K$，其中 $K$ 是简单双向量或零，且 $K^2=a^2-1$。对每个整数 $n\ge0$，$t(R^n)=T_n(a)$，其中 $T_0=1,T_1(x)=x,T_{n+1}(x)=2xT_n(x)-T_{n-1}(x)$（$n\ge1$）。
:::

::: {.proof #pf-three-factor-powers}
展开后约去重复编号。三因子时最高子集的系数由引理 3 消去；余下乘积长度至多二。两个不同双向量的乘积反演时变号，故在可能的 0、2、4 阶中只能有 2 阶。归一化给 $R\widetilde R=1$，所以 $K^2=a^2-1$。其四阶分量 $K\wedge K=0$，所以 $K$ 简单或为零。由 $R^2-2aR+1=0$ 得所述递推。原文四因子例有 $t(R)=-1/4$、$t(R^2)=-1/4\ne T_2(-1/4)$，说明限制不可删。
:::

::: {.corollary #order-graph mathesis="collected:jen2610-permuted-rotor-loops:5:s9" status="written-proof" proof="pf-order-graph" doi="10.5281/zenodo.24404942" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/551"}
**原文推论 9。** 在定理 1 的负平方情形，连边 $\{i,j\}$ 当且仅当 $i<j$ 与 $\tau^{-1}(i)<\tau^{-1}(j)$。设 $e_\tau(S)$ 为 $S$ 内的边数，则 $F_\tau(w)=t(\Theta_k(\tau))$ 等于对子集概率加权的 $(-1)^{e_\tau(S)}$ 之和。逆序的值域为 $\{1\}$；其他次序在 $[0,1]^k$ 上值域为 $[-1,1]$，且有零点。函数依连通分量分解，不能跨任何切断一条边的划分分解。因此恰在逆序时可分解为单变量函数的乘积。
:::

::: {.proof #pf-order-graph}
用全部编号对减去反序对，得到符号公式；概率权重给出界。非空图中只保留一条边的两个端点，其余权重置零，得到 $1-2w_iw_j$，已取遍区间。分量之间边数可加，因而乘积可拆。若切开这条边，限制在两端点时应分解成两个单变量函数；任一变量为零时恒为 1，迫使两个因子均为常数，与交叉项矛盾。
:::
