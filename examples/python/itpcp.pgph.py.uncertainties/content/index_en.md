# Error Propagation: Linear and Monte Carlo

## Introduction

Here you will use the package [uncertainties](https://pythonhosted.org/uncertainties/) for linear error propagation. We want to see where it reaches its limits with nonlinear functions. For comparison, we use the Monte Carlo method, which also works for nonlinear functions but only provides statistical results.

## Task

### 1. Linear Error Propagation

1. Follow the documentation of the uncertainties package and define a measured variable `t` with a value of $0.0$ and an error of $0.1$ as a `ufloat`. Then define a derived quantity `y_sin = sin(t)` and output `y_sin` with `print`. You should get the value and the linearly propagated error. Note: Use the `sin` function from the `uncertainties.umath` module (not `numpy`)

2. Calculate the expected value (`nominal_value`) and standard deviation (`std_dev`) of `y`, and store them together in the dictionary `out_sin = {"val": ..., "err": ...}`.

3. To understand the internal workings, also try the function `y.derivatives[t]`. This gives the partial derivative of `y` with respect to `t`. Apply linear error propagation manually to calculate the error of `y` and store the result in the variable `err_sin_manual`.

### 2. Comparison with Monte Carlo

1. Write a function `sample_uncertainties(t, n)` with default value `n=1000`, that draws `n` random numbers from a normal distribution based on `t` with expected value as its `nominal_value` and standard deviation `std_dev` and returns a `numpy` array. Use `np.random.default_rng` with seed 42 for this.

2. Calculate `t_samples` this way and the respective function values in `sin_t_samples`. Continue to use the `uncertainties` variant of sine and solve the error yourself that you will see shortly when you execute `sin(t_samples)` directly, e.g., through [List comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). Additionally, sample from the original `y` that was determined with linear error propagation, and store the function values in `sin_t_samples_linear`.

3. Plot both distributions in a histogram. Set the argument `density=True` for comparison with the density function. Also plot the density function based on `y_sin` on a `linspace` over `nominal_value +- 6*std_dev`. Conveniently, you can create a function `x_plot, p_plot = pdf_for_plot(x)` that does this generically.

### 3. Break the Linear Error Propagation

Now make the same plot for two more cases:

1. Set standard deviation $\Delta t = 0.3$.
2. Use the function `cos(t+0.05)` instead of `sin(t)` again with $\Delta t = 0.1$.

Think about why what you see happens. Is there a way out?
