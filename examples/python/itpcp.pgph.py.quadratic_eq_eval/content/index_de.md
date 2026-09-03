# Berechnung der linken Seite einer quadratischen Gleichung

## Einleitung

Mithilfe der Funktion `quadratic_eq` haben Sie in einem früheren Beispiel bereits die Lösungen der Gleichung
$$
    ax^2 + bx + c = 0 \qquad a,b,c \in \mathbb{R}
$$
berechnet. Man würde also erwarten, dass man `0` erhält, wenn man die Lösungen $x$ in die Gleichung einsetzt. Dies ist wegen numerischer Ungenauigkeiten jedoch nicht immer der Fall.

## Aufgabe

Schreiben Sie die Funktion

```python
def quadratic_eq_eval(a,b,c,x1,x2):
    # ...
    return r1, r2
```

welche die linke Seite dieser Gleichung für gegebenes `x1` und `x2`, bzw. Koeffizienten `a`, `b`, `c` berechnet und in `r1` bzw. `r2` speichert. D.h. realisieren Sie folgende Formel:

  $$
    r_{1,2} = ax_{1,2}^2 + bx_{1,2} + c \qquad a,b,c \in \mathbb{R}
  $$

## Hinweise

- **Vorschau nächstes Beispiel:**
  Mit Ihrer Funktion können Sie nun überprüfen, wie gut die Gleichung durch `quadratic_eq` gelöst wird: Übergibt man die (gleich großen) arrays `a`, `b`, `c`, sowie die zugehörigen Lösungen `x1` und `x2` (berechnet mit `quadratic_eq`), so kann man beurteilen, wie nahe das Ergebnis bei Null liegt.

* Mit [nan] kann man normal rechnen, wobei jede
 arithmetische Operation mit [nan] wieder [nan] ergibt.