[enumerate]: <https://docs.python.org/3/library/functions.html#enumerate> "enumerate"
[hier]: <https://realpython.com/python-f-strings/#doing-string-interpolation-with-f-strings-in-python> "f-strings"

# Steuerstrukturen: for-Schleifen

## Einleitung
In dieser Woche erhalten Sie eine Einführung in die `for-` und `while`-Steuerstrukturen in Python. Sogenannte Schleifen (*loops*) zählen in allen gängigen Programmiersprachen zu den wichtigsten Bestandteilen des Source Codes. 
Sie dienen allgemein dazu, über Einträge in Listen, Tuples und Arrays zu iterieren und mit diesen dann zu arbeiten. Für den richtigen Umgang ist dementsprechend ein grundlegendes Verständnis von Python Arrays und deren Indizierung notwendig.

In dieser Aufgabe werden Sie ein Programm mit einem sogenannten `for-loop` schreiben. Die Syntax in Python sieht dabei etwa so aus:

```python
for entry in mylist:
    do something with entry
```
Dabei ist es ganz wichtig, dass die Zeilen, die während des `loops` ausgeführt werden sollen, eingerückt sind.

Man kann auch über die Indizes eines Arrays oder einer Liste iterieren. Dafür kann man etwa den Befehl [enumerate] verwenden. Hier ein Beispiel:

```python
for index, entry in mylist:
    otherlist[index] = entry + 1
```

Die beigefügten py-files sollen Ihnen wieder als Beispiel dienen, wie man *for-loops* einsetzen kann.

## Aufgabe
In dieser Aufgabe sollen Sie das File "climate_data_graz.csv" einlesen, das die mittleren Monatstemperaturen der Jahre 2013 und 2023 in Graz (Standort Universität) enthält. Außerdem enthält es noch die langjährigen Monatsmittel, die aus dem Durchschnitt der Jahre 1981-2010 errechnet werden.
Die erste Spalte enthält dabei die Monatsmittel des Jahres 2013, die zweite Spalte die Monatsmittel von 2023 und die dritte Spalte die langjährigen Mittel.

1. Lesen Sie das File mithilfe von `np.loadtxt` ein und nennen Sie es `temp_file`. Achten Sie darauf, dass Sie die Überschriften (erste Zeilen) dabei nicht mit einlesen.
2. Deklarieren Sie die 2 Variablen  `count_2013` und `count_2023` und weisen Sie ihnen den Wert 0 zu.
3. Iterieren Sie nun mit einem for-loop über die Zeilen von `temp_file` und prüfen Sie Folgendes (mit einer if-Abfrage) ab:
   * Wenn das Monatsmittel von 2013 um 2 oder mehr Grad vom langjährigen Mittel abweicht, erhöhen Sie den Wert `count_2013` um eins.
   * Für die Monatsmittel von 2023 gehen Sie analog vor.
4. Am Schluss geben Sie einen f-string aus, der den folgenden Text enthält:
```python
f"Number of strongly deviating monthly averages in 2013: {count_2013}"
f"Number of strongly deviating monthly averages in 2023: {count_2023}"
```
Weitere Hinweise zur Verwendung von f-strings finden Sie [hier].

## Hinweise
* Beachten Sie, dass eine Abweichung +-2 kleiner oder größer als der Monatswert sein kann.
* Achten Sie auf die richtige Indizierung für die Einträge innerhalb der Zeile.
* Quelle: <https://www.landesentwicklung.steiermark.at/>