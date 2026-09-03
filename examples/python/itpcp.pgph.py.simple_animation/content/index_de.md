[FuncAnimation]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html> "FuncAnimation"
[MatplotlibTutorial]: <https://matplotlib.org/stable/tutorials/introductory/animation_tutorial.html> "Matplotlib Tutorial Animations"
[plt.subplots]: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html> "subplots"

# Animation

## Einleitung

In einem Skript `simpleanim` sollen zwei Kurven animiert werden:

$f_1(x, t) = \cos(x) \cos(t)$

$f_2(x, t) = \cos(x-t)$

Matplotlib-Plots lassen sich auf zwei Arten animieren. Einerseits können Sie in einer Schleife für jeden Zeitschritt abwechselnd die Linie updaten und danach manuell für eine bestimmte Zeit pausieren. Wir verwenden hier allerdings die Matplotlib-Klasse [FuncAnimation], die unter anderem den Vorteil bietet, die Animation als Video exportieren zu können.
Für [FuncAnimation] müssen Sie nur eine update-Funktion definieren, die für jedes Frame die Grafikobjekte updated.
 
## Aufgabe  
  Gehen Sie zur Erstellung der Animation mit [FuncAnimation] wie folgt vor:

1. Erzeugen Sie einen Vektor `x` mit `100` Punkten zwischen `0` und `2`$\pi$.

2. Berechnen Sie `cos_x = cos(x)`.

3. Erzeugen Sie einen Vektor `t` mit `48` Punkten zwischen `0` und $2 \pi$. Dieser Vektor stellt die Zeitskala dar, über die die Animation laufen soll, Berechnen Sie `cos_t = cos(t)`.

4. Vor der eigentlichen Animation erzeugen Sie eine figure mit [plt.subplots].
Speichern Sie in `line1` und `line2` die Plot-handles von zwei lines (plt.plot), wobei sowohl die `x_data` als auch die `y_data` leer
 sein sollen (`[]`). Geben Sie als Label jeweils die Funktionsdefinition für $f_1$ und $f_2$ (siehe oben) an und erzeugen Sie die Legende.
 Die Daten für die Linien werden während der Animation geupdated.

5. Setzen Sie die Achsenlimits für `x` und `y` auf das Minimum und Maximum von `x`, bzw. auf `-1` und `1`.

6. [FuncAnimation] benötigt nun eine Funktion, welche für jeden Zeitschritt die Plots updated.
Die Funktion bekommt als Argument die aktuelle Frame-Zahl, welche als Index für die Zeitwerte `t` genommen werden kann. Die Plot-handles müssen als Rückgabewerte zurückgegeben werden.
```python
def update(frame_num):
    """ for each frame, update the data stored on each artist. """

    line1.set_xdata(x)
    line1.set_ydata(f(t[frame_num]))

    # line2.set_...
    #

    return (line1, line2)
```
Hier wird die Funktion `f(t)` für die `y`-Werte vorausgesetzt.

7. Nun können Sie ein Objekt der Klasse [FuncAnimation] erstellen, dem Sie die Figure, die update-Funktion, eine Anzahl an Frames (hier 48), und ein Interval (hier 16) übergeben. Übergeben Sie außerdem das Argument `blit=True`. Anschließend können Sie mit `plt.show()` die Animation anzeigen. Eventuell funktioniert die Darstellung nur wenn Sie das Skript in einem Python Terminal ausführen und nicht im Interactive Mode. Mehr dazu siehe [MatplotlibTutorial].


8. Exportieren Sie mit
    ```python
    ani.save(filename="cos_animation.gif", writer="pillow")
    ```
    ein Gif der Animation, wobei `ani` das FuncAnimation-Object ist.


## Hinweise

* Alle Graphikbefehle in Matplotlib haben als Rückgabewert eine Referenz, die einen späteren Zugriff auf das erstellte Objekt ermöglicht. Damit kann man also alle Eigenschaften von Graphikobjekten nach deren Erzeugung verändern. Dies gilt natürlich auch für die Daten von Linien um die Animation zu beeinflussen.
