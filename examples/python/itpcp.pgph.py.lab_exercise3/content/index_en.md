[np.polyfit]: <https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html>
[plt.errorbar]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html>
[Probability Theory]: <http://itp.tugraz.at/LV/wvl/Statistik/A_WS_pdf.pdf>

# Lab Exercise 3

## Introduction

This exercise is intended to be an introduction to fitting and plotting data with uncertainty.
The data available in this exercise are current and voltage measurements stored in the file `data_lab3.dat`.
The first column contains the voltage values, the second contains the current values.

Simple fits of polynomial functions can be performed in Python using the `numpy` function [np.polyfit].
The function uses a so-called *linear least squares* method, in which the parameters of the polynomial function are
calculated to best describe the data. For a polynomial of degree `n`, the function is applied as follows:

```python
popt, pcov = np.polyfit(xdata, ydata, deg=n, pcov=True)
```

Here `popt` are the optimized parameters and `pcov` is the so-called covariance matrix. The square roots of the diagonal elements of the matrix are the standard deviation of the determined parameters
(for details see script [Probability Theory]). The fitted functions can then be plotted with the uncertainties as error bars using [plt.errorbar] (see documentation).

## Task

Write a script `lab_exercise3.py` in which you analyze the data from the laboratory experiment:

1. Load the data from `data_lab3.dat` and save the columns in appropriate vectors. Make sure that the entire program calculates only with **milliamperes** and not with amperes.

2. Create two vectors of the correct length filled with the uncertainty of the measurements. The uncertainty of the current measurement is 0.5 mA, that of the voltage measurement is 1 V.

3. Fit the data with a straight line (first-order polynomial). Use the command [np.polyfit] for this.

4. Save the fit parameters in the variables `slope` and `offset`.

5. Save the uncertainty of the fit parameters in the variables `delta_slope` and `delta_offset` for a 95% confidence interval (2 sigma).

6. Create a vector `U_fit` with 100 values between the smallest and largest voltage value.

7. Create a vector `I_fit` in which the current values of the line are calculated using `U_fit`, the slope `slope`, and the offset `offset`.

8. Create a graph and plot with [plt.errorbar] the current values in mA on the y-axis against the voltage values in V on the x-axis with their respective uncertainties from point 2.
    * Use red as the line color for the error bars.
    * For the markers, use blue `x`.
    * Do **not** connect the data points.

9. Plot the line (`I_fit` against `U_fit`) as a solid green line.

10. Give the graph the title *Linear Fit* and label the axes as learned in **Lab Exercise 1**.

11. Create a legend for the plots.
    To do this, add a `label` attribute with the respective text for each line. Then display the legend with

    ```python
    plt.legend()
    ```

    The text for the label for the fit should be defined in a variable you create:

    ```
    linear fit: k = `slope` ± `delta_slope` mA/V, d = `offset` ± `delta_offset` V
    ```

    The variables are to be inserted as in the previous example with f-strings. The number of decimal places should be chosen so that the uncertainty has exactly one digit not equal to 0. The associated parameter should also be set to this number of decimal places. The determination of the number of digits can be done manually; no program is needed for this!

## Hints

* Pay attention to the commented first line of the data file!

* To get the 95% confidence interval with 2 sigma, multiply the uncertainty of the fit parameters by 2

* When plotting with [plt.errorbar], you can use the *keyword arguments* `fmt`, `color`, and `ecolor` to set the marker and the colors of the data points and error bars. With `capsize`, you modify the size of the error bars.

* To get the ± character, simply copy it from the task or use LaTeX math mode with `$\pm$`.

* If you did everything correctly, your graph should look like this:

<div align="center">
<img src="mediaFiles/Lab_exercise3.png" alt="Labor 3" width="70%" name="Labor 3"/>
</div>
