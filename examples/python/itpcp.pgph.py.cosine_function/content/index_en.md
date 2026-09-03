# Decaying Cosine Function

## Introduction

In this example, you should apply your knowledge from this week without many hints. Write the following function `fun_exp` with specified input and output:

```python
cos_exp, envelope = fun_exp(x, d)
```

| InOut | Name | Description |
|:-|:-|:-|
| Input | `x`  | x-values of the functions; vector |
| Input | `d`  | decay factor; scalar |
| Output | `cos_exp` | Cosine function in exponential representation; vector |
| Output | `envelope` | envelope function; vector |

which calculates the following functions:

$$
\begin{aligned}
  \text{cos\_exp}(x) &= \frac{1}{2}(\mathrm{e}^{ix} + \mathrm{e}^{-ix}) \\
  \mathrm{envelope}(x) &= \mathrm{e}^{-dx}
\end{aligned}
$$

## Displaying the Functions

The following variables are to be created by you in the script `cos_exp.py`:

|Variable|Value|
|:-|:-|
|`x`| Vector from $0$ to $10\pi$ with $250$ values |
|`d`| Scalar $0.1$ |
|`y`, `A` | Call of your own function with $y = \text{cos\_exp}(x)$, $A = \text{envelope}(x)$ |

Use this to create a figure with multiple lines:

1. Plot $y(x) \cdot A(x)$; solid line; black
2. Plot $A(x)$; solid line; blue
3. Plot $-A(x)$; solid line; blue
4. Limits for abscissa to minimum and maximum of $x$
5. Limits for ordinate to minimum of $-A(x)$ and maximum of $A(x)$
6. Label the abscissa with $x$
7. Label the ordinate with $y(x)$
8. Write a title with the label `Decaying Cosine`


## Hints

* Remember which symbol represents the imaginary unit in Python.

* You should receive a warning that the imaginary part is ignored. Think about how you can avoid this warning.

* The result should look like this:

<center>
<img src="mediaFiles/picture_2.png" alt="mediaFiles/picture_2.png" style="align: middle; width: 50%; "/>
</center>
