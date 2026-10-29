# Vergleich logische Indizierung mit Schleife bzw. Mathematik

## Einleitung

Die Aufgabe hier ist dreigeteilt und soll einen Vergleich von Algorithmen ermöglichen, die mit Hilfe der logischen Indizierung, mit Hilfe von `for`- und `if`-Strukturen bzw. mit Hilfe von mathematischen Funktionen erstellt werden.

Nach Erledigung dieser Aufgabe solltest du verstanden haben, welchen Vorteil die logische Indizierung gegenüber Lösungen mit Schleifen hat und wann man einfach mathematische Funktionen verwenden kann.

## Aufgabe

### 1. Mit logischer Indizierung

Erstelle die Funktion

```python
def randmeanlog(R):
    # ...
    return R
```

die mit Hilfe logischer Indizierung und des NumPy-Befehls `np.mean`

1. alle Werte im Feld `R`, die kleiner als Null sind, durch den Mittelwert der negativen Zahlen ersetzt;
1. alle Werte im Feld `R`, die größer als Null sind, durch den Mittelwert der positiven Zahlen ersetzt.

Achte dabei darauf, dass

- der Hauptteil der Funktion nur maximal vier Zeilen hat,
- **keine** Abfragen oder Schleifen (`for`, `while` und `if`) verwendet werden.

### 2. Mit Schleife

Im zweiten Teil erledigst du die gleiche Aufgabe in einem neuen File mit der Funktion

```python
def randmeanfor(R):
    # ...
    return R
```

unter Verwendung von Schleifen. Es empfiehlt sich folgende Vorgehensweise:

1. Initialisiere vor der ersten Schleife Summen- und Zählvariablen.
1. Ermittle in einer Schleife die Anzahl und Summe aller positiven (negativen) Werte.
1. Bestimme die jeweiligen Mittelwerte.
1. Weise diese in einer zweiten Schleife den entsprechenden Positionen zu.

### 3. Mit mathematischer Funktion

Im dritten Teil erledigst du eine etwas andere Aufgabe mit der Funktion

```python
def randsignum(R):
    # ...
    return R
```

Ersetze in `R`

1. alle Werte $< 0$ durch $-1$ und

1. alle Werte $> 0$ durch $1$.

1. Schreib dies in nur einer Zeile unter Verwendung der NumPy-Funktion [sign] ohne irgendwelche Kontrollstrukturen wie `if`, `for` oder `while`. Überleg dir, warum ein solcher Weg für die ersten beiden Aufgaben nicht möglich ist.

## Hinweise

- Denk daran, dass das Array `R` mehrere Dimensionen haben kann!
- Du kannst trotzdem über nur einen Index iterieren, wenn du die Dimensionen zuvor speicherst, das Array danach mittels [flatten] flach machst und es schließlich wieder in seine alte Form bringst. Alternativ kannst du auch [unravel_index] nutzen.

[flatten]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html "flatten"
[sign]: https://numpy.org/doc/stable/reference/generated/numpy.sign.html "sign"
[unravel_index]: https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html "unravel_index"
