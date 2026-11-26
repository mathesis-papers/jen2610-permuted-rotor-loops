# Which terms cancel when we change the return order?

Turn a sheet of paper, then flip it. Swap the moves and you may get a different result. Now imagine moves $1,2,3$, followed by one undo for each move. Undoing in order $3,2,1$ cancels the moves from the middle out. Undoing in order $1,2,3$ or $2,1,3$ need not return the paper to its start. Can the return order still tell us how to calculate a useful number?

## Three turning planes

Take three perpendicular unit directions $e_1,e_2,e_3$. Use $e_i e_j$ to name an oriented plane. In the paper's triangle example, $e_i^2=-1$, and distinct directions change sign when swapped. Set $B_1=e_1e_2$, $B_2=e_1e_3$, and $B_3=e_2e_3$. Each squares to $-1$, and swapping two different $B_i$'s changes the sign. Yet $B_1B_2B_3=-1$: the first two multiply to $B_3$, leaving $B_3^2$. These plane elements are **bivectors**, and the arithmetic that contains numbers, directions, and their products is a **Clifford algebra**.

Write a turn as $U_i=c_i+s_iB_i$, with $c_i=\cos(\theta_i/2)$ and $s_i=\sin(\theta_i/2)$. Its undo is $\widetilde U_i=c_i-s_iB_i$: multiplying them gives $c_i^2+s_i^2=1$. Rather than finding the entire combined move, we keep only its ordinary real-number component, the **scalar part** $t$. For instance, $t(2+3B_1)=2$.

Jenzer's Theorem 5.5 imposed an extra rule: the ordered product of any nonempty selection of the bivectors must have scalar part zero. Remark 5.5 asks whether we can drop that *star condition*. The triangle breaks the rule. Its forward product has scalar part $c_1c_2c_3-s_1s_2s_3$, not just the product of the cosines.

## Count the pairs that keep their order

Let $I=\{1,\dots,k\}$; let $\tau$ list the return indices in order; and write $\iota(\tau,S)$ for the number of pairs in $S$ that are reversed on the way back. Set $w_i=s_i^2$. Imagine flipping independent biased coins: index $i$ joins $S$ with probability $w_i$. Give a minus sign to each selected pair whose order **stays the same** on the return leg. The scalar part is the average of the resulting sign.

::: {.theorem #loop-formula mathesis="collected:jen2610-permuted-rotor-loops:5:s1" lean="D5/S3/QuadraticForms/JenzerPermutedRotorLoop.result" title="The subset formula for every return order"}
Let $V$ be finite-dimensional over the reals with a nondegenerate quadratic form $q$ of any signature. In $\mathrm{Cl}(V,q)$, for every $k\ge1$, every pairwise anticommuting bivector family with $B_i^2=-1$, every real angle vector and every return permutation $\tau$, the loop $\Theta_k(\tau)=U_1\cdots U_k\widetilde U_{\tau(1)}\cdots\widetilde U_{\tau(k)}$ satisfies
$$
t(\Theta_k(\tau))=\sum_{S\subseteq I}(-1)^{|S|(|S|+3)/2+\iota(\tau,S)}\prod_{i\in S}w_i\prod_{i\notin S}(1-w_i).
$$
The star condition is not required.
:::

The exponent $|S|(|S|+3)/2$ has the same parity as $\binom{|S|}{2}$. Removing the reversed pairs leaves exactly the pairs that keep their order. For return order $2,1,3$, those pairs are $\{1,3\}$ and $\{2,3\}$. Set all three $w_i$ to $1/2$. If 3 is not selected, the sign is positive. If it is selected, the four choices of 1 and 2 give $+,-,-,+$. The overall average is $1/2$. Change the return to $3,2,1$ and there are no pairs to count: the average is $1$. Restrict to a single counted pair $i,j$ and the answer is $1-2w_iw_j$.

## What happened to the extra terms?

Select $S$ on the outward leg and $T$ on the return. When the sets match, every bivector has a partner. The signs from undoing, swapping and squaring combine to give the sign in the formula.

When the sets differ, remove repeated indices. The scalar part satisfies $t(xy)=t(yx)$, so conjugating by an invertible $B_j$ leaves it unchanged. Conjugation fixes $B_j$ but flips every other bivector. For a nonempty even number of remaining indices, choose $j$ inside; for an odd number short of the whole family, choose $j$ outside. The product changes sign in either case. Its scalar part therefore vanishes.

There is one possible exception: every index appears exactly once and $k$ is odd. Then $T$ is the complement of $S$. All these terms share a factor $t(B_1\cdots B_k)\prod_i c_i s_i$. To sum their signs, switch to markers $x_i$ that still swap with a minus sign but now square to zero. In this *exterior algebra*, swapping adjacent factors introduces only an even correction:
$$
(1+x)(1+y)=(1+2xy)(1+y)(1+x).
$$
Those corrections commute with everything. Move the return into reverse order and cancel each $(1+x_i)(1-x_i)=1$ from the middle. Only even-degree terms remain. The coefficient using all the markers once is thus zero for odd $k$, which cancels the whole exceptional group. **The terms need not vanish individually; their sum does.**

## What this does and does not tell us

Draw an edge between every pair that keeps its order. The sign now comes from the parity of the edges among the chosen vertices. No edges gives the constant 1. If an edge exists, keeping only its endpoints can realize every value from $-1$ to $1$. Disconnected pieces multiply independently, but no factorization can separate the endpoints of an edge. This probability model applies directly to the square-minus-one formula, not to arbitrary mixed signs. Nor does the scalar formula determine scalar parts of all powers: the paper's three-factor result cannot simply be carried over to four factors.

::: {.film src="001-return-order"}
From the triangle to subset signs: why the cancellation survives a reordered return.
:::

The seminar deck follows the same example and spells out the two sign arguments in its speaker notes.

::: {.slides src="return-order"}
English seminar slides and speaker notes.
:::

This reading follows Haobo Ma and Wenlin Zhang's [version 5](https://doi.org/10.5281/zenodo.24404942) (CC BY 4.0). The question is N. Jenzer's Remark 5.5, p. 19 of [*Star-Ordered Rotor Loops in Clifford Algebras*](https://arxiv.org/abs/2610.21593v1); his Theorem 5.2 already covers the same-order case. The paper traces conjugation averaging to Shirokov and odd exterior cancellation to Diehl–Reizenstein, with an antecedent in de Bruijn. Its contribution here is the extension to every return permutation, not those earlier results.
