[Lohnsteuer]: <https://www.finanz.at/steuern/lohnsteuertabelle/#Lohnsteuertabelle_2024> "Lohnsteuer - finanz.at"
[Sozialversicherung]: <https://www.gesundheitskasse.at/cdscontent/?contentid=10007.870462> "Sozialversicherung - sozialversicherung.at"
# Brutto Netto Rechner

## Einleitung

In dieser Aufgabe wird es darum gehen einen Funktion zu implementieren, welche basierend auf einem gegebenen Bruttobetrag den Nettobetrag berechnet. Folgende Informationen zum Österreichischem Steuersystem sind dabei relevant:

### Lohnsteuertabelle

In Österreich gilt folgende Lohnsteuertabelle: 
| (Jahres-) Einkommen (2024) | Steuersatz (2024) |
|------------------|-------------------|
| bis 12.816 Euro | 0 % |
| bis 20.818 Euro | 20 % |
| bis 34.513 Euro | 30 % |
| bis 66.612 Euro | 40 % |
| bis 99.266 Euro | 48 % |
| bis 1.000.000 Euro | 50 % |
| ab 1.000.000 Euro | 55 % |

Wichtig die Steuerstufen sind progressiv: sprich auf die ersten 12.816€ zahlt man keine Steuern schließlich 20% usw. 

Siehe auch [Lohnsteuer]. 

### Sozialversicherung 

Für die Sozialversicherung wird vom Bruttolohn **vor** Steuer **ab** einem Einkommen von **über 518€ (monatlich) 18,12% abgezogen**. Die **Höchstbeitragsgrundlage sind 6.060€ pro Monat**, man zahlt also maximal 13.176,86€ (6.060 * 12 * 0,1812) Sozialversicherung im Jahr. Alle weiteren Einkommen über 72720€ (6.060 * 12) erhöhen somit den SV-Beitrag nicht weiter. 

Anmerkung: Die Regeln zum SV-Beitrag wurden leicht angepasst. 

Siehe auch [Sozialversicherung].

### Beispiel 21.000€ Bruttojahreseinkommen

21.000 * 18,12% = 3.805,20€ (SV-Beitrag - unter Höchstbeitragsgrundlage von 72720€ p.a. aber über 518€ pro Monat)
Steuergrundlage = 17.194,8€
bis 12.816€ -> 12.816 * 0% = 0
bis 20.818€ -> 4.378,8 * 20% = 875,76
Steuern gesamt: 875,76

Nettolohn: 16.319,04€


## Aufgabe
1. Schreiben Sie eine Funktion die einen Bruttogehalt (float) nimmt und den zugehörigen Nettogehalt auf den nächsten Cent gerundet ausgibt. 


## Hinweise

* Relevant für unsere Berechnung hier ist lediglich die Lohnsteuer vom Bruttobetrag abzüglich der Sozialversicherung. Es handelt sich hier um eine abgewandelte Formel zur tatsächlich verwendeten. 