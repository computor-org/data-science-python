# Polynome

## Einleitung 
Polynome sind mathematische Funktionen, die aus Summen von Potenzen einer Variablen bestehen. Allgemein hat ein Polynom $n$-ten Grades die Form:
$$a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$$

Polynome kann man aufgrund ihrer einfachen Struktur gut addieren, subtrahieren, multiplizieren und auch ableiten und integrieren.

Dies soll nun mittels einer Python-Klasse in `polynom.py` umgesetzt werden. 

### Polynom-Klasse: 
Ein Objekt der Klasse `Polynom` sollte durch Übergabe einer Liste von Koeffizienten erstellt werden. Dabei sollte der erste Koeffizient dem höchsten Grad des Polynoms entsprechen, z.B.: `Polynom([5,0,0,2,3])` entspricht $$5x^4 + 2x + 3.$$


Zudem sollte die Klasse die Python-internen Methoden `__add__`, `__sub__`, `__mul__`, `__eq__`, `__str__`, `__call__` und `__len__` überschreiben (siehe [function-overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/) für mehr Details). Diese sollen es möglich machen, Polynome zu addieren, subtrahieren, multiplizieren und auszugeben. 

* Die Addition `__add__` von zwei Polynomen soll ein neues Polynom zurückgeben, das die Summe der beiden Polynome ist, z.B. `Polynom([5,0,0,2,3]) + Polynom([1,0,6,0,0])` ergibt `Polynom([6,0,6,2,3])`. Analog dazu die Subtraktion `__sub__` und Multiplikation `__mul__`.

* Die Methode `__eq__` soll zwei Polynome auf Gleichheit überprüfen, z.B. `Polynom([5,0,0,2,3]) == Polynom([5,0,0,2,3])` soll `True` zurückgeben.

* Die Methode `__str__` soll das Polynom als String zurückgeben, z.B. `Polynom([5,0,0,2,3])` soll `5x^4 + 2x + 3` ausgeben.

* Die Methode `__call__` soll das Polynom für einen gegebenen Wert von `x` auswerten, z.B. `Polynom([5,0,0,2,3])(2)` soll `87` zurückgeben.

* Die Methode `__len__` soll den Grad des Polynoms zurückgeben, z.B. `len(Polynom([5,0,0,2,3]))` soll `4` zurückgeben.

* Zudem soll die Klasse eine Methode `derivative` haben, die das Polynom ableitet und das abgeleitete Polynom zurückgibt.

* Schließlich soll die Klasse eine Methode `integrate` haben, die das Polynom integriert und das integrierte Polynom zurückgibt. Die Konstante des Integrals sollte dabei $0$ sein.

## Aufgabe 
1. Schreibe Tests für die Klasse `Polynom` in `test_polynom.py`, um sicherzustellen, dass die Implementierung der Methoden korrekt ist. 

2. Nutze dazu `assert`-Statements von pytest. Um die Methoden testen zu können, solltest du auch die `__eq__`-Methode implementiert haben, damit du die Polynome vergleichen kannst!

3. Für jeden überladenen Operator soll mindestens ein Test geschrieben werden und auch für die Methoden `derivative` und `integrate`.


## Hinweis 
 * Der Test in dieser Übung überprüft nur die Klasse.