# Zero runs and four-cycle capture

Start with two numbers, $0,1$. To get the next number, square the older one and add it to the newer one, then keep only the remainder on division by three. The next two numbers are $1$ and $2$. After that, $2+1^2=3$ leaves remainder $0$, and the pair of numbers has returned to $(0,1)$. From there the same instructions give the same future. This small example is the key both to searching an infinite sequence and to telling when a pattern guarantees repetition.

Haobo Ma and Wenlin Zhang’s [version 3 paper](https://doi.org/10.5281/zenodo.24408308) extends two questions of Steven R. Finch. Its first result shows that a bound on the length of a pattern need not be reached. Its second distinguishes when a sequence is already repeating from when a long enough pattern certifies that it is repeating.

## A sequence with a longer memory

Choose a lag $k\ge2$. The first $k-1$ entries are $0$ and entry $k$ is $1$. After that use $x_n=x_{n-1}+x_{n-k}^2\pmod 3$. All indices start at $1$. Squaring turns each nonzero entry into $1$ modulo three: $1^2$ and $2^2$ leave the same remainder. So each step either stays put or advances one place around the circle $0,1,2$.

A **run with $g$ gaps** begins at $r\ge k+1$ and has zeros at $r,r+4,\ldots,r+4g$, with no other zeros between them. It has $g+1$ zeros, and it can be part of a longer run. For instance, at lag two the block from position $5$ through $9$ is $0,1,1,2,0$: two zeros, one gap. The identical-looking block from $1$ through $5$ does not count, because it starts before $k+1$.

## Why fifteen is not always reached

Finch showed that for lags congruent to $0$ or $1$ modulo four, the number of gaps is at most $\lfloor(k-1)/4\rfloor$. The bound at lag $61$ is $15$. An upper bound does not promise a witness: the allowed length might never occur in this particular sequence.

::: {#lag-61 .remark mathesis="collected:finch-zero-runs:3:s1" title="Theorem 1: ten is the exact maximum at lag 61"}
At lag $61$ the maximum is exactly ten gaps, and the ten-gap runs start precisely at $2780+8946m$ for integers $m\ge0$. The least eventual period is $8946$ and the least $\mu$ such that $x_{n+8946}=x_n$ for all $n>\mu$ is $739$.
:::

The next term only needs the oldest and newest entries in the current window of $61$ terms. Write that window as a base-three number $S_j$ with the newest entry on the right; $S_0=1$ is the window ending at position $61$. To advance, discard the leftmost digit, shift the others left by one place, and append the new value. The state is the whole window, not just its newest digit. Only a repeated window guarantees that all later windows repeat.

The manuscript’s finite certificate checks that $S_0$ through $S_{9684}$ are distinct and that the next state is $S_{739}$. Thus the same $8946$ windows recur forever. This gives the *least* period and preperiod, not just a period: an earlier state repeat would contradict distinctness. An eventual period for the entries repeats every corresponding window, and a period for the windows already repeats the entries, by reading each window’s oldest digit.

To look for eleven gaps it is enough to inspect $45$ entries at the end of a window. Reading backwards preserves the pattern because $44$ is a multiple of four. None of the reachable windows passes this test. And any longer run would begin with eleven gaps. For ten gaps the test uses $41$ entries: the only matching window is $S_{2759}$, ending at position $2820$ and giving start $2780$. Its entries are ten copies of $(0,1,2,2)$ followed by $0$. Since the window is on the cycle, every recurrence of it gives another start exactly $8946$ places later. The finite list works because it is closed under the next step, not because it is long.

## Counting from the last disagreement

For a sequence whose least eventual period is four, write $\mu=\mu_A(k)$ for the least nonnegative index after which four-step repetition is exact, so the condition is $x_{n+4}=x_n$ for every $n>\mu$. Let $G=\lceil(k-1)/4\rceil$ and let $z$ be the earliest endpoint of an admissible $G$-gap run. This is called **capture**: a run ends with a zero and specifies at least $k$ consecutive zero/nonzero indicators. Those indicators, together with the endpoint value, determine the future. The start $s=z-4G$ need not be the first zero in the repeating tail.

::: {#capture .remark mathesis="collected:finch-zero-runs:3:s2" title="Theorem 2: the corrected capture offset"}
If $k\ge2$ and the least eventual period is four, then $z-\mu=9$ at $k=2$ and $z-\mu=6$ for $k\ge3$. In the latter case $k\equiv2$ or $3\pmod4$. The two cases give $s=\mu-k+4$ or $s=\mu-k+5$, and $(x_\mu,x_{\mu+1},x_{\mu+2})=(2,2,0)$ or $(1,2,0)$, respectively.
:::

At lag two, the opening example already repeats from the beginning, so $\mu=0$. Here $G=1$ and the first eligible pair of zeros is at $5$ and $9$. This explains why Finch’s original proposed offset of six fails even though it holds for every eligible larger lag.

For $k\ge3$, extend the repeating tail backwards as a four-periodic sequence $c$. Its increments around a cycle sum to zero modulo three, and the number of increments of size one is the number of nonzero entries. A least period of four therefore gives exactly three nonzeros. Starting with its unique zero, the block is $(0,1,a,2)$. The step that stays still must look back to the only zero; it occurs at offset two for $a=1$, and offset three for $a=2$. This forces the two permitted residues of $k$.

The initial stretch of $k$ ones from position $k$ forces $\mu\ge2k-3$ when $a=1$ and $\mu\ge2k-2$ when $a=2$: the cycle can supply at most two or one consecutive ones, respectively. Write $b_n=[x_n\ne0]$ and $L=\mu+2-k$. Comparing steps at index $n+k$ shows that for $n\ge L$ the indicators of $x$ and $c$ agree: both values used to compute the increment are already in the common tail. At $L-1$ the indicators differ, since equal indicators would force $x_\mu=c_\mu$. This is why the zero pattern can be known earlier than the actual values.

At $\mu$, the values disagree but are both nonzero. The first and last nonzero positions of the block cannot be the disagreement: the wrong value at either would force a forbidden step of size two. The middle position then gives the triples in Theorem 2. The recurrence at $\mu+1$ gives $b_{L-1}=0$ in residue class two and $1$ in residue class three. The first two zeros after $\mu$ are $\mu+2$ and $\mu+6$. No capturing run can end at or before $\mu$, because capture would force agreement with $c$ from that endpoint on. To end at $\mu+2$ the candidate starts at $L-2$ in residue class two, giving an extra interior zero at $L-1$, or at $L-1$ in class three, which is nonzero. Both fail. At $\mu+6$ the candidate starts at $L+2$ or $L+3$; the initial bounds on $\mu$ make it admissible, and the matching indicators give the full run.

::: {#neighborhood .remark mathesis="collected:finch-zero-runs:3:s3" title="Corollary 3: the zeros just before capture"}
Under Theorem 2’s hypotheses, the indicators just before the first start $s$ satisfy $b_{s-4}=1$ for larger lags in class two, and $b_{s-5}=0$, $b_{s-1}=1$ for class three. At $k=2$ the proposed neighborhood condition fails: $s=5$ but $b_{s-4}=b_1=0$.
:::

In both larger-lag cases $x_{\mu-1}=1$: in class two it follows a zero and is nonzero; in class three it is nonzero and must step into $x_\mu=1$. Hence the step into $x_\mu$ gives $b_{\mu-k}=1$ or $0$, at $s-4$ or $s-5$, respectively. In class three $s-1=L+2$ is a nonzero position in the matching indicators. The lag-two failure concerns this condition, not by itself the full equivalence proposed by Finch.

::: {.film src="001-zero-runs"}
From a repeating window to the two candidate capture endpoints.
:::

## Evidence and limits

The pinned Lean proof for lag $61$ rules out universal attainment using the missing eleven-gap pattern. It does not assert the ten-gap witness, all its starts, or the least period and preperiod. The pinned Lean proof for capture refutes the original assertion using lag two, not the general $k\ge3$ correction or Corollary 3. Those additions are written proofs in Ma and Zhang’s paper; the finite examples for other lags do not classify which sequences eventually have period four or settle Finch’s six individual attainment cases. The shared contribution requests cover the [exact lag-61 result](https://github.com/the-omega-institute/trureturing-requests/issues/367), the [conditional capture theorem](https://github.com/the-omega-institute/trureturing-requests/issues/368), and the [neighborhood conditions](https://github.com/the-omega-institute/trureturing-requests/issues/369).

The original definitions and questions are in [Finch’s *Three Quadratic Recurrences Modulo 3*, §§4, 6–7](https://arxiv.org/abs/2610.34300v1). [Finch’s 2002 note, §0.2](https://www.mit.edu/~sfinch/seqmod3.pdf) records B. Harder’s earlier computation of the period $8946$. [V. S. Miller’s account](https://mathoverflow.net/questions/50678/finchs-sequence-over-mathbbf-3) records R. Pinch’s explanation of the four-periodic patterns. The full arguments and certificate are in Ma and Zhang, *Extending Finch’s zero-run analysis*, version 3, §§1–4, CC BY 4.0.
