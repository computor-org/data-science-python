[Python-Klassen]: <https://docs.python.org/3/tutorial/classes.html>
[Python-Objekte]: <https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects>
[Python-Methoden]: <https://docs.python.org/3/tutorial/classes.html#method-objects>
[Python-Erbung]: <https://docs.python.org/3/tutorial/classes.html#inheritance>
[Python-Dunder-Methoden]: <https://docs.python.org/3/reference/datamodel.html#special-method-names>

# Objektorientierte Programmierung in Python

## Einleitung

In dieser Einführung zur objektorientierten Programmierung (OOP) mit Python lernen wir, wie man einfache Klassen definiert, Objekte instanziiert, und die grundlegenden Konzepte der OOP, wie Methodenaufrufe.

### Grundlagen von Klassen in Python

Klassen sind in Python die Bausteine für die objektorientierte Programmierung. Eine Klasse ist eine Vorlage für Objekte, die bestimmt, welche Attribute und Methoden die Objekte haben werden. Hier ist ein einfaches Beispiel einer Klasse in Python:

```python
class MeineKlasse:
    def __init__(self, wert):
        self.wert = wert

    def zeige_wert(self):
        print(self.wert)
mein_objekt = MeineKlasse(10)
mein_zweites_objekt = MeineKlasse(20)
mein_objekt.zeige_wert()  # Gibt "10" aus
mein_zweites_objekt.zeige_wert()  # Gibt "20" aus
```

In diesem Beispiel haben wir eine Klasse `MeineKlasse` definiert, die einen Wert speichert und diesen Wert ausgeben kann. Die Methode `__init__` ist ein spezieller Konstruktor, der aufgerufen wird, wenn ein neues Objekt der Klasse erstellt wird. Das passiert in der Zeile `mein_objekt = MeineKlasse(10)`, wo wir ein neues Objekt `mein_objekt` erstellen und ihm den Wert `10` übergeben. Dann rufen wir die Methode `zeige_wert` auf, um den Wert des Objekts auszugeben.

Der `self`-Parameter ist eine Referenz auf das Objekt selbst und wird automatisch an alle Methoden übergeben. `self` referenzieren die Attribute und Methoden des Objekts, auf das die Methode angewendet wird. Nachdem wir in der Methode `__init__` das Attribut `wert` erstellt haben, können wir darauf in der Methode `zeige_wert` mit `self.wert` darauf zugreifen. `mein_objekt.zeige_wert()` gibt uns also die Variable `wert` des Objekts `mein_objekt` zurück und gibt so `10` aus. `mein_zweites_objekt.zeige_wert()` gibt uns die Variable `wert` des Objekts `mein_zweites_objekt` zurück und gibt so `20` aus.

### Wieso sollte ich Klassen verwenden

Klassen sind ein mächtiges Werkzeug, um komplexe Datenstrukturen und Verhaltensweisen zu modellieren. Sie erlauben es, Daten und Funktionen zu kapseln und zu organisieren, was zu einem klareren und wartbareren Code führt. Klassen ermöglichen auch die effiziente Wiederbenutzung von Code, wie wir später sehen werden. 

## Aufgabe 

### 1. Planetenklasse - `planets_class.py`

Wir möchten eine Klasse erstellen, die einen Planeten repräsentiert und Informationen wie Masse, Durchmesser, Umlaufzeit um die Sonne und Abstand zur Sonne speichert. Diese Klasse soll auch Methoden enthalten, um auf diese Informationen zuzugreifen.

Hier ist die Angabe für das Problem:

1. Schreiben Sie eine Python-Klasse namens `Planet`, die folgende Attribute hat:

- `name`: Name des Planeten (als Zeichenkette)
- `mass`: Masse des Planeten in Kilogramm (als Gleitkommazahl)
- `diameter`: Durchmesser des Planeten in Kilometern (als Gleitkommazahl)
- `orbital_period_around_sun`: Umlaufzeit des Planeten um die Sonne in Tagen (als Gleitkommazahl)
- `distance_from_sun`: Durchschnittlicher Abstand des Planeten von der Sonne in Millionen Kilometern (als Gleitkommazahl)

2. Die Klasse sollte folgende Methoden enthalten:

- `__init__(self, name, mass, diameter, orbital_period_around_sun, distance_from_sun)`: Ein Konstruktor, der die Attribute initialisiert.
- `calc_avg_density(self)`: Eine Methode, die die durchschnittliche Dichte des Planeten berechnet und zurückgibt. Die Dichte eines Planeten wird berechnet, indem die Masse des Planeten durch sein Volumen geteilt wird. 

3. Verwenden Sie die folgenden Werte für die Erde als Beispiel:

- Name: "Earth"
- Masse: 5.972 × 10^24 kg
- Durchmesser: 12.742 km
- Umlaufzeit um die Sonne: 365.24 Tage
- Abstand zur Sonne: 149.6 Millionen km

4. Erstellen Sie dann ein Objekt für die Erde, speicheres in die Variable `earth`.

5. Erstelle auch Objekte für den Merkur, Venus, Mars, Jupiter, Saturn, Uranus und Neptun mit den entsprechenden Werten.  
Speichere die Objekte in den Variablen `mercury`, `venus`, `mars`, `jupiter`, `saturn`, `uranus` und `neptune`.

- Mercury: 3.285 × 10^23 kg, 4.880 km, 87.97 Tage, 57.9 Millionen km
- Venus: 4.867 × 10^24 kg, 12.104 km, 224.7 Tage, 108.2 Millionen km
- Mars: 6.39 × 10^23 kg, 6.779 km, 686.98 Tage, 227.9 Millionen km
- Jupiter: 1.898 × 10^27 kg, 139.822 km, 4,332.59 Tage, 778.6 Millionen km
- Saturn: 5.683 × 10^26 kg, 116.464 km, 10,759.22 Tage, 1,433.5 Millionen km
- Uranus: 8.681 × 10^25 kg, 50.724 km, 30,687.15 Tage, 2,872.5 Millionen km
- Neptune: 1.024 × 10^26 kg, 49.244 km, 60,190.03 Tage, 4,495.1 Millionen km

6. Welcher Planet hat die höchste durchschnittliche Dichte?
Speichere den Namen des Planeten mit der höchsten Dichte in der Variable `planet_with_highest_density`.

### 2. Dictionary - `planets_dict.py`

1. Schreibe die gleiche Funktionalität wie in der vorherigen Aufgabe, aber diesmal verwende ein Dictionary und keine Klasse, um die Informationen über die Planeten zu speichern.

Jeder Planet sollte dabei ein eigenes Dictionary sein und alle Planeten sollten in einem übergeordneten Dictionary `planets` gespeichert werden.

Verwende die gleichen Werte wie in der vorherigen Aufgabe für die Planeten.

3. Berechne die durchschnittliche Dichte jedes Planeten und speichere wieder den Namen des Planeten mit der höchsten Dichte in der Variable `planet_with_highest_density`.