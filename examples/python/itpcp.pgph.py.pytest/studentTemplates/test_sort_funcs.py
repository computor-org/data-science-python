# examples:
from sort_funcs import func, bubblesort


def test_example():  # this is one test case in pytest
    assert func(3) == 4
    assert func(4) == 5
    assert func(7) != 100


def test_basic():
    assert bubblesort([]) == []
    assert bubblesort([1, 2, 3]) == [1, 2, 3]


def test_sort():
    assert bubblesort([3, 2, 1]) == [1, 2, 3]
    assert bubblesort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]


def test_sort_rand():
    for _ in range(10):
        import random

        arr = [random.randint(0, 100) for _ in range(100)]
        assert bubblesort(arr) == sorted(arr)
