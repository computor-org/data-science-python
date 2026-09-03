[meshgrid]: <https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html> "meshgrid"
[3D surface]: <https://matplotlib.org/stable/gallery/mplot3d/surface3d.html> "3D surface"

# Plot eines kreisförmigen Torus

## Einleitung

### Mathematische Grundlagen
Die Oberfläche eines [Torus](http://de.wikipedia.org/wiki/Torus) ist definiert durch:
$$
\begin{aligned}
  x & =  [ R + r \cdot \cos(\theta) ] \cos(\phi) \\
  y & =  [ R + r \cdot \cos(\theta) ] \sin(\phi) \\
  z & =  r \cdot \sin(\theta)
\end{aligned}
$$

mit den folgenden Toruskoordinaten:

* $\phi$: der toroidaler Winkel $\phi \in [0, 2 \pi]$ und entspricht `t` auf Wikipedia.

* $\theta$: der poloidaler Winkel mit $\theta \in [0, 2 \pi]$ und entspricht `p` auf Wikipedia.

* $R$: der Hauptradius, sprich der Abstand vom Mittelpunkt bis zum Mittelpunkt der Röhre.

* $r$: der Nebenradius, sprich der Radius der Röhre.


## Aufgabe

Schreiben Sie nun das Skript `torus`, in dem Sie einen Torus darstellen. 

1. Für die Berechnung der Toruskoordinaten schreiben Sie eine Funktion `torus_coor(phi, theta, r, R)`, die die eindimensionalen Winkel und skalaren Radien als Input nimmt und die zweidimensionalen ([meshgrid]) Koordinaten `x`, `y` und `z` ausgibt.

2. Ploten Sie anschließend die Oberfläche des Torus in einem 3D-Plot, wobei Sie die Stützstellen frei wählen können, sowie die Details der Darstellung im Plot. Die Beschriftung sollte allerdings sinnvoll sein.

3. Achten Sie das die Achsen gleich skaliert sind.

4. Zum Schluss speichern Sie das Bild als `.png`-Datei ab.

## Hinweise
* [meshgrid]
* [3D surface]
* [Color maps](https://matplotlib.org/stable/users/explain/colors/colormaps.html)



<div align="center">
<img src="mediaFiles/torus.png" width="70%" name="Torus"/>
</div>