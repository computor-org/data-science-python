[np.cumsum]: <https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html> "np.cumsum"
# Approximation of $\pi$ with Series

## Introduction

One of the most important and partly fastest methods to calculate $\pi$ is using series. For this reason, various series that have played a major role in the history of $\pi$ are presented here:


1. Gottfried W. Leibniz, one of the founders of differential calculus, derived a series representation of $\frac{\pi}{4}$ in 1682, which is still called the Leibniz series in his honor today.
$$ \frac{\pi}{4} = \sum ^{\infty} _{k=0} \frac{(-1)^k}{2k+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \dots$$
This series can also be obtained via the Taylor expansion of the $\arctan$ function evaluated at point $1$, since $\arctan (1) = \frac{\pi}{4}$.

2. Since the Leibniz series unfortunately converges very slowly to $\pi$, the mathematician John Machin continued to work with the series expansion of $\arctan$ and found a very fast converging series:
$$\frac{\pi}{4} = 4 \arctan \frac{1}{5} - \arctan \frac{1}{239} = 4 \cdot \sum ^{\infty} _{k=0} (-1)^k \frac{\left( \frac{1}{5}\right)^{2k+1} }{2k+1} - \sum ^{\infty} _{k=0} (-1)^k \frac{\left( \frac{1}{239}\right)^{2k+1} }{2k+1}$$
With this series, he calculated $\pi$ to 100 decimal places in 1706. It is still often used today for the numerical calculation of $\pi$.

3. Euler already quoted $\pi$ with 148 digits in his first published volume <i>Introductio in Analysin Infinitorum</i> (1748). He discovered several formulas for calculating $\pi$, almost all of which can be traced back to the series expansion of $\frac{\sin (x)}{x} = 1 - \frac{x^2}{3!}+\frac{x^4}{5!}-\frac{x^6}{7!}$. An example of this is:
$$\frac{\pi ^2}{6} = \sum ^{\infty} _{k=1} \frac{1}{k^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots$$
The series discovered by Euler also corresponds to the Riemann $\zeta$ function at point $2$, $\zeta (2) = \frac{\pi ^2}{6}$.

4. A very modern series is the Bailey-Borwein-Plouffe formula (BBP formula), which was only found in 1995. This not only enables a very fast calculation of $\pi$, but can also be used to calculate individual digits of $\pi$ without knowing the previous ones.
$$\pi = \sum ^{\infty} _{k=0} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right)$$

## Task

Complete the following tasks:

1. Create the variable `N = 25` and with it the arrays `k0` (goes from `0` to `N - 1`) and `k1` (goes from `1` to `N`). `k0` should be used for those series that start at zero and `k1` for those that start with $k = 1$. Since you will be working with very small numbers in some cases, initialize `k0` and `k1` as `np.float64`.

2. Save in the arrays `pv1`, `pv2`, `pv3`, and `pv4` the approximation for the above series. `pv1` should contain the individual steps of the Leibniz series, `pv2` those of Machin, `pv3` those of Euler, and `pv4` the values of the BBP formula. The easiest way is to create arrays that contain the individual summands and then add them with [np.cumsum]. [np.cumsum] forms the sum of all preceding components. Note that not all sums start with $k=0$! Do not use loops!

3. The values of the series still need to be raised to a power or multiplied by appropriate prefactors to yield $\pi$.

4. Now plot the result in two subplots one above the other. The $x$-axis should be the number of steps used for the series approximation (i.e., from `1` to `N`) for both plots. The first plot should contain a straight line at the value $\pi$ and the values of the series. The second plot should be semi-logarithmic in $y$ ([semilogy]). In this, enter the distance ( = `abs(pv-pi)` ) to $\pi$.


5. Create appropriate axis labels, titles, and labels for the task.


## Hints

* Reference plot:

<div align="center">
<img src="mediaFiles/plot.png" alt="Test Image" width="100%" name="Plot"/>
</div>
