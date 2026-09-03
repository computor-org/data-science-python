[Wikipedia]: <https://en.wikipedia.org/wiki/Roman_numerals> "Wikipedia"

# Roman Numerals

## Introduction

The following task is intended as a small *warm-up* exercise for working with `python dictionaries`. Using a function, numbers in Roman notation are to be converted to Arabic numbers.

### Roman Numbers

The following notation applies to Roman numbers:

|Roman|Arabic|
|:--|:--|
``I`` | 1
``V`` | 5
``X`` | 10
``L`` |  50
``C`` | 100
``D`` | 500
``M`` | 1000

Roman notation is basically descending from the highest to the lowest digit. *Exception:* If a lower digit precedes a higher digit, it is subtracted from the higher digit:

```python
IV = 4
IX = 9
```

The Roman digits and corresponding Arabic numbers from the table above are to be stored as `key-value pairs` in a `dictionary`.

## Task

1. Write a function in `int_roman.py` that takes Roman numerals as input in the form of `strings` and converts them to Arabic numbers, such as

```python
arabic = int_roman("XV")  # yields 15
```

2. Furthermore, the function should have a docstring that describes the functionality of the function, which should follow the [numpy-docstring](https://numpydoc.readthedocs.io/en/latest/format.html) conventions.

3. The function should also raise a `ValueError` if the input does not contain Roman numerals or does not have the data type `str`.

## Hints

* An introduction to Roman numerals can be found on [Wikipedia].
Here, the simple rules as described in the article under `Subtractive principle` should be used.
