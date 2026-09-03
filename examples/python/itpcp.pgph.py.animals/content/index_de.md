# Tiere

## Einleitung

In dieser Aufgabe sehen wir uns den Vorteil von abstrakten Klassen an. 

Zuerst starten wir aber mit einer Klasse `Animal` und dem bereits bekannten Funktionalitäten: 

## Aufgabe

### 1. Animals Switch (animals_switch.py)
Fülle die offenen TODOs in der animals_switch.py Datei aus.

- Implementiere die `__init__` Methode der Klasse `Animal`.
- Implementiere die `make_sound` Methode der Klasse `Animal`. Unterscheide dazu zwischen den Tieren `dog`, `cat`, `pig` und `frog` wobei die Tiere folgende Sounds machen: 
  - dog: Woof
  - cat: Miau
  - pig: Oink
  - frog: Quack
- Implementiere die `make_sound` Methode der Klasse `Animal` so, dass sie den Sound des jeweiligen Tieres ausgibt.**Wichtig:** Benutze dabei das `match` Statement.
- Überschreibe die `__repr__` Methode der Klasse `Animal` so, dass sie den Namen des Tieres und das Alter des Tieres ausgibt wenn man ein Tier ausgibt -> `print(dog)` sollte `Name: Wuffi, Age: 7` ausgeben.
- Implementiere die `create_animals_from_config(config_file)` Funktion, welche das config (`animals.txt`) file öffnet und die Tiere erstellt. Die Funktion soll eine Liste von Tieren zurückgeben.

### Config File (animals.txt)
In dem config file stehen die Tiere mit ihrem Typ, Namen und Alter jeweils mit einem Leerzeichen getrennt. 

```json
dog Bernd 5
cat Mila 8
dog Dora 7
pig Josh 3
frog Fred 2
```

### 2. Animals Abstract (animals_abstract.py)
Wir nutzen jetzt die Macht von abstrakten Klassen um die Klasse `Animal` zu verbessern und dieses lästige `match` Statement (oder ähnliche `if`-Konstruktionen) loszuwerden.

Implementiere dazu die Klasse `Animal` als abstrakte Klasse und die Klassen `Dog`, `Cat`, `Pig` und `Frog` als Subklassen von `Animal`. Das Gerüst der Klassen ist bereits vorgegeben (mit TODOs): 
- Überschreibe die `__repr__` Methode der Klasse `Animal` so, dass sie den Namen des Tieres und das Alter des Tieres ausgibt wenn
- Implementiere die abgeleiteten Klassen `Dog`, `Cat`, `Pig` und `Frog` so, dass sie den Sound des jeweiligen Tieres ausgeben (make_sound überschreiben)
- Schreibe die `create_animal` Methode in der `AnimalFactory` Klasse so, dass sie das passende Tier erstellt und zurückgibt.
- Implementiere die `create_animals_from_config` Funktion welche das config file öffnet und die Tiere erstellt. Die Funktion soll eine Liste mit den Tieren zurückgeben. Nutze Sie dazu die `AnimalFactory` Klasse um Tiere zu erstellen.

### 3.  Testen der Implementierung
- Es gibt ein Tier des Typs `unicorn` welches klarerweise nicht existiert. Die beiden Implementierungen sollten damit umgehen können und eine entsprechende Fehlermeldung ausgeben. Lass das Programm einmal mit `animals.txt` und einmal mit `exotic_animals.txt` laufen. 
- **Bonus:** schreibe die `create_animals_from_config` Funktion so, dass sie zumindest für die `animals_abstract.py` Implementierung mit nicht existierenden Tieren umgehen kann ohne das Programm zu beenden. Verwende dazu ein `try`-`except` Statement (siehe unten)

```python
try:
    # Code der möglicherweise einen Fehler wirft
except ValueError as e:
    # Code der ausgeführt wird wenn ein Fehler auftritt
```
