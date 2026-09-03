[python strings]: https://docs.python.org/3/library/stdtypes.html#textseq "python strings"


# Zeichenketten

## Einleitung

In diesem Beispiel erhalten Sie eine Einführung in den Umgang mit Zeichenketten in Python. Fortgeschrittene Manipulationen werden in einer späteren Woche wieder aufgegriffen.

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
Da `strings` eine Abfolge von Zeichenketten darstellen, kann man durch Indizierung auf einzelne Zeichen zugreifen. Beachten Sie
hierbei, dass in Python die Indizes immer bei `0` beginnen. Weitere Informationen zum Arbeiten mit Zeichenketten und zur Indizierung finden Sie in den Hinweisen.
 
## Aufgabe

1. Weisen Sie im Skript `strings.py` den nachfolgenden Variablen die entsprechenden Werte zu:

    |Variable|Wert|
    |:-|:-|
    |`s_1`| `graz`|
    |`s_2`| `is`|
    |`s_3`| `a`|
    |`s_4`| `great`|
    |`s_5`| `city!`|

2. Wandeln Sie die Variablen `s_1` und `s_5` in `S_1` und `S_5` um wobei der erste Buchstabe nun ein Großbuchstabe sein soll.

3. Setzen Sie nun aus den Variablen `S_1`,`s_2`,`s_3`,`s_4`,`S_5` die Variable `s` zusammen und fügen Sie zwischen den Worten Leerzeichen ein.

4. Wandeln Sie anschließend den gesamten Satz in Großbuchstaben um und speichern Sie diesen in die Variable `S`.

## Hinweise

* Weitere Informationen, wie man Großbuchstaben in Kleinbuchstaben umwandelt und umgekehrt finden Sie unter [python strings].

* Für die Indizierung verwenden wir die eckigen Klammern `[]` und den Index des Zeichens, auf das wir zugreifen möchten. Zum Beispiel, wenn wir eine Zeichenkette `s = "Hello"` haben, können wir auf das erste Zeichen mit `s[0]` zugreifen, was `'H'` zurückgibt. Um den Rest der Zeichenkette zu erhalten, können wir Slicing verwenden, z.B. `s[1:]` gibt `'ello'` zurück.

* Für diese Aufgabe gibt es mehrere Lösungswegen und Funktionen, welche zum korrekten Endergebnis führen. Probieren Sie ruhig verschiedene aus!


## Keywords

- Zeichenketten