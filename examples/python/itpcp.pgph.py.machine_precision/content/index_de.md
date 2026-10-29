[Maschinengenauigkeit]: <https://de.wikipedia.org/wiki/Maschinengenauigkeit> "Maschinengenauigkeit"
[input]: <https://docs.python.org/3/library/functions.html#input> "input"
[dtype]: <https://numpy.org/doc/stable/reference/arrays.dtypes.html> "dtype"
[print]: <https://docs.python.org/3/library/functions.html#print> "print"
[finfo]: <https://numpy.org/doc/stable/reference/generated/numpy.finfo.html>

# Vergleich von Formeln

## Einleitung

In dieser Aufgabe soll die Äquivalenz mathematischer Identitäten mithilfe des Vergleichsoperators `==` untersucht werden.

Achte auf den Unterschied zwischen 'analytischen' Äquivalenzen und den Ergebnissen numerischer Berechnungen.
 
## Aufgabe

Erzeuge das Python-Skript `compare`, welches mathematische Identitäten überprüft.

1. Lass dazu den Benutzer die Variablen $x$ und $y$ mit Hilfe der [input]-Funktion definieren. Ihr Datentyp ist `np.double`. Nutze `input`, um bei der Ausführung deutlich zu machen, welcher Wert gerade an der Reihe ist, also zum Beispiel:

    ```python
    x = input('Please input x: ')
    ```

2. Erzeuge die Arrays `left` und `right` und setze folgende Ausdrücke ein.

    |n|`left`|`right`|
    |-|:----:|:-----:|
    |0|$\log\left(\dfrac{x}{y}\right)$|$\log(x) - \log(y)$
    |1|$\log(xy)$|$\log(x) + \log(y)$
    |2|$\exp(\mathrm{i} x)$|$\cos(x) + \mathrm{i} \sin(x)$
    |3|$\exp(-\mathrm{i} x)$|$\cos(x) - \mathrm{i} \sin(x)$
    |4|$\exp(x + y)$|$\exp(x) \exp(y)$
    |5|$\exp(x - y)$|$\dfrac{\exp(x)}{\exp(y)}$
    |6|$\sin(x + y)$|$\sin(x) \cos(y) + \sin(y) \cos(x)$
    |7|$\cos(2x)$|$2 \cos(x)^{2} - 1$
    |8|$\sin(2x)$|$2 \sin(x) \cos(x)$
    |9|$\cosh(x)$|$\dfrac{\exp(x) + \exp(-x)}{2}$

    ! Achtung, der Datentyp muss `np.cdouble, np.complex128, np.complex_, np.cdouble,`oder `complex` sein, damit der Test funktioniert. 

3. Überprüfe, ob die beiden Arrays die gleichen Inhalte haben. Nutze dafür den Operator `==` und speichere das Ergebnis in die Variable `v_exact`. Wie du merken wirst, werden nicht alle Spalten übereinstimmen. Dies liegt daran, dass wegen der unterschiedlichen Berechnungsarten Differenzen in den letzten Kommastellen auftreten können.

4. Überprüfe daher, ob die absolute Differenz von den Arrays kleiner ist als $10 \varepsilon$ und speichere das Ergebnis in die Variable `v_epsilon`. $\varepsilon$ ist dabei die Maschinengenauigkeit, die die obere Grenze für Rundungsfehler und die Distanz zwischen 1,0 und der nächsthöheren darstellbaren Gleitkommazahl angibt. Für `np.float64` liegt $\varepsilon$ bei $2^{-52}$. In wenigen Fällen reicht sogar $\varepsilon$ noch nicht aus, um numerisch die Äquivalenz von zwei Ergebnissen zu zeigen, mit $10 \varepsilon$ ist man aber meist auf der sicheren Seite.

5. Gib `v_exact` und `v_epsilon` mittels [print] mit vorangestelltem erklärenden Text aus. Überleg dir oder diskutiere mit deinem Tutor die Ausgabe dieses Beispiels.

## Hinweise

* Da [input] einen String liefert, musst du $x$ und $y$ erst in einen anderen Datentyp umwandeln.

* Achte beim Initialisieren deiner Arrays darauf, dass diese auch komplexe Werte enthalten werden. Das heißt, du musst den Datentyp, [dtype], auf komplex setzen.

* Die imaginäre Einheit wird in Python als $j$ geschrieben.

* Für die Maschinengenauigkeit orientierst du dich an der Dokumentation zu [finfo].

