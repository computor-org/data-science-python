[diag]: <https://numpy.org/doc/stable/reference/generated/numpy.diag.html> "diag"
[eye]: <https://numpy.org/devdocs/reference/generated/numpy.eye.html> "eye"
[isclose]: <https://numpy.org/doc/stable/reference/generated/numpy.isclose.html> "isclose"
# Lineare Gleichungssysteme, Diagonalmatrix, Probe

## Einleitung

In dieser Aufgabe soll ein lineares Gleichungssystem gelöst werden. Das Ergebnis wird mithilfe einer Probe untersucht.

## Aufgabe
Schreiben Sie ein Skript `linalg_diag_matrix`, welches ein gegebenes Gleichungssystem löst und das Ergebnis einer Probe unterzieht.


1. Lesen Sie eine Variable `n` mithilfe von input ein. Stellen Sie sicher, dass `n` ein integer ist. Falls `n` kein integer ist, setzen Sie `n` = $5$.

2. Erstellen Sie eine $2n \times 2n$ Matrix `A`, deren Hauptdiagonale aus Einsern besteht und deren Nebendiagonalen ausschließlich `0.5` enthalten. Erzeugen Sie diese Matrix mit den Befehlen [eye] und [diag].
    $$
      A = 
      \begin{bmatrix}
        1      & 0.5    & 0      & 0      & \ldots \\
        0.5    & 1      & 0.5    & 0      & \ldots \\
        0      & 0.5    & 1      & 0.5    & \ldots \\
        0      &  0     & 0.5    & 1      & \ldots \\
        \vdots & \vdots & \vdots & \vdots & \ddots
      \end{bmatrix}
    $$

3. Erzeugen Sie mit anschließend den Vektor `b` mit folgender Gestalt:
    $$
      \mathbf{b} = 
      \begin{bmatrix}
        0 \\
        1 \\
        0 \\
        2 \\
        0 \\
        3 \\
        \vdots \\
        0 \\
        n \\
      \end{bmatrix}
    $$


4. Lösen Sie nun das lineare Gleichungssystem $\mathbf{Ax} = \mathbf{b}$ und speichern Sie den Lösungsvektor in `x`.

5. Machen Sie die Probe $\mathbf{Ax - b}$ und speichern Sie diese Differenz in `check` (sollte im Idealfall $\mathbf{0}$ sein).
    
6. Überprüfen Sie, ob `check` tatsächlich ausschließlich Nullen enthält: Geben Sie den logischen Vektor dieses Vergleichs in der Form `check: 'Werte des Vergleichs'` formatiert aus. Das könnte bspw. so aussehen:       
	
            check: [1 0 0 0 1 0 0 1 1 1]

	Enthält er nur Einser? Warum nicht?
  
7. Führen Sie eine sinnvollere Art der Probe aus. 


## Hinweise

* Bei der Ausgabe von `check` sieht man, dass diese Probe fehlschlägt. Dies liegt daran, dass durch die endliche Genauigkeit der Zahlen stets Rundungsfehler auftreten. Aus diesem Grund ist es **nicht sinnvoll** auf **Gleichheit** zu prüfen. Es macht lediglich Sinn auf **beinahe Gleichheit** zu prüfen. Dazu kann der *relative* oder der *absolute* Fehler verwendet werden. Hier soll eine absolute Fehlerschranke verwendet werden. 

		error_limit = 1E-8

    Auch nutzen kann man hier die numpy Funktion [isclose]! Damit ist nun die Durchführung einer sinnvollen Probe der Form
    ```python
    if ...:
        print('Check successful')
    else:
        print('Check unsuccessful')
    ```
    möglich.