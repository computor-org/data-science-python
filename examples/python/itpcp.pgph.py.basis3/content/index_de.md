[NumPy]: <https://numpy.org/doc/stable/>
[Matplotlib]: <https://matplotlib.org/stable/api/index.html>
[Matplotlib-Userguide]: <https://matplotlib.org/stable/users/index.html>
[legend]: <https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html>
[xlim]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html>
[xlabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html>
[ylabel]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html>

# Kombination von Funktionen

## Einleitung

Die Übung beschäftigt sich mit der Berechnung und dem Plotten
von einfachen Funktionen.

### Kommentare

Es ist empfehlenswert sich anzugewöhnen, den Code zu kommentieren, um in Zukunft mit einem Blick sofort zu wissen, was in diesem Teil des Programms passiert (und vor allem warum).
    Eine gute Methode ist, bevor man mit dem Programmieren beginnt, den Programmablauf zu planen und als Kommentare hinzuschreiben, also zum Beispiel:

        # Define the parameters

        # Define the functions

        # Compute the function values

        # Plot the results

    Nun lässt man die Kommentare einfach stehen, und schreibt unter die jeweiligen Zeilen den entsprechenden Code. Es mag hier trivial erscheinen, aber üben Sie das auch schon in einfachen Beispielen!


## Aufgabe

Erzeugen Sie im Skript `basis3` (File: `basis3.py`)
ein Programm, das die Funktionen berechnet und graphisch darstellt.

1. Erzeugen sie mit den Formeln
    $$
    \begin{aligned}
    x_a  &= -2 \pi \\
    x_e  &= +2 \pi \\
    x_n  &= 180
    \end{aligned}
    $$
    die Variablen `x_a`, `x_e` und `x_n`.

2. Erzeugen Sie einen Vektor `x` mit `x_n` äquidistanten Werten zwischen
    obigem Anfangs- und Endpunkt (`linspace`).

3. Berechnen Sie damit die Funktionen (Namen: `f1`, `f2` und `f3`)
    $$
    \begin{aligned}
    f_1  &= \frac{x}{2\pi} \; \sin(x) \\
    f_2  &= \frac{x^2}{(2\pi)^2} \; \sin^2(x) \\
    f_3  &= \frac{x^3}{(2\pi)^3} \; \sin^3(x)  .
    \end{aligned}
    $$

4. Plotten Sie in einer Figure die Funktionen $f_1(x)$
    (rot), $f_2(x)$ (blau) und $f_3(x)$ (grün). Die genau [RGB](https://matplotlib.org/stable/users/explain/colors/colors.html)-Spezifizierung
    ist `rot=(1.0, 0.0, 0.0, 1)`, `blau=(0.0, 0.0, 1.0, 1)` und `grün=(0.0, 1.0, 0.0, 1)`.

5. Versehen Sie die Zeichnung mit einer Beschriftung ([xlabel], [ylabel])
    der x-Achse (`x`) und der y-Achse (`f(x)`).

6. Stellen Sie die Limits der x-Achse auf die Werte von $x_a$ und $x_e$ ein
    ([xlim]).

7. Außerdem soll es eine Legende ([legend]) geben, wobei
    die Bezeichnungen der Linien in der Legende `f1(x)`, `f2(x)` und
    `f3(x)` sein sollen.
    Stellen Sie sicher, dass die Legende *explizit* gestetzt wird. Die Legende
    soll unten in der Mitte innerhalb des Plots platziert werden.

## Hinweise

* Nutzen Sie die [NumPy]- und [Matplotlib]-Dokumentationen sowie den [Matplotlib-Userguide], um die richtige Verwendung der notwendigen Befehle herauszufinden!

* Hinweise zur Positionierung der Legende finden Sie unter dem entsprechenden `loc`-Stichwort (siehe [legend]).
