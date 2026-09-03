[len]: <https://docs.python.org/3/library/functions.html#len> "len"
[np.nan]: <https://numpy.org/doc/stable/reference/constants.html> "np.nan"
[np.ndim]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html> "np.ndim"
[np.size]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html> "np.size"
[np.shape]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html> "np.shape"
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> "np.ravel"
[np.copy]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html> "np.copy"
[np.delete]: <https://numpy.org/doc/stable/reference/generated/numpy.delete.html> "np.delete"
[np.astype]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html> "np.astype"

# Index and Colon

## Introduction

This task is about deepening the handling of indexing and slicing in Python. We will learn how to efficiently access and manipulate elements, vectors, and matrices within a two-dimensional data structure.
By working with a matrix M and various operations on it, functions like `np.ravel`, `np.copy`, `np.delete`, and `np.astype` are introduced and practiced.

### Indexing

 This refers to accessing individual elements in an array or matrix. In Python, indices start at 0. For two-dimensional arrays, the first index stands for the row and the second for the column. Example: `M[1, 2]` accesses the element in the second row and third column.

### Slicing
Using slicing, you can extract subarrays or submatrices from a matrix. For example, `M[:, 2]` returns the entire third column, while `M[1:4, :]` returns rows 2 to 4.

## Task

Write a Python script `sindex` (File: `sindex.py`) that accomplishes the following
tasks for a matrix `M`. First read
the hints (see below):

1. Save the following information in the specified variables:

    Variable     | Task
    :------------|:------
    `M`     | (9 x 8) matrix with all integers in the interval [-36, 35] (ascending order)
    `prop1` | Dimension of `M`
    `prop2` | "Length" of `M`
    `prop3` | "Shape" of `M`
    `prop4` | Number of elements in `M`

2. Save the following scalars from `M`:

    Variable     | Task
    :------------|:------
    `n1` | second row, first column
    `n2` | third entry
    `n3` | last entry
    `n4` | second to last entry

3. Save the following vectors from `M`:

    Variable     | Task
    :------------|:------
    `z1` | second to fourth position
    `z2` | first to last position with step size four
    `z3` | second and second to last position
    `z4` | third row, all columns
    `z5` | last to first position, think about using `-1` as step size.
    `z6` | the first, twice the second, three times the third position

4. Save the following vectors from `M`:

    Variable     | Task
    :------------|:------
    `s1` | all rows, third column
    `s2` | first to second to last row, second to last column
    `s3` | last to first row, second column
    `s4` | all rows, middle column (see hint)

5. Save the following matrices from `M`:

    Variable     | Task
    :------------|:------
    `m1` | second to third row, all columns
    `m2` | first to last row with step size 2, all columns
    `m3` | all rows, second to second to last column
    `m4` | first to last row with step size 3, first to last column with step size 2;
    `m5` | last to first row, third to second column (second column not inclusive)
    `m6` | the three middle rows, the three middle columns (see hint)

6. Create five matrices `M1`, `M2`, `M3`, `M4`, and `M5` with the same content as `M` and
 replace parts of their content:

    Variable     | Task
    :------------|:------
    `M1` | first to last position with step size 2, by value [np.nan]
    `M2` | first to last row with step size 2, all columns, by value [np.nan]
    `M3` | second to second to last row, second to last column, by value zero
    `M4` | the four corners by [np.nan]
    `M5` | cut out the second and second to last row, and the second and second to last column ([np.delete])

## Hints

* Important commands: [np.ndim], [len], [np.shape], [np.size], [np.ravel], [np.astype]

* Note that in Python, list and array indices start with 0!

* When using two indices in a two-dimensional matrix, the first stands for the row and the second for the column.

* To get the n-th element of a matrix (the number at the n-th position), first convert the matrix to a vector ([np.ravel]).

* Define a vector of the matrix elements to later access only these.
 E.g., `Avec = np.ravel(A)` to later use `Avec[1]` instead of `np.ravel(A)[1]`

* With an even number of columns, there is no middle column. Then the
 following column is meant, e.g., $6/2=3$, or $5/2=2.5\rightarrow 3$.
 I.e., the middle column with six columns should be the third, and the middle of five columns should also be the third. *Integer division* can be helpful here.

* Note in part 6 that [np.nan] is defined as a float, but the matrix entries of `M` are integers. So you will need to modify the data type of the matrix to be able to insert [np.nan].

* If you want to edit a copy of a matrix, use [np.copy] or `matrix_name.copy()` when assigning, otherwise you will change the original matrix (try it!). Commands like [np.delete] and [np.astype] of course always create a copy.
