[docstring]: <https://en.wikipedia.org/wiki/Docstring#Python> "docstring"
[figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "figure"
[help]: <https://docs.python.org/3/library/functions.html#help> "help"
[plot]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html> "plot"


# Simple Plot with DocString

## Introduction

In this task, three curves are again created using the [plot] command. It is often useful to add a brief explanation or information about when and by whom the code was written. This is done using a [docstring].

### Docstring

Docstrings are used to provide general information about a class, a module, or a function.
Usually this is a descriptive text to explain in more detail what function the following lines of code (or the class, module, function) have and how they are used.
At the beginning of a code, information such as the creation date, which person wrote the code for what purpose, the version, etc. is also specified as a docstring.
A docstring is therefore important for documenting the code.

While short comments for individual lines of code and expressions are written using `#`:

```python
m = 3               # [kg], mass
g = 9.81            # [m/s^2], average gravitational acceleration
F_g = m * g         # gravitational force
```

docstrings are built in using multi-line comments. At the beginning of a script, this could be implemented as follows:

```python
"""
Multiline comment
This code snippet serves as an example for a docstring
Created by: TU Graz ITPCP
Date: 23.09.2024
"""
```



## Task
 The following plot is to be created by you in the script `plot_docstr.py`:

1. Define the variables

    |Variable|Value|
    |:--|:--|
    |`x`| Vector from $-\pi$ to $+\pi$ with $200$ values|
    |`y_1`| $y_{1} = x$|
    |`y_2`| $y_{2} = x^{2}$|
    |`y_3`| $y_{3} = x^{3}$|

2. Create a matplotlib figure with multiple lines: Plot
    * $y_{1}(x)$; solid line; red
    * $y_{2}(x)$; dashed line; blue
    * $y_{3}(x)$; dotted line; black

3. Set the limits of the abscissa to minimum and maximum of $x$, the limits of the ordinate to minimum and maximum of $y_{3}$.

4. Label the abscissa with $x$, the ordinate with $f(x)$ and give the Figure the title `Test`.

5. Write a [docstring] at the beginning of the script: This should then be callable in the
console (`python` in the terminal, not in the file itself or Interactive Window)
with the command `help(plot_docstr)`. Since Python [help]
only allows this for modules, classes, and functions, you have to use
a trick for this attempt: First enter `import plot_docstr` in the console
to import `plot_docstr.py` as a module.

For automatic verification, the help text should contain the following:

        Python Script: "Name of the script"
        Simple plotting program
        Name: "First name" "Last name"
        Date: "Date in format DD.MM.YYYY"


## Hints

* You can copy the help text here in the task (point 5) and then paste it into the program
(Copy&Paste). Replace everything in quotation marks (`"`) with
the necessary text or the necessary date, e.g., `"First name"` with
`Carmen`. Leave other parts of the text as they are.

* For the test, the quotation marks (`"`) in the docstring **must not** remain.


## Keywords

- Docstring
- Comments
- Plotting