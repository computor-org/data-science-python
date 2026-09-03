# Lineares Gleichungssystem, Kegelschnitte

## Einleitung

Ein [Kegelschnitt] ist eine Kurve, die entsteht, wenn man die Oberfläche eines
Doppelkegels mit einer Ebene schneidet. Dabei entsteht entweder eine Ellipse (2), wobei
ein Kreis eine Spezialform davon ist (1), eine Parabel (3) oder eine Hyperbel (4).

<div align="center">
<img src="mediaFiles/kegelschnitt.jpg" width="60%"/>
</div>

Geht die schneidende Fläche durch die Kegelspitze, so kann ein Punkt, eine Gerade oder
ein Geradepaar herauskommen.

<div align="center">
<img src="mediaFiles/kegelschnitt2dmittelpunkt.png" width="40%"/>
</div>

Allgmein kann man Kegelschnitte in der folgenden Form schreiben (verallgemeinerte
quadratische Form)

$$
   z(x,y) = s_1 x^2 + 2 s_2 x y + s_3 y^2 + s_4 x + s_5 y + s_6 \; .
$$

Bei bekannten Datenpunkten $x_d$ und $y_d$ kann man $z(x_d,y_d)=0$ als lineares
Gleichungssystem für $s_i$ auffassen $\mathbf{As}=\mathbf{b}$, also

$$
   s_1 x_d^2 + 2 s_2 x_d y_d + s_3 y_d^2 + s_4 x_d + s_5 y_d + s_6 = 0 \; .
$$

Da wir sechs Unbekannte $s_i$ haben, brauchen wir auch sechs Datenpaare. Überzeugen Sie
sich gegebenenfalls mit Stift und Papier, dass das equivalent in Matrixschreibweise
geschrieben werden kann:

$$
\begin{bmatrix}
x_1^2 & 2x_1y_1 & y_1^2 & x_1 & y_1 & 1 \\
x_2^2 & 2x_2y_2 & y_2^2 & x_2 & y_2 & 1 \\
x_3^2 & 2x_3y_3 & y_3^2 & x_3 & y_3 & 1 \\
x_4^2 & 2x_4y_4 & y_4^2 & x_4 & y_4 & 1 \\
x_5^2 & 2x_5y_5 & y_5^2 & x_5 & y_5 & 1 \\
x_6^2 & 2x_6y_6 & y_6^2 & x_6 & y_6 & 1 \\\end{bmatrix}  \,
\begin{bmatrix} s_1 \\ s_2 \\ s_3 \\ s_4 \\ s_5 \\ s_6 \end{bmatrix} \ =
\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}. \;
$$

In dieser Form ist es allerdings ein homogenes Gleichungssystem, das immer die triviale
Lösung $s_i=0$ hat. Man kann sich hier aber helfen indem man einen der Koeffizienten
$s_k=1$ setzt und den entsprechenden Term auf die rechte Seite bringt. Wählt man **zum
Beispiel** den dritten Term $s_3=1$, so lautet das inhomogene Gleichungssystem

$$
  s_1 x_d^2 + 2 s_2 x_d y_d + s_4 x_d + s_5 y_d + s_6 = -y_d^2 \; ,
$$

beziehungsweise

$$
\begin{bmatrix}
x_1^2 & 2x_1y_1 & x_1 & y_1 & 1 \\
x_2^2 & 2x_2y_2 & x_2 & y_2 & 1 \\
x_3^2 & 2x_3y_3 & x_3 & y_3 & 1 \\
x_4^2 & 2x_4y_4 & x_4 & y_4 & 1 \\
x_5^2 & 2x_5y_5 & x_5 & y_5 & 1 \\
\end{bmatrix}  \,
\begin{bmatrix} s_1 \\ s_2  \\ s_4 \\ s_5 \\ s_6 \end{bmatrix} \ =
\begin{bmatrix} -y_1^2 \\ -y_2^2 \\ -y_3^2 \\ -y_4^2 \\ -y_5^2 \end{bmatrix}. \;
$$

Weil wir nun nur noch fünf Unbekannte haben, brauchen wir nun auch nur noch fünf
Datenpaare $(x, y)$ um unser lineares Gleichungssystem $\mathbf{As}=\mathbf{b}$
vollständig zu definieren.

## Aufgabe

Schreiben Sie nun ein Skript `linalg_conic_sections` in dem Sie folgende Aufgaben lösen:

1. Erzeugen Sie zwei Vektoren `xd` und `yd` mit fünf gleichverteilten Zufallszahlen
   zwischen $-0.5$ und $0.5$ mittels [np.random.rand].

1. Erzeugen Sie mit Hilfe dieser Vektoren die Hilfsmatrix

$$
M = [x_d^2~,~2 x_d y_d~,~y_d^2~,~x_d~,~y_d~,~1],
$$

beziehungsweise in Matrixschreibweise

$$
\begin{bmatrix}
    x_1^2 & 2x_1y_1 & y_1^2 & x_1 & y_1 & 1 \\
    x_2^2 & 2x_2y_2 & y_2^2 & x_2 & y_2 & 1 \\
    x_3^2 & 2x_3y_3 & y_3^2 & x_3 & y_3 & 1 \\
    x_4^2 & 2x_4y_4 & y_4^2 & x_4 & y_4 & 1 \\
    x_5^2 & 2x_5y_5 & y_5^2 & x_5 & y_5 & 1 \\
\end{bmatrix}.
$$

3. Erzeugen Sie die ganzzahlige Zufallszahl `n` im Intervall [0, 5]. Diese Zahl stellt
   den Index jener Spalte dar, die auf die rechte Seite des Gleichungssystems gebracht
   werden soll.

1. Erzeugen Sie damit den logischen Vektor `L`, der an der Stelle `n` False ist und an
   allen anderen Stellen True ist.

1. Erzeugen Sie nun die Matrix `A` und den Inhomogenitätsvektor `b`. Verwenden Sie dafür
   Ihren logischen Vektor `L` bzw. seine Negation `~L`. Siehe Hinweise. Achten Sie auf
   die Vorzeichen!

1. Lösen Sie das entsprechende Gleichungssystem $\mathbf{As}=\mathbf{b}$. Achten Sie
   darauf, dass `s` an der Stelle `n` $1$ sein muss. Lösen sie also nur für `s[L]` und
   setzen Sie an die verbliebene Position die Eins. Damit ist das Problem gelöst und das
   Ergebnis muss noch visualisiert werden.

1. Erzeugen Sie dafür zwei Vektoren `x` und `y` mit `30` Punkten zwischen `-1` und `1`.
   Alle Kombinationen von `x`- und `y`-Werten (die man für einen 3 dimensionalen Plot
   benötigt) kann man mit dem Befehl [np.meshgrid] erzeugen und erhält damit die
   Matrizen `xx` und `yy`. Durch Auswertung der ersten Gleichung in der *Einführung*
   erhält man für diese Matrizen `zz(xx,yy)`.

1. Stellen Sie die Fläche `zz` [graphisch] in einem 3D-Plot dar, wobei die Farbe den
   Wert der Funktion repräsentiert (siehe Hinweise für Beispiele). Wählen Sie eine
   [colormap].

1. Zeichnen Sie die Datenpunkte als Punkte in diesen Plot ein. Dabei sollen die Punkte
   nicht durch Linien verbunden sein.

1. Zeichnen Sie den erhaltenen Kegelschnitt als Höhenschichtlinie ein. Dafür gibt es den
   matplotlib-Befehl [contour]. Wir suchen allerdings den Schnitt $z(x,y) = 0$. Setzen
   Sie daher `levels` auf die Zahl $0$.

## Hinweise

- `A` besteht aus allen Zeilen von `M`, allerdings nicht aus allen Spalten. Spalte `n`
  ist nicht in `A` enthalten. Nutzen sie dafür `L` bzw. `~L` als Spalten-Index. Analog
  dazu besteht der Vektor `b` nur aus der negativen `n`-ten Spalte von `M`.

<div align="center">
<img src="mediaFiles/ellipse.png" width="80%"/>
</div>

<div align="center">
<img src="mediaFiles/hyperbel.png" width="80%"/>
</div>

<div align="center">
<img src="mediaFiles/parabel.png" width="80%"/>
</div>

- Wenn Sie das Python-Skript nicht im Interactive-Mode, sondern im Terminal starten
  ("Run Python-File in VSCode), öffnet sich für den Plot ein Fenster indem Sie den 3D
  Plot mit dem Curser drehen können und die Perspektive ändern. (plt.show() nicht
  vergessen!)

- Setzen Sie bevor Sie das erste mal Zufallszahlen mit numpy generieren den Seed auf
  einen fixen Wert. Sie können den Wert ändern um verschiedene Pseudo-Zufallszahlen
  erhalten und damit unterschiedliche Kegelschnitte. Damit der Test funktioniert, müssen
  die den seed joch auf $3$ setzen.

```python
np.random.seed(3)
```

[colormap]: https://matplotlib.org/stable/tutorials/colors/colormaps.html "colormap"
[contour]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html "contour"
[graphisch]: https://matplotlib.org/stable/gallery/mplot3d/surface3d.html "graphisch"
[kegelschnitt]: https://de.wikipedia.org/wiki/Kegelschnitt "kegelschnitt"
[np.meshgrid]: https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html "np.meshgrid"
[np.random.rand]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html "np.random.rand"
