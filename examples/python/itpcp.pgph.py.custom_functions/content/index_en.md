[Docstring]: <https://en.wikipedia.org/wiki/Docstring#Python> "Docstring"
[exp]: <https://numpy.org/doc/stable/reference/generated/numpy.exp.html> "exp"
[cosh]: <https://numpy.org/doc/stable/reference/generated/numpy.cosh.html> "cosh"
[sqrt]: <https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html> "sqrt"

# Creating and Plotting Custom Functions

## Introduction

This exercise deals with creating and plotting custom functions.
For this, two Python functions `sgauss` and `secansh`, as well as a Python script `pscript` need to be created.
Note that <span style="color: red;">3 different py files</span> need to be filled by you!

### Functions

Functions allow you to define a specific code (e.g., an algorithm) only once and execute it multiple times with different parameters.
Functions receive values for the input variables (arguments) when called, perform calculations with them, and return output variables.
(You have already encountered some predefined functions in the previous exercises, for example `print` or `plot`).

Functions are defined with the keyword **`def`**.
An example of a simple function named `compute_sum`, which receives two variables `a` and `b`, calculates the sum, and returns the result with the keyword **`return`**, is:

```python
def compute_sum(a, b):
    """return the sum of two numbers a, b"""
    result = a + b
    return result
```

Important in Python is the indentation of the function definition! Unlike some other programming languages where the function block is delimited with { ... }, in Python everything that is indented at the same *level* belongs to the function.

At the beginning of the function definition, between three double quotation marks `""" ... """`, there should be a so-called *[Docstring]* that gives a brief description of the function.
This can be displayed later, e.g., with `help(compute_sum)`.

This above function can then be called as follows:

```python
new_var = compute_sum(3, 4)
```

The variable `new_var` now has the value 7.

It is also important to understand that the variables defined within a function are not available outside the function. So we cannot access `result` in the script.

Multiple return values can be returned separated by commas:

```python
def sum_and_diff(a, b):
    """returns the sum and difference of
    two numbers a and b"""

    return a + b, a - b

ab_sum, ab_diff = sum_and_diff(3, 4)
```

Here we get the value 7 for `ab_sum` and the value -1 for `ab_diff`.

It is useful to define important functions separately from the main script in their own files. This way they can be reused by other programs and help avoid hard-to-find errors.

Suppose we define our two functions `compute_sum` and `sum_and_diff` in a file `my_functions.py` in the same directory, with the content

```python
# ...put necessary imports for the function definitions here

def compute_sum(a, b):
    """return the sum of two numbers a, b"""
    result = a + b
    return result

def sum_and_diff(a, b):
    """returns the sum and difference of
    two numbers a and b"""

    return a + b, a - b
```

then we can import and use these functions in our main script:

```python
from my_functions import compute_sum, sum_and_diff

# Now we can use our defined functions
new_var = compute_sum(3, 4)
ab_sum, ab_diff = sum_and_diff(3, 4)
```

### Probability Distributions

* The function $$g = \frac{1}{s\sqrt{2\pi}} \exp \left( -\frac{(x-x_0)^2}{2s^2} \right)$$
    is the Gaussian function. It corresponds to the
    probability density of a probability distribution, namely the normal distribution.
    A probability density satisfies the condition that the area under the entire function
    equals 1. This so-called **normalization** is ensured by the normalization factor.
    The normalization factor of the function `g` is the
    term $1/(s\sqrt{2\pi})$.

* The function $$h = \frac{1}{\pi s} {\operatorname{sech}} \left( -\frac{x-x_0}{s} \right)$$
    is the hyperbolic secant. Like the Gaussian function, it represents a
    probability density and therefore also satisfies the condition that the
    area under the entire function equals 1.
    The normalization factor of the function `h` is the
    term $1/(\pi s)$.

## Task

### Calculation of the Gaussian Bell Curve

Create a function `sgauss` in the file of the same name,
that with the call

```python
g = sgauss(x, x_0, s)
```

calculates the Gauss function `g` from the introduction. The inputs of the function should be

```
x   : Vector of x-values
x_0 : Scalar, location of the maximum
s   : Scalar, half-width
```

### Calculation of the Hyperbolic Secant Function

Create a function `secansh` in the file of the same name,
that with the call

```python
h = secansh(x, x_0, s)
```

calculates the hyperbolic secant function `h` from the introduction. The inputs of the
function should be

```
x   : Vector of x-values
x_0 : Scalar, location of the maximum
s   : Scalar, half-width
```

### Calculation and Simple Plotting of the Gaussian Bell Curve and Hyperbolic Secant

Create a program in the script `pscript.py` that calculates and graphically displays the two
functions.

Choose for the parameters the values
$x_0 = 2$ and $s = 0.2$, where $x_0$ is the location of the maximum and $s$ is the
half-width.
(You can also test with other `x_0` and `s` values. How do the curves behave then?)

1. Create the variables `x_a`, `x_e`, and `x_n` using the formulas
    $$
    \begin{aligned}
      x_a  &= x_0 - 5s \\
      x_e  &= x_0 + 5s \\
      x_n  &= 300
    \end{aligned}
    $$

2. Create a vector `x` with
    `x_n` equidistant values between the above start and end point (`linspace`).

3. Now calculate using **your own** functions `sgauss` and `secansh` the variables
    `g` as the result of `sgauss` and `h` as the result of `secansh`.

4. Plot both functions $g(x)$ (red)
    and $h(x)$ (blue) in a figure.

5. Provide the drawing with labels for the x-axis (`x`) and the y-axis (`f(x)`).
    There should also be a legend, where the designation of the two
    lines in the legend should be `Gauss` and `Sech`.

## Hints

* The hyperbolic secant is defined as
$$ \operatorname{sech} (x) = 1 / \cosh (x) $$

* Python help for individual commands can be found at [sqrt], [exp], [cosh].

* The number $e$ as such does not exist in Python. It must be created using
the function [exp].

* Think about what happens when you run the function files like a Python script!
