# Fitting Radioactive Decays

## Introduction

In this Python script, various interpolation methods are applied to data and the results are compared graphically.

## Task


1. Load the measurement data from the `inter_data.dat` file. The first column of the file contains the $x$ values and the second column contains the $y$ values.


2. Create the array `x_int`, which contains evenly distributed numbers from the first to and including the last $x$ value with $500$ support points.

3. Apply various interpolation methods using scipy:

    - `'nearest'`: The nearest neighbor method where the interpolated value at a query point is the value at the nearest sample grid point (discontinuous).

    - `'linear'`: The interpolated value at a query point is based on linear interpolation of the values at neighboring grid points in each dimension (values are continuous, derivatives are discontinuous).

    - `'pchip'`: (Piecewise Cubic Hermite Interpolating Polynomial) The interpolated value at a query point is based on a shape-preserving piecewise cubic interpolation of the values at neighboring grid points (values and first derivative are continuous, curvature is discontinuous).

    - `'cubic'`: Cubic spline interpolation. The interpolated value at a query point is based on a cubic interpolation of the values at neighboring grid points in each dimension (values, first derivative, and curvature are continuous).

4. Save the interpolated $y$ values as `y_nearest`, `y_linear`, `y_pchip`, and `y_spline`.


5. Create a $2 \times 2$ subplot to display the results for each interpolation method. Also plot the original values.
