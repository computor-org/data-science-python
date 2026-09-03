[Docstring]: <https://en.wikipedia.org/wiki/Docstring#Python> "Docstring"
[exp]: <https://numpy.org/doc/stable/reference/generated/numpy.exp.html> "exp"
[cosh]: <https://numpy.org/doc/stable/reference/generated/numpy.cosh.html> "cosh"
[sqrt]: <https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html> "sqrt"

# Erstellen und Plotten eigener Funktionen

## Einleitung

Die Übung beschäftigt sich mit dem Erstellen und Plotten eigener Funktionen.
Hierfür sind zwei Python-Funktionen `sgauss` und `secansh`, sowie ein Python-Skript `pscript` zu erzeugen.
Beachten Sie, dass <span style="color: red;">3 verschiedene py-Files</span> von Ihnen zu befüllen sind!

### Funktionen

Funktionen ermöglichen es, einen bestimmten Code (z.B. einen Algorithmus) nur einmal zu definieren, und öfters mit unterschiedlichen Parametern auszuführen.
Funktionen erhalten beim Aufruf Werte für die Inputvariablen, (Argumente), führen damit Berechnungen durch und geben Outputvariablen zurück.
(Sie haben in den bisherigen Übungen auch schon einige vordefinierte Funktionen kennengelernt, zum Beispiel `print` oder `plot`).

Funktionen werden mit dem Schlüsselwort **`def`** definiert.
Ein Beispiel für eine einfache Funktion mit Namen `compute_sum`, welche zwei Variablen `a` und `b` erhält, die Summe berechnet und das Ergebnis mit dem Schlüsselwort **`return`** zurückgibt, ist:

```python
def compute_sum(a, b):
    """return the sum of two numbers a, b"""
    result = a + b
    return result
```

Wichtig ist in Python die Einrückung der Funktionsdefinition! Im Gegensatz zu einigen anderen Programmiersprachen, in denen mit { ... } der Funkionsblock abgegrenzt wird, gehört in Python alles, was in der gleichen *Ebene* eingerückt ist, zur Funktion.

Am Anfang der Funktionsdefinition sollte zwischen drei doppelten Anführungszeichen `""" ... """` ein sogenannter *[Docstring]* stehen, der eine kurze Beschreibung der Funktion gibt.
Dieser lässt sich später anzeigen z.B. mit `help(compute_sum)`.

Diese obrige Funktion kann dann wie folgt aufgerufen werden:

```python
new_var = compute_sum(3, 4)
```

Die Variable `new_var` hat nun den Wert 7.

Wichtig ist auch zu verstehen, dass die Variablen, die innerhalb einer Funktion definiert werden, außerhalb der Funktion nicht verfügbar sind. Wir können also im Skript nicht auf `result` zugreifen.

Mehrere Rückgabewerte lassen sich durch Kommas getrennt zurückgeben:

```python
def sum_and_diff(a, b):
    """returns the sum and difference of
    two numbers a and b"""

    return a + b, a - b

ab_sum, ab_diff = sum_and_diff(3, 4)
```

Hier erhalten wir für `ab_sum` den Wert 7 und für `ab_diff` den Wert -1.

Es ist sinnvoll, wichtige Funktionen getrennt vom Hauptskript in eigenen Dateien zu definieren. So können sie von anderen Programmen wiederverwendet werdenund helfen dabei, schwer auffindbare Fehler zu vermeiden. 

Angenommen, wir definieren unsere beiden Funktionen `compute_sum` and `sum_and_diff` in einem File `my_functions.py` im selben Verzeichnis, mit dem Inhalt

```python
# ...put necessary imports for the function definitions here

def compute_sum(a, b):
    """return the sum of two numbers a, b"""
    result = a + b
    return result

def sum_and_diff(a, b):
    """returns the sum and difference of
    two numbers a and b"""

    return a + b, a - b
```

dann können wir uns unserem Hauptskript diese Funktionen importieren und verwenden:

```python
from my_functions import compute_sum, sum_and_diff

# Now we can use our defined functions
new_var = compute_sum(3, 4)
ab_sum, ab_diff = sum_and_diff(3, 4)
```

### Wahrscheinlichkeitsverteilungen

* Die Funktion $$g = \frac{1}{s\sqrt{2\pi}} \exp \left( -\frac{(x-x_0)^2}{2s^2} \right)$$
    ist die Gaussfunktion. Sie dient der Berechnung und dem einfachen Plotten der Gaußschen Glockenkurve. Ebenso kann der Secans Hyperbolicus auf Basis der Funktion [exp] erzeugt werden.

* Überlegen Sie sich, was passiert, wenn man die Funktionsfiles wie ein Python-Skript ausführt! Die Funktion `g` entspricht der Wahrscheinlichkeitsdichte einer Wahrscheinlichkeitsverteilung, nämlich der Normalverteilung. Eine Wahrscheinlichkeitsdichte genügt der Bedingung, dass die Fläche unter der gesamten Funktion den Wert 1 annimmt. Diese sogenannte Normierung wird durch den Normierungsfaktor sichergestellt. Der Normierungsfaktor der Funktion g ist der Term $1/(s\sqrt{2\pi})$.

* Die Funktion $$h = \frac{1}{\pi s} {\operatorname{sech}} \left( -\frac{x-x_0}{s} \right)$$
    ist der Secans Hyperbolicus. Er stellt wie die Gaussfunktion eine
    Wahrscheinlichkeitsdichte dar und genügt daher ebenfalls der Bedingung, dass die
    Fläche unter der gesamten Funktion den Wert 1 annimmt.
    Der Normierungsfaktor der Funktionen `h` ist der
    Term $1/(\pi s)$.

## Aufgabe

### Berechnung der Gaussschen Glockenkurve

Erzeugen Sie die Funktion `sgauss` im gleichnamigen File,
die mit dem Aufruf

```python
g = sgauss(x, x_0, s)
```

die Gauss-Funktion `g` aus der Einleitung berechnet. Die Inputs der Funktion sollen

```
x   : Vektor von x-Werten
x_0 : Skalar, Lage des Maximums
s   : Skalar, Halbwertsbreite
```

sein.

### Berechnung der Funktion Secans Hyperbolicus

Erzeugen Sie die Funktion `secansh` im gleichnamigen File,
die mit dem Aufruf

```python
h = secansh(x, x_0, s)
```

die Secans Hyperbolicus Funktion `h` aus der Einleitung berechnet. Die Inputs der
Funktion sollen

```
x   : Vektor von x-Werten
x_0 : Skalar, Lage des Maximums
s   : Skalar, Halbwertsbreite
```

sein.

### Berechnung und einfaches Plotten der Gaussschen Glockenkurve und des Secans Hyperbolicus

Erzeugen Sie im Skript `pscript.py` ein Programm, das die beiden
Funktionen berechnet und graphisch darstellt.

Wählen Sie für die Parameter die Werte
$x_0 = 2$ und $s = 0.2$, wobei $x_0$ die Lage des Maximums und $s$ die
Halbwertsbreite sind.
(Sie können testweise auch andere `x_0` und `s` ausprobieren. Wie verhalten sich dann die Kurven?)

1. Erzeugen Sie mit den Formeln
    $$
    \begin{aligned}
      x_a  &= x_0 - 5s \\
      x_e  &= x_0 + 5s \\
      x_n  &= 300
    \end{aligned}
    $$
    die Variablen `x_a`, `x_e` und `x_n`.

2. Erzeugen Sie damit einen Vektor `x` mit
    `x_n` äquidistanten Werten zwischen obigem Anfangs- und Endpunkt (`linspace`).

3. Berechnen Sie nun mit Hilfe **Ihrer eigenen** Funktionen `sgauss` und `secansh` die Variablen
    `g` als Ergebnis von `sgauss` und `h` als Ergebnis von `secansh`.

4. Plotten Sie in einer Figure die beiden Funktionen $g(x)$ (rot)
    und $h(x)$ (blau).

5. Versehen Sie die Zeichnung mit einer Beschriftung der x-Achse (`x`) und der y-Achse (`f(x)`).
    Ausserdem soll es eine Legende geben, wobei die Bezeichnung der beiden
    Linien in der Legende `Gauss` und `Sech` sein soll.

## Hinweise

* Der Secans Hyperbolicus ist definiert als
$$ \operatorname{sech} (x) = 1 / \cosh (x) $$

* Python-Hilfe zu einzelnen Befehlen finden Sie unter [sqrt], [exp], [cosh].

* Die Zahl $e$ als solches existiert in Python nicht. Sie muss mit Hilfe
der Funktion [exp] erzeugt werden.

* Überlegen Sie sich, was passiert, wenn man die Funktionsfiles wie ein Python-Skript ausführt!