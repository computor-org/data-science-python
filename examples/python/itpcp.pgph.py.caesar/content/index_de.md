<!-- Ceasar source wiki -->
[caesar]: <https://en.wikipedia.org/wiki/Caesar_cipher> "caesar"

# Caesar Verschlüsselung

## Einleitung

Die [Caesar-Verschlüsselung][caesar] ist eine der einfachsten und bekanntesten Verschlüsselungstechniken. Sie ist ein spezieller Fall der Substitutionschiffre, bei der das ursprüngliche Alphabet durch ein um eine konstante Zahl verschobenes Alphabet ersetzt wird.

Die Verschlüsselung funktioniert also durch eine zyklische Verschiebung der Buchstaben. Die Verschiebung wird durch einen Parameter bestimmt, der als Schlüssel bezeichnet wird: 

Beispielsweise wird das Wort "Hallo" mit einem Schlüssel von $z=3$ verschlüsselt zu "Kdoor".
Dabei gibt $z$ die Anzahl der Schritte an, die ein Buchstabe im Alphabet weitergerückt wird.

Für den Schlüssel $z=3$ sieht die Verschlüsselungstabelle wie folgt aus:

| Klartext | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geheimtext | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |


## Aufgabe

### 1. Verschlüsselung & Entschlüsselung

1. Schreiben Sie eine Funktion `caesar_encrypt(text: str, key: int, alphasize: int = 85) -> str`, die einen Text `text` mit einem Schlüssel `key` verschlüsselt. Das Alphabet hat eine Größe von `alphasize` Zeichen.

2. Schreiben Sie eine Funktion `caesar_decrypt(text: str, key: int, alphasize: int = 85) -> str`, die einen verschlüsselten Text `text` mit einem Schlüssel `key` entschlüsselt. Das Alphabet hat eine Größe von `alphasize` Zeichen.

3. Beide Funktionen sollen für alle Schlüssel $0 \leq z$ funktionieren (falls $z$ größer als die Anzahl der Buchstaben im Alphabet ist, soll die Verschiebung von vorne beginnen; Sprich $z=\mathrm{alphasize} + 1$ verschlüsselt gleich wie $z=1$).

### 2. Codes knacken

So jetzt wollen wir einmal richtig codes knacken! 

1. Lesen Sie den Text aus der Datei `enc.txt` ein und entschlüsseln Sie ihn. Folgendes ist dabei zu beachten: 

    Der Text gliedert sich in 3 Unterabschnitte, die jeweils unterschiedlich verschlüsselt wurden und sukzessive schwerer zu entschlüsseln sind.

    1) Well this is easy: Dieser Text ist mit einem unbekannten Schlüssel verschlüsselt worden, versuche diesen zu knacken. Speichere den entschlüsselten Text in der Datei `dec1.txt`.
    2) This is a bit harder: Vielleicht sind in diesem Text die Zeilen unterschiedlich verschlüsselt. Der Titel und Text aus 1) geben vielleicht einen Hinweis. Gibt es Zeichenfolgen, die gehäuft vorkommen? Speichere den entschlüsselten Text in der Datei `dec2.txt`.
    3) This is the hardest: Das ist wohl noch schwieriger. Vielleicht gibt es ja Tipps in Text 2) Speichere den entschlüsselten Text in der Datei `dec3.txt`.

#### Viel Spaß beim Knacken!