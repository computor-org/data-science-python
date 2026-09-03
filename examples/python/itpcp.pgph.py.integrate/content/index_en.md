[ValueError]: https://docs.python.org/3/library/exceptions.html#ValueError
[erf]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.erf.html
[epsilon]: https://numpy.org/doc/stable/reference/generated/numpy.finfo.html
[np.sum]: https://numpy.org/doc/stable/reference/generated/numpy.sum.html
# Numerical Integration

## Introduction

To integrate numerically, we divide our integral into several smaller integrals. Our first integration method is the simple trapezoidal method. We first focus only on the partial integral in blue, see sketch. We can generally write this as $\int_{x_i}^{x_{i + 1}} f(x) \, dx$ and approximate it as

$$
\int_{x_i}^{x_{i + 1}} f(x) \, dx \approx f_{i + 1} \cdot h + \frac{(f_{i} - f_{i + 1})}{2} \cdot h \\ = \frac{h(f_{i} + f_{i + 1})}{2},
$$


where we used the notation $f_{i} = f(x_{i})$ and $h = x_{i + 1} - x_i$.

<div align="center">
<img src="mediaFiles/trapez_int.png" alt="Image" width="100%" name="Trapez"/>
</div>


Now we consider the complete integral, i.e., from start $a$ to end $b$. We discretize for equidistant values using $x_i = a + i \cdot h$ with $h = \frac{b - a}{N}$. The value of the complete integral therefore becomes $I_\mathrm{t}$ using the trapezoidal method, which we can rewrite as

$$
\int_{a}^{b} f(x) \, dx \approx I_\mathrm{t} = \frac{h(f_{0} + f_{1})}{2} + \frac{h(f_{1} + f_{2})}{2} \dots + \frac{h(f_{N - 2} + f_{N - 1})}{2}+ \frac{h(f_{N - 1} + f_{N})}{2} \\ = \frac{h(f_{0} + f_{N})}{2} + h \sum ^{N - 1} _{i=1} f_i.
$$

From our sketch, it becomes clear that our result will be closer to the correct value if we increase $N$ and thereby decrease $h$. To find out how the error of the integration method scales with $h$, one could do a Taylor series expansion, but we want to proceed graphically.


## Task



  1. Write in `numeric_int.py` a function that uses the trapezoidal method according to the formula given above. Proceed without loops.
```python
  def trapezoidal(fun, a, b, N):
    """
    input:
    fun: Function to be integrated
    a: lower limit of integration
    b: upper limit of integration
    N: number of subintervals

    output:
    I_t: value of the integral
    """

```

2. Write in `numeric_int.py` analogously a function that uses the Simpson method. This uses $3$ points for each partial integral and the total integral is approximated as

$$
\int_{a}^{b} f(x) \, dx \approx I_\mathrm{s} = \frac{h}{3} (f_0 + 4 f_1 + 2 f_2 + 4 f_3 + \dots + 2 f_{N-2} + 4 f_{N - 1} + f_N).
$$

Proceed here also without loops. Use [ValueError] if $N$ is odd, since the equation in this form only applies to even values of $N$.

```python
  def simpson(fun, a, b, N):
    """
    input:
    fun: Function to be integrated
    a: lower limit of integration
    b: upper limit of integration
    N: number of subintervals

    output:
    I_s: value of the integral
    """
```


3. Now use your functions in `integrate.py` to calculate analytically solvable integrals. Use lambda functions for $\int_0^1 x~dx, \int_0^1 x^2~dx, \int_0^1 x^3~dx, \int_0^1 x^4~dx$ and $\int_0^1 e^{-x^2}~dx$. This allows us to analyze the absolute error of the methods as a function of the interval spacing, $h$. Create the $3$-dimensional array `errors` with dimensions `(i, j, 2)`, where in `[i, j, 0]` the errors for the trapezoidal method and `[i, j, 1]` the errors for the Simpson method should be stored. Here $i$ is the index for the different functions and $j$ is the index for the different $N$ (and thus $h$ since when we increase the number of intervals, we thereby decrease the interval width). Here $N$ should take the values `[10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]`. However, first try your function with lower values of $N$ (You will have to wait a long time here if you used loops).

4. Set errors that are smaller than the machine precision (epsilon) to [epsilon].

5. Create a double-logarithmic subplot for the errors, see figure. Save your figure as `integration_errors.png`.


## Hints
* $\int_0^1 e^{-x^2}~dx = \frac{\sqrt{\pi}}{2} \cdot \text{erf(1)}$, where [erf] is the error function.

* Use [np.sum] instead of sum for the integration methods. Do you see a difference?

* Food for thought: Why do the errors of the different functions scale differently? Think about why the error increases for very small values of $h$. What do you conclude from this?

* Your figure should look approximately like this:


<div align="center">
<img src="mediaFiles/integration_errors.png" alt="Image" width="100%" name="integration_errors"/>
</div>
