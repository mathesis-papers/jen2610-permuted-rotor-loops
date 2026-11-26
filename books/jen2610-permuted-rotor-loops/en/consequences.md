# Further results

Keep the notation $I,\tau,t,U_i$ from the story. Products $B_S$ are in increasing order, with empty product $1$. The numbers below are those of the [v5 manuscript](https://doi.org/10.5281/zenodo.24404942), not this reading's display numbers.

::: {.lemma #trace-support mathesis="collected:jen2610-permuted-rotor-loops:5:s2" status="written-proof" proof="pf-trace-support" doi="10.5281/zenodo.24404942" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/545"}
**Manuscript Lemma 2.** Let $k\ge1$ and let $B_i$ be pairwise anticommuting bivectors in a finite-dimensional real Clifford algebra with a nondegenerate form, with $B_i^2=\varepsilon_i\in\{-1,1\}$. For nonempty $D\subseteq I$, $t(B_D)=0$ unless $D=I$ and $k$ is odd. The exception does not assert nonvanishing.
:::

::: {.proof #pf-trace-support}
Conjugate by $B_j$, whose inverse is $\varepsilon_j B_j$. This flips every generator except $B_j$. Choose $j$ inside a nonempty even set and outside a proper odd set; both choices negate the product but preserve its scalar part, which must therefore be zero.
:::

::: {.remark #odd-cancellation mathesis="collected:jen2610-permuted-rotor-loops:5:s3"}
**Manuscript Lemma 3.** In the real exterior algebra on a basis $e_1,\dots,e_k$, for every permutation $\tau$, $(1+e_1)\cdots(1+e_k)(1-e_{\tau(1)})\cdots(1-e_{\tau(k)})$ has no odd-degree component. This means every odd basis coefficient, not just the top one.
:::

::: {.corollary #mixed-loop mathesis="collected:jen2610-permuted-rotor-loops:5:s4" status="written-proof" proof="pf-mixed-loop" doi="10.5281/zenodo.24404942" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/546"}
**Manuscript Corollary 4.** Use the bivectors of Lemma 2 and arbitrary real $c_i,s_i$, without normalization. For any return permutation,
$$
t(\Theta_k(\tau))=\sum_{S\subseteq I}(-1)^{|S|(|S|+1)/2+\iota(\tau,S)}\prod_{i\in S}(\varepsilon_i s_i^2)\prod_{i\notin S}c_i^2.
$$
:::

::: {.proof #pf-mixed-loop}
Lemmas 2 and 3 remove the total off-diagonal contribution just as in the story. A diagonal word of length $m$ squares to $(-1)^{m(m-1)/2}\prod_{i\in S}\varepsilon_i$. The return contributes $(-1)^{m+\iota(\tau,S)}$; their product gives the sign above.
:::

::: {.corollary #tracial-loop mathesis="collected:jen2610-permuted-rotor-loops:5:s5" status="written-proof" proof="pf-tracial-loop" doi="10.5281/zenodo.24404942" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/547"}
**Manuscript Corollary 5.** Let $A$ be any unital associative real algebra with a linear functional $t$ satisfying $t(1)=1$ and $t(xy)=t(yx)$. Let $k\ge1$ and take pairwise anticommuting elements with $B_i^2=\varepsilon_i1$, $\varepsilon_i=\pm1$. For arbitrary real $c_i,s_i$ and any return order, apply $t$ to the increasing product of $(c_i+s_iB_i)$ followed by the $\tau$-ordered product of $(c_i-s_iB_i)$. The value is the formula of Corollary 4. No grading, finite dimension or involution is needed.
:::

::: {.proof #pf-tracial-loop}
Cyclicity makes conjugation invisible to $t$, and $\varepsilon_i B_i$ remains the inverse of $B_i$. The exterior sign calculation is unchanged because it is performed on formal markers, not in $A$. The diagonal computation uses only the scalar squares and $t(1)=1$.
:::

::: {.corollary #polar-zero mathesis="collected:jen2610-permuted-rotor-loops:5:s6" status="written-proof" proof="pf-polar-zero" doi="10.5281/zenodo.24404942" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/548"}
**Manuscript Corollary 6.** In Corollary 4 take identity return order and $c_i^2-\varepsilon_i s_i^2=1$. Set $z_i=1+\varepsilon_i w_i+\mathrm i\varepsilon_i w_i$, $\rho_i=|z_i|$, and $\alpha_i=\operatorname{atan2}(\varepsilon_i w_i,1+\varepsilon_i w_i)$. The scalar equals $\operatorname{Re}[(1+\mathrm i)\prod_i z_i]=\sqrt2(\prod_i\rho_i)\cos(\pi/4+\sum_i\alpha_i)$. It vanishes exactly when $\sum_i\alpha_i\in\pi/4+\pi\mathbb Z$. With signs fixed, some parameters attain zero exactly when at least two signs agree. Two opposite signs give $1+2w_1w_2$, which never vanishes.
:::

::: {.proof #pf-polar-zero}
The identity $\operatorname{Re}[(1+\mathrm i)\mathrm i^m]=(-1)^{m(m+1)/2}$ turns the identity-order sum into a product. All $z_i$ are nonzero, so the cosine detects zeros. With the other parameters zero, two negative-square factors can each take angle $-3\pi/8$, and two positive-square factors can each take $\pi/8$: these lie in the attainable intervals $[-\pi/2,0]$ and $[0,\pi/4)$, respectively. With no repeated sign only one factor or an opposite-sign pair is possible. The subset sum gives $1$ or $1+2w_1w_2$, respectively.
:::

::: {.corollary #chain-correction mathesis="collected:jen2610-permuted-rotor-loops:5:s7" status="written-proof" proof="pf-chain-correction" doi="10.5281/zenodo.24404942" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/549"}
**Manuscript Corollary 7.** Under Corollary 4's hypotheses, $t(U_1\cdots U_k)$ equals $\prod_i c_i$ for even $k$ and $\prod_i c_i+t(B_I)\prod_i s_i$ for odd $k$. The star condition is automatic unless $k\equiv3\pmod4$; in that case it is equivalent to $t(B_I)=0$.
:::

::: {.proof #pf-chain-correction}
Expand the forward chain and apply Lemma 2. For odd $k$, reversion multiplies $B_I$ by $(-1)^{k(k+1)/2}$ but fixes its scalar part. This also removes the full-set term when $k\equiv1\pmod4$.
:::

::: {.corollary #three-factor-powers mathesis="collected:jen2610-permuted-rotor-loops:5:s8" status="written-proof" proof="pf-three-factor-powers" doi="10.5281/zenodo.24404942" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/550"}
**Manuscript Corollary 8.** In Corollary 4 take $1\le k\le3$ and impose $c_i^2-\varepsilon_i s_i^2=1$. For every return order, let $R=\Theta_k(\tau)$ and $a=t(R)$. Then $R=a+K$ with $K$ a simple bivector or zero and $K^2=a^2-1$. For every integer $n\ge0$, $t(R^n)=T_n(a)$, with $T_0=1,T_1(x)=x,T_{n+1}(x)=2xT_n(x)-T_{n-1}(x)$ for $n\ge1$.
:::

::: {.proof #pf-three-factor-powers}
Reduce repeated indices. For three factors the full-set coefficient vanishes by Lemma 3, so all remaining words have length at most two. A product of distinct bivectors changes sign under reversion; of its possible grades 0, 2 and 4, only grade 2 survives. Normalization gives $R\widetilde R=1$, hence $K^2=a^2-1$. Its grade-four part is $K\wedge K=0$, so $K$ is simple or zero. The equation $R^2-2aR+1=0$ gives the recurrence. The manuscript's four-factor example has $t(R)=-1/4$ and $t(R^2)=-1/4\ne T_2(-1/4)$, so the restriction matters.
:::

::: {.corollary #order-graph mathesis="collected:jen2610-permuted-rotor-loops:5:s9" status="written-proof" proof="pf-order-graph" doi="10.5281/zenodo.24404942" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/551"}
**Manuscript Corollary 9.** In Theorem 1's negative-square setting, join $\{i,j\}$ when $i<j$ and $\tau^{-1}(i)<\tau^{-1}(j)$. With $e_\tau(S)$ the induced edge count, $F_\tau(w)=t(\Theta_k(\tau))$ is the probability-weighted sum of $(-1)^{e_\tau(S)}$. Reverse return has range $\{1\}$; otherwise the range on $[0,1]^k$ is $[-1,1]$ and includes zero. The function factors across connected components and not across any partition cutting an edge. It is a product of single-variable functions exactly for reverse order.
:::

::: {.proof #pf-order-graph}
Subtract reversed pairs from all selected pairs to obtain the edge count. The probability weights give the bound. If an edge exists, set every other weight to zero to obtain $1-2w_iw_j$, which takes every value in the interval. Edge counts add across components, so their sums factor. A partition cutting the selected edge would factor this restriction into single-variable terms; setting either variable to zero forces both terms constant, contradicting the cross term.
:::
