[lower]: <https://python-reference.readthedocs.io/en/latest/docs/str/lower.html> "lower"
[raise]: <https://docs.python.org/3/tutorial/errors.html#raising-exceptions> "raise"

# Reguläre Polyeder

## Einleitung

Die vorliegende Übung beschäftigt sich mit Polyedern. Es sollen Größen wie
Volumen und Oberfläche berechnet werden. Die dafür nötigen mathematischen
Zusammenhänge sind nachfolgend angegeben.

### Mathematische Grundlagen

#### Tetraeder (Tetrahedron)

$$
\begin{aligned}
&V = \frac{a^3}{12} \sqrt{2}  \\
&F = a^2 \sqrt{3} \\
&R = \frac{a}{4} \sqrt{6}  \\
&r = \frac{a}{12} \sqrt{6}  \\
\end{aligned}
$$

#### Würfel (Cube)

$$
\begin{aligned}
  &V = a^3  \\
  &F = 6a^2  \\
  &R = \frac{a}{2} \sqrt{3}  \\
  &r = \frac{a}{2}
\end{aligned}
$$

#### Oktaeder (Octahedron)

$$
\begin{aligned}
  &V = \frac{a^3}{3} \sqrt{2}  \\
  &F = 2a^2 \sqrt{3} \\
  &R = \frac{a}{2} \sqrt{2}  \\
  &r = \frac{a}{6} \sqrt{6}
\end{aligned}
$$

#### Dodekaeder (Dodecahedron)

$$
\begin{aligned}
  &V = \frac{a^3}{4} \left(15 + 7\sqrt{5}\right)  \\
  &F = 3a^2 \sqrt{5\left(5 + 2\sqrt{5}\right) } \\
  &R = \frac{a}{4} \left( 1 + \sqrt{5} \right) \sqrt{3}  \\
  &r = \frac{a}{4} \sqrt{ \frac{50 + 22\sqrt{5}}{5} }
\end{aligned}
$$

#### Ikosaeder (Icosahedron)

$$
\begin{aligned}
  &V = \frac{5a^3}{12} \left(3 + \sqrt{5}\right)  \\
  &F = 5a^2 \sqrt{3} \\
  &R = \frac{a}{4} \sqrt{ 2 \left( 5 + \sqrt{5} \right) }  \\
  &r = \frac{a}{2} \sqrt{ \frac{7 + 3\sqrt{5}}{6} }
\end{aligned}
$$

## Aufgaben

### Teil 1

Definieren Sie eine Funktion in `regular_polyhedra.py`, die mit

```
V, F, R, r = regpol(type, a)
```

aufgerufen wird. Dabei sind die In-/Outputs wie folgt zu verwenden:

```
type : String, Typ des Polyeders ('t', 'c', 'o', 'd', 'i', 'Tetrahedron', 'Cube', usw.)
a   : Vektor, Kantenlänge des Polyeders
V   : Vektor, Volumen des Polyeders
F   : Vektor, Oberfläche des Polyeders
R   : Vektor, Radius der umschreibenden Kugel
r   : Vektor, Radius der einbeschriebenen Kugel
```

In der Funktion sollen folgende Aufgaben erledigt werden:

1. Für eine vorgegebene Kantenlänge `a` soll das Volumen `V`, die Oberfläche `F`,
   der Radius der umschreibenden Kugel `R` und der Radius der eingeschriebenen Kugel
   `r` wahlweise für einen der 5 regulären konvexen Polyeder
   (Tetraeder, Würfel, Oktaeder, Dodekaeder, Ikosaeder) berechnet werden.

2. Mit der String-Variable `type` soll der Typ des regulären Polyeders übergeben
   werden. Verwenden Sie die Buchstaben `'t', 'c', 'o', 'd'` bzw. `'i'` um
   einen der Polyeder auszuwählen. Stellen Sie sicher, dass der richtige
   Polyeder ausgewählt wird für alle möglichen Eingabezeichenketten nicht
   nur für einzelne Zeichen!

3. Die Funktion soll für einen Vektor von `a`-Werten funktionieren und gleich
   lange Vektoren mit den Resultaten für `V`, `F`, `R` und `r` zurückgeben.

4. Zur Unterscheidung der Fälle verwenden Sie die Steuerstrukturen, die Sie bereits kennengelernt haben!

    Überlegen Sie, welche Zeichenkette man als `type` übergeben kann, was `type[1]`
    bedeutet, und was der Befehl [lower] dabei bewirkt.
    Sie sollten die Befehle wie immer in der Konsole ausprobieren.


### Teil 2

Schreiben Sie ein Python Skript `regular_polyhedra_script.py`, das mit mehreren Aufrufen der von
Ihnen implementierten Funktion `regpol` nun einige Variablen berechnet. Gehen Sie wie

    ```
    array([  6,  24,  54, 600])                              # F
    array([0.8660254 , 1.73205081, 2.59807621, 8.66025404])  # R
    array([0.5, 1. , 1.5, 5. ])                              # r
    ```

führen.

Sie können Funktionen zum Testen übrigens auch ausführen, ohne die Ausgabewerte in Variablen zu speichern. Diese werden dann einfach in der Konsole ausgegeben.

* Für jeden Polyeder muss man die Funktion `regpol` genau einmal aufrufen.folgt vor:

1. Definieren Sie eine Variable `edge`, die die Einträge `[1,2,3]` hat.

2. Berechnen Sie die in der nachfolgenden Tabelle geforderten *Größen* für den
    entsprechenden *Polyeder* und speichern Sie diese in die angegebene *Variable*.
    Dabei soll die Funktion `regpol` für jeden Polyeder nur **einmal** aufgerufen
    werden und Größen, die **nicht** in der Tabelle gefragt sind, sollen auch
    **nicht** berechnet werden! (siehe evtl. Hinweise)

| Polyeder | Groesse | Variable |
| ----| :----: | ----: |
| Icosahedron | Volumen | `Volume_i` |
| Tetrahedron | Volumen | `Volume_t` |
| Tetrahedron | Oberfläche | `Area_t` |
| Cube | Volumen | `Volume_c` |
| Cube | Oberfläche | `Area_c` |
| Cube | Radius (außen) | `Radius_c` |
| Dodecahedron | Oberfläche | `Area_d` |
| Dodecahedron | Radius (außen) | `Radius_d` |
| Dodecahedron | Radius (innen) | `radius_d` |
| Octahedron | Radius (außen) | `Radius_o` |
| Octahedron | Radius (innen) | `radius_o` |

## Hinweise

* Programmieren Sie zuerst nur einen Fall (z.B.: Würfel) und probieren Sie
 diesen mit einem Skalar und einem Vektor als Input aus. Erledigen Sie
 erst dann die anderen Fälle. Damit ersparen Sie sich u.U. das
 Duplizieren von Fehlern und das mühsame Ausbessern.

* Überprüfen Sie anhand der folgenden Inputs die richtige Funktionsweise ihrer
    Funktion: Der Aufruf

    ```python
    V, F, R, r = regpol('c', 3)
    ```

    sollte den Output

    ```python
    27                 # V
    54                 # F
    2.598076211353316  # R
    1.5                # r
    ```

    liefern. Ebenso sollte

    ```python
    V, F, R, r = regpol('c', np.array([1,2,3,10]))
    ```

    zum Ergebnis

    ```python
    array([   1,    8,   27, 1000])                          # V
    array([  6,  24,  54, 600])                              # F
    array([0.8660254 , 1.73205081, 2.59807621, 8.66025404])  # R
    array([0.5, 1. , 1.5, 5. ])                              # r
    ```

    führen.

    Sie können Funktionen zum Testen übrigens auch ausführen, ohne die Ausgabewerte in Variablen zu speichern. Diese werden dann einfach in der Konsole ausgegeben.

* Man kann die Position nicht benötigter Outputvariablen mit dem
    Zeichen `_` (Underscore) markieren, d.h. man kann schreiben

    ```python
    _, _, Rad, rad = regpol('Tetra', 1.0)
    ```

    und bekommt als Ergebnis nur die beiden Radien, das Volumen und die Fläche hingegen stehen nicht zur Verfügung.

* Für jeden Polyeder muss man die Funktion `regpol` genau einmal aufrufen.
