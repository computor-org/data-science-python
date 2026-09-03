# Fitten von abklingenden Oszillation
 
## Einleitung


Eine abklingende Oszillation kann beschrieben werden als

$$
\begin{aligned}
  y(t,A,\omega,\phi,\tau) &= A \sin(\omega t + \phi) \cdot \exp(-t / \tau)\; , \\
\end{aligned}
$$
wobei $t$ die Zeit ist, $A$ eine Amplitude, $\omega$ eine Frequenz, $\phi$ eine Phasenverschiebung, und $\tau$ eine Abklingzeit ist. Für die Modellfunktion, die zur Anpassung verwendet wird, verwenden wir die Zeit `t` und die Koeffizienten $A$ (`A`), $\omega$ (`omega`), $\phi$ (`phi`), $\tau$ (`tau`).


## Aufgabe


1. Lesen Sie die Datei `decay_osc.dat` ein. Diese enthält die Messdaten, in der ersten Spalte befinden sich die Zeitpunkte, in der zweiten die Messwerte für $y(t)$.

2. Schreiben Sie die Funktion `f_model`, welche $t$ und die oben genannten Parameter als input nimmt um $y$ zu berechnen.

3. Nutzen Sie [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) von scipy um die Parameter auszurechnen mit `[4, 1, 1, 10]` als Startwerte.

4. Werten sie die gefittete Funktion auf $500$ Stützstellen für `t` aus, beginnend bei $0$ und endend bei $20$ Zeiteinheiten nach dem letzten Messzeitpunkt. Speichern sie das Resultat in `y`

5. Nutzen Sie [fmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html) um den Minimalwert von $y$, `y_min`, zusammen mit dem dazugehörigen Zeitpunkt `t_min` zu erhalten. Finden Sie analog dazu `y_max` mit dazugehörigem `t_max`.

6. Stellen Sie Ihre Ergebnisse graphisch dar. Plotten Sie dazu $y(t)$, die Messwerte und markieren Sie das Minimum und das Maximum von $y(t)$.