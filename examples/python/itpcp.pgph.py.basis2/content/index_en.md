[abs]: <https://numpy.org/doc/stable/reference/generated/numpy.absolute.html> "abs"
[arithmetic operator]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetic operators"
[arange]: <https://numpy.org/doc/stable/reference/generated/numpy.arange.html> "arange"
[linspace]: <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html> "linspace"
[matplotlib]: https://matplotlib.org/stable/tutorials/index.html "matplotlib"
[figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "figure"
[plot]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html> "plot"
[xlim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html> "xlim"
[ylim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html> "ylim"
[xlabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html> "xlabel"
[ylabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html> "ylabel"
[title]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html> "title"
[show]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html "show"

# Simple Plot of Vectors - P1

## Introduction

In this task, it will be demonstrated how plots can be created in Python.
It should also become clear to you how mathematical notation of
algebraic expressions is typically implemented in programming.

A few examples:

*  Variable indices, such as $y_{1}$ or $x_{\text{end}}$,
are often written as `y_1` or `x_end`. By the way, the underscore `_` is the only special character that is permitted in variable and programme names.

*  The absolute value $\lvert x_{1} \rvert$ must be calculated with a
(predefined) program. For this, [abs] is used.

*  In mathematical notation, the multiplication operator does not necessarily need to be
written. So instead of $x_{1} \cdot \lvert x_{1} \rvert$, one can simply write
$x_{1} \lvert x_{1} \rvert$. In a programming language like Python, you must
use operators between parts of formulas, in this case an
[arithmetic operator], namely `*`.

* In mathematics, exponentiation is symbolized by superscript characters, such as $x^2$.
In Python, the operator `**` is used for exponentiating scalars.

## Task

1. Create the following variables in the Python script `basis2` (File: `basis2.py`):

    |Variable| Value  |
    |---|-------|
    |`x_start`| `-3`  |
    |`x_end`| `3`   |
    |`n`| `200`

2. Create the row vector `x_1` with values between `x_start` and `x_end`
and a step size of `one`. Use [arange] for this (be aware of its interval definition).

3. Calculate the following formula with it: $$y_{1} = x_{1} \lvert x_{1} \rvert$$

4. Create a vector ```x_2``` using [linspace]
   from `x_start` to `x_end` with `n` values.


5. Calculate 3 hyperbolic functions with it in the following variables:

    |Variable|Value|
    |---|---|
    |`ysinh`|$\sinh(x_2)$|
    |`ycosh`|$\cosh(x_2)$|
    |`ytanh`|$\tanh(x_2)$|

    You should now have a total of 4 row vectors of length `n` that can be plotted.

6. To visualize our functions, we will use the [matplotlib] library. Plot the following quantities in a [figure] in the given order:

    | Abscissa |Ordinate|Line Specification|
    |----------|---|---|
    | `x_1`    |`y_1`|red; solid; with marker `o`
    | `x_2`    |`ysinh`|black; solid
    | `x_2`    |`ycosh`|blue; solid
    | `x_2`    |`ytanh`|green; solid

     The matplotlib command [plot] is suitable for this. The associated documentation
    also specifies line types.

7.  Set the axis limits with the commands [xlim] and [ylim] to
    the following values:

    |Axis|Minimum|      Maximum      |
    |---|:---:|:-----------------:|
    |`x`-axis|`x_start`|      `x_end`      |
    |`y`-axis|$-\max(\sinh(x_2))$| $+\max(\sinh(x_2))$ |

    When you need the same calculation multiple times, it is much better to
    store the required value in a variable and then use it. Instead of entering the minimum and maximum for [ylim] separately, think about how you can use a variable `y_max` for this.

8.  Create axis labels and an axis title in the following form:

    |Command|Text|
    |---|---|
    |[xlabel]|`x`|
    |[ylabel]|`y(x)`|
    |[title]|`Hyperbolic Functions`|

    To display the graph, the [show] command is necessary after the [plot] commands.

9. Think about why the red curve (created with `x_1`)
looks much more angular than the other curves.


## Hints

* In Python, intervals are right-open, i.e., for [arange] and similar functions,
the endpoints are not included in the generated array. Think about how you
can still include the endpoint in subtask 2.

* In test mode, it is essential that the curves are drawn in the specified order.
    So here definitely in the order hyperbolic sine, hyperbolic cosine, and hyperbolic tangent.

* If you write `plt.title = 'Your Title'` in your program
    instead of `plt.title('Your Title')` and execute this program, then
    the graph will not get a title, but you change the variable `plt.title`.
    From this point on, using the matplotlib command [title] is not
    possible because your definition takes precedence. The problem can only be solved by clicking
    on _Restart_ in the _Interactive Window_.


## Keywords

- Matplotlib
- Plotting