[lambda]: <https://python-reference.readthedocs.io/en/latest/docs/operators/lambda.html> "lambda"
[integrate.quad]: <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad> "integrate"
[example]: <https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html> "example"
[semilogy]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html> "semilogy"

# Approximation of $\pi$ with Integrals

## Introduction

There are some interesting integrals whose solution involves $\pi$. We now want to approximate $\pi$ using three of these integrals.

*  In probability theory, the integral over the [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) is very important:
$$
\int \limits_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

*  Also very important in physics is the function value of the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at position $\frac{1}{2}$:
$$
\Gamma \left(\frac{1}{2}\right) = \int \limits_0^\infty e^{-x}
x^{-\frac{1}{2}}  dx = \sqrt{\pi}
$$

*  A very interesting approximation to $\pi$ also results from this integral:
$$
\int \limits_0^\infty  \frac{\sin x}{x}  dx = \frac{\pi}{2}
$$

## Task

Complete the following tasks:

1. Create the variables `max_iter = 30` and `N = 40` as well as the array `iteration_steps`, which should go from `0` to `max_iter` in `N` steps. As we will see, the end value of `max_iter = 30` is already a very good upper limit for some integrals to approximately converge to $\pi$.

2. Create three zero vectors `[pi_norm, pi_gamma, pi_sin]` that have the length of `iteration_steps`.

3. Store the functions to be integrated (see above) as [lambda] functions in `fun_norm`, `fun_gamma`, and `fun_sin`. Here, `fun_norm` means for example $e^{-x^2}$.

4. Integrate the functions with [integrate.quad] as follows:
    * To see how the integrals converge to the limit value $\pi$, the variable `pi_i(n)` should contain the value of the integral ranging from `0` to `iteration_steps(n)`.
    `i` stands for `norm`, `gamma`, or `sin`.
    * So that the program does not always have to integrate over the entire interval, write a `for` loop in which you calculate the integrals in the interval `[iteration_steps(n-1),iteration_steps(n)]`. To obtain the value `pi_i(n)`, you must still add the result of the previous integrals `pi_i(n-1)`.

5. The results of the integration must still be exponentiated or multiplied by appropriate prefactors to yield $\pi$!

6. Now plot the result using two subplots stacked on top of each other with a shared $x$-axis (`sharex = True`):
    * The first plot should contain both a line at the value $\pi$ and the results of the integrals. Plot these first. The line properties of the plots can be found in the table below. Use `axhline`.

    * The second plot should be semi-logarithmic in $y$ ([semilogy]). In this plot, enter the distance ( $= abs(\pi_i - \pi)$ ) to $\pi$. Again, the corresponding formatting can be found in the table. This plot clearly shows how fast the individual integrals converge to the limit value.

7. Set `xlim` for both diagrams according to the maximum integration limits. Also label both diagrams:
    * The x-axes should each be labeled with "$x$".
    * The y-axis should be labeled with "$f(x)$" for the first plot and "$|\pi - f(x)|$" for the second plot.
    * The title of the first diagram should be "`Values of the Integrals`".
    * The title of the second plot should be "`Convergence of the Integrals`".

8. Add a legend to both diagrams:
     * The $\pi$ line should be labeled with "$\pi$",
     * the function `fun_norm` with "`Normal`",
     * the function `fun_gamma` with "`Gamma`", and
     * the function `fun_sin` with "`Sinus`".

    The legend in the first plot should be placed in the lower right corner and in the second plot in the lower left corner.



**Color and pattern for the plots of the different integrals:**

|Function | Color | Line style
|---|---|---|
|$\pi$ | black | dotted
|`fun_norm` | red | solid line with dots
|`fun_gamma` | blue | solid line with dots
|`fun_sin` | green | solid line with dots


## Hints

* Reference plot:

<div align="center">
<img src="mediaFiles/plot.png" alt= "Test Image" width="70%" name="Plot"/>
</div>
