[np.loadtxt]: <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html> "np.loadtxt"
[Mittelwert]: <https://numpy.org/doc/stable/reference/generated/numpy.mean.html> "np.mean"
[Standardabweichung]: <https://numpy.org/doc/stable/reference/generated/numpy.std.html> "np.std"
[fstrings]: <https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings> "fstrings"
[unbiased]: <https://en.wikipedia.org/wiki/Bias_of_an_estimator#Sample_variance>

# Laborübung 1

## Einleitung

Diese Aufgabe hat es zum Ziel zu zeigen, wie Python in Laborübungen verwendet werden kann. Dafür sollen Temperaturdaten
aus einem File eingelesen und als Plot ausgegeben werden.

Im Datenfile `data_lab1.dat` sind Temperaturdaten gegen ihren Messzeitpunkt in Stunden
abgespeichert. Die erste Spalte enthält den Zeitpunkt der Messung, die zweite die Temperaturwerte.

## Aufgabe

1. Fügen Sie im File `data_lab1.dat` 3 weitere Datenpunkte hinzu:

    |Time|Temperatur
    |---|---|
    |19.5|10.1|
    |20|9.3|
    |21|8|

2. Laden Sie die Daten des Files mittels [np.loadtxt] und speichern Sie diese in die Variable `data`. Die Daten werden als Array gespeichert. Überprüfen Sie die Dimension des Arrays mit dem Attribut `.shape`.

**!** Achten Sie auf die "Form" der Einträge in Ihrem Datenfile. Um mithilfe `Numpy` weiterzurechnen, definieren Sie beim Laden der Daten den Datentyp als `np.float64`. Sehen Sie dazu den Hinweis. 

3. Nutzen Sie Ihre neuen Kenntnisse über Indizierung und speichern Sie die Zeitwerte in die Variable `t` und die Temperaturwerte in `T`.

4. Berechnen Sie den [Mittelwert] und die [Standardabweichung] (siehe Links) der Temperatur über den gesamten Messzeitraum. Speichern Sie den Mittelwert unter `mean_T` und die Standardabweichung unter `std_T`. **Achtung**: Wenn kein exakter Mittelwert bekannt ist (dieser wird hier auch aus den Daten geschätzt), muss der Parameter `ddof` in `np.std` auf `1` gesetzt werden (ergibt *[unbiased] estimator*).

5. Plotten Sie die Temperaturwerte gegen die Zeit.

6. Beschriften Sie die Achsen mit `t / h` und `T / °C`.

7. Erstellen Sie einen String, welchen Sie unter `title_str` speichern und welcher folgenden Text enthalten soll:

   `Temperature Measurement: mean = "mean_T" °C, std = "std_T" °C`

   `"mean_T"` und `"std_T"` sollen dabei durch den jeweilig berechneten Wert mit 2 Nachkommastellen ersetzt werden. Sie müssen dafür einen sogenannten f-string erzeugen (siehe [fstrings]).

8. Beschriften Sie den Plot mit dem `title_str` als Titel.

## Hinweise

* Beim Laden von Daten muss auf den Datentyp im File, sowie die Markierung der Abtrennung geachtet werden. Hier laden wir eine Textdatei. Tun wir dies 'einfach so' wird Python zunächst den Datentyp als `string` interpretieren. Für weitere Berechnungen mit NumPy sollte der Datentyp jedoch `np.float64` sein. Fügen Sie dazu `dtype=np.float64` innerhalb `np.loadtxt()` ein.

* Für den Test darf beim Laden der Daten mitilfe von `np.loadtxt()` nur der Name der Datei eingegeben werden, zB `np.loadtxt('Daten.dat', dtype=np.float64, comments="%")`. Wird stattdessen ein relativer Pfad eingefügt kann dies der Test nicht überprüfen.

* Um den Code lokal (ohne das Testsystem) zu testen, muss sich das Terminal im gleichen Ordner wie das Python-Skript befinden. Falls nicht, klicken Sie mit der rechten Maustaste auf die Datei `lab_exercise1.py`, wählen Sie „Als Pfad kopieren“ und fügen Sie diesen in Ihr Terminal als `cd <path/to/folder>` ein. Anschließend können Sie das Skript ausführen, indem Sie auf die Schaltfläche „Ausführen“ klicken oder `python lab_exercise1.py` in Ihr Terminal eingeben.

* In der ersten Zeile in `data_lab1.dat` finden Sie als Kommentar (`%`) die Beschreibung der Spalten. Beim Importieren der Daten treten Schwierigkeiten auf, diese Beschreibung genauso als float zu interpretieren wie die folgenden Datenpunkte. 
Um die Kommentare im Datenfile beim Laden als solche kennzuzeichnen, fügen Sie `comments="%"` innerhalb `np.loadtxt()` ein.

* Beim Titel muss zur automatischen Überprüfbarkeit auf die Leerzeichen geachtet werden!

* Der hier gesuchte Mittelwert ist ungewichtet, die Zeitpunkte der Messung gehen nicht in seine Berechnung mit ein.