# Kurvendiskussion: Analytische und numerische Lösung

## Einleitung

In dieser Aufgabe geht es darum, eine Kurvendiskussion durchzuführen, indem eine gegebene Funktion analytisch mit [SymPy](https://docs.sympy.org/latest/index.html) und numerisch mit [NumPy](https://numpy.org/doc/stable/) gelöst wird. Falls du das Paket
noch nicht installiert hast, mach das im Terminal mit `pip install sympy`.

Die Kurvendiskussion ist ein wichtiger Schritt in der Untersuchung von Funktionen, bei der Eigenschaften wie Nullstellen, Extrempunkte, Wendepunkte und das Verhalten im Unendlichen bestimmt werden. Dazu ist das Finden von Nullstellen und Ableitungen der Funktionen notwendig und in Python essentiell. Das Finden von Lösungen für Funktionen kann analytisch oder numerisch erfolgen, kommt aber mit unterschiedlichen Schwierigkeiten.

### Analytische Lösung mit SymPy
    
  SymPy bietet eine symbolische Mathematikumgebung, die es dir ermöglicht, mathematische Ausdrücke und Funktionen symbolisch zu manipulieren.
  
  Verwende in `analyt_curve_sketching.py` `sympy.diff()` zur Berechnung von Ableitungen und `sympy.solve()` zur Bestimmung von Nullstellen.
  Nutze `sympy.lambdify()`, um SymPy-Funktionen in numerische Funktionen umzuwandeln, die mit NumPy verwendet werden können.
  Speichere die Positionen der (reellen!) Nullstellen als `roots_fun` und die der Extremwerte als `roots_fun_prime` und `eval_fun_prime`.


### Numerische Lösung mit NumPy

  Nutze in `num_curve_sketching.py` die Funktion `np.gradient()`, um numerische Ableitungen zu berechnen.
  Zur Bestimmung der Nullstellen verwendest du den Wert vor dem Nullübergang. Verwende dafür die Befehle `np.sign()` und `np.where()`, um die Indexe der Nullstellen zu finden. Nutze $x$-Werte von $-3$ bis $3$ mit $10000$ gleichmäßig verteilten Werten.
  Speichere die Positionen der Nullstellen als `x_zero` und die der Extremwerte als `x_extrem` und `y_extrem`.

### Funktionen

Wähle eine der folgenden Funktionen oder definiere deine eigene Funktion. Für den Test musst du jedoch $f_1(x)$ benutzen.

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

  1. Definiere die Funktion, die analysiert werden soll. Verwende dafür eine der angegebenen Funktionen oder denk dir selber eine aus.

  2. Bestimme die Nullstellen (roots) der Funktion und ihrer Ableitung (siehe Hinweis). Speichere die Nullstellen als Liste in der Reihenfolge, wie `sympy.solve()` sie zurückgibt, aber entferne alle Lösungen mit imaginären Anteilen.

  3. Visualisiere die Funktionen sowie ihre Nullstellen und Extrempunkte sowie die erste Ableitung. Verwende verschiedene Marker für die Nullstellen und Extrempunkte, um sie leicht erkennbar zu machen. Erzeuge ebenfalls eine passende Legende sowie Titel und Achsenbeschriftung.


  4. Gib mit dem `print`-Befehl die Werte für $f(x) = 0$ und $f(0)$ aus.

  5. Mach dasselbe für die abgeleitete Funktion.
  
  6. Was fällt dir auf, wenn du die Ausgabe der numerischen und analytischen Werte vergleichst?

  7. Gib zusätzlich mit dem Befehl `sympy.pprint` die Funktion und deren Ableitung aus.

  8. Warum funktioniert die numerische Berechnung von $f_5(x)$, aber nicht die analytische?

## Hinweise

- Beachte, dass die Ausgabe von `sympy.solve` analytisch ist und noch **evaluiert** werden muss. Der Output sollte also den `type()` `float` haben.
- Überleg dir, ob du wiederverwendeten Code in Funktionen packen kannst.
