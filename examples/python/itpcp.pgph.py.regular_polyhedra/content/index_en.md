[lower]: <https://python-reference.readthedocs.io/en/latest/docs/str/lower.html> "lower"
[raise]: <https://docs.python.org/3/tutorial/errors.html#raising-exceptions> "raise"

# Regular Polyhedra

## Introduction

This exercise deals with polyhedra. Quantities such as
volume and surface area are to be calculated. The necessary mathematical
relationships are given below.

### Mathematical Background

#### Tetrahedron

$$
\begin{aligned}
&V = \frac{a^3}{12} \sqrt{2}  \\
&F = a^2 \sqrt{3} \\
&R = \frac{a}{4} \sqrt{6}  \\
&r = \frac{a}{12} \sqrt{6}  \\
\end{aligned}
$$

#### Cube

$$
\begin{aligned}
  &V = a^3  \\
  &F = 6a^2  \\
  &R = \frac{a}{2} \sqrt{3}  \\
  &r = \frac{a}{2}
\end{aligned}
$$

#### Octahedron

$$
\begin{aligned}
  &V = \frac{a^3}{3} \sqrt{2}  \\
  &F = 2a^2 \sqrt{3} \\
  &R = \frac{a}{2} \sqrt{2}  \\
  &r = \frac{a}{6} \sqrt{6}
\end{aligned}
$$

#### Dodecahedron

$$
\begin{aligned}
  &V = \frac{a^3}{4} \left(15 + 7\sqrt{5}\right)  \\
  &F = 3a^2 \sqrt{5\left(5 + 2\sqrt{5}\right) } \\
  &R = \frac{a}{4} \left( 1 + \sqrt{5} \right) \sqrt{3}  \\
  &r = \frac{a}{4} \sqrt{ \frac{50 + 22\sqrt{5}}{5} }
\end{aligned}
$$

#### Icosahedron

$$
\begin{aligned}
  &V = \frac{5a^3}{12} \left(3 + \sqrt{5}\right)  \\
  &F = 5a^2 \sqrt{3} \\
  &R = \frac{a}{4} \sqrt{ 2 \left( 5 + \sqrt{5} \right) }  \\
  &r = \frac{a}{2} \sqrt{ \frac{7 + 3\sqrt{5}}{6} }
\end{aligned}
$$

## Tasks

### Part 1

Define a function in `regular_polyhedra.py` that is called with

```
V, F, R, r = regpol(type, a)
```

The inputs/outputs are to be used as follows:

```
type : String, type of polyhedron ('t', 'c', 'o', 'd', 'i', 'Tetrahedron', 'Cube', etc.)
a   : Vector, edge length of the polyhedron
V   : Vector, volume of the polyhedron
F   : Vector, surface area of the polyhedron
R   : Vector, radius of the circumscribed sphere
r   : Vector, radius of the inscribed sphere
```

The function should accomplish the following tasks:

1. For a given edge length `a`, the volume `V`, the surface area `F`,
   the radius of the circumscribed sphere `R`, and the radius of the inscribed sphere
   `r` should be calculated for one of the 5 regular convex polyhedra
   (tetrahedron, cube, octahedron, dodecahedron, icosahedron).

2. The type of regular polyhedron should be passed with the string variable `type`.
   Use the letters `'t', 'c', 'o', 'd'` or `'i'` to
   select one of the polyhedra. Make sure that the correct
   polyhedron is selected for all possible input strings, not
   just for single characters!

3. The function should work for a vector of `a` values and return equally
   long vectors with the results for `V`, `F`, `R`, and `r`.

4. Use the control structures you have already learned to distinguish cases!

    Consider what string can be passed as `type`, what `type[1]`
    means, and what the command [lower] does.
    You should try the commands in the console as always.


### Part 2

Write a Python script `regular_polyhedra_script.py` that calculates some variables with multiple calls to the
function `regpol` you implemented. Proceed as follows:

1. Define a variable `edge` that has the entries `[1,2,3]`.

2. Calculate the *quantities* required in the following table for the
    corresponding *polyhedron* and save them in the specified *variable*.
    The function `regpol` should only be called **once** for each polyhedron,
    and quantities that are **not** asked for in the table should also
    **not** be calculated! (see hints if needed)

| Polyhedron | Quantity | Variable |
| ----| :----: | ----: |
| Icosahedron | Volume | `Volume_i` |
| Tetrahedron | Volume | `Volume_t` |
| Tetrahedron | Surface Area | `Area_t` |
| Cube | Volume | `Volume_c` |
| Cube | Surface Area | `Area_c` |
| Cube | Radius (outer) | `Radius_c` |
| Dodecahedron | Surface Area | `Area_d` |
| Dodecahedron | Radius (outer) | `Radius_d` |
| Dodecahedron | Radius (inner) | `radius_d` |
| Octahedron | Radius (outer) | `Radius_o` |
| Octahedron | Radius (inner) | `radius_o` |

## Hints

* First program only one case (e.g., cube) and try it
 with a scalar and a vector as input. Only then do
 the other cases. This saves you possibly
 duplicating errors and tedious fixing.

* Check the correct functioning of your function using the following inputs:
    The call

    ```python
    V, F, R, r = regpol('c', 3)
    ```

    should yield the output

    ```python
    27                 # V
    54                 # F
    2.598076211353316  # R
    1.5                # r
    ```

    Likewise

    ```python
    V, F, R, r = regpol('c', np.array([1,2,3,10]))
    ```

    should yield

    ```python
    array([   1,    8,   27, 1000])                          # V
    array([  6,  24,  54, 600])                              # F
    array([0.8660254 , 1.73205081, 2.59807621, 8.66025404])  # R
    array([0.5, 1. , 1.5, 5. ])                              # r
    ```

    By the way, you can also run functions for testing without storing the output values in variables. These are then simply output in the console.

* You can mark the position of unneeded output variables with the
    character `_` (underscore), i.e., you can write

    ```python
    _, _, Rad, rad = regpol('Tetra', 1.0)
    ```

    and get only the two radii as a result; the volume and area, on the other hand, are not available.

* The function `regpol` must be called exactly once for each polyhedron.
