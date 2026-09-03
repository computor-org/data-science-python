import cProfile
import random


### Example (pytest)
def func(x):
    return x + 1


### Examples (profiling)
def slowfunc():
    import time, random

    for _ in range(10):
        time.sleep(random.random() / 100)


def fib(n):
    ### Returns the n-th Fibonacci number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


#### End of Examples


def bubblesort(arr, /, *, key=None, reverse=False):
    ### Sorts the array using bubble sort (Wiki: https://en.wikipedia.org/wiki/Bubble_sort)
    # TODO: Implement bubble sort **after** writing tests for this function!!!
    return arr


def profile_bubblesort():
    # TODO: Profile the bubblesort function using a long unsorted array (5000 or more entries), you can use randint to generate random samples
    import random


def benchmark_bubblesort():
    # TODO: Benchmark the bubblesort function using a long unsorted array (10000 or more entries), you can use randint to generate random samples
    import time, random, matplotlib.pyplot as plt


def timecomplexity():
    # TODO: Plot the time complexity of the bubblesort function using random arrays of different sizes (powers of 2 up to around 10000)
    import time, random, matplotlib.pyplot as plt


if __name__ == "__main__":
    # profiling a function
    cProfile.run("slowfunc()")
    cProfile.run("fib(30)")
    profile_bubblesort()
    benchmark_bubblesort()
    timecomplexity()
    ##################
