# Kurvendiskussion: Analytische und Numerische Lösung

## Einleitung

In dieser Aufgabe geht es darum, eine Kurvendiskussion durchzuführen, indem eine gegebene Funktion analytisch mit [SymPy](https://docs.sympy.org/latest/index.html) und numerisch mit [NumPy](https://numpy.org/doc/stable/) gelöst wird. Falls Sie das Paket
noch nicht installiert haben, machen Sie das im Terminal mit `pip install sympy`.

Die Kurvendiskussion ist ein wichtiger Schritt in der Untersuchung von Funktionen, bei der Eigenschaften wie Nullstellen, Extrempunkte, Wendepunkte und das Verhalten im Unendlichen bestimmt werden. Dazu ist das Finden von Nullstellen und Ableitungen der Funktionen notwendig und in Python essentiell. Das Finden von Lösungen für Funktionen kann analytisch oder numerisch erfolgen, kommt aber mit unterschiedlichen Schwierigkeiten.

### Analytische Lösung mit SymPy
    
  SymPy bietet eine symbolische Mathematikumgebung, die es Ihnen ermöglicht, mathematische Ausdrücke und Funktionen symbolisch zu manipulieren.
  
  Verwenden Sie in `analyt_curve_sketching.py` `sympy.diff()` zur Berechnung von Ableitungen und `sympy.solve()` zur Bestimmung von Nullstellen.
  Nutzen Sie `sympy.lambdify()` um SymPy-Funktionen in numerische Funktionen umzuwandeln, die mit NumPy verwendet werden können.
  Speichern Sie die Positionen der (reellen!) Nullstellen als `roots_fun`. Die der Extremwerte als `roots_fun_prime` und `eval_fun_prime`.


### Numerische Lösung mit NumPy

  Nutzen Sie in `num_curve_sketching.py` die Funktion `np.gradient()` kann verwendet werden, um numerische Ableitungen zu berechnen.
  Zur Bestimmung der Nullstellen verwenden Sie den Wert vor dem Nullübergang. Verwenden Sie dafür den Befehl `np.sign()` und `np.where()` um die Indexe der Nullstellen zu finden. Nutzen Sie $x$-Werte von $-3$ bis $3$ mit $10000$ gleichmäßigverteilte Werte.
  Speichern Sie die Positionen der Nullstellen als `x_zero`. Die der Extremwerte als `x_extrem` und `y_extrem`.

### Funktionen

Wählen Sie eine der folgenden Funktionen oder definieren Sie Ihre eigene Funktion. Für den Test müssen Sie jedoch $f_1(x)$ benutzen.

$$
\begin{aligned}
  f_1(x) &= -x^4 + 6x^2 - x - 2 \\
  f_2(x) &= \sin(x) + \cos(2x) \\
  f_3(x) &= e^{-x^2} \\
  f_4(x) &= \tanh(x) \\
  f_5(x) &= e^{-x^2} \sin(2 \pi x)
\end{aligned}
$$



## Aufgabe

  1. Definieren Sie die Funktion, die analysiert werden soll. Verwenden Sie dafür eine der angegeben Funktion oder denken Sie sich selber eine aus.

  2. Bestimmen Sie die Nullstellen (roots) der Funktion und ihrer Ableitung (siehe Hinweis). Speichern Sie die Nullstellen als Liste in der Reihenfolge, wie `sympy.solve()` sie zurückgibt, aber entfernen Sie alle Lösungen mit imaginären Anteilen.

  3. Visualisieren Sie die Funktionen sowie ihre Nullstellen und Extrempunkte, sowie die erste Ableitung. Verwenden Sie verschiedene Marker für die Nullstellen und Extrempunkte, um sie leicht erkennbar zu machen. Erzeugen Sie ebenfalls eine passende Legende, sowie Titel und Achsenbeschriftung.


  4. Geben Sie mit dem `print` Befehl die Werte für $f(x) = 0$ und $f(0)$ aus.

  5. Machen Sie dasselbe für die abgeleitete Funktion.
  
  6. Was fällt Ihnen auf, wenn sie die Ausgabe der numerischen und analytischen Werte vergleichen?

  7. Geben Sie zusätzlich mit dem Befehl `sympy.pprint` die Funktion und deren Ableitung aus.

  8. Warum funktioniert die numerische Berechnung von $f_5(x)$, aber nicht die analytische?

## Hinweise

- Beachten Sie das die Ausgabe von `sympy.solve` analytisch ist und noch **evaluiert** werden muss. Der output sollte als den `type()` `float` haben.
- Überlegen Sie, ob Sie wiederverwendeten Code in Funktionen packen können.
