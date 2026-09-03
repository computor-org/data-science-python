# Vergleich logische Indizierung mit Schleife bzw. Mathematik

## Einleitung

Die Aufgabe hier ist dreigeteilt und soll einen Vergleich von Algorithmen ermöglichen, die mit Hilfe der logischen Indizierung, mit Hilfe von `for`- und `if`-Strukturen, bzw. mit Hilfe von mathematischen Funktionen erstellt werden.

Nach Erledigung dieser Aufgabe sollten Sie verstanden haben, welchen Vorteil die logische Indizierung gegenüber Lösungen mit Schleifen hat, und wann man einfach mathematische Funktionen verwenden kann.

## Aufgabe

### 1. Mit logischer Indizierung

Erstellen Sie die Funktion

```python
def randmeanlog(R):
    # ...
    return R
```

die mit Hilfe logischer Indizierung und des numpy Befehls `np.mean`

1. alle Werte im Feld `R`, die kleiner als Null sind, durch den Mittelwert der negativen Zahlen ersetzt;
1. alle Werte im Feld `R`, die größer als Null sind, durch den Mittelwert der positiven Zahlen ersetzt.

Achten Sie dabei darauf, dass

- der Hauptteil der Funktion nur maximal vier Zeilen hat,
- **keine** Abfragen oder Schleifen (`for`, `while` und `if`) verwendet werden.

### 2. Mit Schleife

Im zweiten Teil erledigen Sie die gleiche Aufgabe in einem neuen File mit der Funktion

```python
def randmeanfor(R):
    # ...
    return R
```

unter Verwendung von Schleifen. Es empfiehlt sich folgende Vorgehensweise:

1. Initialisieren Sie vor der ersten Schleife Summen- und Zählvariablen.
1. Ermitteln Sie in einer Schleife die Anzahl und Summe aller positiven (negativen) Werte.
1. Bestimmen Sie die jeweiligen Mittelwerte.
1. Weisen Sie diese in einer zweiten Schleife den entsprechenden Positionen zu.

### Mit mathematischer Funktion

Im dritten Teil erledigen Sie eine etwas andere Aufgabe mit der Funktion

```python
def randsignum(R):
    # ...
    return R
```

Ersetzen Sie in `R`

1. alle Werte $< 0$ durch $-1$ und

1. alle Werte $> 0$ durch $1$.

1. Schreiben Sie dies in nur einer Zeile unter Verwendung der numpy-Funktion [sign] ohne irgendwelche Kontrollstrukturen wie `if`, `for` oder `while`. Überlegen Sie, warum ein solcher Weg für die ersten beiden Aufgaben nicht möglich ist.

## Hinweise

- Denken Sie daran, dass das array `R` mehrere Dimensionen haben kann!
- Sie können trotzdem über nur einen index iterieren, wenn Sie die Dimensionen zuvor speichern, das array danach flach machen mittels [flatten] und es schließlich wieder in seine alte Form bringen. Alternativ können Sie auch [unravel_index] nutzen.

[flatten]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html "flatten"
[sign]: https://numpy.org/doc/stable/reference/generated/numpy.sign.html "sign"
[unravel_index]: https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html "unravel_index"
