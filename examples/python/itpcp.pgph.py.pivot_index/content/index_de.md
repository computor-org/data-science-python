# Finden des Pivot-Index

## Einleitung

### Pivot-Index

Der Pivot-Index ist der Index, an dem die Summe aller Zahlen streng links vom Index gleich der Summe aller Zahlen streng rechts vom Index ist.

Wenn der Index am linken Rand des Arrays liegt, ist die linke Summe 0, da keine Elemente links davon vorhanden sind. Dies gilt auch für den rechten Rand des Arrays.

## Aufgabe

1. Gegeben ist ein Array von Ganzzahlen `nums`. Schreiben Sie eine Funktion, die den linksten Pivot-Index des Arrays zurückgibt.

2. Geben Sie den linksten Pivot-Index zurück. Wenn kein solcher Index existiert, soll -1 zurückgegeben werden.

## Hinweise


**Beispiel 1:**

    Eingabe: `nums = [1,7,3,6,5,6]`

    Ausgabe: `3`

    Erklärung:

    Der Pivot-Index ist 3.

    Linke Summe = `nums[0] + nums[1] + nums[2]` = 1 + 7 + 3 = 11

    Rechte Summe = `nums[4] + nums[5]` = 5 + 6 = 11

**Beispiel 2:**

    Eingabe: `nums = [1,2,3]`

    Ausgabe: `-1`

    Erklärung:

    Es gibt keinen Index, der die Bedingungen in der Problemstellung erfüllt.

**Beispiel 3:**

    Eingabe: `nums = [2,1,-1]`

    Ausgabe: `0`

    Erklärung:

    Der Pivot-Index ist 0.

    Linke Summe = 0 (keine Elemente links vom Index 0)

    Rechte Summe = `nums[1] + nums[2]` = 1 + -1 = 0