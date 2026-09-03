# Polynomials

## Introduction
Polynomials are mathematical functions that consist of sums of powers of a variable. In general, a polynomial of degree $n$ has the form:
$$a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$$

Due to their simple structure, polynomials can be easily added, subtracted, multiplied, differentiated, and integrated.

This is now to be implemented using a Python class in `polynom.py`.

### Polynomial Class:
An object of the class `Polynom` should be created by passing a list of coefficients. The first coefficient should correspond to the highest degree of the polynomial, e.g.: `Polynom([5,0,0,2,3])` corresponds to $$5x^4 + 2x + 3.$$


Additionally, the Python internal methods `__add__`, `__sub__`, `__mul__`, `__eq__`, `__str__`, `__call__`, and `__len__` should be overwritten (see [function-overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/) for more details). These should make it possible to add, subtract, multiply, and output polynomials.

* The addition `__add__` of two polynomials should return a new polynomial that is the sum of the two polynomials, e.g., `Polynom([5,0,0,2,3]) + Polynom([1,0,6,0,0])` yields `Polynom([6,0,6,2,3])`. Similarly for subtraction `__sub__` and multiplication `__mul__`.

* The method `__eq__` should check two polynomials for equality, e.g., `Polynom([5,0,0,2,3]) == Polynom([5,0,0,2,3])` should return `True`.

* The method `__str__` should return the polynomial as a string, e.g., `Polynom([5,0,0,2,3])` should output `5x^4 + 2x + 3`.

* The method `__call__` should evaluate the polynomial for a given value of `x`, e.g., `Polynom([5,0,0,2,3])(2)` should return `87`.

* The method `__len__` should return the degree of the polynomial, e.g., `len(Polynom([5,0,0,2,3]))` should return `4`.

* Additionally, the class should have a method `derivative` that differentiates the polynomial and returns the differentiated polynomial.

* Finally, the class should have a method `integrate` that integrates the polynomial and returns the integrated polynomial. The constant of integration should be $0$.

## Task
1. Write tests for the class `Polynom` in `test_polynom.py` to ensure that the implementation of the methods is correct.

2. Use `assert` statements from pytest for this. To be able to test the methods, you should also have implemented the `__eq__` method so that you can compare the polynomials!

3. For each function-overloading operator, at least one test should be written, and also for the methods `derivative` and `integrate`.


## Hint
 * The test in this exercise only checks the class.
