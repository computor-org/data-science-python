[all]: <https://numpy.org/doc/stable/reference/generated/numpy.all.html> "all"
[any]: <https://numpy.org/doc/stable/reference/generated/numpy.any.html> "any"
[if]: <https://docs.python.org/3/tutorial/controlflow.html#if-statements>
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> "np.ravel"

# Control Structures: if Statement

## Introduction

The following examples are intended to familiarize you with control structures, especially the `if statement` in Python. With `if statements`, logical conditions are checked in the script. If these are true in the Boolean sense (`True`), then the code indented below is executed; otherwise, it is ignored during execution.

You should already have been introduced to the concept of control structures in the lecture. The following Python files should show you in which context `if statements` can be used.

* `if_test1`: Simple [if], various notations.
* `if_test2`: In combination with logical operators.
* `if_test3`: Nested [if].
* `if_test4`: No matrices in conditions, [all], [any].
* `if_test5`: Order of conditions is important, as only the branch with the first correct condition is executed.
* `if_test6`: Another if with [all] and [any]. Insert
  the additional line from the comment at the correct position.

Now you should write your own script using `if statements`.

## Task

Write a function `if_test` that with the call

```python
r = if_test(z)
```

for an **arbitrary** numeric array `z` returns one of the following
strings as result in `r`:

1. `none` if no value in `z` is greater than zero;

2. `any` if at least some value in `z` is greater than zero;

3. `two` if exactly two values in `z` are greater than zero;

4. `all` if all values in `z` are greater than zero.

If at this point you do not know <span style="color: red;">how to test your own
function yourself,</span> then read all the hints!

## Hints

* `if` must occur exactly once,
    `elif` must occur exactly twice,
    `else` can, but does not have to occur. (Think about why!)

* Do not forget that `z` can be an **arbitrarily dimensional** array.
    (This applies especially to 3d arrays!) The command [np.ravel] can be helpful here.

* You should call a function yourself in the console and check
  for errors. To do this, proceed as follows:

  * Define a matrix (here M) for example by

    ```python
    M = np.arange(1, 13).reshape(3, 4)       # all greater than zero
    M = np.arange(1, 13).reshape(3, 4) - 12  # none greater than zero
    M = np.arange(1, 13).reshape(3, 4) - 5   # some number greater than zero
    M = np.arange(1, 13).reshape(3, 4) - 10  # exactly two greater than zero
    ```

  * Call the function with this matrix:

    ```python
    r = if_test(M)
    ```

    This is a suggestion. Of course, it is better if you think about
    test possibilities yourself.
