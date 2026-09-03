# Türme von Hanoi

## Einleitung


<div align="center">
<img src="mediaFiles/towers.png" alt="Test Image" width="100%" name="towers"/>
</div>

Die Türme von Hanoi sind ein Spiel, bei dem alle Scheiben vom Startstab (im Bild A) zum Zielstab (B oder C) gebracht werden müssen. Dabei darf immer nur eine Scheibe auf einmal bewegt werden und keine größere Scheibe auf eine kleinere Scheibe gelegt werden.

## Aufgabe


Programmiere Sie die Funktion
```python
solve_hanoi(n, start, destination, auxiliary)
```
die die Türme von Hanoi löst.

Dabei ist `n` die Anzahl an Scheiben, `start` die Position am Anfang (A, B oder C), `destination` das Ziel und `auxiliary` der verbliebene Stab.

Die Funktion soll Ihnen mittels Printbefehlnen die Anweisungen für die Lösung geben. Für `solve_hanoi(3, 'A', 'B', 'C')` sollte Sie folgendes erhalten:

Move disk 1 from A to B.\
Move disk 2 from A to C.\
Move disk 1 from B to C.\
Move disk 3 from A to B.\
Move disk 1 from C to A.\
Move disk 2 from C to B.\
Move disk 1 from A to B.

## Hinweis

* Schreiben Sie eine Funktion, die sich selbst so lange aufruft, bis eine Abbruchbedingung erfüllt ist.
