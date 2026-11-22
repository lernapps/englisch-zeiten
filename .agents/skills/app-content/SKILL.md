---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Zeiten auf dem Zeitstrahl“: Explainer (Strang-App `englisch/grammatik`, Format 2, Sprache Deutsch, englische Beispiele) über die englischen Zeitformen. Auftrag: Issue lernapps/apps#472 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut nur Stufe 5-6 (Kapitel 1 bis 3); Kapitel 4 bis 7 (Stufen 7-8 und 9-10) kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`; diese App ist eine Strang-App des Strangs `grammatik`). Vorwissen: Hello, Millbrook! (#470) und Personalpronomen (#471). Nicht hier: Fragen und Verneinung mit do und did (#473), Bedingungssätze und indirekte Rede (#481), Passiv (#480), Aussprache von -s und -ed (#482), Kapitel 4 bis 7 (spätere Inkremente).

## Competencies

Alle zwölf sind Lücken der Karte, Band 5-6. Eine Seite je Baustein, Ordnung nach `requires`. Von außen braucht die Karte nur `personalpronomen`.

1. Kapitel `immer-oder-jetzt` („Immer oder gerade jetzt?“)
   - Wiederholung `recap: englisch/personalpronomen` → `immer-oder-jetzt/das-brauchst-du` (ohne Übung)
   - `to-be` → `immer-oder-jetzt/to-be`
   - `have-got` → `immer-oder-jetzt/have-got`
   - `simple-present` → `immer-oder-jetzt/simple-present` (Musterseite)
   - `adverbien-haeufigkeit` → `immer-oder-jetzt/haeufigkeit`
   - `present-progressive` → `immer-oder-jetzt/present-progressive`
   - `simple-oder-progressive` → `immer-oder-jetzt/simple-oder-progressive`
2. Kapitel `gestern-und-schon` („Gestern und schon“)
   - `simple-past` → `gestern-und-schon/simple-past`
   - `unregelmaessige-verben` → `gestern-und-schon/unregelmaessig`
   - `present-perfect` → `gestern-und-schon/present-perfect`
3. Kapitel `morgen-und-spaeter` („Morgen und später“)
   - `will-future` → `morgen-und-spaeter/will`
   - `going-to` → `morgen-und-spaeter/going-to`
   - `will-oder-going-to` → `morgen-und-spaeter/will-oder-going-to`

Die „Ich kann“-Sätze stehen in `src/<kapitel>/<seite>.yaml` wie in der Karte (nicht umformulieren). Übungs-IDs: Präfix = Seite (`simple-present-…`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Zeichen am Strahl, Bau-Karte, Merke-Kasten), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`open-task` oder `speaking-task`: den Strahl selbst füllen), `weiter` (nächster Schritt am Wandbild; am Kapitelende ein Rückblick). Titel sagen, was der Abschnitt tut. Die Wiederholungsseite hat nur Text und Tabelle.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken. Jede Seite bringt einen neuen Schritt (`explainer-one-step`).
- Geschichte: Mr Hill lässt die Klasse das Wandbild „Millbrook-Zeitstrahl“ gestalten; Sophie, Ellie, Peter und Amir hängen Karten auf. Figuren und Orte wie in #470 (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers, 11 bis 12), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (graue Haare, braune Jacke), Mrs Parker. Millbrook School, Schultag ab 8:45. Geburtstage: Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Tabellen heißen „Klassenzimmer-Poster · Zeitformen“ und „Schulkalender · Zeitangaben“ und wachsen von Seite zu Seite.
- Anrede „du“.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence, tense (aus #470); Zeitnamen als Eigennamen: simple present, present progressive, simple past, present perfect, will-future, going-to.
- Zeitstrahl-Wörter: Strahl, now, Punkt, Punktreihe, Welle, Bogen, Pfeil, Fähnchen (Signalwort), Bau-Karte. Immer dieselben.
- Merksatz: „He, she, it – das s muss mit.“
- Britisches Englisch (favourite, colour). Englische Aufgaben enthalten kein deutsches Wort. Englisches immer mit deutscher Bedeutung, wo ein Wort neu ist.
- Aussprache: keine Lesehilfe und keine Lautschrift hier (IPA gehört zu #482); Hörtexte nur als Sätze.

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → übersetzen/frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`.

- Zeichen zuordnen: `matching` Satz ↔ Zeichen (Punktreihe, Punkt, Welle, Bogen, Pfeil).
- Reihe ordnen: `ordering` Fähnchen always … never; Satzteile (Stellung des Häufigkeitsadverbs).
- Formen ergänzen: `language-task` mode `table` (Person ↔ Form, -s-Spalte), `gap`, `choice` mit `distractors`.
- Form bilden: `language-task` mode `write` mit `cue` (`cue: "play · she"`).
- Entscheiden mit Begründung: `choice`/`true-false`, die Rückmeldung nennt das Zeichen („Ein Punkt mit Zeitangabe: simple past“).
- Hören und schreiben: `language-task` mit `audio` (Diktat, je Seite höchstens drei ganze Sätze, keine Wiederholung zwischen Seiten); Nachsprechen: `speaking-task`.
- Freies Schreiben: `open-task` (Karte für den Strahl).
- Typische Fehler (jeweils `mistakes`): fehlendes -s bei he/she/it; be vergessen („She reading“, „I going to“); „I am go“; Welle für Gewohnheiten und umgekehrt; „goed“ statt went; went/gone verwechselt; present perfect mit yesterday; have/has nach Person; will für schon gefassten Plan, going to für spontanes Angebot.
- Unregelmäßige Verben: 38 nach Klangmustern, Liste auf der Seite `gestern-und-schon/unregelmaessig` (Poster „Klassenzimmer-Poster · Unregelmäßige Verben“): sing sang sung · swim swam swum · drink drank drunk · begin began begun · ring rang rung · run ran run · come came come · write wrote written · drive drove driven · ride rode ridden · take took taken · give gave given · eat ate eaten · see saw seen · know knew known · buy bought bought · bring brought brought · think thought thought · catch caught caught · teach taught taught · go went gone · do did done · be was/were been · have had had · make made made · say said said · pay paid paid · meet met met · read read read · sit sat sat · get got got · find found found · lose lost lost · leave left left · cut cut cut · put put put · hit hit hit · let let let. Alle Grundformen sind A1.
- Keine Komponente (`prefer-built-in-block`); eine Ziehen-Übung auf dem Strahl wäre ein Wunsch für ein Inkrement.
- Keine Datendateien: jede Tatsache steht einmal in ihrer Seite.

## Figures

- Zeichen des Zeitstrahls (eine SVG-Familie `src/images/zeitstrahl-<seite>.svg`, eigene Zeichnung, `CC-BY-4.0`, gleich auf jeder Seite; Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox; Farben: now #c0392b, Punkte #2c6fd8, Welle #8e44ad, Bogen #138d75, Pfeil und will #d35400): now = senkrechter roter Strich; simple = ausgefüllte Punkte (Gewohnheit = Reihe, einzelnes Ereignis = ein Punkt mit Zeitangabe); progressive = Welle über now; perfect = Bogen von links bis now; going to = Pfeil, der bei now beginnt; will = Punkt rechts ohne Pfeil; Signalwörter als Fähnchen; links früher, rechts später. Das -s bei he/she/it farbig.
- Bau-Karten: be + -ing, have + 3. Form, be + going to + Grundform, will + Grundform.
- Gebaut: `zeitstrahl-leer` (das-brauchst-du), `-to-be`, `-punktreihe` (simple-present), `-haeufigkeit`, `-welle`, `-beides` (simple-oder-progressive), `-punkt-links`, `-punkt-und-bogen`, `-bogen` (nicht benutzt, Reserve), `-will`, `-going-to`, `-will-oder-going-to`, `-ganz` (Rückblick K3, alle Zeichen). `zeitstrahl-ganz.svg` wächst mit jedem Inkrement.
- Szenen: je Seite eine `szene-<seite>.svg` mit den Figuren, kopiert als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook) und gleich gelassen; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. Quelle „eigene Zeichnung“, Lizenz `CC-BY-4.0`. `alt` sagt, was die Szene zeigt, nie die Lösung; in Aufgaben zeigt der Strahl nur die Legende, nie das Ergebnis.
- Jede Figur funktioniert bei 360 px (viewBox, Beschriftung innerhalb); Skizzen liegen in `.vibe/sketches/`.
- Poster und Kalender sind `table`-Blöcke, wachsen von Seite zu Seite.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2; Wörter der Übungen stammen daraus; außerhalb der Liste stehen nur sink (Poster-Eintrag in `unregelmaessig`) und friends (Mehrzahl von friend); `yet` ist A2). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA): `English irregular verbs` (Klangmuster sing – sang – sung, Ablaut; regelmäßige Verben auf -ed), `Present perfect` und `English verbs` (Formen und Gebrauch), geöffnet am 2026-11-21. Nicht geprüft: deutsche Wikipedia ohne Seite „Zeitform (Englisch)“ (404), kein Klexikon-Artikel gelesen. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

## Hörliste

Hörsätze bleiben natürlich; kein Name nur für den Klang. `regen_audio.py` schneidet das Ausklingen der Stimme am Satzende ab. Diese 38 Sätze enden auf ein einsilbiges Wort; sie sind die gezielte Hörprobe der Ersteller:in (Datei in `src/audio/` · Satz · Seite):

| Datei | Satz | Seite |
|---|---|---|
| `we-are-going-to-watch-a-film.mp3` | We are going to watch a film. | `morgen-und-spaeter/going-to` |
| `amir-sometimes-eats-lunch-at-school.mp3` | Amir sometimes eats lunch at school. | `immer-oder-jetzt/haeufigkeit` |
| `peter-and-ellie-often-take-the-bus.mp3` | Peter and Ellie often take the bus. | `immer-oder-jetzt/haeufigkeit` |
| `we-often-play-football-at-school.mp3` | We often play football at school. | `immer-oder-jetzt/haeufigkeit` |
| `we-usually-walk-to-school.mp3` | We usually walk to school. | `immer-oder-jetzt/haeufigkeit` |
| `has-amir-got-a-bike.mp3` | Has Amir got a bike? | `immer-oder-jetzt/have-got` |
| `he-has-not-got-a-phone.mp3` | He has not got a phone. | `immer-oder-jetzt/have-got` |
| `she-has-got-a-bike.mp3` | She has got a bike. | `immer-oder-jetzt/have-got` |
| `they-have-got-a-dog.mp3` | They have got a dog. | `immer-oder-jetzt/have-got` |
| `amir-has-just-come-home.mp3` | Amir has just come home. | `gestern-und-schon/present-perfect` |
| `ellie-has-never-run-to-school.mp3` | Ellie has never run to school. | `gestern-und-schon/present-perfect` |
| `sophie-has-taken-a-book-home.mp3` | Sophie has taken a book home. | `gestern-und-schon/present-perfect` |
| `we-have-just-seen-mr-hill.mp3` | We have just seen Mr Hill. | `gestern-und-schon/present-perfect` |
| `peter-is-running-now.mp3` | Peter is running now. | `immer-oder-jetzt/present-progressive` |
| `they-are-making-a-cake.mp3` | They are making a cake. | `immer-oder-jetzt/present-progressive` |
| `amir-always-eats-lunch.mp3` | Amir always eats lunch. | `immer-oder-jetzt/simple-oder-progressive` |
| `mr-hill-often-reads-a-book.mp3` | Mr Hill often reads a book. | `immer-oder-jetzt/simple-oder-progressive` |
| `peter-is-eating-lunch-now.mp3` | Peter is eating lunch now. | `immer-oder-jetzt/simple-oder-progressive` |
| `sophie-reads-a-book-every-day.mp3` | Sophie reads a book every day. | `immer-oder-jetzt/simple-oder-progressive` |
| `we-are-watching-a-film-now.mp3` | We are watching a film now. | `immer-oder-jetzt/simple-oder-progressive` |
| `ellie-studied-english-two-days-ago.mp3` | Ellie studied English two days ago. | `gestern-und-schon/simple-past` |
| `peter-and-amir-played-football-last-week.mp3` | Peter and Amir played football last week. | `gestern-und-schon/simple-past` |
| `amir-studies-english-at-home.mp3` | Amir studies English at home. | `immer-oder-jetzt/simple-present` |
| `ellie-watches-a-film-after-school.mp3` | Ellie watches a film after school. | `immer-oder-jetzt/simple-present` |
| `they-play-football-every-day.mp3` | They play football every day. | `immer-oder-jetzt/simple-present` |
| `are-sophie-and-ellie-tired.mp3` | Are Sophie and Ellie tired? | `immer-oder-jetzt/to-be` |
| `ellie-is-a-good-friend.mp3` | Ellie is a good friend. | `immer-oder-jetzt/to-be` |
| `we-are-not-tired.mp3` | We are not tired. | `immer-oder-jetzt/to-be` |
| `mr-hill-gave-peter-a-book.mp3` | Mr Hill gave Peter a book. | `gestern-und-schon/unregelmaessig` |
| `we-drank-water-at-home.mp3` | We drank water at home. | `gestern-und-schon/unregelmaessig` |
| `we-saw-a-film-at-home.mp3` | We saw a film at home. | `gestern-und-schon/unregelmaessig` |
| `ellie-will-probably-come-next-week.mp3` | Ellie will probably come next week. | `morgen-und-spaeter/will` |
| `i-will-help-you-soon.mp3` | I will help you soon. | `morgen-und-spaeter/will` |
| `it-will-rain-soon.mp3` | It will rain soon. | `morgen-und-spaeter/will` |
| `sophie-will-be-here-soon.mp3` | Sophie will be here soon. | `morgen-und-spaeter/will` |
| `we-will-probably-win.mp3` | We will probably win. | `morgen-und-spaeter/will` |
| `peter-has-a-ticket-and-he-is-going-to-watch-a-film.mp3` | Peter has a ticket and he is going to watch a film. | `morgen-und-spaeter/will-oder-going-to` |
| `sophie-will-answer-the-phone.mp3` | Sophie will answer the phone. | `morgen-und-spaeter/will-oder-going-to` |

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen.
3. Strahl-SVG um die neuen Zeichen erweitern (Inkremente: Welle in der Vergangenheit, Bogen wird Welle, Fähnchen since/for, Stoppschild für Zustandsverben, Punktreihe in der Vergangenheit für used to) und das Poster um die Zeilen der Seite.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 3 in `selfAssessment` (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz, alle 72 Sätze der App, 6 je Seite: je 3 für Diktat und Nachsprechen), erzeugt mit `~/.cache/lernapps/audio/venv/bin/python .agents/skills/app-content/scripts/regen_audio.py .agents/skills/app-content/scripts/audio-texte.json "<Satz>"` (Skript aus hello-millbrook, schneidet das Ausklingen ab); anhören lassen; Sätze nicht zwischen Seiten wiederholen und nicht wörtlich (auch nicht mit getauschtem Namen) auf derselben Seite verwenden; Hörsätze bleiben natürlich (ein Name steht nur, wenn der Satz ihn braucht, zum Beispiel als Anrede); einsilbig endende Sätze in die Hörliste eintragen.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus #470 übernommen (hello-millbrook):
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen.
- Eine Tabelle, die eine Übung beantwortet, steht nicht direkt über ihr.
- Englische Aufgaben enthalten kein deutsches Wort.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen; `case: wrong` nur dort, wo die Seite Großschreibung unterrichtet.
- Auswahlaufgaben zur Großschreibung zeigen alle Optionen gleich geschrieben.
- Audio: das Ausklingen der Stimme am Satzende abschneiden (`regen_audio.py`); kein Name nur für den Klang anhängen, Hörsätze bleiben natürlich, einsilbig endende stehen in der Hörliste.
- Bilder: Beschriftungen innerhalb des `viewBox` halten.
Aus dieser App (Lerner-Check der Musterseite, Gesamtcheck, Sprachprüfung):
- Die Antwort einer Frage steht nie im Absatz direkt darüber; die Einstiegsfrage fragt, was der Text noch nicht sagt.
- Bilder: Die Bildunterschrift nennt, wer wer ist (Sophie Zöpfe, Ellie roter Pferdeschwanz, Amir Brille, Peter gelbe Jacke); das `alt` verrät nie die Lösung.
- Das Merke-Kasten nennt andere Verben als die Übungen, sonst schreiben die Kinder nur ab.
- Als Auswahl nur echte Lernerfehler (is like, are plays), keine Unwörter (likees).
- Eine Übung für die Selbsteinschätzung nennt in Hinweis und Meldung weder „Spalte“ noch „Poster“ noch „oben“.
- Gleichwertige Kurzformen zulassen (I'm not, you're not, Amir's not; `accepted` oder `(a|b)`); Stellen mit „already“ und Zeitangabe so bauen, dass es nur eine richtige Zeit gibt.
- Der englische Cue enthält kein deutsches Wort; der deutsche Hinweis steht in `source` oder in der Aufgabe.
- Audio: Wörter, die die Stimme falsch liest, nicht in Hörsätzen verwenden: „lives“ klang wie das Nomen „leives“ (Mehrzahl von life) → der Satz heißt jetzt „Sophie likes football.“. Neue Hörsätze anhören; bei Verben, die auch Nomen sind (lives, leaves, close, wind), ein anderes Verb nehmen.
- Hörsätze sind neue Sätze: keiner steht wörtlich oder mit getauschtem Namen im Einstieg, Poster, Merke, Bildtext oder in einer Übung derselben Seite (Prüfskript über alle Seiten vor jedem Checkpoint).
- Einheitliche Wörter: Punktreihe, Welle über now, Poster, happy = froh, phone = Telefon / Handy.
