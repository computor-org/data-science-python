[numpy.arange]: <https://numpy.org/doc/stable/reference/generated/numpy.arange.html> "numpy.arange"
[numpy.linspace]: <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html> "numpy.linspace"
[numpy.random]: <https://numpy.org/doc/stable/reference/random/index.html> "numpy.random"
[numpy.floor]: <https://numpy.org/doc/stable/reference/generated/numpy.floor.html> "numpy.floor"
[numpy.cumsum]: <https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html> "numpy.cumsum"

# Creating Vectors

## Introduction

In this task, various vectors should be created.

Think about what you have learned in the previous examples.
When using functions, read their documentation carefully. Pay special attention when generating random numbers to which intervals the functions are defined on.

In the submission version of the example, no output should be made in the console.

## Task

1. Create in the Python script `vector_create` (File: `vector_create.py`) the following vectors:

| Variable    | Value                                                                                                                |
|-------------|:--------------------------------------------------------------------------------------------------------------------|
| `zeros`     | Zeros - 8 elements                                                                                                 |
| `ones`      | Ones - 7 elements                                                                                                 |
| `fives`     | Fives - 6 elements                                                                                                 |
| `vec1`      | 0 to 5 with step size 1                                                                                               |
| `vec2`      | 0 to 5 with step size 0.5                                                                                             |
| `vec3`      | 5 to 0 with (absolute) step size 1                                                                                   |
| `lin1`      | 90 points in the closed interval $[0,5]$ (linear spacing)                                                     |
| `log1`      | 9 points in the closed interval $[10^{-2},10^{2}]$ (logarithmic spacing, base $10$)                        |
| `log2`      | Base-10 logarithm ($\log_{10}$) of `log1`                                                                          |
| `log3`      | 6 points in the closed interval $[\mathrm{e}^{-2},\mathrm{e}^{3}]$ (logarithmic spacing, base $\mathrm{e}$) | |
| `calc1`     | The numbers $[1, 2, 4, 8, \dotsc, 1024]$ calculated with a vector operation                                         |
| `calc2`     | The numbers  $[1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dotsc, \frac{1}{32}]$ calculated with a vector operation  |
| `calc3`     | The numbers  $[1,3,6,10,15,21]$ with one operation                                                                  |

2. For the vectors `calc1` to `calc3`, think about what "function rule" the vectors follow, and try to express this mathematically.

## Hints

- Try to find the corresponding commands using the NumPy or SciPy documentation. Helpful functions can be found under [numpy.arange], [numpy.linspace] and [numpy.cumsum].
