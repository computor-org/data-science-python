[numpy.arange]: <https://numpy.org/doc/stable/reference/generated/numpy.arange.html> "numpy.arange"
[numpy.linspace]: <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html> "numpy.linspace"
[numpy.random]: <https://numpy.org/doc/stable/reference/random/index.html> "numpy.random"
[numpy.floor]: <https://numpy.org/doc/stable/reference/generated/numpy.floor.html> "numpy.floor"
[numpy.cumsum]: <https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html> "numpy.cumsum"

# Erzeugung von Vektoren

## Einleitung

In dieser Aufgabe sollen verschiedene Vektoren erzeugt werden.

Denken Sie in diesem Beispiel darüber nach, was Sie in den vorherigen Beispielen gelernt haben.
Lesen Sie sich bei der Verwendung von Funktionen deren Dokumentation genau durch. Achten Sie insbesondere bei der Erzeugung von Zufallszahlen darauf, auf welche Intervalle die Funktionen definiert sind.

Bei der Abgabeversion des Beispiels soll in der Konsole keine Ausgabe gemacht werden. 

## Aufgabe

1. Erzeugen Sie im Python-Skript `vector_create` (File: `vector_create.py`) folgende Vektoren:

| Variable    | Wert                                                                                                                |
|-------------|:--------------------------------------------------------------------------------------------------------------------|
| `zeros`     | Nullen - 8 Elemente                                                                                                 |
| `ones`      | Einsen - 7 Elemente                                                                                                 |
| `fives`     | Fünfer - 6 Elemente                                                                                                 |
| `vec1`      | 0 bis 5 mit Abstand 1                                                                                               |
| `vec2`      | 0 bis 5 mit Abstand 0.5                                                                                             |
| `vec3`      | 5 bis 0 mit (absolutem) Abstand 1                                                                                   |
| `lin1`      | 90 Punkte im geschlossenen Intervall $[0,5]$ (linearer Abstand)                                                     |
| `log1`      | 9 Punkte im geschlossenen Intervall $[10^{-2},10^{2}]$ (logarithmischer Abstand, Basis $10$)                        |
| `log2`      | Zehner-Logarithmus ($\log_{10}$) von `log1`                                                                          |
| `log3`      | 6 Punkte im geschlossenen Interval $[\mathrm{e}^{-2},\mathrm{e}^{3}]$ (logarithmischer Abstand, Basis $\mathrm{e}$) | |
| `calc1`     | Die Zahlen $[1, 2, 4, 8, \dotsc, 1024]$ berechnet mit einer Vektoroperation                                         |
| `calc2`     | Die Zahlen  $[1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dotsc, \frac{1}{32}]$ berechnet mit einer Vektoroperation  |
| `calc3`     | Die Zahlen  $[1,3,6,10,15,21]$ mit einer Operation                                                                  |

2. Für die Vektoren `calc1` bis `calc3` überlegen Sie sich, welcher „Funktionsvorschrift“ die Vektoren genügen, und versuchen Sie, diese mathematisch auszudrücken. 

## Hinweise

- Versuchen Sie unter Benutzung der NumPy- bzw. SciPy-Dokumentation die entsprechenden Befehle zu finden. Hilfreiche Funktionen finden Sie unter [numpy.arange], [numpy.linspace] und [numpy.cumsum].