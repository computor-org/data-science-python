[Maschinengenauigkeit]: <https://de.wikipedia.org/wiki/Maschinengenauigkeit> "Maschinengenauigkeit"
[input]: <https://docs.python.org/3/library/functions.html#input> "input"
[dtype]: <https://numpy.org/doc/stable/reference/arrays.dtypes.html> "dtype"
[print]: <https://docs.python.org/3/library/functions.html#print> "print"
[finfo]: <https://numpy.org/doc/stable/reference/generated/numpy.finfo.html>

# Vergleich von Formeln

## Einleitung

In dieser Aufgabe soll die equivalenz mathematischer Identitäten mithilfe des Vergleichsoperators `==` untersucht werden.

Achten Sie auf den Unterschied zwischen 'analytischen' Equivalenzen und den Ergebnissen numerischer Berechnungen.
 
## Aufgabe

Erzeugen Sie das Python-Skript `compare`, welches mathematische Identitäten überprüft.

1. Lassen Sie dazu den Benutzer die Variablen $x$ und $y$ mit Hilfe der [input]-Funktion definieren. Ihr Datentyp ist `np.double`. Nutzen Sie `input`, um bei der Ausführung deutlich zu machen, welcher Wert gerade an der Reihe ist, also zum Beispiel:

    ```python
    x = input('Please input x: ')
    ```

2. Erzeugen Sie die Arrays `left` und `right` und setzen Sie folgende Ausdrücke ein.

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

    ! Achtung, der Datentyp muss `np.cdouble, np.complex128, np.complex_, np.cdouble,`oder `complex` sein, sodass der Test funktioniert. 

3. Überprüfen Sie, ob die beiden Arrays die gleichen Inhalte haben. Nutzen Sie dafür den Operator `==` und speichern Sie das Ergebnis in die Variable `v_exact`. Wie Sie merken werden, werden nicht alle Spalten übereinstimmen. Dies liegt daran, dass wegen den unterschiedlichen Berechnungsarten Differenzen in den letzten Kommastellen auftreten können.

4. Überprüfen Sie daher, ob die absolute Differenz von den Arrays kleiner ist als $10 \varepsilon$ und speichern Sie das Ergebnis in die Variable `v_epsilon`. $\varepsilon$ ist dabei die Maschinengenauigkeit, die die obere Grenze für Rundungsfehler und die Distanz zwischen 1.0 und der nächsthöheren Nachkommazahl angibt. Für `np.float64` liegt $\varepsilon$ bei $2^{-52}$. In wenigen Fällen reicht sogar $\varepsilon$ noch nicht aus, um numerisch die Äquivalenz von zwei Ergebnissen zu zeigen, mit $10 \varepsilon$ ist man aber meist auf der sicheren Seite.

5. Geben Sie `v_exact` und `v_epsilon` mittels [print] mit vorangestelltem erklärenden Text aus. Überlegen Sie sich oder diskutieren Sie mit Ihrem Tutor über die Ausgabe dieses Beispiel.

## Hinweise

* Da [input] einen String liefert, müssen Sie $x$ und $y$ erst in einen anderen Datentyp umwandeln.

* Achten Sie beim Initialisieren Ihrer Arrays darauf, dass diese auch komplexe Werte enthalten werden. Das heißt, Sie müssen den Datentyp, [dtype], auf komplex setzen.

* Die imaginäre Einheit wird in Python als $j$ geschrieben.

* Für die Maschinengenauigkeit orientieren Sie sich an der Dokumentation zu [finfo].

