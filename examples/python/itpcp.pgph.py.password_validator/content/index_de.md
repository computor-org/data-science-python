# Password Validator

## Einleitung

In der folgenden Aufgabe sollen Sie ein einfaches Skript programmieren, das die Stärke eines eingegebenen Passworts überprüft.
Die Stärke wird dabei nach folgenden Kriterien erhoben:

- Das Passwort muss mindestens 8 Zeichen lang sein.
- Es muss mindestens eine Zahl, ein Sonderzeichen und einen Großbuchstaben enthalten.
- Es darf keine fortlaufenden oder sich wiederholenden Zahlen oder Buchstaben (`abcd`, `1234`, `55555`) enthalten (ab 4 Zeichen). Sprich (`abc`, `123`, `555`) sind erlaubt, aber nicht (`abcd`, `1234`, `55555`). Des weiteren ist aber `ABCdEFG` erlaubt, da die Großbuchstaben nicht fortlaufend sind (weil sie von einem Kleinbuchstaben unterbrochen werden). `ABCDEF` wäre jedoch nicht erlaubt, da die Buchstaben fortlaufend sind.

## Aufgabe

Schreiben Sie im Script `check_password.py` die Funktion `check_password(pw)`, die einen `string` als mögliches Passwort einliest und oben genannten Kriterien abprüft.
Diese Funktion soll nichts zurückgeben! Gehen Sie folgendermaßen vor:

1. Prüfen Sie die Kriterien mit `if` und/oder `elif`/`else` Statements ab.
1. Um zu überprüfen, ob das Passwort Sonderzeichen, Zahlen und Großbuchstaben enthält, können Sie das Modul [string] importieren und mit den dort definierten Formaten arbeiten (z.B. mit `string.digits`).
1. Sie können dann über die Ziffern/Großbuchstaben/Sonderzeichen iterierten und überprüfen, ob mindestens eines davon im vorgeschlagenen Passwort vorhanden ist. Wenn die Kriterien nicht erfüllt sind, sollen folgende strings in der Konsole ausgegeben werden:
   - Weniger als 8 Zeichen: *"Password too short!"*
   - Keine Zahl: *"Password contains no number!"*
   - Kein Sonderzeichen: *"Password contains no special character!"*
   - Keine Großbuchstaben: *"Password contains no uppercase letter!"*
   - fortlaufende oder sich wiederholende Zahlen/Buchstaben: *"Password contains more than 3 consecutive or repeated characters!"*
1. Die logische Überprüfung ob *keines* der definierten Zeichen vorhanden ist, kann elegant mit den keywords [all] und `not` gelöst werden.
1. Wenn alle Kriterien erfüllt sind, soll in der Konsole *"Strong password"* ausgegeben werden.

## Hinweise

- Wenn Sie mit dem [string]-Modul arbeiten und etwa die Ziffern '0123456789' in eine Liste aus einzelnen Digits umwandeln wollen, können Sie dies mit dem `*`-Operator tun:

```python
s = "0123"
print ([*s])
>>> ["0", "1", "2", "3"]
```

Der `*`-Operator *entpackt* dann die einzelnen Ziffern und Sie können über die Einträge iterieren.

- mit ord() können Sie den ASCII-Wert eines Zeichens herausfinden. So ist z.B. der ASCII-Wert von 'A' = 65, 'B' = 66, ..., 'Z' = 90.
  Fortlaufende Buchstaben können Sie also überprüfen, indem Sie den ASCII-Wert der Buchstaben vergleichen.

- Testen Sie die Stärke folgender Passwörter:

| Passwort  | Ergebnis |
| ---    | ----------   |
| asd   | Password too short!  |
| passwortneu   | Password contains no number!   |
| passwortneu25   | Password contains no special character!   |
| passwortneu25!   | Password contains no uppercase letter!    |
| Passwortneu25!  | Strong password  |
| Passsswortneu25!   | Password contains more than 3 consecutive or repeated characters!   |
| Passwortneu2222! | Password contains more than 3 consecutive or repeated characters! |
| abcd_Passwortneu25! | Password contains more than 3 consecutive or repeated characters! |

[all]: https://docs.python.org/3/library/functions.html#all "all"
[string]: https://docs.python.org/3/library/string.html "string"
