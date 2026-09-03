# Fitten von radioaktiven Zerfällen

## Einleitung

In diesem Python-Skript werden verschiedene Interpolationsmethoden auf Daten angewendet und die Ergebnisse grafisch verglichen.

## Aufgabe


1. Laden Sie die Messdaten aus der `inter_data.dat` Datei. Die erste Spalte der Datei sind die $x$-Werte und die zweite Spalte die $y$-Werte.


2. Erstellen Sie das Array `x_int`, welches gleichmäßig verteilte Zahlen vom ersten bis inklusive dem letzten $x$-Wert mit $500$ Stützstellen enthält.

3. Wenden sie mittels scipy verschiedene Interpolationsmethoden an:

    - `'nearest'`: Die nächste Nachbarschaftsmethode wobei der interpolierte Wert an einem Abfragepunkt der Wert an dem nächstgelegenen Stichprobenrasterpunkt ist (diskontinuierlich).

    - `'linear'`: Der interpolierte Wert an einem Abfragepunkt basiert auf der linearen Interpolation der Werte an den benachbarten Gitterpunkten in der jeweiligen Dimension (Werte sind stetig, Ableitungen sind unstetig).

    - `'pchip'`: (Piecewise Cubic Hermite Interpolating Polynomial) Der interpolierte Wert an einem Abfragepunkt basiert auf einer formerhaltenden stück-weisen kubischen Interpolation der Werte an benachbarten Gitterpunkten (Werte und erste Ableitung sind stetig, die Krümmung ist diskontinuierlich).

    - `'cubic'`: Kubische Spline-Interpolation. Der interpolierte Wert an einem Abfragepunkt basiert auf einer kubischen Interpolation von den Werten an benachbarten Gitterpunkten in der jeweiligen Dimension (Werte, erste Ableitung, und Krümmung sind stetig).

4. Speichern Sie die interpolierten $y$-Werte als `y_nearest`, `y_linear`, `y_pchip` und `y_spline` ab.


5. Erstellen Sie einen $2 \times 2$-Subplot, um die Ergebnisse für jede Interpolationsmethode darzustellen. Plotten Sie auch die ursprünglichen Werte hinzu.