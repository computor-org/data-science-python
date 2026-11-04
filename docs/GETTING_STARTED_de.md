# Lernen mit Computor

Die drei Kurse der Reihe „Data Science mit Python“ sind in der
[Kursaufteilung](../COURSE_MAP.md) aufgeführt. Die Aufgabenstellung einer Übung steht in
ihrem Ordner in `content/index_de.md` (englisch: `content/index_en.md`). Um das
öffentliche Material zu lesen, brauchst du kein Konto. Musterlösungen für Lehrende
und nicht öffentliche Bewertungstests werden getrennt aufbewahrt.

## VS Code auf dem Desktop

Installiere Python 3.12 und VS Code. Klone das Repository
[data-science-python](https://github.com/computor-org/data-science-python), öffne seinen Ordner und
installiere die Erweiterung **Computor** des Herausgebers `computor-org`. Führe in
einer virtuellen Python-Umgebung `python -m pip install --require-hashes -r requirements.lock`
aus. Kopiere mitgelieferte Vorlagen für Studierende und Eingabedateien, soweit es sie
gibt, in einen Arbeitsordner und führe deinen Code lokal aus. Manche Übungen beginnen
mit einer leeren Datei. Deine Umgebung prüfst du mit `python -m pytest tests`.

## GitHub Codespaces

[Erstelle einen Codespace](https://codespaces.new/computor-org/data-science-python?quickstart=1).
Dafür brauchst du ein GitHub-Konto, und es gelten das Kontingent und die Abrechnung von
GitHub. Die vorbereitete Entwicklungsumgebung des Codespace installiert die fest versionierten Python-Abhängigkeiten und
die Computor-Erweiterung. Dein Code läuft in deinem Codespace und nicht auf den Servern
von Computor. Ein KI-Modell wird nicht installiert.

## Kurse und Lena

Melde dich bei Computor an, um einem Kurs beizutreten, deinen Fortschritt zu speichern,
deine Arbeit abzugeben und Lena in den Kursnachrichten um Hinweise oder Rückmeldungen zu
bitten. Ein gehosteter Arbeitsbereich ist optional: Wenn dessen Kapazität ausgeschöpft
ist, kannst du in VS Code auf dem Desktop oder in Codespaces weiterarbeiten. Lena
verarbeitet Fragen mit einem nicht öffentlichen KI-Dienst der TU Graz und kann keinen Code
ausführen. Deine Nachrichten und deine abgegebene Arbeit stehen im Kursverlauf deines Kontos;
Näheres regelt die Datenschutzerklärung der Plattform.

Um Lena zu fragen, schreibst du in den Nachrichten zu einer Aufgabe `@lena` oder gibst `@`
ein und wählst Lena aus den Vorschlägen aus. Auch `@luna`, die ältere Schreibweise, und das kurze
`@ai` erreichen dieselbe Tutorin; den Vorschlag auszuwählen ist nicht nötig.
