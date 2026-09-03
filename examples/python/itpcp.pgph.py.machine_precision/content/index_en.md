[Machine Precision]: <https://en.wikipedia.org/wiki/Machine_epsilon> "Machine Precision"
[input]: <https://docs.python.org/3/library/functions.html#input> "input"
[dtype]: <https://numpy.org/doc/stable/reference/arrays.dtypes.html> "dtype"
[print]: <https://docs.python.org/3/library/functions.html#print> "print"
[finfo]: <https://numpy.org/doc/stable/reference/generated/numpy.finfo.html>

# Comparison of Formulas

## Introduction

In this task, the equivalence of mathematical identities is to be examined using the comparison operator `==`.

Pay attention to the difference between 'analytical' equivalences and the results of numerical calculations.

## Task

Create the Python script `compare`, which verifies mathematical identities.

1. Have the user define the variables $x$ and $y$ using the [input] function. Their data type is `np.double`. Use `input` to make clear during execution which value is currently required, for example:

    ```python
    x = input('Please input x: ')
    ```

2. Create the arrays `left` and `right` and insert the following expressions.

    |n|`left`|`right`|
    |-|:----:|:-----:|
    |0|$\log\left(\dfrac{x}{y}\right)$|$\log(x) - \log(y)$
    |1|$\log(xy)$|$\log(x) + \log(y)$
    |2|$\exp(\mathrm{i} x)$|$\cos(x) + \mathrm{i} \sin(x)$
    |3|$\exp(-\mathrm{i} x)$|$\cos(x) - \mathrm{i} \sin(x)$
    |4|$\exp(x + y)$|$\exp(x) \exp(y)$
    |5|$\exp(x - y)$|$\dfrac{\exp(x)}{\exp(y)}$
    |6|$\sin(x + y)$|$\sin(x) \cos(y) + \sin(y) \cos(x)$
    |7|$\cos(2x)$|$2 \cos(x)^{2} - 1$
    |8|$\sin(2x)$|$2 \sin(x) \cos(x)$
    |9|$\cosh(x)$|$\dfrac{\exp(x) + \exp(-x)}{2}$

    ! Attention, the data type must be `np.cdouble, np.complex128, np.complex_, np.cdouble,` or `complex` for the test to work.

3. Check whether the two arrays have the same contents. Use the operator `==` for this and save the result in the variable `v_exact`. As you will notice, not all columns will match. This is because differences in the last decimal places can occur due to the different calculation methods.

4. Therefore, check whether the absolute difference of the arrays is less than $10 \varepsilon$ and save the result in the variable `v_epsilon`. $\varepsilon$ is the machine precision, which indicates the upper limit for rounding errors and the distance between 1.0 and the next higher decimal number. For `np.float64`, $\varepsilon$ is $2^{-52}$. In a few cases, even $\varepsilon$ is not sufficient to numerically demonstrate the equivalence of two results, but with $10 \varepsilon$ you are usually on the safe side.

5. Output `v_exact` and `v_epsilon` using [print] with preceding explanatory text. Think about or discuss with your tutor about the output of this example.

## Hints

* Since [input] returns a string, you must first convert $x$ and $y$ to another data type.

* When initializing your arrays, make sure that they will also contain complex values. This means you must set the data type, [dtype], to complex.

* The imaginary unit is written as $j$ in Python.

* For the machine precision, refer to the documentation for [finfo].
