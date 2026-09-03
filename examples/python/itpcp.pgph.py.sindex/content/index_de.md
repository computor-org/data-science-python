[len]: <https://docs.python.org/3/library/functions.html#len> "len"
[np.nan]: <https://numpy.org/doc/stable/reference/constants.html> "np.nan"
[np.ndim]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html> "np.ndim"
[np.size]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html> "np.size"
[np.shape]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html> "np.shape"
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> "np.ravel"
[np.copy]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html> "np.copy"
[np.delete]: <https://numpy.org/doc/stable/reference/generated/numpy.delete.html> "np.delete"
[np.astype]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html> "np.astype"

# Index und Doppelpunkt

## Einleitung

In dieser Aufgabe geht es darum, den Umgang mit Indexierung und Slicing in Python zu vertiefen. Dabei werden wir lernen, wie man effizient auf Elemente, Vektoren und Matrizen innerhalb einer zweidimensionalen Datenstruktur zugreift und diese manipuliert.
Durch die Arbeit mit einer Matrix M und verschiedenen Operationen darauf, werden Funktionen wie `np.ravel`, `np.copy`, `np.delete` und `np.astype` vorgestellt und geübt.

### Indexierung

 Dies bezeichnet den Zugriff auf einzelne Elemente in einem Array oder einer Matrix. In Python beginnen Indizes bei 0. Bei zweidimensionalen Arrays steht der erste Index für die Zeile und der zweite für die Spalte. Beispiel: `M[1, 2]` greift auf das Element in der zweiten Zeile und dritten Spalte zu.

### Slicing 
Mithilfe von Slicing kann man Subarrays oder Teilmatrizen aus einer Matrix extrahieren. Zum Beispiel gibt `M[:, 2]` die gesamte dritte Spalte zurück, während `M[1:4, :]` die Zeilen 2 bis 4 ausgibt.

## Aufgabe

Schreiben Sie ein Python-Skript `sindex` (File: `sindex.py`), das für eine Matrix `M` folgende
Aufgaben erledigt. Lesen Sie zuerst
die Hinweise (siehe unten) durch:

1. Speichern Sie folgende Information in den angegebenen Variablen:

    Variable     | Aufgabe
    :------------|:------
    `M`     | (9 x 8)-Matrix mit allen ganzen Zahlen im Intervall [-36, 35] (aufsteigende Reihenfolge)
    `prop1` | Dimension von `M`
    `prop2` | „Länge“ von `M`
    `prop3` | Größe „Form" von `M`
    `prop4` | Anzahl der Elemente in `M`

2. Speichern Sie folgende Skalare aus `M`:

    Variable     | Aufgabe
    :------------|:------
    `n1` | zweite Zeile, erste Spalte
    `n2` | dritter Eintrag
    `n3` | letzter Eintrag
    `n4` | vorletzter Eintrag

3. Speichern Sie folgende Vektoren aus `M`:
  
    Variable     | Aufgabe
    :------------|:------
    `z1` | zweite bis vierte Position
    `z2` | erste bis letzte Position mit Schrittweite vier
    `z3` | zweite und vorletzte Position
    `z4` | dritte Zeile, alle Spalten
    `z5` | letzte bis erste Position, denken Sie an die Verwendung von `-1` als Schrittweite.
    `z6` | die erste, zweimal die zweite, dreimal die dritte Position

4. Speichern Sie folgende Vektoren aus `M`:
  
    Variable     | Aufgabe
    :------------|:------
    `s1` | alle Zeilen, dritte Spalte
    `s2` | erste bis vorletzte Zeile, vorletzte Spalte
    `s3` | letzte bis erste Zeile, zweite Spalte
    `s4` | alle Zeilen, mittlere Spalte (siehe Hinweis)

5. Speichern Sie folgende Matrizen aus `M`:
  
    Variable     | Aufgabe
    :------------|:------
    `m1` | zweite bis dritte Zeile, alle Spalten
    `m2` | erste bis letzte Zeile mit Schrittweite 2, alle Spalten
    `m3` | alle Zeilen, zweite bis vorletzte Spalte
    `m4` | erste bis letzte Zeile mit Schrittweite 3, erste bis letzte Spalte mit Schrittweite 2;
    `m5` | letzte bis erste Zeile, dritte bis zweite Spalte (zweite Spalte nicht inklusiv)
    `m6` | die drei mittleren Zeilen, die drei mittleren Spalten (siehe Hinweis)

6. Erzeugen Sie fünf Matrizen `M1`, `M2`, `M3`, `M4` und `M5` mit dem gleichen Inhalt wie `M` und
 ersetzen Sie Teile ihres Inhalts:
  
    Variable     | Aufgabe
    :------------|:------
    `M1` | erste bis letzte Position mit der Schrittweite 2, durch Wert [np.nan]
    `M2` | erste bis letzte Zeile mit der Schrittweite 2, alle Spalten, durch Wert [np.nan]
    `M3` | zweite bis vorletzte Zeile, vorletzte Spalte, durch Wert Null
    `M4` | die vier Ecken durch [np.nan]
    `M5` | schneiden Sie die zweite und vorletzte Zeile, bzw. die zweite und vorletzte Spalte aus ([np.delete])

## Hinweise

* Wichtige Befehle: [np.ndim], [len], [np.shape], [np.size], [np.ravel], [np.astype]

* Beachten Sie, dass in Python die Listen- und Array-Indices mit 0 beginnen!

* Verwendet man in einer zweidimensionalen Matrix zwei Indices, dann steht der erste für die Zeile und der zweite für die Spalte.

* Um das n-te Element einer Matrix zu erhalten (die Zahl an der n-ten Position) wandeln Sie die Matrix vorher in einen Vektor um ([np.ravel]).

* Definieren Sie sich einen Vektor der Matrixelemente, um später nur auf diese Zuzugreifen. 
 Z.B. `Avec = np.ravel(A)` um später `Avec[1]` anstatt `np.ravel(A)[1]`

* Bei einer geraden Anzahl von Spalten gibt es keine mittlere Spalte. Gemeint ist
 dann die nachfolgende Spalte, also z.B. $6/2=3$, bzw. $5/2=2.5\rightarrow 3$.
 D.h., die mittlere Spalte bei sechs
 Spalten soll die dritte sein und die mittlere von fünf Spalten soll auch die dritte sein. Hier kann *Integer-Division* hilfreich sein.

* Beachten Sie im Teil 6, dass [np.nan] als Float definiert ist, die Matrixeinträge von `M` aber Integers sind. Sie werden also den Datentyp der Matrix modifizieren müssen, um [np.nan] einsetzen zu können.

* Wenn Sie eine Kopie von einer Matrix bearbeiten wollen, verwenden Sie bei der Zuweisung [np.copy] bzw. `matrix_name.copy()`, ansonsten verändern Sie die ursprüngliche Matrix (Ausprobieren!). Befehle wie [np.delete] und [np.astype] erzeugen natürlich immer eine Kopie.
