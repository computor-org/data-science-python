[solve_ivp]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

# Numerische Lösung von Anfangswertproblemen

## Mathematische Einführung

Für Anfangswertprobleme diskretisieren wir die Zeit mittels $t_n = t_0 + n \Delta t$ und führen die Schreibweise $y_n = y(t_n)$ ein. Damit schreiben wir

$$\begin{align*}
\dot{y}_n &= f(t_n, y_n) \\
y_{n + 1} &= y_n + \int_{t_n}^{t_{n+1}}dt' f(t', y(t')), \end{align*}
$$

was immer noch exakt ist. Das Integral können wir jetzt auf verschiedene Weisen approximieren.


1. Explizites Euler-Verfahren:
$$\int_{t_n}^{t_{n+1}}dt' f(t', y(t')) \approx  f(t_n, y_n) \Delta t$$

2. Mittelpunkt-Verfahren:
$$\int_{t_n}^{t_{n+1}}dt' f(t', y(t')) \approx f(t_{n+1/2}, y_{n+1/2}) \Delta t,$$
wobei wir $y_{n + 1/2}$ als $y_n + f(t_n, y_n) \Delta t / 2$
 approximieren können.



## Physikalische Einführung

Ein einfaches Pendel besteht aus einer Masse $m$, die an einem starren, masselosen Stab oder Faden mit Länge $L$ befestigt ist und sich unter dem Einfluss der Schwerkraft frei bewegen kann. Die Bewegung des Pendels lässt sich durch die Bogenlänge $s$, der Weg den die Masse entlang ihres Kreisbogens zurücklegt, beschreiben. Wie man aus der Skizze sehen kann ist die Kraft entlang von $s$

$$
F_s = -m g \sin(\theta),
$$

wobei $g$ die Gravitationsbeschleunigung und $\theta$ der Winkel zwischen der Vertikalen und dem Pendel ist. Da es sich um eine Kreisbewegung handelt steht $s$ mit $\theta$ über die Gleichung $s = L \theta$ in Verbindung. Die Bewegungsgleichung wird daher zu

$$
m \ddot{s} = -m g \sin(\theta) \\
m L \ddot{\theta} = -m g \sin(\theta) \\
\ddot{\theta} = - \frac{g}{L} \sin(\theta).
$$


<div align="center">
<img src="mediaFiles/pendulum.PNG" alt="Image" width="70%" name="pendulum"/>
</div>


Unsere Methode können jedoch nur gewöhnliche Differentialgleichungen erster Ordnung lösen. Daher müssen wir die gewöhnliche Differentialgleichung zweiter Ordnung in ein System von gewöhnlichen Differentialgleichungen erster Ordnung umwandeln. Dazu führen wir die Variablen $\theta_1 = \theta$ und $\theta_2 = \dot{\theta}$ ein. Damit haben wir

$$
\begin{bmatrix} \dot{\theta_1} \\ \dot{\theta_2}  \end{bmatrix} =
\begin{bmatrix} \theta_2 \\ -\frac{g}{L} \sin(\theta_1) \end{bmatrix} \; .
$$

Das bedeutet, dass die Funktion $f$ im Pendelfall nicht explizit von der Zeit abhängigt und wir die Funktion schreiben können als

```python
def pendulum_ode(t, y, g = 9.81, L = 3.0):
  """
  input:
  t: aktueller Zeitpunkt
  y: Array [theta, omega], bestehend aus dem aktuellen Winkel und der Winkelgeschwindigkeit
  g: Gravitationskonstante (Standardwert: 9.81 m/s^2)
  L: Länge des Pendels (Standardwert: 1.0 m)

  output:
  Array [omega, - (g / L) * np.sin(theta)], die die erste Ableitung von theta bzw. omega darstellt
  """
  theta, omega = y
  return [omega, - (g / L) * np.sin(theta)]
```

wobei $ \omega = \dot{\theta}$ die Winkelgeschwindigkeit ist.

## Aufgabe



  1. Schreiben Sie in `integrators.py` eine Funktion, die das Explizites Euler-Verfahren nach oben angegebener Formel nutzt.
```python
  def euler_explicit(fun, dt, t_max, y_0):
      """
      input:
      fun: Funktion, die das Differentialgleichungssystem beschreibt
      dt: Schrittweite
      t_max: Endzeitpunkt
      y_0: Anfangswerte als Array [theta_0, omega_0]

      output:
      t: Array der Zeitpunkte
      y: Array der Lösungen [theta, omega] zu den Zeitpunkten t
      """
```

2. Schreiben Sie in `integrators.py` analog dazu eine Funktion, die das Mittelpunkt-Verfahren nach oben angegebener Formel nutzt.


```python
  def midpoint(fun, dt, t_max, y_0):
      """
      input:
      fun: Funktion, die das Differentialgleichungssystem beschreibt
      dt: Schrittweite
      t_max: Endzeitpunkt
      y_0: Anfangswerte als Array [theta_0, omega_0]

      output:
      t: Array der Zeitpunkte
      y: Array der Lösungen [theta, omega] zu den Zeitpunkten t
      """
```



3. Nutzen Sie  in `pendulum.py` nun Ihre Funktionen um das Anfangswertproblem zu lösen. Erstellen Sie dazu einen Subplot der den Winkel sowie die Winkelgeschwindigkeit darstellt. Testen Sie verschiedene Zeitschritte `dt` $(\Delta t)$ und Anfangsbedingungen `y_0` aus. Fügen Sie außerdem die Lösungen des Runge-Kutta 45 Verfahren (RK45) von [solve_ivp], sowie die der symplektischen Eulermethode hinzu.


4. Schreiben Sie in `pendulum.py` die Funktion `compute_energy(y, m=2.0, L=3.0, g=9.81,)`, welche die Gesamtenergie des Pendels retourniert (Kinetische- und Potentielle Energie). Dabei soll die potentielle Energie $0$ sein, wenn sich das Pendel in Ruhelage befindet. Plotten Sie die Energie als Funktion der Zeit. Überprüfen Sie ob die Energie konstant bleibt (erhöhen Sie hierfür `t_max`).

### Hinweise

* Referenzplot:
<div align="center">
<img src="mediaFiles/pendulum_solutions.png" alt="Image" width="100%" name="pendulum_solutions"/>
</div>
