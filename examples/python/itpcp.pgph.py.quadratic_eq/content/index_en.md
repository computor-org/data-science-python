# Control Structures: The for Loop

In this exercise, you are asked to solve quadratic equations once using a `for` loop and once using logical indexing.

## Mathematical Background

A quadratic equation of the form

$$
    ax^2 + bx + c = 0 \qquad a,b,c \in \mathbb{R}
$$

has the following solutions

$$
  \begin{aligned}
    x_{1,2} &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    && a \neq 0 \\
    x_{1} &= -\frac{c}{b}
    && a = 0 \wedge b \neq 0 \\
    x_{1} &= 0 \qquad \text{trivial solution}
    && a = 0 \wedge b = 0 \wedge c = 0
  \end{aligned}
$$

The expression

$$
    d = b^2 - 4ac
$$

is called the discriminant. In the case $a \neq 0$, its value determines whether there are
two real solutions, one real double solution, or two complex conjugate solutions.
We define that $x_1$ is the solution with $+$ and $x_2$ is the solution with $-$.

For the case

$$
    a = 0 \wedge b = 0 \wedge c \neq 0
$$

there is no solution.

## Task

### For-Loop
Create the Python script `quadratic_eq_for`, which contains the function `quadratic_eq_for` that is called with

```python
def quadratic_eq_for(a, b, c):
    # ...
    return x_1, x_2
```

to solve the quadratic equation with coefficients `a`, `b`, and `c`.

1. The coefficients `a`, `b`, and `c` are arrays of the same size with real numbers.
   This makes it possible to solve the equation for multiple values of the coefficients at once.

1. The results should be calculated as explained in the *Mathematical Background* and
   stored in the arrays `x_1` and `x_2`. `x_1` and `x_2` must then have the
   same size as the input parameters and may contain **complex values**.
   In the case that only one solution exists, the second
   return argument should be set to the value [nan].

1. To solve the problem, a `for` loop, `if`, and `elif` are to be used, and the
   following strategy is recommended:

   - Create arrays for `x_1` and `x_2` of the size of `a` and fill them everywhere
     with the value [nan] (use e.g. [ones_like] for this). Make sure that the arrays have the correct data type so that they can also store complex values later on.
   - Then go through all values of the arrays `a`, `b`, `c` in a loop,
     make a case distinction regarding the current parameters, calculate
     the solutions $x_1$ (and $x_2$) accordingly, and store them at the
     corresponding position in `x_1` (or `x_2`). Make **no** case distinction regarding the discriminant!

1. To verify the function, create the following arrays in the same script after the function:

$$
  \begin{aligned}
    a &= [0, 1, 2, 3, 4, \dotsc, 10] \\
    b &= [1, 2, 4, 8, 16, \dotsc, 1024] \\
    c &= [0, 1, 4, 9, 16, \dotsc, 100] \\
  \end{aligned}
$$

5. Then call your function with these coefficients and check the
   result for plausibility.

### Logical Indexing
Create the Python script `quadratic_eq`, which contains the function `quadratic_eq` that is called with

```python
def quadratic_eq(a, b, c):
    # ...
    return x_1, x_2
```

to solve the quadratic equation with coefficients `a`, `b`, and `c`.

1. The beginning of the task is identical to the previous example using a `for` loop. To solve the problem, *logical indexing* should be used this time, and the following strategy is recommended:

   - Create arrays for `x_1` and `x_2` of the size of `a` and fill them everywhere
     with the value [nan] (use e.g. [ones_like] for this). Make sure that the arrays have the correct data type so that they can also store complex values later on.
   - Then, use logical indexing to make a case distinction regarding the current parameters, which you can then use to calculate the solutions $x_1$ (and $x_2$) and store them in the
    corresponding location in `x_1` (or `x_2`). Make **no** case distinction regarding the discriminant!

1. To verify the function, create the following matrices in the same script after the function:

```python
a = np.reshape(np.arange(-5, 7), (3, 4))
b = a + 1
c = a - 1
```

5. Then call your function with these coefficients and check the
   result for plausibility.

Three things should be considered and taken into account:

- Why is it better to calculate the discriminant only once and then use it in the formula for $x_{1,2}$? Isn't it actually better to take the square root of the discriminant beforehand to then use this quantity directly in the formula for $x_{1,2}$?
- Can the discriminant also become negative? How should this be taken into account?
- How could the `for` loop version be adapted to also support multi-dimensional indexing?

## Hints

- If you initially create the arrays with `nan` entries, you don't need to store
  `nan` in the array again in case of a non-existent solution.

- You can also take the square root of negative numbers with `np.sqrt()` by adding
  `dtype=np.complex128`. For example `np.sqrt(-1,
  dtype=np.complex128)`.

- Examples of an $x_1$ output could look like this:

```python
[-0.00000000e+00       +0.j          1.19160798e+01       +0.j
  7.19722115e+01       +0.j          5.75994792e+02       +0.j
  5.18399923e+03       +0.j          4.97663999e+04       +0.j
  4.97664000e+05       +0.j          5.11882971e+06       +0.j
  5.37477120e+07       +0.j          4.45514108e+08       +0.j
  3.09586821e+09+88920960.46646732j]
```

```python
[ 0.        +0.j         -0.5       +0.8660254j  -0.25      +1.39194109j
 -0.16666667+1.72401341j -0.125     +1.99608993j -0.1       +2.23383079j
 -0.08333333+2.4480718j  -0.07142857+2.64478694j -0.0625    +2.82773651j
 -0.05555556+2.99948555j -0.05      +3.16188235j]
```

**Attention!** This is not the correct solution, other values for a, b, and c were
used.

[nan]: https://numpy.org/doc/stable/user/misc.html "nan"
[ones_like]: https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html "ones_like"
