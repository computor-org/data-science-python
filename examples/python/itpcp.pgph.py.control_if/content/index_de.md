[all]: <https://numpy.org/doc/stable/reference/generated/numpy.all.html> "all"
[any]: <https://numpy.org/doc/stable/reference/generated/numpy.any.html> "any"
[if]: <https://docs.python.org/3/tutorial/controlflow.html#if-statements>
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> "np.ravel"

# Steuerstrukturen: if-Entscheidung

## Einleitung

Die folgenden Beispiele sollen dich mit den Steuerstrukturen, insbesondere mit der `if-Abfrage` in Python vertraut machen. Mit `if-Abfragen` werden logische Bedingungen im Skript überprüft. Sind diese im Bool'schen Sinne wahr (`True`), dann wird der darunter intendierte Code ausgeführt, ansonsten wird er bei der Execution ignoriert.

Du solltest bereits in der Vorlesung mit dem Konzept von Steuerstrukturen in Berührung gekommen sein. Die folgenden Python-Files sollen dir zeigen, in welchem Kontext `if-Statements` eingesetzt werden können.

* `if_test1`: Einfaches [if], verschiedene Schreibweisen.
* `if_test2`: In Kombination mit logischen Operatoren.
* `if_test3`: Geschachteltes [if].
* `if_test4`: Keine Matrizen in Bedingungen, [all], [any].
* `if_test5`: Reihenfolge der Bedingungen ist wichtig, da immer nur
  der Zweig mit der ersten richtigen Bedingung ausgeführt wird.
* `if_test6`: Noch ein if mit [all] und [any]. Füge
  die zusätzliche Zeile aus dem Kommentar an der richtigen Position ein.

Nun sollst du dein eigenes Skript unter der Verwendung von `if-Statements` verfassen.

## Aufgabe

Schreib eine Funktion `if_test`, die mit dem Aufruf

```python
r = if_test(z)
```

für ein **beliebiges** numerisches Feld `z` eine der folgenden
Zeichenketten als Ergebnis in `r` zurückgibt:

1. `none` wenn kein Wert in `z` größer als Null ist;

2. `any` wenn zumindest irgendein Wert in `z` größer als Null ist;

3. `two` wenn genau zwei Werte in `z` größer als Null sind;

4. `all` wenn alle Werte in `z` größer als Null sind.

Falls du zum gegenwärtigen Zeitpunkt nicht weißt, <span style="color: red;">wie man eine eigene
Funktion selbst testet,</span> dann lies alle Hinweise!

## Hinweise

* `if` muss genau einmal,
    `elif` muss genau zweimal,
    `else` kann, muss aber nicht vorkommen. (Überleg dir, wieso!)

* Vergiss nicht, dass `z` ein **beliebig dimensionales** Array sein kann.
    (Dies gilt im Speziellen auch für 3d-Arrays!) Hierbei kann der Befehl [np.ravel] hilfreich sein.

* Eine Funktion soll man selbst in der Konsole aufrufen und auf
  Fehler überprüfen. Dafür geht man wie folgt vor:

  * Definiere dir eine Matrix (hier M) beispielsweise durch

    ```python
    M = np.arange(1, 13).reshape(3, 4)       # alle größer Null
    M = np.arange(1, 13).reshape(3, 4) - 12  # keines größer Null
    M = np.arange(1, 13).reshape(3, 4) - 5   # irgendeine Anzahl größer Null
    M = np.arange(1, 13).reshape(3, 4) - 10  # genau zwei größer Null
    ```

  * Ruf mit dieser Matrix die Funktion auf:

    ```python
    r = if_test(M)
    ```

    Dies ist ein Vorschlag. Besser ist es natürlich, du denkst selber über
    Testmöglichkeiten nach.