<!-- Pytest link -->
[pytest]: https://docs.pytest.org/en/latest/

# Pytest & cProfile

## Einleitung

In dieser Aufgabe werden Pytest und cProfile vorgestellt.

- [Pytest][pytest] ist ein Testing-Framework mithilfe dessen einfach eigene Tests geschrieben werden können.

**Installierung**: `pip install pytest`.

- [cProfile](https://docs.python.org/3/library/profile.html) ist ein built-in Python Modul, welches zum sogenannten 'profiling' eines Codes verwendet wird. Profiling bedeutet dabei die Analyse der Laufzeit und Performance eines Programms, um Engpässe zu identifizieren und den Code zu optimieren.


Es gibt drei Dateien im Übungsordner:
- `test_sort_funcs.py`: Enthält die Tests.
- `sort_funcs.py`: Enthält die zu testenden Funktionen.
- `run.py`: Führt Pytest auf der Testdatei aus.


## Aufgabe 

### 1. Pytest

Betrachte zuerst die Datei `test_sort_funcs.py`. 
Diese enthält bereits Tests für die Funktion `func` als Beispiel. Beim testgetriebenen Entwickeln (**test driven development**) schreibt man zuerst die Tests und dann den Code, um die Tests zu bestehen. Diesen Ansatz möchten wir in der aktuellen Übung verwenden:
1. Schreibe die Tests für die Funktion `bubble_sort` in der Datei `test_sort_funcs.py`. 
Verwende dazu die ```assert```-Anweisung, um zu prüfen, ob die Funktion korrekt funktioniert.
```python
assert 2 + 2 == 4 # This will pass
assert 2 + 2 == 5 # This will fail
```
2. Stell sicher, dass du die Testfunktion `test_<whatever Name you want here>` benennst, sodass Pytest sie als Testfunktion erkennt. 
Schreibe zumindest **3** Tests für die `bubble_sort` Funktion -> das bedeutet, dass du **3 Test Funktionen** in `test_sort_funcs.py` schreiben musst.

### 2. Implement Bubble Sort

2. Implementiere die Funktion `bubble_sort` in der Datei `sort_funcs.py` (du kannst natürlich auf der Wikipedia-Seite des Algorithmus nachsehen, falls du damit nicht vertraut bist).

Stell sicher, dass du die Funktion mit der vorgegebenen Signatur implementierst:

```python
bubblesort(arr, /, *, key=None, reverse=False):
   #CODE
   return arr
```
So hat die Funktion dieselbe Signatur wie die eingebaute [sorted()](https://docs.python.org/3/library/functions.html#sorted) Funktion in Python.
`/` und `*` werden verwendet, um anzuzeigen, dass die Argumente vor `/` nur positionsabhängig sind, und die Argumente nach `*` nur Schlüsselwortargumente (keyword-only arguments) sind. Dies ist eine neue Funktion in Python 3.8. Du kannst diesen Sortieralgorithmus entweder *in-place* oder mit einer Kopie implementieren, solange das zurückgegebene `arr` sortiert ist.

3. Führe die Tests mithilfe der `run.py` Datei aus. Alternativ kannst du einfach `pytest` im Terminal **im Übungsordner** ausführen, indem du den Befehl `pytest` verwendest.

4. **Stell sicher, dass alle Tests bestanden werden**. Falls nicht, korrigiere die `bubble_sort`-Funktion, bis sie alle bestehen. Stell auch sicher, dass du mindestens einen Test mit `reverse=True` und `key` als Schlüsselwortargument einschließt (z. B. sortiere eine Liste von Zeichenfolgen nach der Länge der Zeichenfolgen).

### 3. cProfile

Verwende nun das Modul `cProfile`, um die `bubble_sort`-Funktion zu profilieren. Wie lange dauert es, eine Liste mit 5000 oder mehr zufälligen ganzen Zahlen zu sortieren?

### 4. Benchmarking bubble_sort mit built-in sort

Erstelle ein großes Array (> 10000 Elemente) und sortiere es mit der Funktion `bubble_sort` und der eingebauten Funktion `sort`. Verwende die Funktion [time.perf_counter()](https://docs.python.org/3/library/time.html#time.perf_counter), um die Zeit zu messen, die zum Sortieren des Arrays mit jeder Funktion benötigt wird. Vergleiche die Ergebnisse.

Vergleiche nun die Zeitkomplexität der bubble_sort-Funktion mit der eingebauten sort-Funktion. Führe die bubble_sort-Funktion und die eingebaute sort-Funktion mit Arrays unterschiedlicher Größe aus (z. B. 2,4,8,16,32,...,8192, 16384) und miss die Zeit, die zum Sortieren des Arrays mit jeder Funktion benötigt wird. Stelle die Ergebnisse in einem Diagramm dar. Was kannst du beobachten? Welcher Algorithmus ist schneller? Weitere Informationen zur Zeitkomplexität findest du [hier](https://en.wikipedia.org/wiki/Time_complexity).

## Bonus 

Schreibe einen schnelleren Sortieralgorithmus (z. B. Quicksort) und vergleiche ihn mit der bubble_sort-Funktion und der eingebauten sort-Funktion.

## Hinweise 

* Wenn du einfach `pytest` im Terminal ausführst, werden alle Dateien mit dem Präfix `test_` (im aktuellen Verzeichnis und in Unterverzeichnissen) getestet. Wenn du eine bestimmte Datei testen möchtest, kannst du den Befehl `pytest <Dateiname>` verwenden.

* Der Test prüft nur die `bubble_sort`-Funktion.