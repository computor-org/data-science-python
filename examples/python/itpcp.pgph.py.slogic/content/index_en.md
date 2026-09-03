[np.all]: <https://numpy.org/doc/stable/reference/generated/numpy.all.html> "np.all"
[np.any]: <https://numpy.org/doc/stable/reference/generated/numpy.any.html> "np.any"
[np.where]: <https://numpy.org/doc/stable/reference/generated/numpy.where.html> "np.where"
[np.max]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html> "np.max"
[np.mean]: <https://numpy.org/doc/stable/reference/generated/numpy.mean.html> "np.mean"
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> "np.ravel"
[np.sum]: <https://numpy.org/doc/stable/reference/generated/numpy.sum.html> "np.sum"

# Simple Logical Indexing

## Introduction

Create a matrix `M` with entries from `1` to `72` that has `9` rows and `8` columns. Since we will copy it and perform calculations with it, make sure that the entries are `np.float64` and not `numpy.int32`. Use this matrix for the operations specified below. The tasks should be accomplished using logical indexing. Loops and `if-else` statements are **not** allowed.

## Task

Create a Python script `slogic` that accomplishes the following tasks:

1. Store in the variables `L1` to `L8` the **logical arrays** for the following
    conditions regarding the values in `M`.

    Variable     | Task
    :------------|:------
    `L1` | Values greater than 8
    `L2` | Values greater than or equal to 14 and less than or equal to 30
    `L3` | Values divisible by three (see modulo operator)
    `L4` | Values divisible by four and five
    `L5` | Values divisible by four or five
    `L6` | Values not divisible by three
    `L7` | Values greater than the average of the values ([np.mean])
    `L8` | Values greater than or equal to 75 percent of the maximum value ([np.max])

2. Calculate for `L1` to `L3` the number of values for which the corresponding
     condition is true, and store these in the variables
    `num_L1` to `num_L3`. (See hints)

3. Calculate in `num_L2_L4` the number of values for which the conditions `L2` and `L4` are true.

4. Create a vector consisting of the values from matrix `M` that satisfy the following condition:

    * `L6` (Variable: `w_L6`)
    * not `L5` (Variable: `w_L5`)
    * `L2` and `L5` (Variable: `w_L2_L5`).

5. Calculate the **row and column indices** of the values for which the condition `L6` is true, in the variables `iz6` and `is6` ([np.where]).

6. Calculate the **linear** (flattened) **indices** of the values for which the condition `L6` is true, in the variable `i6` ([np.where], [np.ravel]).

7. Create a matrix `M3` that is equal to the matrix
  `M`. Replace in `M3` all values for which the condition `L3`
  is true with the number 14.

8. Create a matrix `M7` that is equal to the matrix `M`.
    * Replace in `M7` all values for which the condition `L7` is true with a value that is one *greater*
     than the mean value of `M`.
    * Then replace in `M7` all values for which the condition `L7` is **not** true with a value that is one
     *less* than the mean value of `M`.

9. Store in the variable `one_L3` the logical answer to the question whether
  **at least** for **one** element (Hint: [np.any]) in `M` the condition `L3` is true.

10. Store in the variable `none_L3` the logical answer to the question whether
  for **no** element in `M` the condition `L3` is true (Consider how this might be
  related to the previous task).

11. Store in the variable `all_L4` the logical answer to the
  question whether for **all** elements (Hint: [np.all]) in `M` the condition `L4` is true.

12. Store in the variable `not_all_L4` the logical answer to the question whether
    **not** for **all** elements in `M` the condition `L4` is true.

13. Create the following variables:

Variable     | Task
:------------|:------
`s1`   | Sum over all rows along the columns of `M`
`sm1`  | Mean of the values in `s1`
`Lsm1` | Logical vector; `true` where `s1` is between 80% and 100% of `sm1` (inclusive).
`Ssm1` | Those parts (columns) of `M` for which `Lsm1` is true
`s2`   | Sum over all columns along the rows of `M`.
`sm2`  | Mean of the values in `s2`
`Lsm2` | Logical vector; `true` where `s2` is between 80% and 100% of `sm2` (inclusive).
`Ssm2` | Those parts (rows) of `M` for which `Lsm2` is true
`S3`   | Those parts of `M` for which `Lsm1` and `Lsm2` are true

## Hints

* Logically true (``True``) is treated as 1 in arithmetic operations such as addition and multiplication, logically false (``False``) as 0. The number of true values is therefore equal to their sum.

* With so-called *masks* you can perform Boolean indexing in Python.

* As noted above, the commands [np.all] and [np.any] are quite handy. When using them, think about how commands of this type must be applied (see e.g. also [np.sum]).
