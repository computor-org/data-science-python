[lists]: <https://python-reference.readthedocs.io/en/latest/docs/list/> "lists"

# Vokal oder Konsonant

## Einleitung

Schreiben Sie eine Python-Funktion `if_vocal`, die Folgendes ausgibt:

```python
result = if_vocal(character)
```

| **InOut** | **Name** | **Description** | **Type** |
|-|-|-|-|
| Input | `character` | Beliebiger Buchstabe (groß oder klein geschrieben) | `str` |
| Output | `result` | Zeichenkette *Vowel* oder *Consonant* | `str` |

## Aufgabe

1. Diese Funktion liefert als Ausgabewert den String `'Consonant'` oder `'Vowel'`.

2. Der Eingabewert `character` kann sowohl ein Groß- als auch ein Kleinbuchstabe sein.

3. Überlegen Sie, welche Entscheidungsstruktur hier am ehesten geeignet ist.

4. Vokale sind: `a,ä,e,i,o,ö,u,ü`

## Hinweis

### Listen


Eine einfache Methode, um zu überprüfen ob ein Element (z.b. eine Zahl oder auch ein String) in einer Liste vorhanden ist, ist die folgende:

```python
found_4 = 4 in [1, 2, 3, 4, 5]    # This will be True
```

Wir können ebenso nach Strings suchen:

```python
def isInList(test_var, my_list):
    if test_var in my_list: 
        print('Variable gefunden!')
        return True
    else: 
        print('Nicht gefunden!')
        return False


isInList('ab', ['Was geht ab', 4, 'Name'])
>>> Nicht gefunden!

isInList('ab', ['Was geht ab', 'ab', 4, 'Name'])
>>> Variable gefunden!
```

* Beachten Sie, dass im ersten Fall der Sub-String `'ab'` nicht gefunden wurde!

* Verwenden Sie diese Methode in diesem Beispiel um unübersichtliche `if` Abfragen zu vermeiden!

