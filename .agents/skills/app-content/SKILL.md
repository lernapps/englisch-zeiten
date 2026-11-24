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

Inkrement 02 (Stufe 7-8, Branch `increment/02-erzaehlen-dauer-plaene`): neun weitere Lücken der Karte, alle Voraussetzungen in Kapitel 1 bis 3 geübt (keine Wiederholungsseite, kein `ahead`).
4. Kapitel `erzaehlen` („Erzählen: Hintergrund, Handlung, vorher“): `past-progressive` → `erzaehlen/past-progressive` (Musterseite Lesestück) · `past-perfect` → `erzaehlen/past-perfect` · `zeitenfolge-temporalsaetze` → `erzaehlen/zeitenfolge-temporalsaetze` · `present-perfect-oder-simple-past` → `erzaehlen/present-perfect-oder-simple-past`
5. Kapitel `dauer` („Seit wann und wie lange?“): `since-for` → `dauer/since-for` · `present-perfect-progressive` → `dauer/present-perfect-progressive` · `dynamic-stative` → `dauer/dynamic-stative`
6. Kapitel `plaene` („Pläne, Fahrpläne und Zeitpunkte“): `present-fuer-zukunft` → `plaene/present-fuer-zukunft` · `future-progressive-perfect` → `plaene/future-progressive-perfect`
Kapitel 7 (Stufe 9-10) folgt später als Inkrement.

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
- Aussprache: keine Lesehilfe und keine Lautschrift auf diesen Seiten, weil Aussprache und Schrift in einem eigenen Explainer stehen („Klang und Schrift“, #482, mit Lautschrift); hier hören die Kinder ganze Sätze (Diktat, Nachsprechen) und lernen die Form, nicht den Klang von -s und -ed.

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → übersetzen/frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten nur als `(a|b)`-Gruppe im `target` (ein `accepted` einer Sprach-Aufgabe wirkt in der App nicht); `form: { case: hint, punctuation: ok }` in allen Sprach-Aufgaben (sonst meldet die App bei richtiger Antwort „Achte auf die Satzzeichen“). Jeder Einstiegs-`single-choice` hat mindestens drei Optionen, jede mit eigenem `info`. Im Modus `choice` zeigt die App `mistakes` nicht: dort tragen `hint` und die Optionen die Rückmeldung.

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

### Stufe 7-8: Seite mit Lesestück (Kapitel 4 bis 6, Muster `erzaehlen/past-progressive`)

- Abschnitte: `einstieg` (Vorwissens-Frage zum Zeitstrahl, „Das kannst du danach“), `lesestueck` (Titel nennt die Sorte, z. B. „Sophies Tagebuch“; zuerst der Vokabelblock „Wörter zum Tagebuch“, dann der Text in `text`-Blöcken mit nummerierten Zeilen „**[1]** …“, 150 bis 300 Wörter, eigener erfundener Text der Figuren, keine realen Faktenangaben), `neu` (Zeichen am Strahl, Bau-Karte, Merke; kein Satz des Lesestücks wörtlich), `uebung` in drei Stufen (Verstehen: `single-choice`/`multiple-choice` zum Inhalt; Belegen mit Zeile: `multiple-choice` „In welchen Zeilen steht …?“, `language-task` zum Bilden; Meinung/Schreiben im Abschnitt `anwenden` als `open-task`), `anwenden`, `weiter`.
- **Vokabelblock** (`type: vocabulary`, app-templates ab 0.14): ersetzt jede Tabelle, in der nur Wörter und Bedeutungen stehen (Ausdruck · Bedeutung, Wort · Bedeutung, Zeitangabe · Bedeutung). Felder: `caption`, `languages: { source: de, target: en }`, `entries` (`target`, `source`, optional `forms`, `example`, `note`). Eine Wörterliste je Seite (Konventionen Abschnitt 7). Formen-Tabellen (Person · Form) und Zeitformen-Poster bleiben `table`.
- Hinweis `explainer-text-load` (mehr als 350 Wörter zu lesen) ist bei diesen Seiten **bewusst**: Das Lesestück zählt nicht zu den 350 Wörtern Erklärtext (Konventionen Abschnitt 8, Ersteller:in bestätigt).
- Lerner-Check der Musterseite (Kind 7-8): Vorwissens-Frage vom Zeitstrahl aus (nicht ein Satz, den die Seite noch nicht erklärt hat), Glossar vor dem Text, -ing-Regel mit anderen Verben als die Übungen, Frage und Verneinung kurz im Merke, Übungen mit eigener Meldung je Fehler.

## Figures

- Zeichen des Zeitstrahls (eine SVG-Familie `src/images/zeitstrahl-<seite>.svg`, eigene Zeichnung, `CC-BY-4.0`, gleich auf jeder Seite; Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox; Farben: now #c0392b, Punkte #2c6fd8, Welle #8e44ad, Bogen #138d75, Pfeil und will #d35400): now = senkrechter roter Strich; simple = ausgefüllte Punkte (Gewohnheit = Reihe, einzelnes Ereignis = ein Punkt mit Zeitangabe); progressive = Welle über now; perfect = Bogen von links bis now; going to = Pfeil, der bei now beginnt; will = Punkt rechts ohne Pfeil; Signalwörter als Fähnchen; links früher, rechts später. Das -s bei he/she/it farbig.
- Bau-Karten: be + -ing, have + 3. Form, be + going to + Grundform, will + Grundform.
- Gebaut: `zeitstrahl-leer` (das-brauchst-du), `-to-be`, `-punktreihe` (simple-present), `-haeufigkeit`, `-welle`, `-beides` (simple-oder-progressive), `-punkt-links`, `-punkt-und-bogen`, `-will`, `-going-to`, `-will-oder-going-to`, `-ganz` (Rückblick K3, alle Zeichen). `zeitstrahl-ganz.svg` wächst mit jedem Inkrement.
- Szenen: je Seite eine `szene-<seite>.svg` mit den Figuren, kopiert als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook) und gleich gelassen; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. Quelle „eigene Zeichnung“, Lizenz `CC-BY-4.0`. `alt` sagt, was die Szene zeigt, nie die Lösung; in Aufgaben zeigt der Strahl nur die Legende, nie das Ergebnis.
- Jede Figur funktioniert bei 360 px (viewBox, Beschriftung innerhalb); Skizzen liegen in `.vibe/sketches/`.
- Stufe 7-8 (Inkrement 02): `zeitstrahl-<seite>.svg` für past-progressive (Welle in der Vergangenheit, Punkt unterbricht, Fähnchen when), past-perfect (ein Punkt vor dem Punkt), zeitenfolge, ppsp (Punkt links neben Bogen), since-for (Fähnchen since am Startpunkt, Klammer for), present-perfect-progressive (Bogen wird Welle), dynamic-stative (Stoppschild an der Welle), present-fuer-zukunft (Kalender-Punkt und Fahrplan), future-progressive-perfect (Welle um einen Zeitpunkt, Bogen bis dahin); Figuren nur im Text (Sophie 13, Ellie 13, Peter 11, Amir 13), keine neuen Szenen; Mrs Parker wird nicht gezeichnet.
- Poster und Kalender sind `table`-Blöcke, wachsen von Seite zu Seite.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2; Wörter der Übungen stammen daraus; außerhalb der Liste stehen nur sink (Poster-Eintrag in `unregelmaessig`) und friends (Mehrzahl von friend); `yet` ist A2). Inkrement 02: Grammatikfakten aus Wikipedia, geöffnet am 2026-11-22 (nur Fakten): Past continuous, Pluperfect (past perfect), Uses of English verb forms (present perfect progressive, future progressive, future perfect), Stative verb, Future perfect, Sequence of tenses. Die Lesestücke sind eigene erfundene Texte der Figuren ohne reale Faktenangaben; Fahrpläne und Orte sind erfunden. Erste Version: Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA): `English irregular verbs` (Klangmuster sing – sang – sung, Ablaut; regelmäßige Verben auf -ed), `Present perfect` und `English verbs` (Formen und Gebrauch), geöffnet am 2026-11-21. Nicht geprüft: deutsche Wikipedia ohne Seite „Zeitform (Englisch)“ (404), kein Klexikon-Artikel gelesen. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

## Hörliste

Hörsätze bleiben natürlich; kein Name nur für den Klang. `regen_audio.py` (mit Fehllaut-Schnitt `valley_cut`) schneidet das Ausklingen der Stimme am Satzende ab. Die Ersteller:in hört gezielt diese Sätze an. Die neuesten Dateien sind nicht angehört. Prüfung der Sätze: `python3 .agents/skills/app-content/scripts/pruefe_hoersaetze.py` (kein Hörsatz gleicht einem Satz derselben Seite; Namen, Adverbien und Zeitangaben zählen nicht als Unterschied).

### Sätze mit einsilbigem Ende (38)

| Datei | Satz | Seite |
|---|---|---|
| `amir-has-just-come-home.mp3` | Amir has just come home. | `gestern-und-schon/present-perfect` |
| `ellie-has-cleaned-her-room.mp3` | Ellie has cleaned her room. | `gestern-und-schon/present-perfect` |
| `ellie-has-never-run-to-school.mp3` | Ellie has never run to school. | `gestern-und-schon/present-perfect` |
| `sophie-has-taken-a-book-home.mp3` | Sophie has taken a book home. | `gestern-und-schon/present-perfect` |
| `we-have-just-seen-mr-hill.mp3` | We have just seen Mr Hill. | `gestern-und-schon/present-perfect` |
| `we-listened-to-music-last-night.mp3` | We listened to music last night. | `gestern-und-schon/simple-past` |
| `amir-bought-a-drink-at-the-shop.mp3` | Amir bought a drink at the shop. | `gestern-und-schon/unregelmaessig` |
| `we-drank-water-at-home.mp3` | We drank water at home. | `gestern-und-schon/unregelmaessig` |
| `mr-hill-is-never-angry-in-class.mp3` | Mr Hill is never angry in class. | `immer-oder-jetzt/haeufigkeit` |
| `sophie-sometimes-writes-to-her-friends.mp3` | Sophie sometimes writes to her friends. | `immer-oder-jetzt/haeufigkeit` |
| `we-usually-have-breakfast-at-eight.mp3` | We usually have breakfast at eight. | `immer-oder-jetzt/haeufigkeit` |
| `we-usually-walk-to-school.mp3` | We usually walk to school. | `immer-oder-jetzt/haeufigkeit` |
| `he-has-not-got-a-phone.mp3` | He has not got a phone. | `immer-oder-jetzt/have-got` |
| `she-has-got-a-bike.mp3` | She has got a bike. | `immer-oder-jetzt/have-got` |
| `they-have-got-a-very-old-house.mp3` | They have got a very old house. | `immer-oder-jetzt/have-got` |
| `amir-is-waiting-for-the-bus.mp3` | Amir is waiting for the bus. | `immer-oder-jetzt/present-progressive` |
| `i-am-drinking-a-cup-of-tea.mp3` | I am drinking a cup of tea. | `immer-oder-jetzt/present-progressive` |
| `peter-is-swimming-in-the-pool.mp3` | Peter is swimming in the pool. | `immer-oder-jetzt/present-progressive` |
| `they-are-making-a-cake.mp3` | They are making a cake. | `immer-oder-jetzt/present-progressive` |
| `ellie-always-has-a-sandwich-at-lunch.mp3` | Ellie always has a sandwich at lunch. | `immer-oder-jetzt/simple-oder-progressive` |
| `peter-is-making-a-sandwich-now.mp3` | Peter is making a sandwich now. | `immer-oder-jetzt/simple-oder-progressive` |
| `sophie-plays-the-piano-every-day.mp3` | Sophie plays the piano every day. | `immer-oder-jetzt/simple-oder-progressive` |
| `we-are-watching-a-film-now.mp3` | We are watching a film now. | `immer-oder-jetzt/simple-oder-progressive` |
| `amir-studies-english-at-home.mp3` | Amir studies English at home. | `immer-oder-jetzt/simple-present` |
| `ellie-listens-to-music-after-school.mp3` | Ellie listens to music after school. | `immer-oder-jetzt/simple-present` |
| `ellie-is-a-good-friend.mp3` | Ellie is a good friend. | `immer-oder-jetzt/to-be` |
| `the-children-are-not-at-home.mp3` | The children are not at home. | `immer-oder-jetzt/to-be` |
| `ellie-and-sophie-are-going-to-swim-after-lunch.mp3` | Ellie and Sophie are going to swim after lunch. | `morgen-und-spaeter/going-to` |
| `i-am-going-to-buy-a-new-bag.mp3` | I am going to buy a new bag. | `morgen-und-spaeter/going-to` |
| `we-are-going-to-wash-the-car.mp3` | We are going to wash the car. | `morgen-und-spaeter/going-to` |
| `i-think-she-will-like-the-cake.mp3` | I think she will like the cake. | `morgen-und-spaeter/will` |
| `maybe-peter-will-bring-his-bike.mp3` | Maybe Peter will bring his bike. | `morgen-und-spaeter/will` |
| `mr-hill-will-probably-be-late.mp3` | Mr Hill will probably be late. | `morgen-und-spaeter/will` |
| `sophie-will-be-here-soon.mp3` | Sophie will be here soon. | `morgen-und-spaeter/will` |
| `we-will-see-you-soon.mp3` | We will see you soon. | `morgen-und-spaeter/will` |
| `amir-will-open-the-door.mp3` | Amir will open the door. | `morgen-und-spaeter/will-oder-going-to` |
| `it-is-raining-so-peter-will-take-the-bus.mp3` | It is raining, so Peter will take the bus. | `morgen-und-spaeter/will-oder-going-to` |
| `sophie-has-a-new-bike-and-she-is-going-to-ride-it-to-school.mp3` | Sophie has a new bike and she is going to ride it to school. | `morgen-und-spaeter/will-oder-going-to` |

### Fehllaut-Schnitt: Dateien, bei denen er gegriffen hat (14)

| Datei | entfernt |
|---|---|
| `ellie-is-a-good-friend.mp3` | 45 ms |
| `she-has-got-a-bike.mp3` | 45 ms |
| `they-are-making-a-cake.mp3` | 55 ms |
| `peter-is-going-to-look-at-the-ticket.mp3` | 65 ms |
| `sophie-has-got-a-red-jacket.mp3` | 35 ms |
| `we-listened-to-music-last-night.mp3` | 55 ms |
| `amir-bought-a-drink-at-the-shop.mp3` | 75 ms |
| `sophie-sometimes-writes-to-her-friends.mp3` | 45 ms |
| `we-usually-have-breakfast-at-eight.mp3` | 55 ms |
| `ellie-always-has-a-sandwich-at-lunch.mp3` | 85 ms |
| `we-are-cleaning-the-classroom-at-the-moment.mp3` | 55 ms |
| `ellie-and-sophie-are-going-to-swim-after-lunch.mp3` | 95 ms |
| `amir-will-open-the-door.mp3` | 25 ms |
| `mr-hill-will-probably-be-late.mp3` | 75 ms |

### Sätze mit mehrsilbigem Ende (34)

Risiko: eine Silbe wird angeschnitten. Gezielt anhören: `amir-cleaned-his-room-on-sunday.mp3`, `amir-is-happy-today.mp3`, `amir-is-hungry-so-he-will-eat-a-pizza.mp3`, `are-sophie-and-ellie-tired.mp3`, `ellie-danced-with-sophie.mp3`, `ellie-is-eating-breakfast.mp3`, `ellie-is-going-to-be-twelve-in-july.mp3`, `ellie-often-visits-her-grandmother.mp3`, `ellie-sat-with-amir.mp3`, `has-mr-hill-got-any-children.mp3`, `i-have-got-a-big-family.mp3`, `it-will-be-cold-on-sunday.mp3`, `mr-hill-is-in-the-classroom.mp3`, `mr-hill-often-drinks-coffee.mp3`, `mr-hill-teaches-english.mp3`, `my-name-is-sophie-and-i-like-music.mp3`, `peter-always-drinks-milk-in-the-morning.mp3`, `peter-has-already-written-to-ellie.mp3`, `peter-is-going-to-look-at-the-ticket.mp3`, `peter-ran-home-yesterday.mp3`, `peter-sang-a-song-at-the-party.mp3`, `peter-watches-football-every-saturday.mp3`, `sophie-called-her-mother-on-monday.mp3`, `sophie-has-got-a-red-jacket.mp3`, `sophie-helped-peter-with-homework.mp3`, `sophie-is-listening-to-music.mp3`, `sophie-likes-football.mp3`, `sophie-sang-at-home-yesterday.mp3`, `they-go-to-the-park-on-sunday.mp3`, `we-are-cleaning-the-classroom-at-the-moment.mp3`, `we-are-going-to-cook-dinner-on-friday.mp3`, `we-are-going-to-dance-at-the-party.mp3`, `we-are-going-to-dance-on-10-july.mp3`, `we-danced-at-school-yesterday.mp3`.

### Hörliste Inkrement 02 (Stufe 7-8, Kapitel 4 bis 6)

Alle 54 Hörsätze sind mit `regen_audio.py` (Fehllaut-Schnitt) erzeugt. Sätze mit Schnitt an der Senke sind mit ms markiert; die Ersteller:in hört gezielt die markierten Sätze und die, die auf ein kurzes Wort enden (Spalte „Ende“). Kein Satz ist angehört worden.

| Seite | Datei | Satz | Ende | Schnitt |
|---|---|---|---|---|
| `dauer/dynamic-stative` | `he-likes-cheese-but-he-is-eating-an-apple.mp3` | He likes cheese, but he is eating an apple. | apple |  |
| `dauer/dynamic-stative` | `i-need-a-bigger-bag-for-my-books.mp3` | I need a bigger bag for my books. | books |  |
| `dauer/dynamic-stative` | `i-understand-the-rules-but-i-am-still-learning.mp3` | I understand the rules, but I am still learning. | learning |  |
| `dauer/dynamic-stative` | `my-little-brother-wants-a-new-football.mp3` | My little brother wants a new football. | football |  |
| `dauer/dynamic-stative` | `she-believes-every-word-of-the-story.mp3` | She believes every word of the story. | story |  |
| `dauer/dynamic-stative` | `we-love-the-new-teacher-and-we-are-working-hard.mp3` | We love the new teacher, and we are working hard. | hard | 25 ms |
| `dauer/present-perfect-progressive` | `how-long-have-you-been-learning-french.mp3` | How long have you been learning French? | french |  |
| `dauer/present-perfect-progressive` | `my-cat-has-been-hiding-under-the-bed-since-breakfast.mp3` | My cat has been hiding under the bed since breakfast. | breakfast |  |
| `dauer/present-perfect-progressive` | `my-parents-have-been-painting-the-kitchen-for-two-days.mp3` | My parents have been painting the kitchen for two days. | days | 65 ms |
| `dauer/present-perfect-progressive` | `she-has-been-practising-the-guitar-all-week.mp3` | She has been practising the guitar all week. | week |  |
| `dauer/present-perfect-progressive` | `the-students-have-been-singing-since-lunch.mp3` | The students have been singing since lunch. | lunch | 85 ms |
| `dauer/present-perfect-progressive` | `why-have-you-been-crying.mp3` | Why have you been crying? | crying |  |
| `dauer/since-for` | `how-long-has-your-sister-worked-in-the-shop.mp3` | How long has your sister worked in the shop? | shop |  |
| `dauer/since-for` | `i-have-not-seen-him-since-the-party.mp3` | I have not seen him since the party. | party |  |
| `dauer/since-for` | `i-have-wanted-a-dog-since-my-last-birthday.mp3` | I have wanted a dog since my last birthday. | birthday |  |
| `dauer/since-for` | `my-brother-has-played-the-piano-for-six-months.mp3` | My brother has played the piano for six months. | months |  |
| `dauer/since-for` | `our-teacher-has-been-ill-for-a-week.mp3` | Our teacher has been ill for a week. | week |  |
| `dauer/since-for` | `they-have-been-in-london-for-three-days.mp3` | They have been in London for three days. | days |  |
| `erzaehlen/past-perfect` | `had-they-met-before-the-party.mp3` | Had they met before the party? | party |  |
| `erzaehlen/past-perfect` | `he-hadn-t-visited-the-museum-before.mp3` | He hadn't visited the museum before. | before |  |
| `erzaehlen/past-perfect` | `my-brother-hadn-t-tried-the-soup.mp3` | My brother hadn't tried the soup. | soup |  |
| `erzaehlen/past-perfect` | `sophie-had-lost-her-pen-before-the-lesson.mp3` | Sophie had lost her pen before the lesson. | lesson |  |
| `erzaehlen/past-perfect` | `the-teacher-had-left-the-room-before-the-bell-rang.mp3` | The teacher had left the room before the bell rang. | rang |  |
| `erzaehlen/past-perfect` | `we-had-already-eaten-when-dad-came-home.mp3` | We had already eaten when Dad came home. | home |  |
| `erzaehlen/past-progressive` | `i-was-cooking-while-he-was-listening-to-music.mp3` | I was cooking while he was listening to music. | music |  |
| `erzaehlen/past-progressive` | `mr-hill-was-drinking-tea-when-the-phone-rang.mp3` | Mr Hill was drinking tea when the phone rang. | rang |  |
| `erzaehlen/past-progressive` | `my-sister-was-sleeping-when-i-arrived.mp3` | My sister was sleeping when I arrived. | arrived |  |
| `erzaehlen/past-progressive` | `the-students-were-waiting-in-the-hall.mp3` | The students were waiting in the hall. | hall |  |
| `erzaehlen/past-progressive` | `they-were-playing-cards-in-the-garden.mp3` | They were playing cards in the garden. | garden |  |
| `erzaehlen/past-progressive` | `what-were-you-doing-at-nine-o-clock.mp3` | What were you doing at nine o'clock? | o'clock | 25 ms |
| `erzaehlen/present-perfect-oder-simple-past` | `have-you-tried-the-new-cake-yet.mp3` | Have you tried the new cake yet? | yet |  |
| `erzaehlen/present-perfect-oder-simple-past` | `i-haven-t-finished-my-homework-yet.mp3` | I haven't finished my homework yet. | yet | 65 ms |
| `erzaehlen/present-perfect-oder-simple-past` | `my-uncle-has-bought-a-new-car.mp3` | My uncle has bought a new car. | car |  |
| `erzaehlen/present-perfect-oder-simple-past` | `she-has-already-sent-the-letter.mp3` | She has already sent the letter. | letter |  |
| `erzaehlen/present-perfect-oder-simple-past` | `they-watched-the-match-on-saturday.mp3` | They watched the match on Saturday. | saturday |  |
| `erzaehlen/present-perfect-oder-simple-past` | `we-went-to-the-beach-two-days-ago.mp3` | We went to the beach two days ago. | ago |  |
| `erzaehlen/zeitenfolge-temporalsaetze` | `after-she-had-finished-her-work-she-went-out.mp3` | After she had finished her work, she went out. | out | 25 ms |
| `erzaehlen/zeitenfolge-temporalsaetze` | `after-they-had-cleaned-the-hall-the-teachers-went-home.mp3` | After they had cleaned the hall, the teachers went home. | home |  |
| `erzaehlen/zeitenfolge-temporalsaetze` | `as-soon-as-the-shop-opens-i-will-buy-some-bread.mp3` | As soon as the shop opens, I will buy some bread. | bread |  |
| `erzaehlen/zeitenfolge-temporalsaetze` | `before-you-leave-please-turn-off-the-lights.mp3` | Before you leave, please turn off the lights. | lights |  |
| `erzaehlen/zeitenfolge-temporalsaetze` | `we-will-have-lunch-after-the-match-ends.mp3` | We will have lunch after the match ends. | ends |  |
| `erzaehlen/zeitenfolge-temporalsaetze` | `when-the-music-stops-everybody-will-clap.mp3` | When the music stops, everybody will clap. | clap | 75 ms |
| `plaene/future-progressive-perfect` | `at-twelve-tomorrow-my-parents-will-be-driving-to-the-seaside.mp3` | At twelve tomorrow my parents will be driving to the seaside. | seaside |  |
| `plaene/future-progressive-perfect` | `by-friday-amir-will-have-cleaned-the-whole-kitchen.mp3` | By Friday Amir will have cleaned the whole kitchen. | kitchen |  |
| `plaene/future-progressive-perfect` | `by-tonight-she-will-have-painted-the-whole-room.mp3` | By tonight she will have painted the whole room. | room |  |
| `plaene/future-progressive-perfect` | `they-will-be-arriving-at-midnight.mp3` | They will be arriving at midnight. | midnight |  |
| `plaene/future-progressive-perfect` | `this-time-next-week-we-will-be-lying-on-the-beach.mp3` | This time next week we will be lying on the beach. | beach |  |
| `plaene/future-progressive-perfect` | `will-you-be-working-tomorrow-evening.mp3` | Will you be working tomorrow evening? | evening |  |
| `plaene/present-fuer-zukunft` | `are-you-meeting-your-friends-this-weekend.mp3` | Are you meeting your friends this weekend? | weekend |  |
| `plaene/present-fuer-zukunft` | `i-am-playing-tennis-with-my-cousin-on-saturday.mp3` | I am playing tennis with my cousin on Saturday. | saturday |  |
| `plaene/present-fuer-zukunft` | `my-cousin-is-coming-to-our-house-on-sunday.mp3` | My cousin is coming to our house on Sunday. | sunday |  |
| `plaene/present-fuer-zukunft` | `the-concert-begins-at-eight-o-clock.mp3` | The concert begins at eight o'clock. | o'clock |  |
| `plaene/present-fuer-zukunft` | `the-lesson-finishes-at-a-quarter-to-four.mp3` | The lesson finishes at a quarter to four. | four |  |
| `plaene/present-fuer-zukunft` | `we-are-having-dinner-with-our-grandparents-tonight.mp3` | We are having dinner with our grandparents tonight. | tonight | 35 ms |

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
- Als Auswahl nur echte Lernerfehler (is like, are plays, eated, has did), keine erfundenen Unwörter (likees, is will).
- Höchstens eine kurze Wörtertabelle je Seite („Klassenzimmer-Poster · Wörter dieser Seite“ oder „Schulkalender · Zeitangaben“): sie nennt nur Wörter außerhalb von A1 und weniger einfache Wörter; einfache Wörter (A1) gelten als bekannt. Seiten mit mehr als etwa 25 Items kürzen.
- Übungssätze und Beispielsätze der Erklärung (Text, Poster, Merke, Bildtext) sind verschiedene Sätze; ein Prüfskript über alle Seiten vergleicht die Lösungen (`target`, richtige Option, Zuordnung) mit dem Erklärtext derselben Seite.
- Eine Übung für die Selbsteinschätzung nennt in Hinweis und Meldung weder „Spalte“ noch „Poster“ noch „oben“.
- Gleichwertige Kurzformen zulassen (I'm not, you're not, Amir's not; `accepted` oder `(a|b)`); Stellen mit „already“ und Zeitangabe so bauen, dass es nur eine richtige Zeit gibt.
- Der englische Cue enthält kein deutsches Wort; der deutsche Hinweis steht in `source` oder in der Aufgabe.
- Audio: Wörter, die die Stimme falsch liest, nicht in Hörsätzen verwenden: „lives“ klang wie das Nomen „leives“ (Mehrzahl von life) → der Satz heißt jetzt „Sophie likes football.“. Neue Hörsätze anhören; bei Verben, die auch Nomen sind (lives, leaves, close, wind), ein anderes Verb nehmen.
- Hörsätze sind neue Sätze: keiner steht wörtlich oder mit getauschtem Namen im Einstieg, Poster, Merke, Bildtext oder in einer Übung derselben Seite (Prüfskript über alle Seiten vor jedem Checkpoint).
- Ein Hörsatz unterscheidet sich von jedem Satz derselben Seite (Einstieg, Poster, Merke, Bildtext, Übungen, Meldungen) in mehr als Name, Adverb, Zeitangabe oder einem Wort. Prüfung: `python3 .agents/skills/app-content/scripts/pruefe_hoersaetze.py` (Treffer 0) vor jedem Commit mit neuem Audio.
- Die Lösung einer Übung steht nicht wörtlich im Text darüber und nicht in einer anderen Übung derselben Seite (Poster zeigen andere Beispielwörter als die Übungen; Auswahl- und Schreibübung nehmen nie dieselben Sätze). Hinweis: `python3 .agents/skills/app-content/scripts/pruefe_doppelte.py` (Doppelte zwischen Cue und Fehlerantworten derselben Übung sind in Ordnung, ebenso die Zusammenfassung im Abschnitt `weiter`).
- Jede Seite hat mindestens vier Übungen, bei denen eine falsche Antwort eine eigene Rückmeldung bekommt: Schreibübungen mit `mistakes` je Item oder `single-choice` mit `info` je Option. `language-task` im Modus `choice` zeigt die Meldungen aus `mistakes` nicht; dort zählt nur der `hint`.
- Einheitliche Wörter: Punktreihe, Welle über now, Poster, happy = froh, phone = Telefon / Handy.
