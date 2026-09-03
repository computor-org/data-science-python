# Analysis of Solutions of a Quadratic Equation 1

## Introduction

In this task, we want to reuse the functions written in `itpcp.pgph.py.quadratic_eq` and `itpcp.pgph.py.quadratic_eq_eval`.

Therefore, you can only solve this example if you have already created `quadratic_eq` and `quadratic_eq_eval`.

## Task

Write the function

```python
def quadratic_eq_test(n, rmin, rmax):
    # ...
    return x1, x2, r1, r2
```

which evaluates the functions `quadratic_eq` and `quadratic_eq_eval` that you wrote previously.

1. Set the default values

   | Variable | Meaning              | Default |
   | -------- | -------------------- | ------- |
   | `n`      | Size of the matrices | `16`    |
   | `rmin`   | Minimum random number| `3`     |
   | `rmax`   | Maximum random number| `6`     |

1. Create 3 arrays `a`, `b`, and `c`. These should consist of random numbers between
   `rmin` and `rmax` and have the size $n \times n$.

1. Set the middle column of `a`, and the middle row of `b` to zero.
   If there is no middle column/row (when `n` is an even number), the
   values in the column/row with the next lower index are set to zero. Use
   the function [ceil] for this (e.g., for `n=5` the middle is `3rd`, for `n=4` the
   middle should be `2nd`).

1. Call the function `quadratic_eq` with `a`, `b`, and `c`.

1. Call the function `quadratic_eq_eval` with the results of `quadratic_eq`.

1. Return the results of `quadratic_eq` in `x1`, `x2`, and the results of
   `quadratic_eq_eval` in `r1`, `r2`.

## Hints

- The numpy function [rand](n, n) returns an $n\times n$ matrix of random numbers
  between 0 and 1. The adaptation to the interval `(rmin,rmax)` is done by
  scaling (multiplication) and shifting (addition). Alternatively, you can also use
  [np.random.uniform].

- It is important that the order of the first few lines is maintained. It
  could be that this is changed by formatting
  `from quadratic_eq_eval import quadratic_eq_eval` must come last!:

```python
import numpy as np
import sys
import os
# set path to filepath of current file
cur_file_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../itpcp.pgph.py.quadratic_eq_eval/")
sys.path.append("../itpcp.pgph.py.quadratic_eq/")
from quadratic_eq import quadratic_eq  # ! must be placed after sys.path.append
from quadratic_eq_eval import quadratic_eq_eval  # ! must be placed after sys.path.append
```

[ceil]: https://numpy.org/doc/stable/reference/generated/numpy.ceil.html "ceil"
[np.random.uniform]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html "rand_unif"
[rand]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html "rand"
