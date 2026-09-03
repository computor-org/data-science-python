# Curve Analysis: Analytical and Numerical Solution

## Introduction

This task is about performing a curve analysis by solving a given function analytically with [SymPy](https://docs.sympy.org/latest/index.html) and numerically with [NumPy](https://numpy.org/doc/stable/). If you haven't
installed the package yet, do so in the terminal with `pip install sympy`.

Curve analysis is an important step in examining functions, where properties such as zeros, extreme points, inflection points, and behavior at infinity are determined. Finding zeros and derivatives of the functions is necessary for this and essential in Python. Finding solutions for functions can be done analytically or numerically, but comes with different challenges.

### Analytical Solution with SymPy

  SymPy provides a symbolic mathematics environment that allows you to symbolically manipulate mathematical expressions and functions.

  Use `sympy.diff()` in `analyt_curve_sketching.py` to calculate derivatives and `sympy.solve()` to determine zeros.
  Use `sympy.lambdify()` to convert SymPy functions to numerical functions that can be used with NumPy.
  Save the positions of the (real!) zeros as `roots_fun`. Those of the extreme values as `roots_fun_prime` and `eval_fun_prime`.


### Numerical Solution with NumPy

  Use the function `np.gradient()` in `num_curve_sketching.py` to calculate numerical derivatives.
  For determining zeros, use the value before the zero crossing. Use the command `np.sign()` and `np.where()` to find the indices of the zeros. Use $x$ values from $-3$ to $3$ with $10000$ evenly distributed values.
  Save the positions of the zeros as `x_zero`. Those of the extreme values as `x_extrem` and `y_extrem`.

### Functions

Choose one of the following functions or define your own function. For the test, however, you must use $f_1(x)$.

$$
\begin{aligned}
  f_1(x) &= -x^4 + 6x^2 - x - 2 \\
  f_2(x) &= \sin(x) + \cos(2x) \\
  f_3(x) &= e^{-x^2} \\
  f_4(x) &= \tanh(x) \\
  f_5(x) &= e^{-x^2} \sin(2 \pi x)
\end{aligned}
$$



## Task

  1. Define the function to be analyzed. Use one of the given functions or think of your own.

  2. Determine the zeros (roots) of the function and its derivative (see Hint). Save the roots as a list in the order that `sympy.solve()` returns it, but remove any solutions with imaginary parts.

  3. Visualize the functions as well as their zeros and extreme points, as well as the first derivative. Use different markers for zeros and extreme points to make them easily recognizable. Also create an appropriate legend, as well as title and axis labels.


  4. Output the values for $f(x) = 0$ and $f(0)$ with the `print` command.

  5. Do the same for the derived function.

  6. What do you notice when comparing the output of numerical and analytical values?

  7. Additionally, output the function and its derivative with the command `sympy.pprint`.

  8. Why does the numerical calculation of $f_5(x)$ work, but not the analytical one?

## Hints

- Note that the output of `sympy.solve` is analytical and still needs to be **evaluated**. The output should have the `type()` `float`.
- Consider packaging reused code into functions.
