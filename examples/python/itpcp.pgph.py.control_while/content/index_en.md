# Control Structures: The while Loop

## Introduction

In the `while` loop, unlike the `for` loop, a code block is iterated over as long as a defined condition is logically true (`True`). Often an initial variable is initialized before the loop, which is then modified during execution:

```python
counter = 0
while counter <=10:
    do something
    counter += 1
```

Here too, attention must be paid to the indentation of the code block. The examples serve as reference points for how `while` control structures can be used.

## Task

Initialize the random number generator from `numpy` by adding `numpy.random.seed(42)` globally.
Write a function `while_test` that can be called as follows:

```python
z, count = while_test(z, count_lim)
```

`z` is a double vector and `count_lim` is an integer scalar.
The tasks of the function should be:

1. `z` should be (element-wise) divided by an equally sized array of uniformly distributed
   random numbers in the half-open interval `[1,2)` until all values in `z` are less
   than `1`. **For each division, new random numbers should be generated**.

1. In the variable `count`, it should be counted how many times the array was divided.

1. If `count` reaches the value `count_lim`, the
   [while] loop should be exited **after** the corresponding division.

## Hints

- If you do not test the function with a one-dimensional double array `z`, but e.g. with a scalar, a multi-dimensional array, an integer vector, or a Python list, unexpected errors may occur depending on the implementation. Since the expected data type is precisely defined here, it is the user's responsibility to provide this data type. However, if you want to write your function to accept more general inputs, [np.asarray] and possibly [np.random.random_sample] are helpful for this specific example.
- Loops can be terminated with the keyword [break].

[break]: https://docs.python.org/3/reference/simple_stmts.html#break "break"
[np.asarray]: https://numpy.org/doc/stable/reference/generated/numpy.asarray.html "np.asarray"
[np.random.random_sample]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html "np.random.random_sample"
[while]: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming "while"
