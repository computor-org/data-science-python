[join]: <https://docs.python.org/3/library/stdtypes.html#str.join> "join"
[len]: <https://docs.python.org/3/library/functions.html#len> "len"
[list]: <https://docs.python.org/3/library/stdtypes.html#typesseq> "list"
[split]: <https://docs.python.org/3/library/stdtypes.html#str.split> "split"
[str]: <https://docs.python.org/3/library/stdtypes.html#textseq> "str"
[string]: <https://docs.python.org/3/library/string.html> "string"
[type]: <https://docs.python.org/3/library/functions.html#type> "type"
[upper]: <https://docs.python.org/3/library/stdtypes.html#str.upper> "upper"

# Zeichen und Zeichenketten

## Einleitung

Neben Zahlen gibt es in jeder Programmiersprache natürlich auch einen Datentyp für
Zeichen (Characters). In Python ist das der Datentyp [str] (kurz für _String_).
Definiert werden Zeichen mit Hilfe des einfachen Hochkommas (`'`) am Anfang und am Ende.
Soll also die Variable `s` den Inhalt `a` haben, dann muss man `s = 'a'` schreiben.
Würde man hingegen `s = a` schreiben, dann würde die Variable `s` den Wert der Variablen `a`
haben, also resultiert z.B.

	a = 7
	s = a

im Wert `7` sowohl für `a` als auch für `s`.

Zeichenketten kann man als Vektor (Array) von Zeichen auffassen. Eine solche ist z.B.
`s = 'abc'` oder `s = '123'`. Im zweiten Fall sind es die Zeichen `123` und nicht die
Zahl $123$. Es ergibt also einen wichtigen Unterschied, ob man `s = '123'` oder `s = 123`
schreibt. Einzelne Zeichen oder Zeichenketten kann man mit Hilfe des Operators `+`
zu längeren Zeichenketten verbinden. Zeichenketten können wiederum in Listen gespeichert
werden, die ähnlich wie Arrays indiziert werden können. Im Gegensatz zu NumPy-Arrays
können Listen in Python aber Elemente mit beliebigen Datentypen beinhalten, also
insbesondere Zeichenketten mit unterschiedlicher Länge.

|Code|Resultat|
|---|---|
|`s = 'a' + 'b' +'c'`|`'abc'`|
|`s2 = s + s`|`'abcabc'`|
|`l = [s, s2]`|`['abc', 'abcabc']`|
|`l[0]`|`'abc'`|

Die korrekte aber umständliche Scheibweise `s = 'a' + 'b' + 'c'` ersetzt man
sinnvollerweise durch `s = 'abc'` mit dem gleichen Ergebnis.

Auf einzelne Zeichen in einer Zeichenkette kann man mit Hilfe eines Index zugreifen, `s2[3]`
und `l[1][3]` liefern das Zeichen `a`, also den vierten Buchstaben obiger Zeichenkette.

Will man auf mehrere Zeichen zugreifen, kann man die für [list] dokumentierte Doppelpunktnotation
verwenden, `s2[3:6]` ergibt dann `abc`. Das letzte Element kann auch ausgelassen werden,
also z.B. `s2[3:]`. Im Gegensatz zu „echten“ Arrays (und Listen) sind Zeichenketten in
Python aber nicht in Skalare (hier also einzelne Zeichen) zerlegbar: Tatsächlich liefert
`s2[3]` eine Zeichenkette der Länge 1; diese Schreibweise entspricht demnach `s2[3:4]`.

Ein weiterer Unterschied ist, dass Zeichenketten in Python unveränderbar sind. Sie können
also mit der Index-Notation eine bestehende Zeichenkette im Nachhinein nicht mehr modifizieren.

## Aufgabe

### Elementarer Umgang mit Zeichenketten

Führen Sie im Python-Skript `basis_char` einige einfache Definitionen von Variablen durch:

1. Weisen Sie folgenden Variablen die angegebenen Werte zu:

    |Variable|Wert|
    |---|---|
    |`s1`|`a`
    |`s2`|`b`
    |`c1`|`das`
    |`c2`|`ist`
    |`c3`|`eine`
    |`c4`|`wunderbare`
    |`c5`|`uebung`
    |`blank`|*ein Leerzeichen*
    |`exclaim`|*ein Rufzeichen*

    <span style="color: red;">Achtung:</span> Die letzten beiden Variablen-Werte sind so zu verstehen,dass die Variable `exclaim` bspw. nur das Zeichen *!* enthalten soll. Wenn Sie also in der
    Konsole `exclaim` eingeben soll die Ausgabe `'!'` lauten.

2. Erzeugen Sie nun die Variable `s3` durch Verbinden der Variablen `s1` und `s2`.

3. Erzeugen Sie aus den Variablen `c1` und `c5` die Variablen `C1` und `C5`, wobei jetzt der
    erste Buchstabe ein Großbuchstabe sein soll ([upper]). Verwenden Sie dabei
    wirklich die Variable `c1` und schreiben Sie nicht `C1='Das'`. `C1` wird also aus `c1`
    „zusammengestückelt“. Auf einzelne Zeichen in einer Zeichenkette kann man mit einem
    Index zugreifen (z.B.: `C1[0]` ist das erste Zeichen in `C1`).

4. Setzen Sie nun die Variable `sentence` aus `C1`, `c2`, `c3`, `c4` und `C5` zusammen, wobei
    zwischen den Worten ein Leerzeichen und am Ende des Satzes ein Rufzeichen stehen soll.
    (Verwenden Sie dazu die definierten Variablen.)

5. Ermitteln Sie mit Hilfe des Befehls [type] den Datentyp von Variablen:

    |Variable|Wert|
    |---|---|
    |`type_sentence`|Datentyp der Variable `sentence`|
    |`type_number`|Datentyp der Zahl `12`|

    Wenn Sie den Datentyp als Zeichenkette verwenden wollen, müssen sie auf diese Variablen
    z.B. mit `type_number.__name__` zugreifen.

6. Ermitteln Sie mit [len] die Anzahl der Zeichen in `sentence` und speichern Sie
    diese Information in der Variable `length_sentence`.

7. Erzeugen Sie folgende Variablen:

    |Variable|Wert|
    |---|---|
    |`all_upper`|Alle Großuchstaben von `A` bis `Z` in einer Zeichenkette|
    |`all_lower`|Alle Kleinbuchstaben von `a` bis `z` in einer Zeichenkette|
    |`all_both` |Obige Zeichenketten als zwei Elemente einer Liste|

    Sie können dafür die Konstanten im Modul [string] verwenden.

### Umgang mit Zeichenketten mithilfe von Listen

Hier noch ein kleines Beispiel zum Thema Teilen und
Zusammensetzen von Zeichenketten mit Hilfe der Befehle
[split], [join], [list]. Beachten Sie, dass `split` und `join` als **Methoden**
den Zeichenketten nachgestellt sind, also z.B. `s.join()` statt `join(s)`.

1. Speichern Sie in der Variablen `str1` die Zeichenkette:

    'abcdef'

2. Teilen Sie die Zeichenkette `str1` mit [list] in einzelne Zeichen und
   speichern Sie das Ergebnis in `list1`:

    ['a', 'b', 'c', 'd', 'e', 'f']

3.  Erzeugen Sie aus `list1` mit [join] folgende Zeichenkette in der
    Variablen `str2`:

    'a- -b- -c- -d- -e- -f'

4. Teilen Sie `str2` mit [split] beim Leerzeichen und speichern Sie das Ergebnis
   in `list2`.

    ['a-', '-b-', '-c-', '-d-', '-e-', '-f']

Die Variablen `list1` und `list2` sind Listen. Diese können ähnlich wie NumPy-Arrays
indiziert werden, aber auf jedem Platz beliebige Python-Konstrukte beinhalten, also
nicht nur eine Zahl oder einen Buchstaben, sondern ganze Arrays oder ganze
Zeichenketten.

Lässt sich Unterpunkt 2 auch mit [split] lösen? Probieren Sie aus, was Sie mit
`str1.split()` und `str1.split('')` erhalten.

## Hinweise

* Wenn man mehrere aufeinanderfolgende Zeichen aus einer Zeichenkette entnehmen will, also
    beispielsweise die ersten drei Einträge einer Zeichenkette `s`, so ist dies prinzipiell mit

    s[0] + s[1] + s[2]

    möglich. Die elegantere Variante wäre hierbei jedoch die Doppelpunktnotation,

    s[0:3]

    oder

    s[:3]

* Da es bei der Verbindung von Zeichenketten auf die Reihenfolge der jeweiligen Zeichenketten ankommt,
ist der Operator `+` bei Zeichenketten nicht wie gewohnt kommutativ.

* Sie können Zeichenketten wie `'ABC...Z'` auch unter Zuhilfenahme von `range`, `ord`, `chr` erzeugen.
Dafür sind allerdings kompliziertere Konstrukte wie `for`-Schleifen oder die Funktion `map` erforderlich.

