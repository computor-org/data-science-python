# Data Types (Classes) in Python

## Introduction

In this task, variables of different (numeric) data types (File:
`data_types.py`) are created, the data type of the variables is checked, and the variables
are converted (transformed into another type).

### Classes in Python and NumPy

Basically, a distinction is made between the classes Boolean (logical), Numeric, Text
(string), Function and Object references, and structures like Lists, Tuples,
Dictionaries, etc. Different modules can in turn define classes (we can
also define our own classes), such as the widely used NumPy array, which
can contain numbers of certain basic types. In this exercise, we limit ourselves to
numeric types.

In Python itself, there are the numeric data types `bool` (*Boolean*, `True` or
`False`), `int` (*integer*, whole number), `float` (*floating point with double precision*,
floating point number), `complex` (complex floating point number). These are automatically
recognized by Python and do not need to be specified.

```python
var_int = 3                 # integer
var_float = 3.              # float, double precision
var_float2 = 3.1            # float, double precision
var_string = 'hello world'  # string
var_compl = 4 + 1j          # complex double
```

These are extended for numerical programs with the [NumPy data types], which
can underlie NumPy arrays. For example, Python `float` corresponds to
`np.float64` (`numpy` is often abbreviated as `np`). However, there are also `np.float32`,
`np.float16`, etc. with correspondingly many bits for representing numbers.

Easy to imagine are the size restrictions of data types for integers. The
integers include *signed* (e.g., `int8`,
`int16`, ...) and *unsigned* (e.g., `uint8`, `uint16`, ...)
integers. Here, `np.int8` for example has 8 bits available. The largest possible number?
$127$, since of course negative numbers $\ge -128$ are also possible.

And with `uint8` (u stands for unsigned)? Here the largest number is $2^8-1 = 255$.

More detailed information can be found in the documentation about [NumPy data types].

The data type `str` (so-called character strings or *strings*) occurs, among other things, in
labeling plots (e.g., with `xlabel`).

List, Tuple, Dict, Set, ... function like containers and can contain multiple
data types. More details on this can be found in the additional exercise on structures.

In object-oriented programming languages like Python, you can create your own classes
(data types) (e.g., a class Polynomials). In this class, you can
for example define a method for adding polynomials. This also allows you to
*overload* operators like `+`, `-`, `*`, `/`, etc. A `+` operator applied to an
object of the class Polynomials would then perform polynomial addition.

With the command `type(var_name)`, you can display the class of the variable
`var_name` in the console. To save the class name as a string, access
the attribute `__name__`, so

```python
type(var_name).__name__
```

If the variable is a NumPy array, you can display the type of the stored numeric values with the attribute
`dtype`.

With the command `help(var_name)`, you can display the class of a variable and all
commands defined for it (`+` for example as function `__add__()`).

## Task

1. Declare the following 6 variables with different [NumPy data types] with
   the following values. For automatic testing, it is essential that you use
   <span style="color: red;">exactly these names</span> for your variables!
   Use the console to test your program!

   | Variable | Value               | Data Type |
   | -------- | ------------------- | --------- |
   | `a`      | $80$                | int8      |
   | `b`      | $121$               | uint8     |
   | `c`      | $116$               | uint16    |
   | `d`      | $e^{4.645}$         | double    |
   | `e`      | $111.111$           | double    |
   | `f`      | $\frac{141}{4} \pi$ | single    |

1. Now save the data types of the just declared variables `a` to `f` under
   the names `type_a` to `type_f`.

1. Analogous to declaring variables, you can also redeclare them (assign a new
   data type). This is also called *cast* and is done for example as follows:

   ```python
   var = np.int8(1.34)
   var2 = np.float(var)
   ```

   It is immediately apparent that this is not always safe.

   Now cast all the just defined decimal numbers to integer (replace the
   old variables with the new values). Use **no** bit specifications (like `int8` or `uint16`).

   Next, declare the variables `a` to `f` with the function [chr] to the
   data type `str`. Save the result under the variables `char_a` to
   `char_f`.

   The class `str` in Python has implemented the operator `+` as an example so that
   it simply concatenates strings.

   Now create the variable `word` where you combine `char_a` to `char_f` in alphabetical
   order and output the resulting string with `print`.
   Surprised?

1. Now we address the dangers of these casts.

   With smaller data types, memory can be saved on the one hand, but information
   can also be lost when redeclaring (casting). Define
   the following variables as `double`:

   | Variable | Value                 |
   | -------- | --------------------- |
   | `test1`  | $1.8 \cdot 10^{-60}$  |
   | `test2`  | $1.4$                 |
   | `test3`  | $1.5$                 |
   | `test4`  | $128$                 |

   Cast the variable `test1` to the type `single` and save the result
   as `cast_test1`. What happens to `test1`?

   Try to cast the variables `test2` to `test4` to the type `uint8`
   (`cast_test2` to `cast_test4`). What do you notice? What happens when you
   cast `cast_test4` to the type `int8` (`cast_test5`)? Now try for yourself whether
   casting also works for `test_4`. Answer the following question for yourself: Does
   this have something to do with the size of the data type? (To answer this, the
   `view` member function of numpy's data types (`np.uint16(22).view(np.int16)`)
   can be used)

   The differences you see are partly related to the largest and smallest
   representable numbers for a certain data type. The
   Python standard data type `int` (`long`) has no limit in representability,
   but the [NumPy data types] are limited to their bit count and usually
   system-dependent. To find out more, there are commands like
   `np.finfo(np.float64)`, see documentation on [floatinfo] and [numpy.finfo].

1. When combining different data types, note that Python (or
   NumPy) automatically casts to the more comprehensive data type.

   Create the following variables

   | Variable    | Value | Data Type |
   | ----------- | ----- | --------- |
   | `pos_var_1` | 255   | uint8     |
   | `pos_var_2` | 1     | int8      |
   | `pos_var_3` | 1     | double    |
   | `pos_var_4` | 1     | uint8     |

   Now save in the variables `p1_plus_p2`, `p1_plus_p3`, and `p1_plus_p4` the
   sum of the first and the second, the first and the third, and the first and the
   fourth variable respectively.

   Do both results match? Can you explain the results?

## Hints

- Declaration in Python is simply done in the form of `var = datatype(value)`, e.g.,
  `var = np.float32(1.13)`. The data type `double` or `int` does not need to be
  specified, as this is the default case (depending on the definition of the value: 1.0
  or 1).

[chr]: https://docs.python.org/3/library/functions.html#chr
[floatinfo]: https://docs.python.org/3/library/sys.html#sys.float_info
[NumPy data types]: https://numpy.org/doc/stable/user/basics.types.html
[numpy.finfo]: https://numpy.org/doc/stable/reference/generated/numpy.finfo.html
