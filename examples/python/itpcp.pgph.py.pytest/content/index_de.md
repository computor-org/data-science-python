<!-- Pytest link -->
[pytest]: https://docs.pytest.org/en/latest/

# Pytest & cProfile

## Einleitung

In dieser Aufgabe werden Pytest und cProfile vorgestellt.

- [Pytest][pytest] ist ein Testing-Framework mithilfe dessen einfach eigene Tests geschrieben werden können.

**Installierung**: `pip install pytest`.

- [cProfile](https://docs.python.org/3/library/profile.html) ist ein built-in Python mModul, welches zum sogenannten 'profiling' eines Codes verwendet wird. Profiling bedeutet dabei die Analyse der Laufzeit und Performance eines Programms, um Engpässe zu identifizieren und den Code zu optimieren.


Es gibt drei Dateien im Übungsordner:
- `test_sort_funcs.py`: Enthält die Tests.
- `sort_funcs.py`: Enthält die zu testenden Funktionen.
- `run.py`: Führt Pytest auf der Testdatei aus.


## Aufgabe 

### 1. Pytest

Betrachten Sie zuerst die Datei `test_sort_funcs.py` file. 
Diese enthält bereits Tests für die Funktion `func` als Beispiel. Beim Testgetriebenen Entwickeln (**test driven development**) schreibt man zuerst die Tests und dann den Code, um die Tests zu bestehen. Diesen Ansatz möchten wir in der aktuellen Übung verwenden:
1. Schreiben Sie die Tests für die Funktion `bubble_sort` in der Datei `test_sort_funcs.py`. 
Verwenden Sie dazu die ```assert```-Anweisung, um zu prüfen, ob die Funktion korrekt funktioniert.
```python
assert 2 + 2 == 4 # This will pass
assert 2 + 2 == 5 # This will fail
```
2. Stellen Sie sicher, dass Sie die Testfunktion `test_<whatever Name you want here>` benennen, sodass Pytest sie als Testfunktion erkennt. 
Schreiben Sie zumindest **3** Tests für die `bubble_sort` Funktion -> das bedeutetet, dass Sie **3 Test Funktionen** in `test_sort_funcs.py` schreiben müssen.

### 2. Implement Bubble Sort

2. Implementieren Sie die Funktion `bubble_sort` in der Datei `sort_funcs.py` (Sie können natürlich auf der Wikipedia-Seite des Algorithmus nachsehen, falls Sie damit nicht vertraut sind).

Stellen Sie sicher, dass Sie die Funktion mit der vorgegebenen Signatur implementieren:

```python
bubblesort(arr, /, *, key=None, reverse=False):
   #CODE
   return arr
```
So hat die Funktion dieselbe Signatur wie die eingebaute [sorted()](https://docs.python.org/3/library/functions.html#sorted) Funktion in Python.
`/` und `*` werden verwendet, um anzuzeigen, dass die Argumente vor `/` nur positionsabhängig sind, und die Argumente nach `*` nur Schlüsselwortargumente (keyword-only arguments) sind. Dies ist eine neue Funktion in Python 3.8. Sie können diesen Sortieralgorithmus entweder *in-place* oder mit einer Kopie implementieren, solange das zurückgegebene `arr` sortiert ist.

3. Führen Sie die Tests mithilfe der `run.py` Datei aus. Alternativ, können Sie einfach `pytest` im Terminal **im Übungsordner** ausführen, indem Sie den Befehl `pytest` verwenden.

4. **Stellen Sie sicher, dass alle Tests bestanden werden**. Falls nicht, beheben Sie die `bubble_sort`-Funktion, bis sie alle bestehen. Stellen Sie auch sicher, dass Sie mindestens einen Test mit `reverse=True` und `key` als Schlüsselwortargument einschließen (z. B. sortieren Sie eine Liste von Zeichenfolgen nach der Länge der Zeichenfolgen).

### 3. cProfile

Verwenden Sie nun das Modul `cProfile`, um die `bubble_sort`-Funktion zu profilieren. Wie lange dauert es, eine Liste mit 5000 oder mehr zufälligen ganzen Zahlen zu sortieren?

### 4. Benchmarking bubble_sort mit built-in sort

Erstellen Sie ein großes Array (> 10000 Elemente) und sortieren Sie es mit der Funktion `bubble_sort` und der eingebauten Funktion `sort`. Verwenden Sie die Funktion[time.perf_counter()](https://docs.python.org/3/library/time.html#time.perf_counter) , um die Zeit zu messen, die zum Sortieren des Arrays mit jeder Funktion benötigt wird. Vergleichen Sie die Ergebnisse.

Vergleichen Sie nun die Zeitkomplexität der bubble_sort-Funktion mit der eingebauten sort-Funktion. Führen Sie die bubble_sort-Funktion und die eingebaute sort-Funktion mit Arrays unterschiedlicher Größe aus (z. B. 2,4,8,16,32,...,8192, 16384) und messen Sie die Zeit, die zum Sortieren des Arrays mit jeder Funktion benötigt wird. Stellen Sie die Ergebnisse in einem Diagramm dar. Was können Sie beobachten? Welcher Algorithmus ist schneller? Weitere Informationen zur Zeitkomplexität finden Sie [hier](https://en.wikipedia.org/wiki/Time_complexity).

## Bonus 

Schreiben Sie einen schnelleren Sortieralgorithmus (z. B. Quicksort) und vergleichen Sie ihn mit der bubble_sort-Funktion und der eingebauten sort-Funktion.

## Hinweise 

* Wenn Sie einfach `pytest` im Terminal ausführen, werden alle Dateien mit dem Präfix `test_` (im aktuellen Verzeichnis und in Unterverzeichnissen) getestet. Wenn Sie eine bestimmte Datei testen möchten, können Sie den Befehl `pytest <Dateiname>` verwenden.

* Der Test prüft nur die `bubble_sort`-Funktion.