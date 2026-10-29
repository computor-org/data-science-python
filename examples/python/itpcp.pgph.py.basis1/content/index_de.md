[arithmetische Operatoren]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetische Operatoren"
[Gleitkommazahlen]: <https://docs.python.org/3/tutorial/floatingpoint.html> "Gleitkommazahlen"
[cos]: <https://numpy.org/doc/stable/reference/generated/numpy.cos.html> "cos"
[exp]: <https://numpy.org/doc/stable/reference/generated/numpy.exp.html> "exp"
[sin]: <https://numpy.org/doc/stable/reference/generated/numpy.sin.html> "sin"
[sqrt]: <https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html> "sqrt"
# Einfache Berechnungen

## Einleitung

In dieser Aufgabe werden arithmetische Operatoren (`+`, `-`, `*`, `/`) vorgestellt. Aus der Aufgabe `01_math_constants` werden die Exponentialfunktion `exp` und trigonometrische Funktionen wiederholt. 

Für das automatische Testen ist es unbedingt notwendig, dass du <span style="color: red;">genau diese Namen</span> für deine Variablen verwendest!
Probier dein Programm in der Konsole aus, bevor du es abgibst.

In den Hinweisen findest du weitere Erläuterungen zu den Operatoren und Funktionen. 


## Aufgabe

1. Erzeuge im Python-Skript `basis1` (File: `basis1.py`)
die Variablen `a` und `b` und gib ihnen die Werte
`5.4` und `1.2`.

2. Berechne nun folgende Größen, wobei links die Variablennamen stehen. Benutze dazu das Python-Modul `numpy`, wie in Aufgabe 01.

$$
\begin{aligned}
\texttt{sum\_ab} & = a + b \\
\texttt{diff}    & = a - b \\
\texttt{prod}    & = a\cdot b \\
\texttt{quot}    & = \frac{a}{b} \\
\texttt{power}     & = a^{b} \\
\texttt{root}  & = \sqrt{a} \\
\texttt{root3}   & = a^{1/3} \\
\texttt{expo}    & = \mathrm{e}^{-a} \\
\texttt{trig1}   & = \sin (a) \\
\texttt{trig2}   & = \sin(a+b) \\
\texttt{trig3}   & = \cos (\pi \cdot a)
\end{aligned}
$$

## Hinweise

* Python-Hilfe zu einzelnen Befehlen findest du unter [sqrt], [exp],
[sin], [cos]. Die Operatoren `+`, `-`, `*` und `/` bezeichnet man als [arithmetische Operatoren].
Das Python-Tutorial befasst sich darüber hinaus mit Einschränkungen bei der Verwendung von
[Gleitkommazahlen].

* Die Zahl $e$ als solche existiert in Python nicht. Sie muss mit Hilfe
der Funktion [exp] erzeugt werden.

* Variablennamen, die bereits von Python belegt sind (wie zum Beispiel ```sum```), sollten unbedingt vermieden werden, da diese Funktionen ansonsten nicht aufrufbar sind! 


## Keywords

- Arithmetische Operatoren
- NumPy-Funktionen