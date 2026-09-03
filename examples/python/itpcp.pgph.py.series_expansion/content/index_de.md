[np.shape]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html> "shape"
[np.ravel]: <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html> "ravel"
[np.meshgrid]: <https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html> "meshgrid"

# Sinus Reihenentwicklung

## Einleitung

In dieser Übung lernen Sie eine neue Methode zur Reihenberechnung kennen.

Als einfaches Beispiel für eine unendliche Reihe wird hier die Taylorreihe der Funktion sin($x$) verwendet. Diese ist gegeben durch

$$
\begin{aligned}
  \sin(x)
  &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots \\
  &= \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
  \; ,
\end{aligned}
$$

welche für alle $\lvert x \rvert < \infty$ konvergiert.
Solche unendlichen Reihen kann man am Computer durch endliche Partialsummen näherungsweise berechnen. Abhängig von der gewählten Reihe und von den Werten für $x$, konvergieren sie langsamer, schneller oder eben gar nicht zum gewünschten Wert.

Summen dieser Art kann man in NumPy sehr gut ohne die Verwendung von for-Schleifen programmieren. Nützlich sind dabei folgende Informationen:

Äußerst praktisch für die Berechnung solcher Reihen ist der Befehl [np.meshgrid]. Damit kann man aus einem Vektor `x` mit allen $x$-Werten und einem Vektor `k` mit allen $k$-Werten zwei gleich große Matrizen erzeugen:

```python
x = np.arange(-2, 3)    # -2 bis 2
k = np.arange(0, 6)     # 0 bis 5
xx, kk = np.meshgrid(x, k)
```

```python
>>> xx
array([[-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2],
       [-2, -1,  0,  1,  2]])

>>> kk
array([[0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5]])
```

Mit dem Befehl

```python
A = xx ** (2 * kk + 1)
```

kann man nun z.B. $x^{2k+1}$ für alle Werte von $x$ und $k$ gleichzeitig
ausrechnen.

```python
>>> A
array([[   -2,    -1,     0,     1,     2],
       [   -8,    -1,     0,     1,     8],
       [  -32,    -1,     0,     1,    32],
       [ -128,    -1,     0,     1,   128],
       [ -512,    -1,     0,     1,   512],
       [-2048,    -1,     0,     1,  2048]])
```

Die Summe über alle $k$-Werte kann man dann mit Hilfe des `np.sum`-Befehles erhalten, wobei die Dimension entlang derer summiert werden soll über das Schlüsselwort `axis` angegeben wird. Hier wollen wir entlang der Zeilen (Achse 0) summieren, sodass pro $x$-Wert ein Eintrag bleibt:

```python
>>> S = np.sum(A, axis=0)
>>> S
array([-2730,    -6,     0,     6,  2730])
```

Dabei wird jedes Element von `S`, ($\{S\}_{x}$) durch Aufsummieren über die $x$-Spalte berechnet

$$\{S\}_{x} = \sum_{k = 0}^{n} A_{k, x} = A_{0, x} + \dotsb + A_{n, x} \; .$$

Da NumPy auf Rechnen mit Matrizen optimiert ist, läuft das Programm bei größeren Datenmengen so wesentlich schneller als mit den sonst üblichen for-Schleifen.

Statt mit der Summe kann die gesamte Reihenauswertung auch mit Hilfe der Matrizenmultiplikation durchgeführt werden. Aus der linearen Algebra ist bekannt, dass für einen $(1 \times n)$-Vektor $f$ (Zeilenvektor) und eine $(n \times m)$-Matrix $A$ gilt

$\{f \cdot A\}_{l} = \sum_{k} f_{k} A_{kl} \; . $

Erzeugt man nun für alle Werte von $k$ den Vektor $f = (−1)^{k} / (2k + 1)!$, kann man mit
$f \cdot A$ (in Python `f.dot(A)`) für alle Werte von $x$ gleichzeitig den jeweiligen Wert der Teilsumme erhalten. (Mit diesen speziellen Beispielen für $A$ und $f$ bekommt man die Reihenentwicklung für den Sinus.)

## Aufgabe

Schreiben Sie eine Funktion `series_expansion`, die mit

```python
r, u = series_expansion(x, n)
```

aufgerufen wird. `x` ist ein beliebiges Array aus $x$-Werten, für die die Reihe
ausgewertet werden soll. `n` (Skalar) ist der Index, bis zu dem summiert werden
soll. Der Rückgabewert `r` soll die $n$-te Partialsumme

$$
  r(x) = \sum_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!}
$$

sein. Für `u` soll außerdem der analytische Wert der Funktion

$$
u = \sin(x).
$$

berechnet werden. Gehen Sie wie folgt vor:

1. Speichern Sie sich die Größe von `x` ([np.shape]) in einer Variable und wandeln Sie anschließend die Variable in einen Vektor um ([np.ravel]). Die weiteren Rechnungen sind mit einem Vektor angenehmer und durch das Speichern der ursprünglichen Größe geht keine Information verloren.

2. Verwenden Sie für die Berechnung der Reihe den Befehl [np.meshgrid], wie in der Einleitung beschrieben. Dadurch erübrigen sich for-Schleifen. Speichern Sie das Ergebnis der $n$-ten Partialsumme in `r`.

3. Berechnen Sie den analytischen Wert für `u`.

4. Formen Sie mit der zuvor gespeicherten Variable die Vektoren `r` und `u` so um, dass sie die ursprüngliche Größe von `x` haben.

5. Berechnen und plotten Sie für $x \in [-\pi, \pi]$ (gleichverteilt mit 100 Stützstellen) die analytische Funktion zusammen mit den ersten 3 Partialsummen (also für $n = 0, 1, 2$). Verwenden Sie für die Partialsummen eine Schleife. Plotten Sie die analytische Funktion als gestrichelte Linie (`linestyle`-Argument) und lassen Sie die Partialsummen in der voreingestellten durchgezogenen Linie. Erstellen Sie eine Legende mit den Beschriftungen `'sin(x)'`, `'1. partial sum'`, `'2. partial sum'`, `'3. partial sum'` (in dieser Reihenfolge; $n = 0$ entspricht der 1. Partialsumme).