[join]: <https://docs.python.org/3/library/stdtypes.html#str.join> "join"
[len]: <https://docs.python.org/3/library/functions.html#len> "len"
[list]: <https://docs.python.org/3/library/stdtypes.html#typesseq> "list"
[split]: <https://docs.python.org/3/library/stdtypes.html#str.split> "split"
[str]: <https://docs.python.org/3/library/stdtypes.html#textseq> "str"
[string]: <https://docs.python.org/3/library/string.html> "string"
[type]: <https://docs.python.org/3/library/functions.html#type> "type"
[upper]: <https://docs.python.org/3/library/stdtypes.html#str.upper> "upper"

# Characters and Strings

## Introduction

In addition to numbers, every programming language naturally also has a data type for
characters. In Python, this is the data type [str] (short for _String_).
Characters are defined using the single quote (`'`) at the beginning and at the end.
So if the variable `s` should have the content `a`, you must write `s = 'a'`.
If you were to write `s = a` instead, then the variable `s` would have the value of variable `a`,
so for example

	a = 7
	s = a

results in the value `7` for both `a` and `s`.

Strings can be thought of as vectors (arrays) of characters. Such a string is e.g.
`s = 'abc'` or `s = '123'`. In the second case, these are the characters `123` and not the
number $123$. So it makes an important difference whether you write `s = '123'` or `s = 123`.
Individual characters or strings can be connected to longer strings using the `+` operator.
Strings can in turn be stored in lists,
which can be indexed similarly to arrays. In contrast to NumPy arrays,
lists in Python can contain elements with any data types, so
in particular strings of different lengths.

|Code|Result|
|---|---|
|`s = 'a' + 'b' +'c'`|`'abc'`|
|`s2 = s + s`|`'abcabc'`|
|`l = [s, s2]`|`['abc', 'abcabc']`|
|`l[0]`|`'abc'`|

The correct but cumbersome notation `s = 'a' + 'b' + 'c'` is sensibly replaced
by `s = 'abc'` with the same result.

Individual characters in a string can be accessed using an index, `s2[3]`
and `l[1][3]` yield the character `a`, i.e., the fourth letter of the above string.

If you want to access multiple characters, you can use the colon notation documented for [list],
`s2[3:6]` then yields `abc`. The last element can also be omitted,
e.g. `s2[3:]`. Unlike "real" arrays (and lists), strings in
Python cannot be decomposed into scalars (here individual characters): In fact,
`s2[3]` returns a string of length 1; this notation therefore corresponds to `s2[3:4]`.

Another difference is that strings in Python are immutable. So you
cannot modify an existing string retroactively using index notation.

## Task

### Basic Handling of Strings

Perform some simple variable definitions in the Python script `basis_char`:

1. Assign the following values to the variables:

    |Variable|Value|
    |---|---|
    |`s1`|`a`
    |`s2`|`b`
    |`c1`|`das`
    |`c2`|`ist`
    |`c3`|`eine`
    |`c4`|`wunderbare`
    |`c5`|`uebung`
    |`blank`|*a space character*
    |`exclaim`|*an exclamation mark*

    <span style="color: red;">Attention:</span> The last two variable values are to be understood such that the variable `exclaim` should only contain the character *!*. So if you type `exclaim` in the
    console, the output should be `'!'`.

2. Now create the variable `s3` by concatenating the variables `s1` and `s2`.

3. Create the variables `C1` and `C5` from the variables `c1` and `c5`, where now the
    first letter should be an uppercase letter ([upper]). Actually use
    the variable `c1` here and do not write `C1='Das'`. So `C1` is
    "assembled" from `c1`. Individual characters in a string can be accessed with an
    index (e.g.: `C1[0]` is the first character in `C1`).

4. Now compose the variable `sentence` from `C1`, `c2`, `c3`, `c4`, and `C5`, where
    there should be a space between words and an exclamation mark at the end of the sentence.
    (Use the defined variables for this.)

5. Determine the data type of variables using the command [type]:

    |Variable|Value|
    |---|---|
    |`type_sentence`|Data type of the variable `sentence`|
    |`type_number`|Data type of the number `12`|

    If you want to use the data type as a string, you need to access these variables
    e.g. with `type_number.__name__`.

6. Determine the number of characters in `sentence` using [len] and store
    this information in the variable `length_sentence`.

7. Create the following variables:

    |Variable|Value|
    |---|---|
    |`all_upper`|All uppercase letters from `A` to `Z` in a string|
    |`all_lower`|All lowercase letters from `a` to `z` in a string|
    |`all_both` |The above strings as two elements of a list|

    You can use the constants in the [string] module for this.

### Handling Strings Using Lists

Here is a small example on splitting and
joining strings using the commands
[split], [join], [list]. Note that `split` and `join` as **methods**
follow the strings, i.e., `s.join()` instead of `join(s)`.

1. Store the string in the variable `str1`:

    'abcdef'

2. Split the string `str1` into individual characters using [list] and
   store the result in `list1`:

    ['a', 'b', 'c', 'd', 'e', 'f']

3.  Create from `list1` using [join] the following string in the
    variable `str2`:

    'a- -b- -c- -d- -e- -f'

4. Split `str2` at the space using [split] and store the result
   in `list2`.

    ['a-', '-b-', '-c-', '-d-', '-e-', '-f']

The variables `list1` and `list2` are lists. These can be indexed similarly to NumPy arrays,
but can contain any Python constructs in each position, so
not just a number or a letter, but entire arrays or entire
strings.

Can subtask 2 also be solved with [split]? Try out what you get with
`str1.split()` and `str1.split('')`.

## Hints

* If you want to extract multiple consecutive characters from a string, for example
    the first three entries of a string `s`, this is principally possible with

    s[0] + s[1] + s[2]

    However, the more elegant variant would be the colon notation,

    s[0:3]

    or

    s[:3]

* Since the order of the respective strings matters when concatenating strings,
the `+` operator for strings is not commutative as usual.

* You can also create strings like `'ABC...Z'` using `range`, `ord`, `chr`.
However, this requires more complicated constructs like `for` loops or the `map` function.
