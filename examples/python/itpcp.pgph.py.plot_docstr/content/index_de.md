[docstring]: <https://en.wikipedia.org/wiki/Docstring#Python> "docstring"
[figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "figure"
[help]: <https://docs.python.org/3/library/functions.html#help> "help"
[plot]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html> "plot"


# Einfacher Plot mit DocString

## Einleitung

In dieser Aufgabe werden erneut drei Kurven mithilfe des Befehls [plot] erzeugt. Oft ist es nützlich, einem Code eine kurze Erklärung oder Informationen, wann und von wem dieser geschrieben wurde hinzuzufügen. Dies wird mithilfe eines [docstring] durchgeführt.

### Docstring

Docstrings werden dazu verwendet, allgemeine Informationen zu einer Klasse, eines Moduls, oder einer Funktion anzugeben. 
Meist ist dies ein beschreibender Text, um näher zu erläutern, welche Funktion die folgenden Codezeilen (bzw. die Klasse, das Modul, die Funktion) haben und wie sie verwendet werden. 
Am Anfang eines Codes werden auch Informationen wie das Erstellungsdatum, welche Person den Code zu welchem Zweck schrieb, die Version, etc. als Docstring angegeben.
Ein Docstring ist also wichtig für die Dokumentation des Codes.

Während kurze Kommentare für einzelne Codezeilen und Ausdrücke mithilfe des `#` geschrieben werden:

```python
m = 3               # [kg], Masse
g = 9.81            # [m/s^2], durchschnittliche Erdbeschleunigung
F_g = m * g         # Gewichtskraft
```

werden Docstrings mithilfe mehrzeiliger Kommentare eingebaut. Am Anfang eines Skriptes könnte dies beispielweise so realisiert werden:

```python
"""
Multiline comment
This code snippet serves as an example for a docstring
Created by: TU Graz ITPCP
Date: 23.09.2024
"""
```



## Aufgabe 
 Folgender Plot ist von Ihnen im Skript `plot_docstr.py` zu erzeugen:

1. Definieren Sie die Variablen

    |Variable|Wert|
    |:--|:--|
    |`x`| Vektor von $-\pi$ bis $+\pi$ mit $200$ Werten|
    |`y_1`| $y_{1} = x$|
    |`y_2`| $y_{2} = x^{2}$|
    |`y_3`| $y_{3} = x^{3}$|

2. Erzeugen Sie eine matplotlib-Figure mit mehreren Linien: Plotten Sie
    * $y_{1}(x)$; durchgehende Linie; rot
    * $y_{2}(x)$; strichlierte Linie; blau
    * $y_{3}(x)$; punktierte Linie; schwarz

3. Setzen Sie die Limits der Abszisse auf Minimum und Maximum von $x$, die Limits der Ordinate auf Minimum und Maximum von $y_{3}$.

4. Bezeichnen Sie die Abszisse mit $x$, die Ordinate mit $f(x)$ und geben Sie der Figure den Titel `Test`.

5. Schreiben Sie am Anfang des Skripts einen [docstring]: Dieser soll dann in der
Konsole (`python` im Terminal, nicht im File selbst oder Interactive Window) 
mit dem Befehl `help(plot_docstr)` aufgerufen werden können. Da Python [help] 
dies nur für Module, Klassen und Funktionen ermöglicht, muss man bei diesem Versuch 
zu einem Trick greifen: Geben Sie zuvor in der Konsole `import plot_docstr` ein, 
um `plot_docstr.py` wie ein Modul zu importieren.

Zur automatischen Überprüfung soll der Hilfetext Folgendes enthalten:

        Python Script: "Name des Skripts"
        Simple plotting program
        Name: "Vorname" "Nachname"
        Date: "Datum im Format TT.MM.JJJJ"


## Hinweise

* Sie können den Hilfetext hier in der Angabe (Punkt 5) kopieren und dann im Programm
einfügen (Copy&Paste). Ersetzen Sie alles unter Anführungszeichen (`"`) durch
den notwendigen Text oder das notwendige Datum, also `"Vorname"` z.B. durch
`Carmen`. Andere Teile des Textes belassen Sie, wie sie sind.

* Für den Test dürfen die Anfürhungszeichen (`"`) im docstring **nicht** bestehen bleiben.


## Keywords

- Docstring
- Kommentare
- Plotten