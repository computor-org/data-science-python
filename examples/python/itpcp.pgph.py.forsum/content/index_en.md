# Sums and Loops

## Introduction

The purpose of this task is to understand how the practical command [np.sum]
would have to be implemented with [for] loops. When programming further with Python,
one naturally always uses [np.sum] and not a loop.

Create a matrix `M` with 4 rows and 6 columns for testing purposes. The entries of the
matrix should run from 1 to 24 along the columns:

$$
\begin{pmatrix}
  1 & 5 & \dots & 21 \\
  2 & 6 & \dots & 22 \\
  \vdots & \vdots & & \vdots \\
  4 & 8 & \dots & 24
\end{pmatrix}
$$

This matrix can be created with [np.arange] and [ndarray.reshape] followed by transposing.

## Task

Create a Python script `forsum` that accomplishes the following tasks:

1. Calculate the sum over all rows using the command [np.sum] and save
   it in the variable `sum_s1`. *Summation over all rows* means
   that you add all rows:

   ```
        Row 1 + Row 2 + Row 3 + ... (element-wise)
   ```

1. Similarly calculate the sum over all columns and save the result in
   `sum_s2`. *Summation over all columns* corresponds to

   ```
        Column 1 + Column 2 + Column 3 + ... (element-wise)
   ```

1. Calculate the sum over all values of the array with [np.sum] and save
   it in `sum_st`.

1. Determine the number of rows (`nz`), columns (`ns`), and elements
   (`nn`) of `M` and save them in the specified variables ([np.shape],
   [np.size]).

1. Now perform the summations over all rows (`sum_f1`), all columns (`sum_f2`),
   and all elements (`sum_ft`) in three different [for] loops.
   Save these results in the specified variables. Use as
   loop index the variables `i_z`, `i_s`, and `i_n` respectively.

1. **Note the hints**

1. Think about what dimensions you would expect from these operations
   and check their actual dimension using the `shape` member of the numpy arrays.
   What do you notice? Why might this be the case?

## Hints

- The row index is the index into the first dimension and the column index is the
  index into the second dimension.

- If you need a specific row `z` or column `s` of a matrix `M`, you can achieve
  this with `M[z,:]` or `M[:,s]`.

- When summing with [for], you first allocate the corresponding sum variable with
  zeros [np.zeros] in the appropriate size and then start
  adding in the loop. The loop itself then runs over all rows or columns or
  elements. For rows and columns, you use the property that
  arithmetic operators act on entire vectors (matrices).

- For summing over all values using [for], you only need a
  single loop if you use the function [np.flat].

[for]: https://docs.python.org/3/tutorial/controlflow.html "for"
[ndarray.reshape]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html "ndarray.reshape"
[np.arange]: https://numpy.org/doc/stable/reference/generated/numpy.arange.html "np.arange"
[np.flat]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html "np.flat"
[np.shape]: https://numpy.org/doc/stable/reference/generated/numpy.shape.html "np.shape"
[np.size]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html "np.size"
[np.sum]: https://numpy.org/doc/stable/reference/generated/numpy.sum.html "np.sum"
[np.zeros]: https://numpy.org/doc/stable/reference/generated/numpy.zeros.html "np.zeros"
