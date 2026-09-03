# Summen und Schleifen

## Einleitung

Der Sinn dieser Aufagbe ist es, zu verstehen, wie man den praktischen Befehl [np.sum]
mit [for]-Schleifen realisieren müsste. Beim weiteren Programmieren mit Python verwendet
man dafür natürlich immer [np.sum] und keine Schleife.

Erzeugen Sie zu Testzwecken eine Matrix `M` mit 4 Zeilen und 6 Spalten. Die Einträge der
Matrix sollen von 1 bis 24 entlang der Spalten laufen:

$$
\begin{pmatrix}
  1 & 5 & \dots & 21 \\
  2 & 6 & \dots & 22 \\
  \vdots & \vdots & & \vdots \\
  4 & 8 & \dots & 24
\end{pmatrix}
$$

Diese Matrix kann mit [np.arange] und [ndarray.reshape] und anschließendem Transponieren
erzeugt werden.

## Aufgabe

Erzeugen Sie ein Python-Skript `forsum`, das folgende Aufgaben erfüllt:

1. Berechnen Sie mit Hilfe des Befehls [np.sum] die Summe über alle Zeilen und speichern
   Sie diese in die Variable `sum_s1`. Mit *Summation über alle Zeilen* ist gemeint,
   dass man alle Zeilen addiert:

   ```
        Zeile 1 + Zeile 2 + Zeile 3 + ... (punktweise)
   ```

1. Berechnen Sie analog die Summe über alle Spalten und speichern Sie das Ergebnis in
   `sum_s2`. *Summation über alle Spalten* entspricht

   ```
        Spalte 1 + Spalte 2 + Spalte 3 + ... (punktweise)
   ```

1. Berechnen Sie mit [np.sum] die Summe über alle Werte des Arrays und speichern Sie
   diese in `sum_st`.

1. Bestimmen Sie die Anzahl der Zeilen (`nz`), der Spalten (`ns`) und der Elemente
   (`nn`) von `M` und speichern Sie diese in die angegebenen Variablen ([np.shape],
   [np.size]).

1. Führen Sie die Summationen über alle Zeilen (`sum_f1`), alle Spalten (`sum_f2`)
   und alle Elemente (`sum_ft`) nun in drei unterschiedlichen [for]-Schleifen durch.
   Speichern Sie diese Ergebnisse in die angegebenen Variablen. Verwenden Sie als
   Schleifenindex die Variablen `i_z`, `i_s` bzw. `i_n`.

1. **Beachten Sie die Hinweise**

1. Überlegt euch welche Dimensionen ihr euch bei diesen Operatorionen erwarten würdet
   und schaut mittels dem `shape` member von den numpy Arrays ihre eigentliche Dimension
   nach. Was fällt euch auf? Wieso dürfte das wohl so sein?

## Hinweise

- Der Zeilenindex ist der Index in die erste Dimension und der Spaltenindex ist der
  Index in die zweite Dimension.

- Braucht man eine bestimmte Zeile `z` oder Spalte `s` einer Matrix `M`, so erreicht man
  das mit `M[z,:]` bzw. `M[:,s]`.

- Bei der Summation mit [for] belegt man die entsprechende Summenvariable vorher mit
  Nullen [np.zeros] in der entsprechenden Größe und beginnt in der Schleife dann
  hinzuzufügen. Die Schleife selbst läuft dann über alle Zeilen oder Spalten oder
  Elemente. Bei Zeilen und Spalten verwendet man die Eigenschaft, dass die
  arithmetischen Operatoren auf ganze Vektoren (Matrizen) wirken.

- Für die Summation über alle Werte mit Hilfe von [for] braucht man auch nur eine
  einzelne Schleife, wenn man die Funktion [np.flat] verwendet.

[for]: https://docs.python.org/3/tutorial/controlflow.html "for"
[ndarray.reshape]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html "ndarray.reshape"
[np.arange]: https://numpy.org/doc/stable/reference/generated/numpy.arange.html "np.arange"
[np.flat]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html "np.flat"
[np.shape]: https://numpy.org/doc/stable/reference/generated/numpy.shape.html "np.shape"
[np.size]: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html "np.size"
[np.sum]: https://numpy.org/doc/stable/reference/generated/numpy.sum.html "np.sum"
[np.zeros]: https://numpy.org/doc/stable/reference/generated/numpy.zeros.html "np.zeros"
