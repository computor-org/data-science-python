[animation]: https://matplotlib.org/stable/users/explain/animations/animations.html
[contour]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html
[meshgrid]: https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
# Animation eines Pendels

## Einleitung

Wir wollen nun unser Pendel animieren. Nutzen Sie dazu [animation]. 

## Aufgabe


1. Ändern Sie die Funktion `euler_symplectic(fun, dt, t_max, y_0)`, (und Ihre eigenen Funktionon aus der letzten Übung) Funktion, sodass $\theta$ nun nur noch von $-\pi$ bis $\pi$ gehen kann, da ein Wert von $\theta = 3.2$ auch zu $\theta = 3.2 - \pi$ korrespondiert.

2. Erstellen Sie eine Animation. Diese soll aus einem Subplot mit zwei Spalten bestehen. Links soll das Pendel dargestellt werden und rechts die Position im Phasenraum. Dieser wird durch $\theta$ auf der $x$-Achse und $\omega$ auf der $y$-Achse beschrieben (Erinnerung: $\dot{\theta} = \omega$, die Winkelgeschwindigkeit).

3. Nutzen Sie [contour] um Konturen von konstanter Gesamtenergie darzustellen. Wie auch im letzten Beispiel soll die potentielle Energie $0$ sein, wenn sich das Pendel in Ruhelage befindet.

4. Probieren Sie unterschiedliche Anfangswerte, Längen, Gravitationsbeschleunigungen und Massen aus. Testen Sie außerdem auch Ihre eigenen Funktionen von der letzten Übung. Beobachten Sie außerdem die zwei verschiedene "Bereiche" im Phasenraum.
   
5. Speichern Sie Ihre schönste Animation als ein `gif` ab.

## Hinweise

* Nutzen Sie [meshgrid] für die Konturen.

* Der Test überprüft in diesem Beispiel nur ob Sie die Änderung an `euler_symplectic(fun, dt, t_max, y_0)` vorgenommen haben.