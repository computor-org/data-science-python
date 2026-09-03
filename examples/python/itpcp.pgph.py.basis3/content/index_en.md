[NumPy]: <https://numpy.org/doc/stable/>
[Matplotlib]: <https://matplotlib.org/stable/api/index.html>
[Matplotlib-Userguide]: <https://matplotlib.org/stable/users/index.html>
[legend]: <https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html>
[xlim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html>
[xlabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html>
[ylabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html>

# Combination of Functions

## Introduction

This exercise deals with the calculation and plotting
of simple functions.

### Comments

It is recommended to get into the habit of commenting your code, so that in the future you can immediately see at a glance what is happening in this part of the program (and especially why).
    A good method is to plan the program flow before you start programming and write it down as comments, for example:

        # Define the parameters

        # Define the functions

        # Compute the function values

        # Plot the results

    Now simply leave the comments in place and write the corresponding code under the respective lines. It may seem trivial here, but practice this even in simple examples!


## Task

Create a program in the script `basis3` (File: `basis3.py`)
that calculates and graphically displays the functions.

1. Create the variables `x_a`, `x_e`, and `x_n` using the formulas
    $$
    \begin{aligned}
    x_a  &= -2 \pi \\
    x_e  &= +2 \pi \\
    x_n  &= 180
    \end{aligned}
    $$

2. Create a vector `x` with `x_n` equidistant values between
    the above starting and ending points (`linspace`).

3. Calculate the functions with it (names: `f1`, `f2`, and `f3`)
    $$
    \begin{aligned}
    f_1  &= \frac{x}{2\pi} \; \sin(x) \\
    f_2  &= \frac{x^2}{(2\pi)^2} \; \sin^2(x) \\
    f_3  &= \frac{x^3}{(2\pi)^3} \; \sin^3(x)  .
    \end{aligned}
    $$

4. Plot the functions $f_1(x)$
    (red), $f_2(x)$ (blue), and $f_3(x)$ (green) in a Figure. The exact [RGB](https://matplotlib.org/stable/users/explain/colors/colors.html) specification
    is `red=(1.0, 0.0, 0.0, 1)`, `blue=(0.0, 0.0, 1.0, 1)`, and `green=(0.0, 1.0, 0.0, 1)`.

5. Provide the drawing with labels ([xlabel], [ylabel])
    for the x-axis (`x`) and the y-axis (`f(x)`).

6. Set the limits of the x-axis to the values of $x_a$ and $x_e$
    ([xlim]).

7. There should also be a legend ([legend]), where
    the labels of the lines in the legend should be `f1(x)`, `f2(x)`, and
    `f3(x)`.
    Make sure that the legend is set *explicitly*. The legend
    should be placed at the bottom center inside the plot.

## Hints

* Use the [NumPy] and [Matplotlib] documentation as well as the [Matplotlib-Userguide] to find out how to correctly use the necessary commands!

* Hints for positioning the legend can be found under the corresponding `loc` keyword (see [legend]).
