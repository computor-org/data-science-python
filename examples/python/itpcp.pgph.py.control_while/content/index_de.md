# Steuerstrukturen: Die while-Schleife

## Einleitung

In der `while`-Schleife wird, anders als bei der `for`-Schleife, so lange über einen Code-Block iteriert, wie eine festgelegte Bedingung logisch wahr (`True`) ist. Oft wird dabei vor der Schleife eine Anfangsvariable initiiert, die dann während der Execution verändert wird:

```python
counter = 0
while counter <=10:
    do something
    counter += 1
```

Auch hier ist wieder auf die Einrückung des Code-Blocks zu achten. Die Beispiele dienen Ihnen wieder als Anhaltspunkte, wie `while`-Steuerstrukturen verwendet werden können.

## Aufgabe

Initialisieren Sie den Random Number Generator von `numpy` indem sie global `numpy.random.seed(42)` hinzufügen.
Schreiben Sie eine Funktion `while_test`, die wie folgt aufgerufen werden
kann:

```python
z, count = while_test(z, count_lim)
```

`z` ist dabei ein Double-Vektor und `count_lim` ein Integer-Skalar.
Die Aufgaben der Funktion sollen sein:

1. `z` soll solange (punktweise) durch einen gleich großes Array gleichverteilter
   Zufallszahlen im halboffenen Interval `[1,2)` dividiert werden, bis alle Werte in `z` kleiner
   als `1` sind. **Für jede Divison sollen neue Zufallszahlen erzeugt werden**.

1. In der Variablen `count` soll gezählt werden, wie oft das Array dividiert wurde.

1. Falls `count` den Wert `count_lim` erreicht, soll **nach** der entsprechenden Divison die
   [while]-Schleife verlassen werden.

## Hinweise

- Falls Sie die Funktion nicht mit einem eindimensionalen Double-Array `z` testen, sondern z.B. mit einem Skalar, einem mehrdimensionalen Array, einem Integer-Vektor oder einer Python-Liste, könnten je nach Implementation unerwartete Fehler auftreten. Da hier der erwartete Datentyp genau definiert ist, liegt die Verantwortung beim User, auch diesen Datentyp bereit zu stellen. Möchten Sie Ihre Funktion aber so schreiben, dass sie allgemeinere Inputs akzeptiert, ist bei diesem konkreten Beispiel [np.asarray] und ggf. [np.random.random_sample] hilfreich.
- Schleifen können mit dem Keyword [break] abgebrochen werden.

[break]: https://docs.python.org/3/reference/simple_stmts.html#break "break"
[np.asarray]: https://numpy.org/doc/stable/reference/generated/numpy.asarray.html "np.asarray"
[np.random.random_sample]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html "np.random.random_sample"
[while]: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming "while"
