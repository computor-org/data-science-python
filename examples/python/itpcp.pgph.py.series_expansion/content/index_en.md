[np.shape]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html> "shape"
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html> "ravel"
[np.meshgrid]: <https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html> "meshgrid"

# Sine Series Expansion

## Introduction

In this exercise, you will learn a new method for series calculation.

As a simple example for an infinite series, the Taylor series of the function sin($x$) is used here. This is given by

$$
\begin{aligned}
  \sin(x)
  &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots \\
  &= \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
  \; ,
\end{aligned}
$$

which converges for all $\lvert x \rvert < \infty$.
Such infinite series can be approximately calculated on a computer using finite partial sums. Depending on the chosen series and the values for $x$, they converge slower, faster, or not at all to the desired value.

Sums of this type can be programmed very well in NumPy without using for loops. The following information is useful:

Extremely practical for calculating such series is the command [np.meshgrid]. With it, you can create two equally sized matrices from a vector `x` with all $x$ values and a vector `k` with all $k$ values:

```python
x = np.arange(-2, 3)    # -2 to 2
k = np.arange(0, 6)     # 0 to 5
xx, kk = np.meshgrid(x, k)
```

```python
>>> xx
array([[-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2]])

>>> kk
array([[0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5]])
```

With the command

```python
A = xx ** (2 * kk + 1)
```

you can now calculate e.g. $x^{2k+1}$ for all values of $x$ and $k$ simultaneously.

```python
>>> A
array([[   -2,    -1,     0,     1,     2],
       [   -8,    -1,     0,     1,     8],
       [  -32,    -1,     0,     1,    32],
       [ -128,    -1,     0,     1,   128],
       [ -512,    -1,     0,     1,   512],
       [-2048,    -1,     0,     1,  2048]])
```

The sum over all $k$ values can then be obtained using the `np.sum` command, where the dimension along which to sum is given via the `axis` keyword. Here we want to sum down the rows (axis 0) so that one entry remains for each $x$:

```python
>>> S = np.sum(A, axis=0)
>>> S
array([-2730,    -6,     0,     6,  2730])
```

Each element of `S`, ($\{S\}_{x}$) is calculated by summing over the $x$ column

$$\{S\}_{x} = \sum_{k = 0}^{n} A_{k, x} = A_{0, x} + \dotsb + A_{n, x} \; .$$

Since NumPy is optimized for matrix calculations, the program runs significantly faster with larger data sets than with the usual for loops.

Instead of using the sum, the entire series evaluation can also be performed using matrix multiplication. From linear algebra, it is known that for a $(1 \times n)$ vector $f$ (row vector) and an $(n \times m)$ matrix $A$

$\{f \cdot A\}_{l} = \sum_{k} f_{k} A_{kl} \; . $

If you now create the vector $f = (−1)^{k} / (2k + 1)!$ for all values of $k$, you can obtain the respective value of the partial sum for all values of $x$ simultaneously with
$f \cdot A$ (in Python `f.dot(A)`). (With these specific examples for $A$ and $f$, you get the series expansion for the sine.)

## Task

Write a function `series_expansion` that is called with

```python
r, u = series_expansion(x, n)
```

`x` is an arbitrary array of $x$ values for which the series
is to be evaluated. `n` (scalar) is the index up to which to sum.
The return value `r` should be the $n$-th partial sum

$$
  r(x) = \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
$$

For `u`, the analytical value of the function

$$
u = \sin(x).
$$

should also be calculated. Proceed as follows:

1. Save the size of `x` ([np.shape]) in a variable and then convert the variable to a vector ([np.ravel]). Further calculations are easier with a vector, and no information is lost by saving the original size.

2. Use the command [np.meshgrid] to calculate the series, as described in the introduction. This eliminates the need for for loops. Save the result of the $n$-th partial sum in `r`.

3. Calculate the analytical value for `u`.

4. Reshape the vectors `r` and `u` with the previously saved variable so that they have the original size of `x`.

5. Calculate and plot for $x \in [-\pi, \pi]$ (uniformly distributed with 100 support points) the analytical function together with the first 3 partial sums (i.e. for $n = 0, 1, 2$). Use a loop for the partial sums. Plot the analytical function as a dashed line (`linestyle` argument) and leave the partial sums in the default solid line style. Create a legend with the labels `'sin(x)'`, `'1. partial sum'`, `'2. partial sum'`, `'3. partial sum'` (in that order; `n = 0` is labelled as the 1st partial sum).