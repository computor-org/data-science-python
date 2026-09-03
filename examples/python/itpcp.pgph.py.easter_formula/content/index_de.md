[arithmetischen Operator]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "arithmetische Operatoren"
[Wikipedia-Artikel]: <https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel> "Gaußsche Osterformel"
[f-string]: <https://docs.python.org/3/tutorial/inputoutput.html> "f-string"
[input]: <https://docs.python.org/3/library/functions.html#input> "input"
[int]: <https://docs.python.org/3/library/functions.html#int> "int"
[print]: <https://docs.python.org/3/library/functions.html#print> "print"

# Gaußsche Osterformel

## Einleitung

Bei der Gaußschen Osterformel handelt es sich um einen Satz von Gleichungen, mithilfe welcher das Datum des Ostersonntages für ein gewähltes Jahr berechnet werden kann.

Im folgenden werden nur die Gleichungen wiedergegeben (Variable `X` ist die Jahreszahl). 
Nähere Informationen zum Algorithmus findet man in diesem [Wikipedia-Artikel].

$$
\begin{aligned}
a & = X \mod 19 \\
b & = X \mod 4 \\
c & = X \mod 7 \\
k & = X \div 100 \\
p & = (8 k + 13) \div 25 \\
q & = k\div 4 \\
M & = (15 + k - p - q) \mod 30 \\
N & = (4 + k - q) \mod 7 \\
d & = (19 a + M) \mod 30 \\
e & = (2 b + 4 c + 6 d + N) \mod 7 \\
E & = 22 + d + e \\
\end{aligned}
$$
Die Variable $E$ steht hier für die Python-Variable `easter_sunday`.

Bei diesen Formeln ist zu beachten, dass das Ergebnis von `easter_sunday` das Datum des Ostersonntages in Märztagen darstellt (d.h. 32. März = 1. April,
usw.). 

Die Operation $\div$ stellt die Ganzzahldivision (Division ohne Rest) dar, die in Python mit dem [arithmetischen Operator] `//` anstelle von `/` notiert wird.
Unter $\mod{}$ (modulo) versteht man den Rest der Division, z.B. $5 \mod 3 = 2$.
Modulo wird in Python mit dem Operator `%` notiert, d.h. `5 % 3` liefert als Ergebnis `2`.

## Aufgabe

Erzeugen Sie ein Python-Skript `easter_formula`, welches das Datum
des Ostersonntages in einem bestimmten Jahr mit der Gaußschen
Osterformel berechnet.


Das Skript soll folgende Dinge tun:

 1. Lesen Sie die Jahreszahl unter der Variablen `X` von der Tastatur ein ([input]).
  Der Text für die Eingabeaufforderung sollte **`"Year for calculating Easter: "`** lauten. Um die eingelesene Zeichenkette in eine Ganzzahl umzuwandeln, verwenden
  Sie die Funktion [int].

2. Berechnen Sie die Formeln aus dem Einführungsteil. Verwenden Sie dabei die gleichen
    Variablennamen.

3. Wie im Einführungsteil beschrieben, erhält man das Datum des Ostersonntages in Märztagen.
  Schöner wäre es aber die Trennung in die Monate März und April vorzunehmen. Fügen Sie
  dazu bitte vor dem [print]-Befehl die Programmzeilen
  ```python
  if easter_sunday <= 31:
      month = 'March'
  else:
      easter_sunday -= 31
      month = 'April'
  ```
  ein. Die obige if-else-Steuerstruktur, welche die Zuordnung zum richtigen Monat
  vornimmt, wird in einer späteren Woche näher behandelt und soll Sie hier nicht weiter beirren.
  Der Operator `-=` bedeutet, dass von der Variable `easter_sunday` der Wert 31
  subtrahiert wird; mit dieser Schreibweise muss man den Variablennamen nicht wiederholen.

4.  Geben Sie das Datum des Ostersonntages formatiert mit der Funktion
  [print] aus. Um die jeweiligen Werte in die
  Zeichenkette einzusetzen, bieten sich [f-string]s an. Folgender Satz (Zeichenkette) sollte von `print` ausgegeben werden:

  **Easter Sunday in the year "value of X" is on "value of easter_sunday" "value of month"**
   

## Hinweise

* Dieses Skript verwendet die Python-Funktion [input]. Benutzen Sie daher _Run Python File_ statt _Run in Interactive Window_, um das Skript im _Terminal_ auszuführen, wo Sie das gewünschte Jahr eingeben können

* Achten Sie darauf, die Variablen der Osterformel richtig zu berechnen, siehe Einleitung. 
Achten Sie ebenfalls auf die korrekte Wahl der verwendeten Operatoren.

* Probieren Sie Ihre Osterformel selbst aus!

Einige Ostersonntage zum selbstständigen Testen:

| Jahr   | Ostersonntag |                                       
| ---    | ----------   | 
| 2025   | 20. April    | 
| 2024   | 31. März     |                      
| 2022   | 17. April    |       
| 2005   | 27. März     |                       
| 1990   | 15. April    |                         
| 1500   | 01. April    |                    
              

## Keywords

- Konsolen-Eingabe
- Konsolen-Ausgabe
- Modulus