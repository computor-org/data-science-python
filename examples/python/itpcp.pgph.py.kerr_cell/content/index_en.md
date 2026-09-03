[Probability Theory]: <http://itp.tugraz.at/LV/wvl/Statistik/A_WS_pdf.pdf>
[birefringent]: <http://en.wikipedia.org/wiki/Birefringence>
[np.loadtxt]: <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html> "np.loadtxt"
[plt.errorbar]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html> "plt.errorbar"
[np.polyfit]: <https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html> "np.polyfit"

# Kerr Cell

## Introduction

When isotropic dielectrics are placed in a homogeneous electric field,
they acquire the optical properties of a uniaxial
crystal and become [birefringent]. For the
phase difference $\Delta\phi$ between ordinary and extraordinary
rays, the *empirical Kerr law* states:
$$
  \Delta \phi = c\cdot U^2 \quad
  \begin{array}{rcl}
    c & \ldots & \text{Constant that depends on the wavelength of light} \\
    U & \ldots & \text{Voltage across a capacitor that generates the electric field}
  \end{array}
$$

In a laboratory experiment, data was recorded for this in `kerrtab_pu.dat`.
The file `kerrtab_pu.dat` contains the following data:

* Column 1: $U^2$
* Column 2: $\Delta\phi$ for green light
* Column 3: Error for green light
* Column 4: $\Delta\phi$ for yellow light
* Column 5: Error for yellow light
* Column 6: $\Delta\phi$ for blue light
* Column 7: Error for blue light

## Task

Write a Python script `kerr_cell` in which you analyze the data from the laboratory experiment:

1. Load the data from `kerrtab_pu.dat` using [np.loadtxt].

2. Create a graph and plot with [plt.errorbar] the $\Delta\phi$ including their errors as a function of $U^2$ for each color (all three in the same coordinate system). Help for plotting with error bars can be found in the hints.

    * Use the corresponding line colors green, yellow, and blue.
    * For the markers, use `*`, `o`, and `x`.
    * Do **not** connect the data points.
    * Follow this plotting order.
    * Give the error bar caps size 8.

3. Perform a linear fit for the constants `c_green`, `c_yellow`, and
  `c_blue`. Help for linear fitting can be found in the hints.

4. Output all constants formatted in the above
   order as follows:

    `U^2 dependence of phi for green light: 0.00047174`

    Pay attention to the exact spelling!

5. Plot the 3 regression lines `y_green = c_green*x` etc., over a vector
    `[0, 1.1*max(U^2)]` with 100 support points.

6. Turn on the grid for the graph.

7. Label the axes with $U^2$ and $\Delta\phi$
   (in LaTeX syntax, see hint).

8. Title the graph with `Linear Fit`.

9. Create a legend with `green`, `yellow`, and
  `blue`. (This is also useful when the image is printed in black and white).

10. Position the legend in the upper left.

11. Save the graph under the filename `voltage_dependence.png`.

## Hints

* To read the data, you can use [np.loadtxt]. `dtype=np.float64` can be helpful.

* First create all error bars and then the three regression lines.

* You can use the command [np.polyfit] for linear fitting. However, this does not necessarily
 place the regression line through the origin. If you want to achieve this, you may only use
 the formula $y = kx$ for the line. This leaves only
 the slope $k$ as the only parameter to be fitted. This is calculated from ($N$ = number of data points)
 $$k = \frac{\sum_{n=1}^{N}x_n y_n}{\sum_{n=1}^{N}x_n^2}$$

* For those interested: The analytical calculations for linear regression can be found
 in the script [Probability Theory] from page 296.

* In Matplotlib graphics, you can insert LaTeX syntax in labels and titles as follows:

    ```python
    plt.title(r"$\Delta U$")
    ```

* The text output should look like this:

    ```
    U^2 dependence of phi for green light: 0.00047174
    U^2 dependence of phi for yellow light: 0.00044188
    U^2 dependence of phi for blue light: 0.00062186
    ```

    To get the correct number of digits, use .nf where n indicates the number of desired digits. For example:

    ```
    print(f"U^2 dependence of phi for green light: {c_green:.8f}")
    ```

    Attention! For the test, the values must be rounded to exactly 8 decimal places.


* If you did everything correctly, your graph should look like this:

<div align="center">
<img src="mediaFiles/kerr_cell_image.png" alt="Test Image" width="100%" name="Kerrzelle"/>
</div>
