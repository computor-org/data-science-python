[plt.figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "plt.figure"
[plt.show]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html> "plt.show"

# Setting Default Values - Beat Frequency

## Introduction

This exercise deals with setting default values in functions, i.e.,
values that are automatically set when input parameters are missing.
For this, a Python function `beat` and
a Python script `plot_beat`, which visualizes the results of the function
`beat`, are to be created.

### Setting Default Values

Functions often require parameters that (almost always) take constant values, e.g., the refractive index of air or gravitational acceleration. These can be assigned a default value in the definition of a function:

```python
def free_fall(t, x_0, v_0, g=9.81)
```

When calling the function, default values can also be omitted:

```python
t = 2.0
x_0 = 20.0
v_0 = 0.0
g_0 = 9.80665
x, v = free_fall(t, x_0, v_0)       # g = 9.81
x, v = free_fall(t, x_0, v_0, g_0)  # g = 9.80665
```

When defining a function, function arguments with default values should always be placed after arguments without default values. For arguments without default values (*required arguments*), the order is very important, as it determines which values are assigned to which variables.

In the following tasks, you will learn to work with default values in functions.

## Task

### Function

1. Write a Python function `beat` that calculates the following functions with the call

    ```python
    x, y = beat(t, nu1, nu2, A)
    ```

    $$
    \begin{aligned}
      x(t) &= A \left( \sin(2 \pi \nu_1 t) + \cos(2 \pi \nu_2 t) \right) \\
      y(t) &= A \left( \sin(2 \pi \nu_1 t) - \cos(2 \pi \nu_2 t) \right)
    \end{aligned}
    $$

    `t` is a time vector.

2. Set the default values for the inputs `nu1`, `nu2`, and `A` to

    $$
    \begin{aligned}
      \nu_1 &= 5.0 \\
      \nu_2 &= 4.5 \\
      A     &= 1.0
    \end{aligned}
    $$

### Script

Write a Python script `plot_beat` that graphically displays the results of the
function `beat`.

1. Create a vector `t` using the function `np.linspace` that contains 400
    support points in the range from 0 to 4.

2. Call `beat` so that apart from `t`, the default values are used.

3. Create a figure in which the beat is plotted:
    * Display `x` and `y` as a function of `t` in one
      coordinate system.
      The first line should represent $x(t)$ and the second line $y(t)$.
      The $y(t)$ graph should also be drawn in red color.

    * Give the figure the title *Beat Oscillation*, label the x-axis
      with *t*, the y-axis with *Amplitude*

4. Create another figure that displays a Lissajous figure:
    * Display $y(x)$. The result yields a Lissajous figure
      (provided `nu1` and `nu2` form a rational ratio)

    * Give the figure the title *Lissajous-Figure*, label the x-axis
      with *x*, the y-axis with *y*.

## Hints

* Two plots in separate windows are to be created. The first
    graph should display a beat, and the second a Lissajous figure.
    To initialize a new window for a plot, the functions [plt.figure] and [plt.show] exist. For each of the graphs, these are to be used as follows:

```python
plt.figure()
# Plot commands
plt.show()
```

* At the end, your graphs should look like this:

<div align="center">
<img src="mediaFiles/beat_oscillation.png" alt="Beat Oscillation" width="50%" name="Beat Oscillation"/>
</div>

<div align="center">
<img src="mediaFiles/Lissajous-Figure.png" alt="Lissajous Figure" width="50%" name="Lissajous Figure"/>
</div>
