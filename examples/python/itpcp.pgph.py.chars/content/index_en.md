[python strings]: https://docs.python.org/3/library/stdtypes.html#textseq "python strings"


# Strings

## Introduction

In this example, you will get an introduction to working with strings in Python. Advanced manipulations will be revisited in a later week.

### Strings

Chains of characters are stored as so-called `strings` and are fundamental data types in all common higher-level programming languages. A `string` generally consists
of a sequence of characters that are converted into binary language through a defined character encoding (usually UTF-8).
This allows text files to be imported, displayed, and manipulated.

A `string` can be created with either double (`"`) or single (`'`) quotation marks. Variable assignment is done
as with all other data types, for example

```python
a = 'Hello World'
print(a)

Hello World
```

In Python, `string` is a so-called `immutable` data type. This means that a
`string` once assigned to a variable can no longer be changed and you may need to create a new variable.

Manipulation of `strings` is done intuitively with the usual mathematical operations, for example

```python
s1 = 'bra'
s2 = 'ket'
print(s1 + 'c' + s2)

bracket
```
Since `strings` represent a sequence of character strings, you can access individual characters through indexing. Note
that in Python, indices always start at `0`. More information on working with strings and indexing can be found in the hints.

## Task

1. Assign the following values to the variables in the script `strings.py`:

    |Variable|Value|
    |:-|:-|
    |`s_1`| `graz`|
    |`s_2`| `is`|
    |`s_3`| `a`|
    |`s_4`| `great`|
    |`s_5`| `city!`|

2. Convert the variables `s_1` and `s_5` to `S_1` and `S_5` where the first letter should now be an uppercase letter.

3. Now compose the variable `s` from the variables `S_1`, `s_2`, `s_3`, `s_4`, `S_5` and insert spaces between the words.

4. Then convert the entire sentence to uppercase and save it in the variable `S`.

## Hints

* More information on how to convert uppercase letters to lowercase and vice versa can be found at [python strings].

* For indexing, we use the square brackets `[]` and the index of the character we want to access. For example, if we have a string `s = "Hello"`, we can access the first character with `s[0]`, which will return `'H'`. To get the rest of the string, we can use slicing, e.g., `s[1:]` will return `'ello'`.

* There are several solution approaches and functions for this task that lead to the correct result. Feel free to try different ones!


## Keywords

- Strings