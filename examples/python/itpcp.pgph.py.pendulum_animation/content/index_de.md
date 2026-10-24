[animation]: https://matplotlib.org/stable/users/explain/animations/animations.html
[contour]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html
[meshgrid]: https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
# Animation eines Pendels

## Einleitung

Wir wollen nun unser Pendel animieren. Nutze dazu [animation]. 

## Aufgabe


1. Ändere die Funktion `euler_symplectic(fun, dt, t_max, y_0)` (und deine eigenen Funktionen aus der letzten Übung) so, dass $\theta$ nun nur noch von $-\pi$ bis $\pi$ gehen kann, da ein Wert von $\theta = 3.2$ auch zu $\theta = 3.2 - 2\pi$ korrespondiert.

2. Erstelle eine Animation. Diese soll aus einem Subplot mit zwei Spalten bestehen. Links soll das Pendel dargestellt werden und rechts die Position im Phasenraum. Dieser wird durch $\theta$ auf der $x$-Achse und $\omega$ auf der $y$-Achse beschrieben (Erinnerung: $\dot{\theta} = \omega$, die Winkelgeschwindigkeit).

3. Nutze [contour], um Konturen von konstanter Gesamtenergie darzustellen. Wie auch im letzten Beispiel soll die potentielle Energie $0$ sein, wenn sich das Pendel in Ruhelage befindet.

4. Probiere unterschiedliche Anfangswerte, Längen, Gravitationsbeschleunigungen und Massen aus. Teste außerdem auch deine eigenen Funktionen von der letzten Übung. Beobachte außerdem die zwei verschiedenen "Bereiche" im Phasenraum.
   
5. Speichere deine schönste Animation als ein `gif` ab.

## Hinweise

* Nutze [meshgrid] für die Konturen.

* Der Test überprüft in diesem Beispiel nur, ob du die Änderung an `euler_symplectic(fun, dt, t_max, y_0)` vorgenommen hast.