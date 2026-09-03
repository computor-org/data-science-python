# Gaussian Distribution

## Introduction

### Mathematical Background

In probability theory and also in physics, the normal distribution or Gaussian distribution has great significance. It is defined by

$$
\begin{align}
g(x)= \frac{1}{{\color{red}\sigma} \sqrt{2\pi}} \exp\left\{-\frac{(x-{\color{red}x_{0}})^2}{2 \color{red}\sigma^2}\right\} \; ,
\end{align}
$$

where $x_{0}$ and $\sigma$ are the parameters of the distribution. At $x_{0}$ lies both the maximum and the center of symmetry, and $\sigma$ is the distance from this center to the inflection points. As for any probability distribution,

$$
\begin{align}
\int_{-\infty}^{\infty} g(x) \, \mathrm{d} x = 1 \; .
\end{align}
$$

In physics, a summation over several Gaussian functions with different parameters is also frequently used. The purpose of this is to represent several maxima simultaneously. In general, the function can then be defined as

$$
\begin{align}
g(x)= \frac{1}{n} \sum_{k=1}^{n} \frac{1}{{\color{red}\sigma_k} \sqrt{2\pi}} \exp\left\{-\frac{(x-{\color{red}x_{0k}})^2}{2 \color{red}\sigma_k^2}\right\} \; ,
\end{align}
$$

where $x_{0k}$ and $\sigma_k$ have the same meaning as before. The summation is over all $n$ values of the parameters $x_{0k}$ and $\sigma_k$. Therefore, to maintain normalization, we divide by $n$.


## Task

You need to create two files:

### Function

Write a function `gauss1d` that with the following call

```python
g = gauss1d(x, x0, sig)
```

calculates the Gaussian distribution as a function of the vector `x`.

1. Set the default values

    ```python
        x0 = [-1.0, 1.0]
        sig = [ 0.5, 1.0]
    ```

2. Initialize `g` as a field of zeros with the size of `x`.

3. Form the sum over all $k$ values of the parameters ($k = 1, \dotsc, n$) using
  a single for loop. Don't forget
  that `x` can be an array.

### Script

Write a script `gauss1d_script.py` and complete the following
tasks:

1. Create a row vector `v` with `400` values between `-5` and `5`.

2. Define `max_val = [-2,0,2,4]`.

3. Define `sig_val = [0.5,0.25,0.125,0.0625]`. Think about how you can easily
  create this vector without writing out the values!

4. Calculate the variable `y` using these values with `gauss1d`.

5. Plot `y(v)`.


## Hints

* A for loop helps with the summation over
  the individual contributions to the sum. It is
  practical if you create a field before the loop that is the same
  size as the input variable `x`, but contains only zeros.
  The most sensible command for this is:

    ```python
    g = np.zeros(x.shape)
    ```

  Then you can write `g = g + ...` (or with *compound assignment* also `g += ...`)
  in the loop and at each pass the values for one peak
  are added. After the end of the loop, you must divide by the number of peaks
  `n`, i.e., by the length of the vector `x0` (or `sig`).
  This ensures normalization even with multiple peaks.
