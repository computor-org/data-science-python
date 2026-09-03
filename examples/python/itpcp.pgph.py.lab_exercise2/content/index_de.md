[np.loadtxt]: <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html> "np.loadtxt"
[np.mean]: <https://numpy.org/doc/stable/reference/generated/numpy.mean.html> "np.mean"
[matplotlib.pyplot]: <https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html> "matplotlib.pyplot"
[np.exp]: <https://numpy.org/doc/stable/reference/generated/numpy.exp.html> "np.exp"

# Laborübung 2

## Einleitung

In der folgenden Aufgabe sollen Sie die Messdaten einer Messung am Oszilloskop auslesen und graphisch darstellen. Aufgaben wie diese werden Ihnen später in Laborübungen häufig begegnen.

## Aufgabe

1. Lesen die Daten einer Messung am Oszilloskop aus dem File `oscillation.dat` mithilfe von [np.loadtxt] ein. Setzen Sie dabei den Datentyp auf `np.float64`. Die Daten sind folgendermaßen zu interpretieren:

   | Linke Spalte     | Rechte Spalte    |
   |------------------|------------------|
   | Zeit in Sekunden | Messsignal in mV |

2. Schauen Sie sich die Daten an, indem Sie sie mithilfe von [matplotlib.pyplot] plotten. Verwenden Sie für die Daten eine durchgezogene blaue Linie.

3. In den Daten scheint es einen Offset zu geben (Null-Auslenkung der Schwingung nicht auf der x-Achse). Kalibrieren Sie das Signal, sodass die Null-Auslenkung beim Plotten auf der x-Achse liegt (das heißt bei y = 0).

4. Es handelt sich offenbar um eine gedämpfte harmonische Schwingung, deren Amplitude von 1 exponentiell abfällt. Verwenden Sie  [np.exp], um die beiden einhüllenden exponentiellen Funktionen der Amplitude zu plotten. Verwenden Sie eine durchgezogene rote Linie und setzen Sie dabei die Dämpfungskonstante auf $\delta = 0.03$.

5. Beschriften Sie die x-Achse mit `Time (s)` und die y-Achse mit `Signal (mV)`. Geben Sie Ihrer Graphik den Titel `Damped harmonic oscillation`.


## Hinweise

* Vergessen Sie beim Laden der Daten nicht, auf den Datentyp (`np.float64`) und die Kommentare (`comments='%'`) zu achten!

* Um den Offset von den Daten abzuziehen, verwenden Sie [np.mean].

* Weitere Informationen zum Plotten von Daten finden Sie in der  [matplotlib.pyplot]-Dokumentation.

* Achtung! Achten Sie auf die Reihenfolge der Plots. Achten Sie darauf, die Einhüllende als zweites zu plotten! Die obere einhüllende Kurve der exponentiellen Abnahme muss zuerst geplottet werden, da der Test dies sonnst als Fehler erkennt.

* Am Ende sollte Ihr Plot so aussehen:

<div align="center">
<img src="mediaFiles/Lab_exercise2.png" alt="Test Image" width="50%" name="Schwingung"/>
</div>
