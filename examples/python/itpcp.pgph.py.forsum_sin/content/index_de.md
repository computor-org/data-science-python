[for]: <https://docs.python.org/3/tutorial/controlflow.html#for-statements> "for"

# Taylorreihe des Sinus

## Einleitung

In dieser Aufgabe lernen wir, wie man mithilfe von for-Schleifen eine Summe über eine mathematische Reihe berechnet und grafisch darstellt. Konkret betrachten wir die Taylorreihe des Sinus und bauen sie Schritt für Schritt auf, um zu sehen, wie sich die Approximation des Sinus entwickelt, wenn wir immer mehr Terme der Reihe hinzufügen.

## Aufgabe

Erzeuge ein Python-Skript `for_sum_sin`, das folgende Aufgaben
erfüllt:

1. Erzeuge einen Vektor $x$ mit $100$ Punkten zwischen $-\pi$ und $\pi$
    und einen gleich großen Vektor $y$ mit lauter Nullen.

2. Erzeuge eine Figure und plotte $y(x)$.

3. Addiere nun in einer [for]-Schleife von $n=0$ bis $n=6$
    jeweils eine Teilsumme $s_n$ der Reihe für den Sinus
    $$ s_n(x) = (-1)^n \frac{x^{2n+1}}{(2n+1)!} $$
    zum vorherigen Wert von $y$ und plotte in der gleichen Figure $y(x)$.

4. Nach der Schleife plottest du noch $\sin(x)$ in einer anderen Farbe.

## Hinweise

* Im Plot sollte man die Linie bei Null und
    $$
    \begin{aligned}
    S_0 & = s_0 \\
    S_1 & = s_0 + s_1 \\
    S_2 & = s_0 + s_1 + s_2 \\
        & \vdots
    \end{aligned}
    $$
    sehen. Schlussendlich nähert sich $S_n(x)$ dem Sinus an.

* Du wirst in einer späteren Übung andere Methoden kennenlernen, um Reihen
 zu berechnen. Hier soll nur verstanden werden, wie das mit Hilfe einer
 [for]-Schleife bewerkstelligt wird.
