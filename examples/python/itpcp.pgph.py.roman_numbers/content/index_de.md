[Wikipedia]: <https://de.wikipedia.org/wiki/R%C3%B6mische_Zahlschrift> "Wikipedia"

# Römische Ziffern

## Einleitung

Die folgende Aufgabe soll als kleine *Warm-up*-Übung für den Umgang mit `python dictionaries` dienen. Mithilfe einer Funktion sollen Zahlen in römischer Notation in arabische Zahlen umgewandelt werden.

### Römische Zahlen

Für römische Zahlen gilt folgende Notation:

|Römisch|Arabisch|
|:--|:--|
``I`` | 1
``V`` | 5
``X`` | 10
``L`` |  50
``C`` | 100
``D`` | 500
``M`` | 1000

Römische Notation erfolgt dabei grundsätzlich absteigend von der höchsten zur niedrigsten Ziffer. *Ausnahme:* Wenn eine niedrigere Ziffer vor einer höheren Ziffer steht, wird diese von der höheren Ziffer abgezogen:

```python
IV = 4
IX = 9
```

Die römischen Ziffern und entsprechenden arabischen Zahlen der obigen Tabelle sollen dabei als `key-value pairs` in einem `dictionary` gespeichert werden.

## Aufgabe

1. Schreibe eine Funktion in `int_roman.py`, die als Eingabe römische Ziffern in Form von `strings` nimmt und diese in arabische Zahlen umwandelt, etwa

```python
arabic = int_roman("XV")  # ergibt 15
```

2. Weiters soll die Funktion einen Docstring haben, der die Funktionsweise der Funktion beschreibt, dieser sollte den [numpy-docstring](https://numpydoc.readthedocs.io/en/latest/format.html) Konventionen folgen.

3. Ebenfalls soll die Funktion einen `ValueError` werfen, wenn die Eingabe keine römischen Ziffern enthält oder nicht vom Datentyp `str` ist.

## Hinweise

* Eine Einführung zu römischen Zahlen findet sich auf [Wikipedia].
Hier sollen die einfachen Regeln verwendet werden, wie sie in dem Artikel im Punkt `Subtraktionsregel` beschrieben sind.