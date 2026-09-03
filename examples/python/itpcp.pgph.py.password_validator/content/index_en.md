# Password Validator

## Introduction

In the following task, you should program a simple script that checks the strength of an entered password.
The strength is determined according to the following criteria:

- The password must be at least 8 characters long.
- It must contain at least one number, one special character, and one uppercase letter.
- It must not contain consecutive or repeating numbers or letters (`abcd`, `1234`, `55555`) (from 4 characters onwards). So (`abc`, `123`, `555`) are allowed, but not (`abcd`, `1234`, `55555`). Furthermore, `ABCdEFG` is allowed since the uppercase letters are not consecutive (because they are interrupted by a lowercase letter). However, `ABCDEF` would not be allowed since the letters are consecutive.

## Task

Write the function `check_password(pw)` in the script `check_password.py`, which reads a `string` as a possible password and checks the above criteria.
This function should not return anything! Proceed as follows:

1. Check the criteria with `if` and/or `elif`/`else` statements.
1. To check whether the password contains special characters, numbers, and uppercase letters, you can import the [string] module and work with the formats defined there (e.g., with `string.digits`).
1. You can then iterate over the digits/uppercase letters/special characters and check whether at least one of them is present in the proposed password. If the criteria are not met, the following strings should be output in the console:
   - Less than 8 characters: *"Password too short!"*
   - No number: *"Password contains no number!"*
   - No special character: *"Password contains no special character!"*
   - No uppercase letters: *"Password contains no uppercase letter!"*
   - Consecutive or repeating numbers/letters: *"Password contains more than 3 consecutive or repeated characters!"*
1. The logical check whether *none* of the defined characters is present can be elegantly solved with the keywords [all] and `not`.
1. If all criteria are met, *"Strong password"* should be output in the console.

## Hints

- If you work with the [string] module and want to convert the digits '0123456789' into a list of individual digits, you can do this with the `*` operator:

```python
s = "0123"
print ([*s])
>>> ["0", "1", "2", "3"]
```

The `*` operator then *unpacks* the individual digits and you can iterate over the entries.

- With ord() you can find out the ASCII value of a character. For example, the ASCII value of 'A' = 65, 'B' = 66, ..., 'Z' = 90.
  You can therefore check consecutive letters by comparing the ASCII value of the letters.

- Test the strength of the following passwords:

| Password  | Result |
| ---    | ----------   |
| asd   | Password too short!  |
| passwortneu   | Password contains no number!   |
| passwortneu25   | Password contains no special character!   |
| passwortneu25!   | Password contains no uppercase letter!    |
| Passwortneu25!  | Strong password  |
| Passsswortneu25!   | Password contains more than 3 consecutive or repeated characters!   |
| Passwortneu2222! | Password contains more than 3 consecutive or repeated characters! |
| abcd_Passwortneu25! | Password contains more than 3 consecutive or repeated characters! |

[all]: https://docs.python.org/3/library/functions.html#all "all"
[string]: https://docs.python.org/3/library/string.html "string"
