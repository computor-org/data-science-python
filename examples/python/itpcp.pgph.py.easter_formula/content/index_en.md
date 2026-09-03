[arithmetic operator]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetic operators"
[Wikipedia article]: <https://en.wikipedia.org/wiki/Date_of_Easter#Anonymous_Gregorian_algorithm> "Gaussian Easter Formula"
[f-string]: <https://docs.python.org/3/tutorial/inputoutput.html> "f-string"
[input]: <https://docs.python.org/3/library/functions.html#input> "input"
[int]: <https://docs.python.org/3/library/functions.html#int> "int"
[print]: <https://docs.python.org/3/library/functions.html#print> "print"

# Gaussian Easter Formula

## Introduction

The Gaussian Easter formula is a set of equations that can be used to calculate the date of Easter Sunday for a chosen year.

Below, only the equations are given (variable `X` is the year number).
More information about the algorithm can be found in this [Wikipedia article].

$$
\begin{aligned}
a & = X \mod 19 \\
b & = X \mod 4 \\
c & = X \mod 7 \\
k & = X \div 100 \\
p & = (8 k + 13) \div 25 \\
q & = k\div 4 \\
M & = (15 + k - p - q) \mod 30 \\
N & = (4 + k - q) \mod 7 \\
d & = (19 a + M) \mod 30 \\
e & = (2 b + 4 c + 6 d + N) \mod 7 \\
E & = 22 + d + e \\
\end{aligned}
$$
The variable $E$ here stands for the Python variable `easter_sunday`.

With these formulas, note that the result of `easter_sunday` represents the date of Easter Sunday in March days (i.e., March 32 = April 1,
etc.).

The operation $\div$ represents integer division (division without remainder), which in Python is denoted with the [arithmetic operator] `//` instead of `/`.
$\mod{}$ (modulo) means the remainder of division, e.g., $5 \mod 3 = 2$.
Modulo is denoted in Python with the operator `%`, i.e., `5 % 3` returns `2`.

## Task

Create a Python script `easter_formula` that calculates the date
of Easter Sunday in a specific year using the Gaussian
Easter formula.


The script should do the following:

 1. Read the year number under the variable `X` from the keyboard ([input]).
  The text for the input prompt should be **`"Year for calculating Easter: "`**. To convert the read string to an integer, use
  the function [int].

2. Calculate the formulas from the introduction section. Use the same
    variable names.

3. As described in the introduction section, you get the date of Easter Sunday in March days.
  However, it would be nicer to separate into the months March and April. Please add
  the following program lines before the [print] command:
  ```python
  if easter_sunday <= 31:
      month = 'March'
  else:
      easter_sunday -= 31
      month = 'April'
  ```
  The above if-else control structure, which assigns to the correct month,
  will be discussed in more detail in a later week and should not confuse you here.
  The operator `-=` means that the value 31 is subtracted from the variable `easter_sunday`;
  with this notation, you don't have to repeat the variable name.

4.  Output the date of Easter Sunday formatted with the function
  [print]. To insert the respective values into the
  string, [f-string]s are suitable. The following sentence (string) should be output by `print`:

  **Easter Sunday in the year "value of X" is on "value of easter_sunday" "value of month"**


## Hints

* This script uses the Python function [input]. Therefore, use _Run Python File_ instead of _Run in Interactive Window_ to run the script in the _Terminal_, where you can enter the desired year.

* Make sure to calculate the variables of the Easter formula correctly, see introduction.
Also pay attention to the correct choice of operators used.

* Try out your Easter formula yourself!

Some Easter Sundays for self-testing:

| Year   | Easter Sunday |
| ---    | ----------    |
| 2025   | April 20      |
| 2024   | March 31      |
| 2022   | April 17      |
| 2005   | March 27      |
| 1990   | April 15      |
| 1500   | April 01      |


## Keywords

- Console input
- Console output
- Modulus