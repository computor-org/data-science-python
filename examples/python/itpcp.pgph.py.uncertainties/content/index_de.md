# Fehlerfortpflanzung: linear und Monte Carlo

## Einleitung

Hier nutzen Sie das Paket [uncertainties](https://pythonhosted.org/uncertainties/) für die lineare Fehlerfortpflanzung. Wir wollen sehen, wo sie bei nichtlinearen Funktionen an ihre Grenzen stößt. Zum Vergleich nutzen wir die Monte-Carlo-Methode, die auch bei nichtlinearen Funktionen funktioniert, aber nur statistische Ergebnisse liefert.

## Aufgabe

### 1. Lineare Fehlerfortpflanzung

1. Gehen Sie laut Dokumentation des Pakets uncertainties vor, und definieren Sie eine gemessene Variable `t` mit einem Wert von $0.0$ und einem Fehler von $0.1$ als `ufloat`. Dann definieren Sie eine abgeleiteten Größe `y_sin = sin(t)` und geben Sie `y_sin` mit `print` aus. Sie sollten den Wert und den linear propagierten Fehler von erhalten. Achtung: Verwenden Sie die Funktion `sin` aus dem Modul `uncertainties.umath` (nicht `numpy`)

2. Berechnen Sie Erwartungswert (`nominal_value`) und Standardabweichung (`std_dev`) von `y`, und speichern Sie diese gemeinsam im Dictionary `out_sin = {"val": ..., "err": ...}`.

3. Um die interne Funktionsweise zu verstehen, probieren Sie auch die Funktion `y.derivatives[t]` aus. Diese gibt die partielle Ableitung von `y` nach `t` an. Wenden Sie lineare Fehlerfortpflanzung händisch an, um den Fehler von `y` zu berechnen und speichern Sie das Ergebnis in der Variable `err_sin_manual`.

### 2. Vergleich mit Monte Carlo

1. Schreiben Sie eine Funktion `sample_uncertainties(t, n)` mit default-Wert `n=1000`, die `n` Zufallszahlen aus einer Normalverteilung auf Basis von `t` mit Erwartungswert als dessen `nominal_value` und Standardabweichung `std_dev` zieht und ein `numpy`-array zurückgibt. Verwenden Sie dazu den `np.random.default_rng` mit seed 42.

2. Berechnen Sie so `t_samples` und die jeweiligen Funktionswerte in `sin_t_samples`. Verwenden Sie weiterhin die `uncertainties`-Variante des Sinus und lösen Sie den Fehler selbstständig, den Sie gleich sehen wenn Sie `sin(t_samples)` direkt ausführen, z.B. durch [List comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). Zusätzlich sampeln Sie vom ursprünglichen `y` das mit linearer Fehlerfortpflanzung ermittelt wurde, und speichern Sie die Funktionswerte in `sin_t_samples_linear`.

3. Plotten Sie die beiden Verteilungen in einem Histogramm. Setzen Sie dabei das Argument `density=True` zum Vergleich mit der Dichtefunktion. Plotten Sie auch die Dichtefunktion auf Basis von `y_sin` auf einem `linspace` über `nominal_value +- 6*std_dev`. Praktischerweise können Sie dazu gleich eine Funktion `x_plot, p_plot = pdf_for_plot(x)` erstellen, die das generisch macht.

### 3. Zerstören Sie die lineare Fehlerfortpflanzung

Nun machen Sie den selben Plot für zwei weiter Fälle:

1. Standardabweichung $\Delta t = 0.3$ setzen.
2. Die Funktion `cos(t+0.05)` statt `sin(t)` verwenden wieder mit $\Delta t = 0.1$.

Denken Sie darüber nach, warum das passiert, was Sie sehen. Gibt es einen Ausweg?