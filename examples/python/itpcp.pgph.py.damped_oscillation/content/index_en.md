# Fitting Damped Oscillations

## Introduction


A damped oscillation can be described as

$$
\begin{aligned}
  y(t,A,\omega,\phi,\tau) &= A \sin(\omega t + \phi) \cdot \exp(-t / \tau)\; , \\
\end{aligned}
$$
where $t$ is the time, $A$ is an amplitude, $\omega$ is a frequency, $\phi$ is a phase shift, and $\tau$ is a decay time. For the model function used for fitting, we use time `t` and the coefficients $A$ (`A`), $\omega$ (`omega`), $\phi$ (`phi`), $\tau$ (`tau`).


## Task


1. Read in the file `decay_osc.dat`. This contains the measurement data, with the time points in the first column and the measured values for $y(t)$ in the second column.

2. Write the function `f_model`, which takes $t$ and the above-mentioned parameters as input to calculate $y$.

3. Use [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) from scipy to calculate the parameters, using `[4, 1, 1, 10]` as initial values.

4. Evaluate the fitted function at $500$ points for `t`, starting at $0$ and ending $20$ time units after the last measurement time. Store the result in `y`.

5. Use [fmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html) to obtain the minimum value of $y$, `y_min`, together with the corresponding time point `t_min`. Similarly, find `y_max` with the corresponding `t_max`.

6. Display your results graphically. Plot $y(t)$, the measured values, and mark the minimum and maximum of $y(t)$.
