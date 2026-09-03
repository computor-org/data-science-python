[arithmetic operators]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetic operators"
[floating point numbers]: <https://docs.python.org/3/tutorial/floatingpoint.html> "floating point numbers"
[cos]: <https://numpy.org/doc/stable/reference/generated/numpy.cos.html> "cos"
[exp]: <https://numpy.org/doc/stable/reference/generated/numpy.exp.html> "exp"
[sin]: <https://numpy.org/doc/stable/reference/generated/numpy.sin.html> "sin"
[sqrt]: <https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html> "sqrt"
# Simple Calculations

## Introduction

In this task, arithmetic operators (`+`, `-`, `*`, `/`) are introduced. From the task `01_math_constants`, the exponential function `exp` and trigonometric functions are reviewed.

For automatic testing, it is essential that you use <span style="color: red;">exactly these names</span> for your variables!
Try out your program in the console before submitting it.

In the hints, you will find further explanations of the operators and functions.


## Task

1. Create the variables `a` and `b` in the Python script `basis1` (File: `basis1.py`)
and assign them the values `5.4` and `1.2`.

2. Now calculate the following quantities, where the variable names are on the left. Use the Python module `numpy` as in Task 01.

$$
\begin{aligned}
\texttt{sum\_ab} & = a + b \\
\texttt{diff}    & = a - b \\
\texttt{prod}    & = a\cdot b \\
\texttt{quot}    & = \frac{a}{b} \\
\texttt{power}     & = a^{b} \\
\texttt{root}  & = \sqrt{a} \\
\texttt{root3}   & = a^{1/3} \\
\texttt{expo}    & = \mathrm{e}^{-a} \\
\texttt{trig1}   & = \sin (a) \\
\texttt{trig2}   & = \sin(a+b) \\
\texttt{trig3}   & = \cos (\pi \cdot a)
\end{aligned}
$$

## Hints

* Python help for individual commands can be found at [sqrt], [exp],
[sin], [cos]. The operators `+`, `-`, `*`, and `/` are called [arithmetic operators].
The Python tutorial also deals with limitations when using
[floating point numbers].

* The number $e$ as such does not exist in Python. It must be created using
the function [exp].

* Variable names that are already reserved by Python (such as ```sum```) should be avoided at all costs, as these functions would otherwise not be callable!


## Keywords

- Arithmetic operators
- NumPy functions