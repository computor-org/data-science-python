<!-- Pytest link -->
[pytest]: https://docs.pytest.org/en/latest/

# Pytest & cProfile

## Introduction

In this task, Pytest and cProfile are introduced.

- [Pytest][pytest] is a testing framework that makes it easy to write your own tests.

**Installation**: `pip install pytest`.

- [cProfile](https://docs.python.org/3/library/profile.html) is a built-in Python module used for so-called 'profiling' of code. Profiling means analyzing the runtime and performance of a program to identify bottlenecks and optimize the code.


There are three files in the exercise folder:
- `test_sort_funcs.py`: Contains the tests.
- `sort_funcs.py`: Contains the functions to be tested.
- `run.py`: Runs Pytest on the test file.


## Task

### 1. Pytest

First, look at the file `test_sort_funcs.py`.
This already contains tests for the function `func` as an example. In test-driven development (**test driven development**), you first write the tests and then the code to pass the tests. We want to use this approach in the current exercise:
1. Write the tests for the function `bubble_sort` in the file `test_sort_funcs.py`.
Use the ```assert``` statement to check whether the function works correctly.
```python
assert 2 + 2 == 4 # This will pass
assert 2 + 2 == 5 # This will fail
```
2. Make sure to name the test function `test_<whatever Name you want here>` so that Pytest recognizes it as a test function.
Write at least **3** tests for the `bubble_sort` function -> this means you need to write **3 test functions** in `test_sort_funcs.py`.

### 2. Implement Bubble Sort

2. Implement the function `bubble_sort` in the file `sort_funcs.py` (you can of course look at the algorithm's Wikipedia page if you're not familiar with it).

Make sure to implement the function with the given signature:

```python
bubblesort(arr, /, *, key=None, reverse=False):
   #CODE
   return arr
```
This way the function has the same signature as the built-in [sorted()](https://docs.python.org/3/library/functions.html#sorted) function in Python.
`/` and `*` are used to indicate that the arguments before `/` are positional-only, and the arguments after `*` are keyword-only arguments. This is a new feature in Python 3.8. You can either implement this sorting algorithm in-place or with a copy, as long as the returned `arr` is sorted.

3. Run the tests using the `run.py` file. Alternatively, you can simply run `pytest` in the terminal **in the exercise folder** using the command `pytest`.

4. **Make sure all tests pass**. If not, fix the `bubble_sort` function until they all pass. Also make sure to include at least one test with `reverse=True` and `key` as a keyword argument (e.g., sort a list of strings by the length of the strings).

### 3. cProfile

Now use the `cProfile` module to profile the `bubble_sort` function. How long does it take to sort a list with 5000 or more random integers?

### 4. Benchmarking bubble_sort with built-in sort

Create a large array (> 10000 elements) and sort it with the `bubble_sort` function and the built-in `sort` function. Use the [time.perf_counter()](https://docs.python.org/3/library/time.html#time.perf_counter) function to measure the time needed to sort the array with each function. Compare the results.

Now compare the time complexity of the bubble_sort function with the built-in sort function. Run the bubble_sort function and the built-in sort function with arrays of different sizes (e.g., 2,4,8,16,32,...,8192, 16384) and measure the time needed to sort the array with each function. Plot the results in a graph. What can you observe? Which algorithm is faster? More information about time complexity can be found [here](https://en.wikipedia.org/wiki/Time_complexity).

## Bonus

Write a faster sorting algorithm (e.g., Quicksort) and compare it with the bubble_sort function and the built-in sort function.

## Hints

* If you simply run `pytest` in the terminal, all files with the prefix `test_` (in the current directory and subdirectories) will be tested. If you want to test a specific file, you can use the command `pytest <filename>`.

* The test only checks the `bubble_sort` function.
