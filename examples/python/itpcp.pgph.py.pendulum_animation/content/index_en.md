[animation]: https://matplotlib.org/stable/users/explain/animations/animations.html
[contour]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html
[meshgrid]: https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
# Animation of a Pendulum

## Introduction

We now want to animate our pendulum. Use [animation] for this.

## Task


1. Modify the function `euler_symplectic(fun, dt, t_max, y_0)` (and your own functions from the last exercise) so that $\theta$ can now only go from $-\pi$ to $\pi$, since a value of $\theta = 3.2$ also corresponds to $\theta = 3.2 - \pi$.

2. Create an animation. This should consist of a subplot with two columns. On the left, the pendulum should be displayed, and on the right, the position in phase space. This is described by $\theta$ on the $x$-axis and $\omega$ on the $y$-axis (reminder: $\dot{\theta} = \omega$, the angular velocity).

3. Use [contour] to display contours of constant total energy. As in the last example, the potential energy should be $0$ when the pendulum is at rest.

4. Try different initial values, lengths, gravitational accelerations, and masses. Also test your own functions from the last exercise. Also observe the two different "regions" in phase space.

5. Save your most beautiful animation as a `gif`.

## Hints

* Use [meshgrid] for the contours.

* The test in this example only checks whether you have made the modification to `euler_symplectic(fun, dt, t_max, y_0)`.
