# Calculation of the Left Side of a Quadratic Equation

## Introduction

Using the function `quadratic_eq`, you have already calculated the solutions of the equation
$$
    ax^2 + bx + c = 0 \qquad a,b,c \in \mathbb{R}
$$
in an earlier example. One would therefore expect to get `0` when inserting the solutions $x$ into the equation. However, due to numerical inaccuracies, this is not always the case.

## Task

Write the function

```python
def quadratic_eq_eval(a,b,c,x1,x2):
    # ...
    return r1, r2
```

which calculates the left side of this equation for given `x1` and `x2`, or coefficients `a`, `b`, `c`, and stores it in `r1` or `r2`. I.e., implement the following formula:

  $$
    r_{1,2} = ax_{1,2}^2 + bx_{1,2} + c \qquad a,b,c \in \mathbb{R}
  $$

## Hints

- **Preview next example:**
  With your function, you can now check how well the equation is solved by `quadratic_eq`: If you pass the (equally sized) arrays `a`, `b`, `c`, as well as the corresponding solutions `x1` and `x2` (calculated with `quadratic_eq`), you can evaluate how close the result is to zero.

* With [nan], you can calculate normally, where any
 arithmetic operation with [nan] yields [nan] again.
