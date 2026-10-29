[python strings]: https://docs.python.org/3/library/stdtypes.html#textseq "python strings"


# Zeichenketten

## Einleitung

In diesem Beispiel erhältst du eine Einführung in den Umgang mit Zeichenketten in Python. Fortgeschrittene Manipulationen werden in einer späteren Woche wieder aufgegriffen.

### Zeichenketten

Zeichenketten werden als sogenannte `strings` gespeichert und sind grundlegende Datentypen in allen gängigen höheren Programmiersprachen. Ein `string` besteht im Allgemeinen
aus einer Abfolge von Zeichen, die durch eine festgelegte Zeichenkodierung (meistens UTF-8) in Binärsprache umgewandelt werden. 
Damit können Text-Dateien importiert, dargestellt und manipuliert werden. 

Ein `string` kann sowohl durch doppelte (`"`) als auch einfache (`'`) Anführungszeichen erzeugt werden. Die Variablenzuweisung erfolgt 
wie bei allen anderen Datentypen, etwa

```python
a = 'Hello World'
print(a)

Hello World
```
 
In Python ist der `string` ein sog. `immutable` (unveränderbarer) Datentyp. Das bedeutet, dass ein einmal einer Variablen 
zugewiesener `string` nicht mehr verändert werden kann und man ggf. eine neue Variable erzeugen muss.

Die Manipulation von `strings` erfolgt intuitiv mit den üblichen mathematischen Operationen, etwa

```python
s1 = 'bra'
s2 = 'ket'
print(s1 + 'c' + s2)

bracket
```
Da `strings` eine Abfolge von Zeichen darstellen, kann man durch Indizierung auf einzelne Zeichen zugreifen. Beachte
hierbei, dass in Python die Indizes immer bei `0` beginnen. Weitere Informationen zum Arbeiten mit Zeichenketten und zur Indizierung findest du in den Hinweisen.
 
## Aufgabe

1. Weise im Skript `strings.py` den nachfolgenden Variablen die entsprechenden Werte zu:

    |Variable|Wert|
    |:-|:-|
    |`s_1`| `graz`|
    |`s_2`| `is`|
    |`s_3`| `a`|
    |`s_4`| `great`|
    |`s_5`| `city!`|

2. Wandle die Variablen `s_1` und `s_5` in `S_1` und `S_5` um, wobei der erste Buchstabe nun ein Großbuchstabe sein soll.

3. Setze nun aus den Variablen `S_1`,`s_2`,`s_3`,`s_4`,`S_5` die Variable `s` zusammen und füge zwischen den Worten Leerzeichen ein.

4. Wandle anschließend den gesamten Satz in Großbuchstaben um und speichere ihn in der Variable `S`.

## Hinweise

* Weitere Informationen, wie man Großbuchstaben in Kleinbuchstaben umwandelt und umgekehrt, findest du unter [python strings].

* Für die Indizierung verwenden wir die eckigen Klammern `[]` und den Index des Zeichens, auf das wir zugreifen möchten. Zum Beispiel, wenn wir eine Zeichenkette `s = "Hello"` haben, können wir auf das erste Zeichen mit `s[0]` zugreifen, was `'H'` zurückgibt. Um den Rest der Zeichenkette zu erhalten, können wir Slicing verwenden, z.B. `s[1:]` gibt `'ello'` zurück.

* Für diese Aufgabe gibt es mehrere Lösungswege und Funktionen, welche zum korrekten Endergebnis führen. Probier ruhig verschiedene aus!


## Keywords

- Zeichenketten