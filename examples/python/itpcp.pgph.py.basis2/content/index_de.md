[abs]: <https://numpy.org/doc/stable/reference/generated/numpy.absolute.html> "abs"
[arithmetischen Operator]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetische Operatoren"
[arange]: <https://numpy.org/doc/stable/reference/generated/numpy.arange.html> "arange"
[linspace]: <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html> "linspace"
[matplotlib]: https://matplotlib.org/stable/tutorials/index.html "matplotlib"
[figure]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html> "figure"
[plot]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html> "plot"
[xlim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html> "xlim"
[ylim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html> "ylim"
[xlabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html> "xlabel"
[ylabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html> "ylabel"
[title]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html> "title"
[show]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html "show"

# Einfacher Plot von Vektoren - P1

## Einleitung

In dieser Aufgabe wird vorgestellt, wie Plots in Python erzeugt werden können.
Es sollte Ihnen außerdem klar werden, wie mathematische Schreibweisen von
algebraischen Ausdrücken in der programmiertechnischen Umsetzung standardmäßig umgesetzt werden.

Ein paar Beispiele:

*  Indizes von Variablen, wie z.B. $y_{1}$ oder $x_{\text{end}}$
schreibt man häufig `y_1` oder `x_end`. Der Unterstrich `_` ist übrigens das einzige Sonderzeichen, das in Variablen- und Programmnamen vorkommen darf.

*  Der Absolutbetrag $\lvert x_{1} \rvert$ muss mit einem
(vorgegebenen) Programm berechnet werden. Hierzu wird [abs] verwendet.

*  In mathematischer Schreibweise muss der Multiplikationsoperator nicht unbedingt
geschrieben werden. Man kann also statt $x_{1} \cdot \lvert x_{1} \rvert$ auch einfach
$x_{1} \lvert x_{1} \rvert$ schreiben. In einer Programmiersprache wie Python muss man
natürlich zwischen Teilen von Formeln unbedingt Operatoren verwenden, und zwar in diesem Fall einen
[arithmetischen Operator], nämlich `*`.

* In der Mathematik wird Potenzieren durch hochgestellte Zeichen, wie z.B. $x^2$, symbolisiert.
In Python verwendet man zum Potenzieren von Skalaren den Operator `**`.

## Aufgabe

1. Erzeugen Sie im Python-Skript `basis2` (File: `basis2.py`)
folgende Variablen:

    |Variable| Wert  |
    |---|-------|
    |`x_start`| `-3`  |
    |`x_end`| `3`   |
    |`n`| `200` 

2. Erzeugen Sie den Zeilenvektor `x_1` mit Werten zwischen `x_start` und `x_end`
und einer Schrittweite von `Eins`. Verwenden Sie dafür [arange] (achten Sie auf die Intervalldefinition).

3. Rechnen Sie damit folgende Formel aus: $$y_{1} = x_{1} \lvert x_{1} \rvert$$

4. Erzeugen Sie mit [linspace] einen Vektor ```x_2```
   von `x_start` bis `x_end` mit `n` Werten.


5. Berechnen Sie damit 3 hyperbolische Funktionen in folgenden Variablen:

    |Variable|Wert|
    |---|---|
    |`ysinh`|$\sinh(x_2)$|
    |`ycosh`|$\cosh(x_2)$|
    |`ytanh`|$\tanh(x_2)$|

    Damit sollten Sie nun insgesamt 4 Zeilenvektoren der Länge `n` haben, die man zeichnen
    kann.

6. Um unsere Funktionen zu visualisieren, werden wir die [matplotlib] Bibliothek verwenden. Plotten Sie in einer [figure] die folgenden Größen in der vorgegebenen Reihenfolge:

    | Abszisse |Ordinate|Linienspezifikation|
    |----------|---|---|
    | `x_1`    |`y_1`|rot; durchgezogen; mit Marker `o`
    | `x_2`    |`ysinh`|schwarz; durchgezogen
    | `x_2`    |`ycosh`|blau; durchgezogen
    | `x_2`    |`ytanh`|grün; durchgezogen

     Dazu eignet sich der matplotlib-Befehl [plot]. In der dazugehörigen Dokumentation
    sind auch Linienarten spezifiziert.

7.  Setzen Sie die Achsenlimits mit den Befehlen [xlim] und [ylim] auf
    folgende Werte:

    |Achse|Minimum|      Maximum      |
    |---|:---:|:-----------------:|
    |`x`-Achse|`x_start`|      `x_end`      |
    |`y`-Achse|$-\max(\sinh(x_2))$| $+\max(\sinh(x_2))$ |

    Wenn man öfter die gleiche Berechnung benötigt, ist es viel besser, die
    benötigte Größe in einer Variablen zu speichern und diese dann zu verwenden. Anstatt das Minimum und Maximum für [ylim] extra einzugeben, überlegen Sie sich wie Sie dazu eine Varaible `y_max` verwenden können.

8.  Erzeugen Sie Beschriftungen der Achsen (Labels) und einen Achsen-Titel in folgender Form:

    |Befehl|Text|
    |---|---|
    |[xlabel]|`x`|
    |[ylabel]|`y(x)`|
    |[title]|`Hyperbolic Functions`|

    Um die Grafik anzuzeigen, ist nach den [plot]-Befehlen noch der [show]-Befehl notwendig.

9. Überlegen Sie sich, warum die rote Kurve (die mit `x_1` erzeugt wurde)
viel eckiger aussieht als die anderen Kurven


## Hinweise

* In Python sind Intervalle rechtsoffen, d.h. bei [arange] und ähnlichen Funktionen
sind die Endpunkte im erzeugten Array nicht inbegriffen. Überlegen Sie sich, wie sie
den Endpunkt in Unterpunkt 2 trotzdem inkludieren können.

* Im Testbetrieb ist es unbedingt notwendig, dass die Kurven in der angegebenen Reihenfolge
    gezeichnet werden. Hier also unbedingt in der Reihenfolge Sinus Hyperbolicus, Cosinus Hyperbolicus und Tangens Hyperbolicus.

* Wenn Sie statt `plt.title('Ihr Titel')` in Ihrem Programm
    `plt.title = 'Ihr Titel'` schreiben und dieses Programm ausführen, dann
    bekommt die Grafik keinen Titel, sondern Sie ändern die Variable `plt.title`.
    Ab diesem Zeitpunkt ist die Verwendung des matplotlib-Befehls [title] nicht
    möglich, da Ihre Definition Vorrang hat. Lösen kann man das Problem nur mit Klick
    auf _Restart_ im _Interactive Window_.


## Keywords

- Matplotlib
- Plotten