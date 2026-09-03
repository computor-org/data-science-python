[np.loadtxt]: <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html> "np.loadtxt"
[Mean]: <https://numpy.org/doc/stable/reference/generated/numpy.mean.html> "np.mean"
[Standard Deviation]: <https://numpy.org/doc/stable/reference/generated/numpy.std.html> "np.std"
[fstrings]: <https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings> "fstrings"
[unbiased]: <https://en.wikipedia.org/wiki/Bias_of_an_estimator#Sample_variance>

# Lab Exercise 1

## Introduction

This task aims to show how Python can be used in lab exercises. For this purpose, temperature data
should be read from a file and output as a plot.

In the data file `data_lab1.dat`, temperature data is stored against its measurement time in hours.
The first column contains the time of measurement, the second contains the temperature values.

## Task

1. Add 3 more data points to the file `data_lab1.dat`:

    |Time|Temperature
    |---|---|
    |19.5|10.1|
    |20|9.3|
    |21|8|

2. Load the data from the file using [np.loadtxt] and save it in the variable `data`. The data is stored as an array. Check the dimension of the array with the attribute `.shape`.

**!** Pay attention to the "form" of the entries in your data file. To continue calculating with `Numpy`, define the data type as `np.float64` when loading the data. See the hint for this.

3. Use your new knowledge about indexing and save the time values in the variable `t` and the temperature values in `T`.

4. Calculate the [Mean] and the [Standard Deviation] (see links) of the temperature over the entire measurement period. Save the mean under `mean_T` and the standard deviation under `std_T`. **Note**: When no exact mean is known (it is also estimated from the data here), the parameter `ddof` in `np.std` must be set to `1` (yields *[unbiased] estimator*).

5. Plot the temperature values against time.

6. Label the axes with `t / h` and `T / °C`.

7. Create a string that you save under `title_str` and which should contain the following text:

   `Temperature Measurement: mean = "mean_T" °C, std = "std_T" °C`

   `"mean_T"` and `"std_T"` should be replaced by the respective calculated value with 2 decimal places. You need to create a so-called f-string for this (see [fstrings]).

8. Label the plot with `title_str` as the title.

## Hints

* When loading data, attention must be paid to the data type in the file as well as the marking of the separation. Here we load a text file. If we do this 'just like that', Python will first interpret the data type as `string`. For further calculations with NumPy, however, the data type should be `np.float64`. Add `dtype=np.float64` within `np.loadtxt()` for this.

* For the test, when loading the data using `np.loadtxt()`, only the name of the file may be entered, e.g., `np.loadtxt('Daten.dat', dtype=np.float64, comments="%")`. If a relative path is entered instead, the test cannot check this.

* To test your code locally (without the testing system), you must first ensure your terminal is in the folder containing the python script. If it isn't, right-click the `lab_exercise1.py` file, select "Copy path" and paste it into your terminal as `cd <path/to/folder>`. You can then execute the script by clicking the "Run" button or by entering `python lab_exercise1.py` in your terminal.

* In the first line in `data_lab1.dat`, you will find the description of the columns as a comment (`%`). When importing the data, difficulties arise in interpreting this description as a float like the following data points.
To mark the comments in the data file as such when loading, add `comments="%"` within `np.loadtxt()`.

* For automatic verification, attention must be paid to the spaces in the title!

* The mean sought here is unweighted; the measurement times do not factor into its calculation.
