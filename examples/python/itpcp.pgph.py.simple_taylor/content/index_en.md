[Taylor series]: <https://en.wikipedia.org/wiki/Taylor_series> "Taylor series"
[axes]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html> "axes"
[figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "figure"
[linspace]: <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html> "linspace"
[subplots]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html> "subplots"
[xlim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html> "xlim"
# Taylor Series of the Sine

## Introduction

The Taylor series for the sine up to the fourth term is:
$$
  \sin(x) = x - \frac{x^{3}}{6} + \frac{x^{5}}{120} -
  \frac{x^{7}}{5040} + \dotsb
$$

The goal of this exercise is to visualize how the [Taylor series]
approaches the exact result with each calculated term.

## Task

1. Define the following variables in the script `simple_taylor`:

  |Variable|Value|
  |-|-|
  |`x_max`|$2 \pi$|
  |`x`|Vector with 200 support points on $[-x_{\text{max}}, x_{\text{max}}]$ ([linspace])|
  |`lim`|$1.5$|

2. Calculate the variable `y`, which should contain the sine of `x` as values.
Also calculate `y1`, `y2`, `y3`, and `y4`, which should contain the values for the (above visible) first four terms of the Taylor series (e.g., $\texttt{y1} = x$, $\texttt{y4} = -\dfrac{x^7}{5040}$).

3. Use the command [subplots] to create a [figure] with
multiple coordinate systems.
  Display $2 \times 2$ coordinate systems in one
[figure]. Each of these coordinate systems should display the graph of the
function $\sin(x)$ with a blue, solid line.

4. Additionally,
plot (each with a red dashed line) in the coordinate system:

*  the linear approximation
*  the cubic approximation
*  the Taylor series up to the third term
*  the Taylor series up to the fourth term

The blue line should be drawn first and then the red one in each subplot.

5. Label the axes, and also create a
title. The x-axis should be labeled with `x`, the y-axis with `sin(x)`.
Take the titles from the reference graphic in the hints.

6. For a nicer display, it is recommended to set the limits of the
x-axis to $[-x_{\max}, x_{\max}]$ and the y-axis to `[-lim, lim]`
([xlim]).


## Hints

- [subplots] expects 2 input arguments. The first specifies the number of "rows"
and the second the number of "columns" in the figure. The two return values
are conventionally called `fig, axs` and refer to the
[figure] and the contained coordinate systems ([axes]). The latter is a two-dimensional
array, where the first index stands for the row and the second index for the column.
`plot` is then applied to these coordinate systems - so instead of `plt.plot(...)`,
you write e.g. `ax[1, 0].plot(...)` to draw in the coordinate system in the second row
and first column.

- To prevent the subplots from "interfering" with each other, it is recommended to apply
the command `fig.tight_layout()` before `plt.show()`, where `fig` as mentioned before is the first
output argument of `plot.subplots(...)`.

- Since the variables `y1` to `y4` only contain the individual terms
of the series, it is not enough to just plot e.g. `y4` over `x`.
Instead, all terms of lower order must of course be added when plotting.

- Strictly speaking, the designation of the terms with indices 1 to 4
is imprecise. Mathematically speaking, in a Taylor series the first term
is the one containing $x^{0}$, the second one with $x^{1}$, the third
(quadratic) with $x^{2}$, etc. Here, only the terms that
do not vanish are numbered.

- Your graph should look like this:

![Taylor expansion](mediaFiles/simple_taylor.png "Taylor expansion")

- Make sure that the axis labels and titles correspond to the reference graphic.
Also make sure not to insert spaces before or after labels and titles (Use (`'x'`) not (`' x '`))


## Keywords

- Subplots