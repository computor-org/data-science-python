# Fitting Radioactive Decays

## Introduction

We consider radioactive decay in a decay chain. At time $t = 0$ we have only isotope $1$, namely $N_{01}$ of them. However, isotope $1$ decays to isotope $2$ with the decay constant $\lambda_1$. Isotope $2$ now further decays to the stable isotope $3$. This happens with the decay constant $\lambda_2$. It can be shown that the number of isotope $2$, $N_2(t)$, behaves over time according to the following equation:

$$
  N_2(t) = N_{01} \big[1 - \exp(-\lambda_1 t)\big] \exp(-\lambda_2 t).
$$

We now measure $N_2$ at various times and want to fit the function.

## Task


1. Read in the file `expfun.dat`. This contains the measurement data, with the time points in the first column and the measured values for $N_2(t)$ in the second column.

2. Write the function `f_model`, which takes $t$ and the above-mentioned parameters as input to calculate $N_2$.

3. Use [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) from scipy to calculate `N_01`, `lambda_1`, and `lambda_2`. Use `t` from $0$ to $25$ with $500$ support points and `[100, 4, 0.5]` as initial values.

4. Use your function to determine `N_2(t)`.

5. Use [fmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html) to obtain the maximum value of $N_2$, `N_2max`, together with the corresponding time point `t_max`.

6. Display your results graphically. Plot $N_2(t)$, the measured values, and mark the maximum of $N_2(t)$.

7. Additionally calculate and plot `N_1` and `N_3`, as well as the sum of the $3$ isotopes. Label the graph appropriately. Formulas:

$$
  N_1(t) = N_{01} \exp(-\lambda_1 t),
$$
$$
  N_3(t) = N_{01} \big[1 - \exp(-\lambda_1 t)\big] \big[1 - \exp(-\lambda_2 t)\big].
$$
