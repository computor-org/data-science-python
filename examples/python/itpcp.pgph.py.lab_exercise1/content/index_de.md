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

1. Füge im File `data_lab1.dat` 3 weitere Datenpunkte hinzu:

    |Time|Temperatur
    |---|---|
    |19.5|10.1|
    |20|9.3|
    |21|8|

2. Lade die Daten des Files mittels [np.loadtxt] und speichere diese in die Variable `data`. Die Daten werden als Array gespeichert. Überprüfe die Dimension des Arrays mit dem Attribut `.shape`.

**<span style="color: red;">!!</span>** Achte auf die "Form" der Einträge in deinem Datenfile. Um mithilfe von `Numpy` weiterzurechnen, definiere beim Laden der Daten den Datentyp als `np.float64`. Sieh dir dazu den Hinweis an. 

3. Nutze deine neuen Kenntnisse über Indizierung und speichere die Zeitwerte in die Variable `t` und die Temperaturwerte in `T`.

4. Berechne den [Mittelwert] und die [Standardabweichung] (siehe Links) der Temperatur über den gesamten Messzeitraum. Speichere den Mittelwert unter `mean_T` und die Standardabweichung unter `std_T`. **Achtung**: Wenn kein exakter Mittelwert bekannt ist (dieser wird hier auch aus den Daten geschätzt), muss der Parameter `ddof` in `np.std` auf `1` gesetzt werden (ergibt *[unbiased] estimator*).

5. Plotte die Temperaturwerte gegen die Zeit.

6. Beschrifte die Achsen mit `t / h` und `T / °C`.

7. Erstelle einen String, welchen du unter `title_str` speicherst und welcher folgenden Text enthalten soll:

   `Temperature Measurement: mean = "mean_T" °C, std = "std_T" °C`

   `"mean_T"` und `"std_T"` sollen dabei durch den jeweilig berechneten Wert mit 2 Nachkommastellen ersetzt werden. Du musst dafür einen sogenannten f-string erzeugen (siehe [fstrings]).

8. Beschrifte den Plot mit dem `title_str` als Titel.

## Hinweise

* Beim Laden von Daten muss auf den Datentyp im File, sowie die Markierung der Abtrennung geachtet werden. Hier laden wir eine Textdatei. Tun wir dies 'einfach so', wird Python zunächst den Datentyp als `string` interpretieren. Für weitere Berechnungen mit NumPy sollte der Datentyp jedoch `np.float64` sein. Füge dazu `dtype=np.float64` innerhalb `np.loadtxt()` ein.

* Für den Test darf beim Laden der Daten mithilfe von `np.loadtxt()` nur der Name der Datei eingegeben werden, zB `np.loadtxt('Daten.dat', dtype=np.float64, comments="%")`. Wird stattdessen ein relativer Pfad eingefügt, kann dies der Test nicht überprüfen.

* Um den Code lokal (ohne das Testsystem) zu testen, muss sich das Terminal im gleichen Ordner wie das Python-Skript befinden. Falls nicht, klicke mit der rechten Maustaste auf die Übung `Lab Exercise1`, wähle „Als Pfad kopieren“ und füge diesen in dein Terminal als `cd <path/to/folder>` ein. Anschließend kannst du das Skript ausführen, indem du auf die Schaltfläche „Ausführen“ klickst oder `python lab_exercise1.py` in dein Terminal eingibst. Wenn du aufgefordert wirst, "*Bilder und Texte aus der Zwischenablage abrufen*", klicke auf "*Erlauben*".

* In der ersten Zeile in `data_lab1.dat` findest du als Kommentar (`%`) die Beschreibung der Spalten. Beim Importieren der Daten treten Schwierigkeiten auf, diese Beschreibung genauso als float zu interpretieren wie die folgenden Datenpunkte. 
Um die Kommentare im Datenfile beim Laden als solche kennzuzeichnen, füge `comments="%"` innerhalb `np.loadtxt()` ein.

* Beim Titel muss zur automatischen Überprüfbarkeit auf die Leerzeichen geachtet werden!

* Der hier gesuchte Mittelwert ist ungewichtet, die Zeitpunkte der Messung gehen nicht in seine Berechnung mit ein.


## Keywords

- Datenauswertung
- Mittelwert
- Standardabweichung