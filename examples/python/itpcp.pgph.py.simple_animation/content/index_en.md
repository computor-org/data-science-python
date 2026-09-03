[FuncAnimation]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html> "FuncAnimation"
[MatplotlibTutorial]: <https://matplotlib.org/stable/tutorials/introductory/animation_tutorial.html> "Matplotlib Tutorial Animations"
[plt.subplots]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html> "subplots"

# Animation

## Introduction

In a script `simpleanim`, two curves are to be animated:

$f_1(x, t) = \cos(x) \cos(t)$

$f_2(x, t) = \cos(x-t)$

Matplotlib plots can be animated in two ways. On one hand, you can alternately update the line and then manually pause for a certain time in a loop for each time step. However, we use the Matplotlib class [FuncAnimation] here, which offers, among other things, the advantage of being able to export the animation as a video.
For [FuncAnimation], you only need to define an update function that updates the graphics objects for each frame.

## Task
  Proceed as follows to create the animation with [FuncAnimation]:

1. Create a vector `x` with `100` points between `0` and `2`$\pi$.

2. Calculate `cos_x = cos(x)`.

3. Create a vector `t` with `48` points between `0` and $2 \pi$. This vector represents the time scale over which the animation should run. Calculate `cos_t = cos(t)`.

4. Before the actual animation, create a figure with [plt.subplots].
Save in `line1` and `line2` the plot handles of two lines (plt.plot), where both the `x_data` and the `y_data` should be empty
 (`[]`). Specify the function definition for $f_1$ and $f_2$ (see above) as the label and create the legend.
 The data for the lines will be updated during the animation.

5. Set the axis limits for `x` and `y` to the minimum and maximum of `x`, and to `-1` and `1` respectively.

6. [FuncAnimation] now needs a function that updates the plots for each time step.
The function receives the current frame number as an argument, which can be used as an index for the time values `t`. The plot handles must be returned as return values.
```python
def update(frame_num):
    """ for each frame, update the data stored on each artist. """

    line1.set_xdata(x)
    line1.set_ydata(f(t[frame_num]))

    # line2.set_...
    #

    return (line1, line2)
```
Here the function `f(t)` is assumed for the `y` values.

7. Now you can create an object of the class [FuncAnimation], to which you pass the figure, the update function, a number of frames (here 48), and an interval (here 16). Also pass the argument `blit=True`. Then you can display the animation with `plt.show()`. The display may only work if you run the script in a Python terminal and not in Interactive Mode. More on this see [MatplotlibTutorial].


8. Export a gif of the animation with
    ```python
    ani.save(filename="cos_animation.gif", writer="pillow")
    ```
    where `ani` is the FuncAnimation object.


## Hints

* All graphics commands in Matplotlib have a reference as return value that allows later access to the created object. This allows you to change all properties of graphics objects after their creation. This of course also applies to the data of lines to influence the animation.
