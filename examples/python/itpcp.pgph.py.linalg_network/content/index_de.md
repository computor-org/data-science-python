[linalg.solve]: <https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html> "linalg.solve"

# Lineare Gleichungssysteme und die Kirchoffschen Regeln

## Einleitung

Ein lineares Gleichungssystem der Form $\mathbf{Ax} = \mathbf{b}$ ist homogen, wenn $\mathbf{b} = \mathbf{0}$, ansonsten ist es inhomogen. Egal ob homogen oder inhomogen, wir können das lineare Gleichungssystem mittels numpy.[linalg.solve] lösen.

Haben wir zum Beispiel die Koeffizientenmatrix $\mathbf{A}$ und den Vektor $\mathbf{b}$ gegeben, so können wir den Lösungsvektor $\mathbf{x}$ berechnen.

$$
  \mathbf{A} = 
  \begin{bmatrix}
    1 & 2 & -1 \\ 3 & 4 &  0 \\ -2 & 3 &  1
  \end{bmatrix}
  ,\quad
  \mathbf{b} =
  \begin{bmatrix}
    3 \\ 15 \\ 11
  \end{bmatrix}
$$


```python
import numpy as np

A = np.array([[1, 2, -1],[3, 4, 0], [-2, 3, 1]])
b = np.array([3, 15, 11])

x = np.linalg.solve(A, b)
```

$$
  \mathbf{x} =
  \begin{bmatrix}
    1 \\ 3 \\ 4
  \end{bmatrix}
$$


### Anwendung


Gegeben ist ein Netzwerk mit 4 ohmschen Widerständen und 2 Spannungsquellen:

<div align="center">
<img src="mediaFiles/stromkreis.jpg" alt="Image" width="100%" name="Stromkreis"/>
</div>

Die sich einstellenden Ströme kann man bequem über die Kirchhoffschen Regeln bestimmen:
 
**Knotenregel:** *An jedem Knoten ist die Summe der einfließenden Ströme gleich der Summe der ausfließenden Ströme.*      
  In unserem Beispiel heißt das:
  
* Knoten P: $i_1-i_2+i_3=0$
  
* Knoten Q: $-i_1+i_2-i_3=0$

 In diesem Fall sind das äquivalente Gleichungen, das bedeutet, dass sie uns die gleiche Information liefern. Daher brauchen wir nur eine von ihnen, welche Form ist egal.

**Maschenregel:** *In jeder Masche ist die Summe der Spannungsabfälle gleich der Summe der Spannungsquellen.*
  
* Rechte Schleife: $10~i_2 + (10+15)~i_3 = U_1$

* Linke Schleife: $ 20~i_1 + 10~i_2 = U_2$
    

Nun fassen wir unsere Gleichungen in einem linearen Gleichungssystem zusammen und schreiben es in Matrixform:

$
\begin{bmatrix}
1 & -1 & 1 \\ 0 & 10 & 25 \\ 20 & 10 & 0 \end{bmatrix}  \, 
 \begin{bmatrix} i_1 \\ i_2 \\ i_3 \end{bmatrix} = 
\begin{bmatrix} 0 \\ U_1 \\ U_2 \end{bmatrix} \; .
$

Wobei die erste Zeile der Koeffizientenmatrix unsere Gleichung aus der Kontenregel ist und die anderen zwei Zeilen aus der Maschenregel kommen. Allgemein schreiben wir unseren "Stromvektor" als Vektor $\mathbf{x}$

$
\begin{bmatrix}
1 & -1 & 1 \\ 0 & 10 & 25 \\ 20 & 10 & 0 \end{bmatrix}  \, 
 {\bf x} = 
\begin{bmatrix} 0 \\ U_1 \\ U_2 \end{bmatrix} \; .
$


## Aufgabe

Schreiben Sie nun das Skript `linalg_network`, das dieses Gleichungssystem für verschiedene Werte von $U_{1}$ und $U_{2}$ löst:

1. Speichern Sie den Lösungsvektor des Gleichungssystems für $U_1=90$, $U_2=80$ als Variable `I1`.

2. Speichern Sie den Lösungsvektor des Gleichungssystems für $U_1=125$, $U_2=90$ als Variable `I2`.

3. Lösen Sie das Gleichungssystem **gleichzeitig** für die drei rechten Seiten
       $$
       \begin{bmatrix} 0 \\ 90 \\ 80 \end{bmatrix},
       \begin{bmatrix} 0 \\ 125 \\ 90 \end{bmatrix},
       \begin{bmatrix} 0 \\ 150 \\ 70 \end{bmatrix}
       $$

    und speichern Sie das Ergebnis in der Matrix `I`.

Dies bedeutet, dass aus $\mathbf{b}$ eine Matrix wird, wodurch auch $\mathbf{x}$ (in unserem Fall `I`) zu einer wird.


## Hinweise
* Welche Dimension die beteiligten Vektoren haben müssen, überlegt man sich 
 am besten direkt am Gleichungssystem $\mathbf{Ax}=\mathbf{b}$.

* Die Koeffizienten wurden in diesem Beispiel so gewählt, dass in der Lösung nur ganze Zahlen vorkommen. Überprüfen Sie Ihre Ergebnisse!  