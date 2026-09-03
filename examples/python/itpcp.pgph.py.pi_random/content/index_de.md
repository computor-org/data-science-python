[np.random.rand]: <https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html> "np.random.rand"
[cumsum]: <https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html> "cumsum"

# $\pi$ $-$ nur ein Zufall?

## Einleitung
Man kann $\pi$ auch mithilfe von Zufallszahlen berechnen! Dazu generiert man zufällig Punkte innerhalb eines Quadrat mit Seitenlänge $2a$. In dem Quadrat befindet sich zusätzlich ein Kreis mit Radius $a$, siehe Skizze. 

<div align="center">
<img src="mediaFiles/pi_random.png" alt="Test Image" width="80%" name="Pi"/>
</div>
 
Die Fläche des Quadrates ist $A_\mathrm{Q} = 4a^2$ und die des Kreises $A_\mathrm{K}  = \pi a^2$. Das Verhältnis der Punkte $N_K$, die in den Kreis fallen, zu den Punkten $N_Q$, die in das Quadrat fallen, ist somit näherungsweise das Verhältnis der Flächen:

$$
 \frac{N_\mathrm{K}}{N_\mathrm{Q}} \approx \frac{A_\mathrm{K}}{A_\mathrm{Q}} = \frac{\pi}{4}
$$

Man kann eine Näherung für $\pi$ also erhalten, indem man die Punkte im Kreis durch die Gesamtzahl der Punkte dividiert (da wir Punkte außerhalb des Quadrates ja garnicht zulassen). Für eine bessere Näherung/Fehlerabschätzung empfiehlt sich weiters, das "Zufallsexperiment" oft zu wiederholen.

## Aufgabe
Erledigen Sie folgende Aufgaben:

1. Erzeugen Sie die Variablen `k = 50` und `N = 1E5`. `N` soll dabei die Gesamtzahl der zu erzeugenden Punkte, `k` die Anzahl der Wiederholungen des "Experiments" sein.

2. Betrachten wir nun nur ein Viertel des Kreises/Quadrats. Dabei bleibt das Verhältnis von Punkten (inner-)/außerhalb gleich. Sie können nun jedoch mithilfe von [np.random.rand] ein `(Nx2)`-Array mit Zufallszahlen zwischen `0` und `1` erzeugen. In diesem Array entspricht jede Zeile einem Koordinatenvektor im Viertel-Quadrat. Über die Länge dieser Vektoren können Sie herausfinden, ob der Punkt innerhalb des Viertelkreises liegt, oder nicht.

3. Initialisieren Sie einen Zeilenvektor `p` der Länge `k`. In einer Schleife berechnen Sie nun `k`-mal mithilfe von (jeweils neuen) Zufallszahlen eine Näherung für $\pi$. Speichern Sie alle Ergebnisse im Vektor `p`.

4. Damit wir $\pi$ besser abschätzen können, erzeugen Sie außerdem noch den Zeilenvektor `ps` mit der Länge `k`. In diesem soll an der `i`-ten Stelle der Mittelwert aller vorangegangenen Ergebnisse (Mittelwert der Einträge bis zum `i`-ten Wert von `p`) stehen.

5. Um die Abweichung der Approximation zum Zahlenwert von $\pi$ zu überprüfen,  erzeugen Sie die Variable `err_r`, die den $\bf{relativen}$ Fehler des letzten Mittelwertes enthalten soll (d.h. relative Abweichung von `ps[-1]` von $\pi$).

6. Erstellen Sie einen Plot, in dem Sie
    * den Wert $\pi$ mit einer schwarzen durchgezogenen horizontalen Linie, 
    * `p` als blaue Punkte und 
    * `ps` als rote Linie mit Punkten
       
    in dieser Reihenfolge einzeichnen 

7. Geben Sie den genauen Wert für $\pi$, den letzten Wert der Variable `ps` und den relativen Fehler `err_r` untereinander mit `print` aus. Dabei sollen $\pi$ und der letzte Mittelwert mit jeweils zehn Nachkommastellen, und `err_r` mit drei Nachkommastellen in Exponentialdarstellung ausgegeben werden. Für den Test ist es dabei wichtig, dass es sich um ein großes E handelt, sprich zum Beispiel `1.234E-05`.

8. Erstellen Sie eine passende Achsenbeschriftung und wählen Sie einen passenden Titel.

## Hinweise
* Für den Mittelwert könnte [cumsum] hilfreich sein.

* Vergessen Sie nicht, dass Sie einen Faktor $4$ zu berücksichtigen haben!