# Steuerstrukturen: Die for-Schleife

In dieser Aufgabe sollen von Ihnen quadratische
Gleichungen einmal mithilfe einer `for`-Schleife und einmal mithilfe von logischer Indizierung gelöst werden.

## Mathematische Grundlagen

Eine quadratische Gleichung der Form

$$
    ax^2 + bx + c = 0 \qquad a,b,c \in \mathbb{R}
$$

hat folgende Lösungen

$$
  \begin{aligned}
    x_{1,2} &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    && a \neq 0 \\
    x_{1} &= -\frac{c}{b}
    && a = 0 \wedge b \neq 0 \\
    x_{1} &= 0 \qquad \text{triviale Lösung}
    && a = 0 \wedge b = 0 \wedge c = 0
  \end{aligned}
$$

Der Ausdruck

$$
    d = b^2 - 4ac
$$

wird dabei als Diskriminante bezeichnet. Im Falle $a \neq 0$ entscheidet ihr Wert, ob es
zwei reelle Lösungen, eine reelle Doppellösung, oder zwei konjugiert komplexe Lösungen
gibt. Wir definieren, dass $x_1$ die Lösung mit $+$ und $x_2$ die Lösung mit $-$ ist.

Für den Fall

$$
    a = 0 \wedge b = 0 \wedge c \neq 0
$$

gibt es keine Lösung.

## Aufgabe

### For-Schleife
Erstellen Sie das Python-Skript `quadratic_eq_for`, welches die Funktion `quadratic_eq_for`
beinhaltet, die mit dem Aufruf

```python
def quadratic_eq_for(a, b, c):
    # ...
    return x_1, x_2
```

die quadratische Gleichung mit den Koeffizienten `a`, `b` und `c` löst.

1. Die Koeffizienten `a`, `b` und `c` sind Arrays gleicher Größe mit reellen Zahlen.
   Damit ist es möglich, die Gleichung für mehrere Werte der Koeffizienten gleichzeitig
   zu lösen.

1. Die Ergebnisse sollen wie in den *Mathematischen Grundlagen* erläutert berechnet und
   in den Arrays `x_1` und `x_2` gespeichert werden. `x_1` und `x_2` müssen anschließend die
   gleiche Größe wie die Eingabeparameter haben und enthalten gegebenenfalls **komplexe
   Werte**. Für den Fall, dass nur eine Lösung existiert, sollte das zweite
   Rückgabeargument auf den Wert [nan] gesetzt werden.

1. Zur Lösung des Problems sind eine `for`-Schleife, `if` und `elif` zu verwenden und es
   empfiehlt sich folgende Strategie:

   - Legen Sie für `x_1` und `x_2` Arrays der Größe von `a` an und beschreiben Sie diese
     überall mit dem Wert [nan] (verwenden Sie dafür z.B. [ones_like]). Achten Sie darauf, dass die Arrays den richtigen Datentyp haben, damit sie später auch komplexe Werte speichern können.
   - Gehen Sie anschließend in einer Schleife alle Werte der Arrays `a`, `b`, `c` durch,
     machen Sie eine Fallunterscheidung bezüglich der aktuellen Parameter, berechnen Sie
     demnach die Lösungen $x_1$ (und $x_2$) und speichern Sie diese auf der
     entsprechenden Stelle in `x_1` (bzw. `x_2`). Machen Sie **keine** Fallunterscheidung bezüglich der Diskriminante!

1. Um die Funktion zu überprüfen, legen Sie im selben Skript nach der Funktion folgende
   Arrays an:

$$
  \begin{aligned}
    a &= [0, 1, 2, 3, 4, \dotsc, 10] \\
    b &= [1, 2, 4, 8, 16, \dotsc, 1024] \\
    c &= [0, 1, 4, 9, 16, \dotsc, 100] \\
  \end{aligned}
$$

5. Rufen Sie danach Ihre Funktion mit diesen Koeffizienten auf und überprüfen Sie das
   Ergebnis auf Plausibilität.
  
### Logische Indizierung
Erstellen Sie das Python-Skript `quadratic_eq`, welches die Funktion `quadratic_eq`
beinhaltet, die mit dem Aufruf

```python
def quadratic_eq(a, b, c):
    # ...
    return x_1, x_2
```

die quadratische Gleichung mit den Koeffizienten `a`, `b` und `c` löst.

1. Der Beginn der Aufgabe gleicht dem vorherigen Beispiel mit `for`-Schleife. Zur Lösung des Problems ist diesmal *logische Indizierung* zu verwenden und es empfiehlt sich folgende Strategie:

   - Legen Sie für `x_1` und `x_2` Arrays der Größe von `a` an und beschreiben Sie diese
     überall mit dem Wert [nan] (verwenden Sie dafür z.B. [ones_like]). Achten Sie auch hier darauf, dass die Arrays den richtigen Datentyp haben, damit sie später auch komplexe Werte speichern können.
   - Machen Sie anschließend mittels logischer Indizierung eine Fallunterscheidung bezüglich der aktuellen Parameter mit der Sie demnach die Lösungen $x_1$ (und $x_2$) berechnen und diese auf der
    entsprechenden Stelle in `x_1` (bzw. `x_2`) speichern. Machen Sie **keine** Fallunterscheidung bezüglich der Diskriminante!

1. Um die Funktion zu überprüfen, legen Sie im selben Skript nach der Funktion folgende
   Matrizen an:

```python
a = np.reshape(np.arange(-5, 7), (3, 4))
b = a + 1
c = a - 1
```

5. Rufen Sie danach Ihre Funktion mit diesen Koeffizienten auf und überprüfen Sie das
   Ergebnis auf Plausibilität.

Drei Dinge sollte man sich noch überlegen und berücksichtigen:

- Warum ist es besser die Diskriminante nur einmal zu berechnen und dann in der Formel
  für $x_{1,2}$ zu verwenden? Ist es eigentlich nicht auch besser, vorher die Wurzel aus der Diskriminante zu ziehen
  um dann gleich diese Größe in der Formel für $x_{1,2}$ zu verwenden?
- Kann die Diskriminante auch negativ werden? Inwiefern ist dies zu berücksichtigen?
- Wie könnte man die `for`-Schleifen Variante so anpassen, dass sie auch mehrdimensionale Indizierung unterstützt?

## Hinweise

- Wenn Sie die Arrays anfangs mit `nan`-Einträgen erzeugen, müssen Sie im Fall einer
  nicht existenten Lösung natürlich nicht noch einmal `nan` in das Array speichern.

- Sie können mit `np.sqrt()` auch die Wurzel von negativen Zahlen ziehen, indem Sie
  `dtype=np.complex128` hinzufügen. Zum Beispiel `np.sqrt(-1, dtype=np.complex128)`.

- Beispiele für einen $x_1$ output könnten so aussehen:

```python
[-0.00000000e+00       +0.j          1.19160798e+01       +0.j
  7.19722115e+01       +0.j          5.75994792e+02       +0.j
  5.18399923e+03       +0.j          4.97663999e+04       +0.j
  4.97664000e+05       +0.j          5.11882971e+06       +0.j
  5.37477120e+07       +0.j          4.45514108e+08       +0.j
  3.09586821e+09+88920960.46646732j]
```

```python
[ 0.        +0.j         -0.5       +0.8660254j  -0.25      +1.39194109j
 -0.16666667+1.72401341j -0.125     +1.99608993j -0.1       +2.23383079j
 -0.08333333+2.4480718j  -0.07142857+2.64478694j -0.0625    +2.82773651j
 -0.05555556+2.99948555j -0.05      +3.16188235j]
```

**Achtung!** Das ist nicht die korrekte Lösung, andere Werte für a, b, und c wurden
verwendet.

[nan]: https://numpy.org/doc/stable/user/misc.html "nan"
[ones_like]: https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html "ones_like"
