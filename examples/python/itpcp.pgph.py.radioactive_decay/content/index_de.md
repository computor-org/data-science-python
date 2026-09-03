# Fitten von radioaktiven Zerfällen
 
## Einleitung

Wir betrachten den Radioaktiver Zerfall in einer Zerfallskette. Zur Zeit $t = 0$ haben wir nur Isotop $1$ und zwar $N_{01}$ davon. Isotop $1$ jedoch zerfällt zu Isotop $2$ mit der Zerfallskonstante $\lambda_1$. Isotop $2$ zerfällt nun weiter zu dem stabilen Isotop $3$. Dies passiert mit der Zerfallskonstante $\lambda_2$. Man kann zeigen, dass für die Anzahl an Isotop $2$, $N_2(t)$, sich im Verlauf der Zeit wie die folgende Gleichung verhält:

$$
  N_2(t) = N_{01} \big[1 - \exp(-\lambda_1 t)\big] \exp(-\lambda_2 t).
$$

Wir messen nun $N_2$ zu verschiedenen Zeiten und wollen die Funktion fitten.

## Aufgabe


1. Lesen Sie die Datei `expfun.dat` ein. Diese enthält die Messdaten, in der ersten Spalte befinden sich die Zeitpunkte, in der zweiten die Messwerte für $N_2(t)$.

2. Schreiben Sie die Funktion `f_model`, welche $t$ und die oben genannten Parameter als input nimmt um $N_2$ zu berechnen.

3. Nutzen Sie [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) von scipy um `N_01`, `lambda_1` und `lambda_2` auszurechnen. Nutzen Sie dafür `t` von $0$ bis $25$ mit $500$ Stützstellen und `[100, 4, 0.5]` als Startwerte.

4. Nutzen Sie Ihre Funktion um `N_2(t)` zu bestimmen.

5. Nutzen Sie [fmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html) um den Maximalwert von $N_2$, `N_2max`, zusammen mit dem dazugehörigen Zeitpunkt `t_max` zu erhalten.

6. Stellen Sie Ihre Ergebnisse graphisch dar. Plotten Sie dazu $N_2(t)$, die Messwerte und markieren Sie das Maximum von $N_2(t)$.

7. Berechnen und plotten Sie zusätzlich `N_1` und `N_3`, sowie die Summe von den $3$ Isotopen. Beschriften Sie die Graphik passend. Formeln:
  
$$
  N_1(t) = N_{01} \exp(-\lambda_1 t),
$$
$$
  N_3(t) = N_{01} \big[1 - \exp(-\lambda_1 t)\big] \big[1 - \exp(-\lambda_2 t)\big].
$$
