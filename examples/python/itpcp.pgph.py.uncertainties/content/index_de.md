# Fehlerfortpflanzung: linear und Monte Carlo

## Einleitung

Hier nutzt du das Paket [uncertainties](https://pythonhosted.org/uncertainties/) für die lineare Fehlerfortpflanzung. Wir wollen sehen, wo sie bei nichtlinearen Funktionen an ihre Grenzen stößt. Zum Vergleich nutzen wir die Monte-Carlo-Methode, die auch bei nichtlinearen Funktionen funktioniert, aber nur statistische Ergebnisse liefert.

## Aufgabe

### 1. Lineare Fehlerfortpflanzung

1. Geh laut Dokumentation des Pakets uncertainties vor und definiere eine gemessene Variable `t` mit einem Wert von $0.0$ und einem Fehler von $0.1$ als `ufloat`. Dann definierst du eine abgeleitete Größe `y_sin = sin(t)` und gibst `y_sin` mit `print` aus. Du solltest den Wert und den linear propagierten Fehler erhalten. Achtung: Verwende die Funktion `sin` aus dem Modul `uncertainties.umath` (nicht `numpy`).

2. Berechne Erwartungswert (`nominal_value`) und Standardabweichung (`std_dev`) von `y_sin` und speichere diese gemeinsam im Dictionary `out_sin = {"val": ..., "err": ...}`.

3. Um die interne Funktionsweise zu verstehen, probiere auch die Funktion `y_sin.derivatives[t]` aus. Diese gibt die partielle Ableitung von `y_sin` nach `t` an. Wende lineare Fehlerfortpflanzung händisch an, um den Fehler von `y_sin` zu berechnen, und speichere das Ergebnis in der Variable `err_sin_manual`.

### 2. Vergleich mit Monte Carlo

1. Schreib eine Funktion `sample_uncertainties(t, n)` mit Default-Wert `n=1000`, die `n` Zufallszahlen aus einer Normalverteilung auf Basis von `t` mit Erwartungswert als dessen `nominal_value` und Standardabweichung `std_dev` zieht und ein `numpy`-Array zurückgibt. Verwende dazu den `np.random.default_rng` mit seed 42.

2. Berechne so `t_samples` und die jeweiligen Funktionswerte in `sin_t_samples`. Verwende weiterhin die `uncertainties`-Variante des Sinus und behebe selbstständig den Fehler, den du gleich siehst, wenn du `sin(t_samples)` direkt ausführst, z.B. durch [List comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). Zusätzlich sampelst du vom ursprünglichen `y_sin`, das mit linearer Fehlerfortpflanzung ermittelt wurde, und speicherst die Funktionswerte in `sin_t_samples_linear`.

3. Plotte die beiden Verteilungen in einem Histogramm. Setze dabei das Argument `density=True` zum Vergleich mit der Dichtefunktion. Plotte auch die Dichtefunktion auf Basis von `y_sin` auf einem `linspace` über `nominal_value +- 6*std_dev`. Praktischerweise kannst du dazu gleich eine Funktion `x_plot, p_plot = pdf_for_plot(x)` erstellen, die das generisch macht.

### 3. Zerstöre die lineare Fehlerfortpflanzung

Nun machst du denselben Plot für zwei weitere Fälle:

1. Standardabweichung $\Delta t = 0.3$ setzen.
2. Die Funktion `cos(t+0.05)` statt `sin(t)` verwenden, wieder mit $\Delta t = 0.1$.

Denk darüber nach, warum das passiert, was du siehst. Gibt es einen Ausweg?