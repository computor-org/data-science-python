# Analyse der Lösungen einer quadratischen Gleichung 1

## Einleitung

In dieser Aufgabe wollen wir die in `itpcp.pgph.py.quadratic_eq` und `itpcp.pgph.py.quadratic_eq_eval` geschriebenen
Funktionen weiterverwenden.

Dieses Beispiel können Sie demnach erst lösen, wenn Sie `quadratic_eq` und `quadratic_eq_eval`
bereits erstellt haben.

## Aufgabe

Schreiben Sie die Funktion

```python
def quadratic_eq_test(n, rmin, rmax):
    # ...
    return x1, x2, r1, r2
```

die die von Ihnen zuvor geschriebenen Funktionen `quadratic_eq` und `quadratic_eq_eval` auswertet.

1. Setzen Sie die Default-Werte

   | Variable | Bedeutung            | Default |
   | -------- | -------------------- | ------- |
   | `n`      | Größe der Matrizen   | `16`    |
   | `rmin`   | Minimale Zufallszahl | `3`     |
   | `rmax`   | Maximale Zufallszahl | `6`     |

1. Erzeugen Sie 3 Arrays `a`, `b` und `c`. Diese sollen aus Zufallszahlen zwischen
   `rmin` und `rmax` bestehen und die Größe $n \times n$ haben.

1. Setzen Sie die mittlere Spalte von `a`, und die mittlere Zeile von `b` auf Null.
   Existiert keine mittlere Spalte/Zeile (wenn `n` eine gerade Zahl ist), werden die
   Werte in der Spalte/Zeile mit dem nächst niedrigeren Index auf Null gesetzt. Verwenden Sie
   dafür die Funktion [ceil] (z.B. bei `n=5` ist die Mitte `3.te`, bei `n=4` soll die
   Mitte `2.te` sein).

1. Rufen Sie mit `a`, `b` und `c` die Funktion `quadratic_eq` auf.

1. Rufen Sie mit den Ergebnissen von `quadratic_eq` die Funktion `quadratic_eq_eval` auf.

1. Geben Sie in `x1`, `x2` die Ergebnisse von `quadratic_eq`, in `r1`, `r2` die Ergebnisse von
   `quadratic_eq_eval` zurück.

## Hinweise

- Die numpy-Funktion [rand](n, n) liefert eine $n\times n$ Matrix von Zufallszahlen
  zwischen 0 und 1. Die Anpassung an das Intervall `(rmin,rmax)` erfolgt durch eine
  Skalierung (Multiplikation) und Verschiebung (Addition). Alternativ kann man auch
  [np.random.uniform] verwenden.

- Es ist wichtig, dass die Reihenfolge der ersten paar Zeilen eingehalten wird. Es
  könnte sein, dass diese durch das Formatieren verändert wird
  `from quadratic_eq_eval import quadratic_eq_eval` muss als letztes kommen!:

```python
import numpy as np
import sys
import os
# set path to filepath of current file
cur_file_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../itpcp.pgph.py.quadratic_eq_eval/")
sys.path.append("../itpcp.pgph.py.quadratic_eq/")
from quadratic_eq import quadratic_eq  # ! must be placed after sys.path.append
from quadratic_eq_eval import quadratic_eq_eval  # ! must be placed after sys.path.append
```

[ceil]: https://numpy.org/doc/stable/reference/generated/numpy.ceil.html "ceil"
[np.random.uniform]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html "rand_unif"
[rand]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html "rand"
