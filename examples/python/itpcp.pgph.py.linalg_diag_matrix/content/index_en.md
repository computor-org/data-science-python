[diag]: <https://numpy.org/doc/stable/reference/generated/numpy.diag.html> "diag"
[eye]: <https://numpy.org/devdocs/reference/generated/numpy.eye.html> "eye"
[isclose]: <https://numpy.org/doc/stable/reference/generated/numpy.isclose.html> "isclose"
# Linear Systems of Equations, Diagonal Matrix, Verification

## Introduction

In this task, a linear system of equations is to be solved. The result is examined using a verification.

## Task
Write a script `linalg_diag_matrix` that solves a given system of equations and verifies the result.


1. Read a variable `n` using input. Make sure that `n` is an integer. If `n` is not an integer, set `n` = $5$.

2. Create a $2n \times 2n$ matrix `A` whose main diagonal consists of ones and whose off-diagonals contain only `0.5`. Create this matrix with the commands [eye] and [diag].
    $$
      A =
      \begin{bmatrix}
        1      & 0.5    & 0      & 0      & \ldots \\
        0.5    & 1      & 0.5    & 0      & \ldots \\
        0      & 0.5    & 1      & 0.5    & \ldots \\
        0      &  0     & 0.5    & 1      & \ldots \\
        \vdots & \vdots & \vdots & \vdots & \ddots
      \end{bmatrix}
    $$

3. Then create the vector `b` with the following form:
    $$
      \mathbf{b} =
      \begin{bmatrix}
        0 \\
        1 \\
        0 \\
        2 \\
        0 \\
        3 \\
        \vdots \\
        0 \\
        n \\
      \end{bmatrix}
    $$


4. Now solve the linear system of equations $\mathbf{Ax} = \mathbf{b}$ and save the solution vector in `x`.

5. Perform the verification $\mathbf{Ax - b}$ and save this difference in `check` (should ideally be $\mathbf{0}$).

6. Check whether `check` actually contains only zeros: Output the logical vector of this comparison in the format `check: 'Comparison values'`. This could look like this for example:

            check: [1 0 0 0 1 0 0 1 1 1]

	Does it contain only ones? Why not?

7. Perform a more sensible type of verification.


## Hints

* Looking at the output of `check`, you can see that this verification fails. This is because rounding errors always occur due to the finite precision of numbers. For this reason, it is **not sensible** to check for **equality**. It only makes sense to check for **approximate equality**. The *relative* or *absolute* error can be used for this. Here an absolute error threshold should be used.

		error_limit = 1E-8

    The numpy function [isclose] can also be used here! This now makes it possible to perform a sensible verification of the form
    ```python
    if ...:
        print('Check successful')
    else:
        print('Check unsuccessful')
    ```
