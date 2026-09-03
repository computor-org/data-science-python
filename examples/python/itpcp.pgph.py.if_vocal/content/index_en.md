[lists]: <https://python-reference.readthedocs.io/en/latest/docs/list/> "lists"

# Vowel or Consonant

## Introduction

Write a Python function `if_vocal` that outputs the following:

```python
result = if_vocal(character)
```

| **InOut** | **Name** | **Description** | **Type** |
|-|-|-|-|
| Input | `character` | Any letter (uppercase or lowercase) | `str` |
| Output | `result` | String *Vowel* or *Consonant* | `str` |

## Task

1. This function returns the string `'Consonant'` or `'Vowel'` as output value.

2. The input value `character` can be either an uppercase or a lowercase letter.

3. Think about which decision structure is most suitable here.

4. Vowels are: `a,ä,e,i,o,ö,u,ü`

## Hint

### Lists


A simple method to check whether an element (e.g., a number or a string) is present in a list is the following:

```python
found_4 = 4 in [1, 2, 3, 4, 5]    # This will be True
```

We can also search for strings:

```python
def isInList(test_var, my_list):
    if test_var in my_list:
        print('Variable found!')
        return True
    else:
        print('Not found!')
        return False


isInList('ab', ['Was geht ab', 4, 'Name'])
>>> Not found!

isInList('ab', ['Was geht ab', 'ab', 4, 'Name'])
>>> Variable found!
```

* Note that in the first case the substring `'ab'` was not found!

* Use this method in this example to avoid confusing `if` queries!
