# Comparison of Logical Indexing with Loops and Mathematics

## Introduction

This task is divided into three parts and is intended to enable a comparison of algorithms created using logical indexing, using `for` and `if` structures, or using mathematical functions.

After completing this task, you should understand the advantage of logical indexing over loop-based solutions, and when you can simply use mathematical functions.

## Task

### 1. With Logical Indexing

Create the function

```python
def randmeanlog(R):
    # ...
    return R
```

that using logical indexing and the numpy command `np.mean`

1. replaces all values in the array `R` that are less than zero with the mean of the negative numbers;
1. replaces all values in the array `R` that are greater than zero with the mean of the positive numbers.

Make sure that

- the main part of the function has a maximum of four lines,
- **no** conditional statements or loops (`for`, `while` and `if`) are used.

### 2. With Loop

In the second part, complete the same task in a new file with the function

```python
def randmeanfor(R):
    # ...
    return R
```

using loops. The following approach is recommended:

1. Initialize sum and count variables before the first loop.
1. Determine the count and sum of all positive (negative) values in a loop.
1. Calculate the respective means.
1. Assign these to the corresponding positions in a second loop.

### With Mathematical Function

In the third part, complete a slightly different task with the function

```python
def randsignum(R):
    # ...
    return R
```

Replace in `R`

1. all values $< 0$ with $-1$ and

1. all values $> 0$ with $1$.

1. Write this in only one line using the numpy function [sign] without any control structures such as `if`, `for`, or `while`. Consider why such an approach is not possible for the first two tasks.

## Hints

- Remember that the array `R` can have multiple dimensions!
- You can still iterate over only one index if you save the dimensions beforehand, then flatten the array using [flatten], and finally reshape it back to its original form. Alternatively, you can use [unravel_index].

[flatten]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html "flatten"
[sign]: https://numpy.org/doc/stable/reference/generated/numpy.sign.html "sign"
[unravel_index]: https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html "unravel_index"
