# Gaussverteilung

## Einleitung

### Mathematische Grundlagen

In der Wahrscheinlichkeitsrechnung und auch in der Physik hat die Normalverteilung bzw. Gaussverteilung eine große Bedeutung. Sie ist definiert durch

$$
\begin{align}
g(x)= \frac{1}{{\color{red}\sigma} \sqrt{2\pi}} \exp\left\{-\frac{(x-{\color{red}x_{0}})^2}{2 \color{red}\sigma^2}\right\} \; ,
\end{align}
$$

wobei $x_{0}$ und $\sigma$ die Parameter der Verteilung sind. In $x_{0}$ liegt sowohl das Maximum als auch das Symmetriezentrum, und $\sigma$ ist der Abstand von diesem Zentrum zu den Wendepunkten. Wie für jede Wahrscheinlichkeitsverteilung gilt

$$
\begin{align}
\int_{-\infty}^{\infty} g(x) \, \mathrm{d} x = 1 \; .
\end{align}
$$

In der Physik verwendet man häufig auch eine Summation über mehrere Gaussfunktionen mit jeweils unterschiedlichen Parametern. Dies hat den Sinn, dass man gleichzeitig mehrere Maxima darstellen kann. Allgemein kann man die Funktion dann definieren als 

$$
\begin{align}
g(x)= \frac{1}{n} \sum_{k=1}^{n} \frac{1}{{\color{red}\sigma_k} \sqrt{2\pi}} \exp\left\{-\frac{(x-{\color{red}x_{0k}})^2}{2 \color{red}\sigma_k^2}\right\} \; ,
\end{align}
$$

wobei $x_{0k}$ und $\sigma_k$ die gleiche Bedeutung wie vorher haben. Die Summation erfolgt über alle $ n$ Werte der Parameter $x_{0k}$ und $\sigma_k$. Daher wird – um die Normierung aufrechtzuerhalten – noch durch $n$ dividiert.


## Aufgabe

Es sind von Ihnen zwei Files zu erstellen:

### Funktion

Schreiben Sie eine Funktion `gauss1d`, die mit folgendem Aufruf

```python
g = gauss1d(x, x0, sig)
```

die Gaussverteilung als Funktion des Vektors `x` berechnet.

1. Setzen Sie die Default-Werte

    ```python
        x0 = [-1.0, 1.0]
        sig = [ 0.5, 1.0]
    ```
      
2. Initialisieren Sie `g` als Feld mit Nullen in der Größe von `x`.

3. Bilden Sie die Summe über alle $k$-Werte der Parameter ($k = 1, \dotsc, n$) mit
  Hilfe einer einzigen for-Schleife. Vergessen Sie dabei nicht,
  dass $x$ ein Array sein kann.
    
### Skript

Schreiben Sie ein Skript `gauss1d_script.py` und erledigen Sie folgende
Aufgaben:

1. Erzeugen Sie einen Zeilenvektor `v` mit `400` Werten zwischen `-5` und `5`.

2. Definieren Sie `max_val = [-2,0,2,4]`.

3. Definieren Sie `sig_val = [0.5,0.25,0.125,0.0625]`. Überlegen Sie, wie man diesen Vektor 
  leicht, ohne die Werte so hinzuschreiben, erzeugen kann!

4. Berechnen Sie unter Verwendung dieser Werte mit `gauss1d` die Variable `y`.

5. Plotten Sie `y(v)`.


## Hinweise

* Eine for-Schleife hilft bei der Summation über
  die einzelnen Beiträge zur Summe. Dabei ist es
  praktisch, wenn man noch vor der Schleife ein Feld erzeugt, das gleich
  groß ist wie die Inputvariable `x`, das aber ausschließlich Nullen
  enthält. Der sinnvollste Befehl dafür ist:

    ```python
    g = np.zeros(x.shape)   
    ```
        
  Dann kann man in der Schleife `g = g + ...` (oder mit *compound assignment* auch `g += ...`)
  schreiben und bei jedem Durchlauf werden die Werte für einen Peak
  addiert. Nach dem Ende der Schleife muss man durch die Anzahl der Peaks
  `n`, also durch die Länge des Vektors `x0` (oder `sig`),
  dividieren. Damit ist dann die Normierung auch bei mehreren Peaks
  sichergestellt. 

