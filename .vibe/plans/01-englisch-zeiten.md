---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 3 }
---

# Plan: englisch-zeiten, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

<!-- 1–2 sentences: what learners do, what they learn. -->

## Key decisions

<!-- One line each: decision and reason. Archetype first. Your own choice without the creator: mark "(guess)". -->

- Archetyp `explainer` (Format 2, `strand: englisch/grammatik`): Die Kinder brauchen Erklärung mit Figur (Zeitstrahl, Bau-Karten) und Übungen auf jeder Seite; ein Quiz erklärt nicht, ein Spiel (`interactive`) wäre mehr als das Issue verlangt. Das Issue nennt Format 2. Grenzen: kein Timer, kein Spiel, keine Spracherkennung (Aussprache bewertet das Kind selbst), eigene Farben/Layout nicht möglich; das Setzen von Ereignissen auf den Strahl wird eine Vue-Komponente oder Auswahl-/Ordnungsübung.
- `scope`: ja. Der Abschnitt `anwenden` jeder Seite hat eine `open-task` (Karte für den Strahl); dann verlangt die Laufzeit `scope` in `src/app.yaml` und auf jeder Seite (in eigenen Worten: was die Seite lehrt, nichts mehr). Der Tutor beurteilt die offenen Antworten daran.

## Notes

<!-- Strand or subject, competencies by chapter (ids), didactic approach, scope, sources and licences, open questions. -->

**Karte (Fach `englisch`, Strang `grammatik`), gelesen am 2026-11-21.** Der Ersteller bringt die Inhalte mit (Issue #472); alle zwölf Bausteine der Kapitel 1 bis 3 liegen im Band 5-6 und sind Lücken (`practisedBy` leer):
- Kapitel 1: `to-be` (Schritt 2), `have-got` (2), `simple-present` (2), `adverbien-haeufigkeit` (3), `present-progressive` (3), `simple-oder-progressive` (4).
- Kapitel 2: `simple-past` (3), `unregelmaessige-verben` (4), `present-perfect` (5).
- Kapitel 3: `will-future` (1), `going-to` (4), `will-oder-going-to` (5).
- Einzige Voraussetzung von außerhalb: `personalpronomen` (#471, Schritt 1; von `to-be`, `have-got`, `simple-present`). Wiederholungsseite `recap` am Anfang von Kapitel 1. Alles andere liegt im Explainer (`going-to` braucht `present-progressive` aus Kapitel 1, `simple-past` braucht `simple-present`). Kapitel 2 und 3 brauchen keine weitere Wiederholung von außen; `classroom-phrases` aus #470 braucht keine Karte (nur als Figuren und Wortschatz der Szenen).
- Kapitel 3 steht in der Karte mit `will-future` (Schritt 1) ohne Voraussetzung; didaktisch kommt es nach Kapitel 1 und 2, weil es die Bausteine `going-to` und die Bildung mit be braucht.

**Seiten (eine Kompetenz je Seite, nach `requires` geordnet):**
- Kapitel 1 „Immer oder gerade jetzt?“: `recap` (`englisch/personalpronomen`, Sammel-Wiederholung „Das brauchst du hier“, ohne Übung) · `to-be` · `have-got` · `simple-present` · `adverbien-haeufigkeit` · `present-progressive` · `simple-oder-progressive`.
- Kapitel 2 „Gestern und schon“: `simple-past` · `unregelmaessige-verben` · `present-perfect`. Alle Voraussetzungen liegen im Explainer (`simple-present`), keine Wiederholung nötig.
- Kapitel 3 „Morgen und später“: `will-future` · `going-to` · `will-oder-going-to`. `going-to` braucht `present-progressive` (Kapitel 1, geübt). Kein `ahead`.
- Von außen nur `personalpronomen` (für `to-be`, `have-got`, `simple-present`): Wiederholungsseite am Anfang von Kapitel 1. `classroom-phrases` und anderes aus #470 verlangt die Karte nicht. Nach #471 verlinkt die Seite auf dessen echte Seite, falls schon vorhanden (sonst Link zur Karte).

**Herleiten und Fehlvorstellung, je Kompetenz:**
- `to-be`: Die Kinder ordnen am Strahl Personen (I, he, they …) den Formen am/is/are zu und füllen die Formen aus der Tabelle selbst; Fehler: „I is“, „they is“, Verneinung „I am not“ vs. „I amn't“.
- `have-got`: Sie ergänzen have/has nach Person aus Sätzen zu Dingen der Figuren; Fehler: „she have got“, „I has got“.
- `simple-present`: Eine Reihe Punkte (Gewohnheit) wird in Sätze übersetzt; das -s leuchtet bei he/she/it auf, die Kinder bilden die Form erst selbst; Fehler: fehlendes -s, -s bei I/you/they, „goes/watches“ mit -es.
- `adverbien-haeufigkeit`: Fähnchen always bis never werden auf der Skala geordnet, dann ins Satzgefüge gesetzt; Fehler: Stellung vor to be („He is always late“) vs. vor Vollverb, „always“ am Satzende.
- `present-progressive`: Wellen über now; Bau-Karte be + -ing, die Kinder bilden Sätze mit Bildern; Fehler: be vergessen („She reading“), -ing-Schreibung (running, making), Verben ohne -ing.
- `simple-oder-progressive`: Punktreihe oder Welle? Sie wählen nach Signalwort (always, now); Fehler: Welle für Gewohnheiten („He is playing football every Monday“), Punkte für „now“.
- `simple-past`: Punkt links von now mit Zeitangabe (yesterday, last week); Regelbildung -ed (play – played, study – studied, stop – stopped) selbst ergänzen; Fehler: „played“ mit did, Doppel-Verneinung ist nicht Thema (#473), -ed-Schreibung.
- `unregelmaessige-verben`: Kartenset mit drei Formen, nach Klangmustern sortiert; Kinder sortieren Karten in die Muster und bilden sing–sang–sung selbst nach; Fehler: „goed“, „buyed“, went/gone verwechselt.
- `present-perfect`: Bogen von der Vergangenheit bis now; have + 3. Form (Bau-Karte); Kinder prüfen: Zeitangabe da (Punkt, simple past) oder Ergebnis zählt jetzt (Bogen); Fehler: „I have seen it yesterday“, have/has nach Person, ever/never/already/yet Stellung.
- `will-future`: Punkt rechts von now ohne Pfeil; Kinder unterscheiden Vermutung/spontaner Entschluss; Fehler: „will goes“, „will to go“.
- `going-to`: Pfeil, der schon jetzt beginnt; Bau-Karte be + going to + Grundform; Kinder erkennen Plan oder Anzeichen; Fehler: be vergessen („I going to“), „going to“ mit -ing am Verb.
- `will-oder-going-to`: Pfeil oder Punkt? Wahl nach Anzeichen/Plan oder spontan/Vermutung, nur eindeutige Fälle; Fehler: will für schon gefassten Plan, going to für spontanes Angebot.

**Umfang:**
- Drin: Kapitel 1 bis 3 (12 Bausteine, 13 Seiten mit Wiederholungsseite), Stufe 5-6. Bejahte Aussagesätze, bei to be, have got und will/going to auch Verneinung und einfache Fragen mit der Form selbst (be, have, will). Verneinung und Fragen mit do/did gehören zu #473 und kommen hier nicht vor.
- Draußen: Fragen/Verneinung mit do und did (#473), Bedingungssätze, indirekte Rede (#481), Passiv (#480), Aussprache von -s und -ed (#482), Kapitel 4 bis 7 (Inkremente für 7-8 und 9-10). Die Gründe stehen im Abschnitt „Abgrenzung“ des Issues.
- Datenumfang: unregelmäßige Verben nur die häufigsten, etwa 30 bis 40 aus den Klangmustern ({sing, swim, drink, ring, begin}; {write, drive, ride, rise}; {buy, bring, catch, teach, think}; {go, do, see, eat, take}; {make, have, say, pay}; {cut, put, hit, let}), Liste vollständig in Content method; kein stilles „bis 20“. Zeitangaben und Signalwörter: yesterday, last week/year, ago, now, at the moment, every day, always/usually/often/sometimes/never, already, yet, ever, just, tomorrow, next week, soon.
- Sprachen: Deutsch, Englisch (britisch) als Beispielsprache; Erklärtexte Deutsch (`languages: [de]`), kein zweiter Seitenbaum. Hören und Sprechen mit Stimme `bf_emma`, ganze Sätze (Skill `lernapps-audio`).
- Was die App nicht kann: keine Spracherkennung; Bewertung der Aussprache durch das Kind; kein Timer, kein Spiel.

**Strang und Quellen:** Strang `englisch/grammatik` (Karte `https://lernapps.net/apps/map/englisch.json`, `explainerFocus: competency`, Strang-App; eine Seite übt nur Bausteine des Strangs `grammatik`). Fehlt kein Baustein der Karte. Kein Lehrplan nötig (Strang). Geöffnet am 2026-11-21, nur Fakten, keine Sätze (CC BY-SA): <https://en.wikipedia.org/wiki/English_irregular_verbs> (Klangmuster sing–sang–sung, sink–sank–sunk, Ablaut; regelmäßige Verben auf -ed), <https://en.wikipedia.org/wiki/Present_perfect> und <https://en.wikipedia.org/wiki/English_verbs> (Formen und Gebrauch, geöffnet, Antwort 200). Nicht geprüft: deutsche Wikipedia hat keine Seite „Zeitform (Englisch)“ (404), kein Klexikon-Artikel gelesen. Die Beispielsätze erfinde ich selbst aus dem Alltag der Figuren (Millbrook School, Figuren und Termine aus konventionen.md).

**Üben (Muster aus `foreign-languages.md`):** Das Ziel ist Bilden und Wählen der Zeitform, nicht Auswendiglernen.
- Auf den Strahl setzen: Ereignis aus dem Alltag der Figuren (Satz mit Signalwort) wählen oder ordnen, auf welches Zeichen es gehört (Punkt, Punktreihe, Welle, Bogen, Pfeil). Das ist die tragende Übung; die Kinder leiten die Zeitform aus dem Zeichen her.
- Form wählen (`choice` mit Distraktoren), Lücke füllen (`gap`), Form bilden mit Hinweis (`write` mit `cue`), Tabelle der Formen (`table`), Satzstellung (`ordering`, z. B. Häufigkeitsadverb), Übersetzen DE→EN (`write`) nur wo der Satz eindeutig ist.
- Hören und Sprechen: ganze Sätze mit Stimme `bf_emma` (Diktat `language-task` mit `audio`), Nachsprechen (`speaking-task`) nur wenige je Kapitel; nichts bewertet, wie jemand spricht.
- Typische Fehler mit eigener Rückmeldung: fehlendes -s bei he/she/it; „I am go“ (be + Grundform); -ing ohne be; present progressive für Gewohnheiten (und umgekehrt); *goed* statt went; present perfect mit gestern; will für feste Pläne mit Anzeichen.


**Stand (2026-11-21, Pause):** Explore abgeschlossen (Recherche-Checkpoint bestätigt). Plan fertig bis auf den Checkpoint „Plan und Inhaltsmethode“: er wurde schon an den Orchestrator geschickt (Fragen: Musterseite `simple-present`, Diktat/Nachsprechen auf jeder Seite), die Antwort steht aus. Auf Anweisung des Orchestrators ruht die Arbeit, bis er „weiter“ meldet (der Nutzer klärt zuerst den Grundwortschatz Englisch). Kein Code, keine weiteren Pushes. Bei „weiter“: Antwort zum Plan-Checkpoint abwarten bzw. verwenden, die Wortlisten gegen den geklärten Grundwortschatz prüfen.

**Grundwortschatz-Prüfung (2026-11-21, `https://lernapps.net/apps/map/englisch/grundwortschatz/`, 1343 Wörter A1, 1080 A2):** Alle 38 unregelmäßigen Verben stehen in der Grundform in A1 (sing, swim, drink, begin, ring, run, come, write, drive, ride, take, give, eat, see, know, buy, bring, think, catch, teach, go, do, be, have, make, say, pay, meet, read, sit, get, find, lose, leave, cut, put, hit, let); die Liste führt nur Grundformen, die Formen (sang, sung …) führt die Seite selbst ein. Signalwörter: A1 yesterday, tomorrow, last, week, ago, always, usually, often, sometimes, never, already, ever, just, soon, next, maybe, probably; A2 yet. Alltagswörter: A1 play, watch, study, stop, like, jacket, brother, football, birthday, party, rain, window, door, chair, table, teacher, homework; A2 classroom, lesson. Nicht in der Liste: poster, clouds (cloud): nur wenn die Situation sie braucht, auf der Seite eingeführt und im Inhaltsführer gelistet. Weitere Wörter prüft ein Skript gegen die Liste (Wörter je Seite in den Notes nachführen).

**Lerner-Check der Musterseite `simple-present` (Sub-Agent, Kind 5-6, 1280 und 360 px) und was behoben wurde:** Im Bild war nicht zu erkennen, wer Ellie ist → Bildunterschrift nennt alle vier. Die Antwort der Einstiegsfrage stand im Absatz darüber → Text gekürzt (nur Bedeutung von Saturday und football), Sprechblase sagt every Saturday. Warum now zwischen zwei Punkten liegt, und dass ein Punkt ein Samstag ist → Text und Bildunterschrift. „simple present“ war nicht eingeführt → Text. you doppelt in der Tabelle → you (du), you (ihr). Merke-Kasten gab die Lösungen der Übungen vor → Beispiele teach, fly (Übungen: go, watch, study); Endung, Konsonant, Vokal erklärt. Wörter ohne Erklärung (to, a, and, in, the, on, Saturdays, Parkers, Millbrook) → Poster ergänzt, Sätze ohne Parkers, Millbrook, Saturdays; Audio neu. Unwörter (likees, playes) als Auswahl → echte Lernerfehler (is like, are plays). Stimmt/Stimmt-nicht-Übung (50:50) → Korrekturübung zum Schreiben. Übersetzen: Every Saturday Peter plays football zusätzlich zugelassen, soccer mit eigener Meldung. Offene Aufgabe bezieht jetzt die Punktreihe ein.
**Nicht behebbar im Inhalt (Vorlage `lernapps/app-templates`, an den Orchestrator gemeldet):** Standardmeldung „Deine Fassung kann trotzdem richtig sein. Frag nach, wenn du unsicher bist.“ ohne Tutor sichtbar; „richtig“ mit Warnung zu Groß-/Kleinschreibung nennt ein falsches Wort („day“); „Wähle, tippe oder ordne alles zu“ bei leerer Antwort; Tempo-Knöpfe und „Hilfe“ im Test nicht sichtbar; offene Aufgabe nimmt ein Satzstück an; keine Teilprüfung einzelner Zeilen.

**Sprachprüfung (Sub-Agent, alle 13 Seiten, Englisch und Deutsch) und was behoben wurde:** 26 Funde, alle geprüft; 25 behoben, einer (sink, break, speak nicht auf der Seite) war falsch, weil die Verben im Poster „Wörter dieser Seite“ standen, behoben nur Auftrag und Hinweis. Wichtigste: haeufigkeit „von oft (oben)“ → „von immer (oben)“; present-perfect: Widerspruch bei „Zeitangabe“ (Tabelle heißt „Signalwörter für das present perfect“), Distraktoren mit `did` zu `has did`, `accepted` ergänzt; present-progressive: `alt` verriet die Lösung, Verdopplungsregel genauer; simple-oder-progressive: Fähnchen über der Welle; to-be: Kurzformen zugelassen (you're not, Amir's not); will: Beispielsatz mit I think; will-oder-going-to: deutsche Wörter aus dem englischen Cue in `source`; einheitlich Punktreihe und Poster, happy = froh, phone = Telefon / Handy. Audio: alle 72 Hörtexte stimmen mit den Seiten überein (geprüft). Kein Satz zwischen Seiten doppelt.
**Wörter außerhalb A1/A2 (im Inhaltsführer gelistet):** sink (Poster-Eintrag auf `unregelmaessig`), poster (A1/A2-Liste kennt es nicht, im Poster der Seite erklärt), friends (Mehrzahl von friend). `yet` ist A2.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Ja, passt. Kapitel 1 bis 3 stimmen mit Issue und requires der Karte. Reihenfolge: simple-oder-progressive nach present-progressive und adverbien-haeufigkeit; unregelmaessige-verben nach simple-past; present-perfect danach; will-future frei (Anfang K3); going-to nach present-progressive; will-oder-going-to zuletzt. Unregelmäßige Verben 30-40 nach Klangmustern, passend zu A1/A2. Ungeprüftes bleibt im Inhaltsführer als ungeprüft. Jede Seite bringt einen neuen Schritt (explainer-one-step); Figuren-Szenen passen zum Zeitstrahl-Bild.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

- Goal: „Ich weiß, welche englische Zeitform ich für Gewohnheiten, gerade Laufendes, Vergangenes, Pläne und Dauer brauche, und kann sie bilden.“ Ein Zeitstrahl mit dem Punkt now trägt den Explainer; die Kinder setzen Ereignisse aus dem Alltag der Figuren selbst auf den Strahl. (Issue lernapps/apps#472)
- Learners: Englisch, Strang „Grammatik“, Stufen 5-6, 7-8, 9-10; diese erste Version nur Stufe 5-6 (Kapitel 1 bis 3). Vorwissen: Hello, Millbrook! (#470) und Personalpronomen (#471). (Issue #472 und Startnachricht)
- Model and focus: Vorbild Hello, Millbrook! (#470, `lernapps/hello-millbrook`); Schwerpunkt Visualisierung (Zeitstrahl mit festen Zeichen) und Übungen, die aus dem Zeichen die Form herleiten. (Issue #472, Didaktik; konventionen.md)
- Hurdles: -s bei he/she/it vergessen; Verlaufsform für Gewohnheiten; unregelmäßige Verben (went/gone); present perfect mit Zeitangabe; will oder going to. Eigene Rückmeldung je Fehler. (Issue #472: „Das -s bei he, she und it leuchtet auf“, Signalwörter als Fähnchen)
- Content: Sprachlich und didaktisch von mir nach dem Issue und der Lernlandkarte; Figuren, Orte, Begriffe nach konventionen.md (Epic #489). Keine eigenen Materialien des Erstellers.
- Amount: Nur Kapitel 1 „Immer oder gerade jetzt?“ (6 Bausteine), 2 „Gestern und schon“ (3) und 3 „Morgen und später“ (3). Kapitel 4 bis 7 kommen später als Inkremente. (Startnachricht)
- Languages: Deutsche Erklärtexte, englische Beispiele, britisches Englisch (konventionen.md §4).
- Look and feel: fixed by the archetype (Look der Laufzeit, ruhig wie ein Arbeitsblatt, Dunkelmodus folgt dem Gerät). Die Zeichen des Zeitstrahls sind eigene Abbildungen im Stil von #470.
- Terms: „Ausdruck“, nie „Wendung“; Fachbegriffe noun, verb, adjective, sentence, tense; Zeitstrahl, now, Punkt, Welle, Bogen, Fähnchen, Bau-Karte (Issue #472). Anrede „du“.
- Finding the app: Zeitformen Englisch, simple present, present progressive, simple past, present perfect, will, going to, Zeitstrahl. (aus den Bausteinen des Issues abgeleitet; der Ersteller bestätigt am Checkpoint)

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Plan bestätigt. simple-present als Musterseite ist richtig. Diktat und Nachsprechen auf jeder Seite, je höchstens drei ganze Sätze, Sätze wiederholen sich nicht zwischen Seiten; Audio mit regen_audio.py, Namen am Satzende zweisilbig. Wörter aus A1/A2 (Grundwortschatz), Ausnahmen nur eingeführt und im Inhaltsführer gelistet; Wörter und 38 unregelmäßige Verben gegen die Liste prüfen und in den Notes festhalten.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

**Aufbau.** Strang-App `strand: englisch/grammatik`, Format 2, `languages: [de]`. Drei Kapitel (`immer-oder-jetzt`, `gestern-und-schon`, `morgen-und-spaeter`), 13 Seiten, eine Kompetenz je Seite, Reihenfolge wie in den Notes (am Checkpoint „Recherche“ bestätigt). Alle Abschnitts-IDs gleich: `einstieg` (Szene, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Zeichen und Bau-Karte, Merke-Kasten), `uebung` (mindestens vier, leicht → schwer), `anwenden` (den Strahl selbst füllen: `open-task` oder `speaking-task`), `weiter` (nächster Schritt der Geschichte). Die Wiederholungsseite hat keine Übung.

**Geschichte (Figuren aus konventionen.md, nicht ändern).** Mr Hill lässt die Klasse ein Wandbild „Millbrook-Zeitstrahl“ gestalten: Sophie, Ellie, Peter und Amir hängen Karten auf den Strahl (K1: was sie immer tun und was gerade passiert; K2: was gestern und schon passiert ist; K3: was kommt, z. B. die Geburtstage am 5. Mai, 10. Juli, 12. Oktober, 14. Oktober). Jede Seite hat eine Szene (`szene-<seite>.svg`, Figuren als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 kopiert) und endet mit dem nächsten Schritt am Wandbild. Zwei wachsende Bilder: der **Zeitstrahl** (eine SVG-Familie; K1 now mit Punktreihe und Welle, K2 nach links mit Punkt und Bogen, K3 nach rechts mit Pfeil und Punkt) und die Tabelle „Klassenzimmer-Poster · Zeitformen“ (Zeichen · Form · Beispiel); in K2 und K3 dazu „Schulkalender · Zeitangaben“ (Signalwörter).

**Zeichen** (eigene SVG in `src/images/`, Quelle „eigene Zeichnung“, `CC-BY-4.0`; gleich auf jeder Seite, im Inhaltsführer unter „Figures“ festgeschrieben): now = senkrechter Strich; simple = ausgefüllte Punkte (Gewohnheit = Reihe, einzelnes Ereignis = ein Punkt mit Zeitangabe); progressive = Welle über now; perfect = Bogen von links bis now; going to = Pfeil, der bei now beginnt; will = Punkt rechts ohne Pfeil. Signalwörter hängen als Fähnchen am Strahl. Bau-Karten: be + -ing, have + 3. Form, be + going to + Grundform, will + Grundform. Das -s bei he/she/it ist farbig hervorgehoben („He, she, it – das s muss mit.“). In Aufgaben zeigt die Figur den leeren Strahl mit Legende, nie das Ergebnis (`explainer-figure-hides-answer`).

**Komponente? Nein (guess).** Das Setzen auf den Strahl wird mit eingebauten Blöcken geübt: `matching` (Satz ↔ Zeichen), `ordering` (Fähnchen von always bis never; Ereignisse nach Zeit), `labelled-figure` mit `language-task` (Marker am Strahl). Eine Ziehen-Komponente kostet Logik, Test und Text ohne JavaScript (`prefer-built-in-block`); sie bleibt Wunsch für ein Inkrement (im Inhaltsführer vermerkt).

**Muster je Kompetenz** (leicht → schwer, jede Übung mit `mistakes` und `hint`):
- `to-be`: `matching` Person ↔ Form; `language-task` `table` (am/is/are mit Lücken); `choice` mit Distraktoren; `write` Verneinung und Frage aus Cue; Diktat; Nachsprechen.
- `have-got`: `choice` have/has; `gap` nach Person mit Dingen der Figuren; `write` Frage und Verneinung mit have got; Diktat; Nachsprechen.
- `simple-present`: `matching` Satz ↔ Punktreihe; `table` Formen mit -s-Spalte; `gap`/`write` mit Cue (`cue: "play · she"`); Schreibung (goes, watches, studies) als `choice`; Diktat; Nachsprechen.
- `adverbien-haeufigkeit`: `ordering` Fähnchen always–never; `ordering` Satzteile (She often plays …; He is never late); `gap` Stellung; `write` mit Cue; Diktat.
- `present-progressive`: Bau-Karte; `matching` Szene-Satz ↔ Welle; `table` Formen; `gap` (-ing-Schreibung running, making, writing); `write` aus Szene; Diktat; Nachsprechen.
- `simple-oder-progressive`: `choice` mit Signalwort-Fähnchen; `matching` Signalwort ↔ Zeichen; `gap` mit Klammer-Cue; `true-false` mit Begründung; `write`; Diktat.
- `simple-past`: `table` -ed-Bildung (play – played, study – studied, stop – stopped, like – liked); `choice` Zeitangabe (yesterday, last week, two days ago); `gap` mit Cue; `write`; Diktat; Nachsprechen. Nur Bejahung (did-Verneinung gehört zu #473).
- `unregelmaessige-verben`: Kartenset in Klangmustern („Klassenzimmer-Poster · Unregelmäßige Verben“); `matching` Grundform ↔ past; `table` (drei Formen mit Lücken); Muster erkennen (sing – sang – sung → swim); `write` mit Cue; `choice` went/gone; Diktat; Nachsprechen.
  Verben (Auswahl A1/A2, Grundwortschatz-Seite der Karte vorher öffnen): sing sang sung · swim swam swum · drink drank drunk · begin began begun · ring rang rung · run ran run · come came come · write wrote written · drive drove driven · ride rode ridden · take took taken · give gave given · eat ate eaten · see saw seen · know knew known · buy bought bought · bring brought brought · think thought thought · catch caught caught · teach taught taught · go went gone · do did done · be was/were been · have had had · make made made · say said said · pay paid paid · meet met met · read read read · sit sat sat · get got got · find found found · lose lost lost · leave left left · cut cut cut · put put put · hit hit hit · let let let (38).
- `present-perfect`: Bau-Karte have + 3. Form (Formen von der vorigen Seite); `matching` Signalwort (ever, never, already, yet, just) ↔ Bogen; `choice` simple past oder present perfect nur in eindeutigen Fällen (Zeitangabe → past, Ergebnis zählt jetzt → perfect); `gap`; `ordering` Satzstellung (already, yet); Diktat; Nachsprechen. Ohne since/for (Kapitel 5).
- `will-future`: `choice` Vermutung oder spontaner Entschluss; `table` Form (will + Grundform, alle Personen gleich); `gap`/`write` mit Cue (maybe, I think, probably); `matching` Situation ↔ Satz; Diktat; Nachsprechen.
- `going-to`: Bau-Karte be + going to + Grundform (be aus K1); `table`; `choice` be-Form; `gap`; `matching` Anzeichen ↔ Satz („Look at the clouds!“ ↔ „It is going to rain.“); `write`; Diktat; Nachsprechen.
- `will-oder-going-to`: `choice` mit Begründung im Feedback („Der Plan steht schon: going to“, „spontan: will“); `matching` Situation ↔ Zeichen; `true-false` mit Begründung; `write` Pläne der Figuren; Diktat; Rückblick auf K3. Nur eindeutige Fälle.

**Rückmeldungen.** Jeder typische Fehler der Notes ist ein `mistakes`-Eintrag mit eigener Meldung, die die Regel am Zeichen benennt („Eine Punktreihe: he, she, it – das s muss mit“, „Ein Punkt mit Zeitangabe → simple past, kein Bogen“). Gleichwertige Antworten mit `(a|b)` (isn't/is not, I'm/I am); britische Schreibung.

**Hören und Sprechen.** Stimme `bf_emma`, nur ganze Sätze, erzeugt mit `.agents/skills/app-content/scripts/regen_audio.py` (Kopie aus hello-millbrook, schneidet das Ausklingen ab). Namen am Satzende zweisilbig (Sophie, Peter, Ellie, Amir). Jede Seite ein Diktat (`<seite>-hoeren`), dazu Nachsprechen (`<seite>-nachsprechen`). Die Aussprache von -s und -ed bleibt in #482.

**Wörter.** Quelle: Grundwortschatz-Seite der Karte (`https://lernapps.net/apps/map/englisch/grundwortschatz/`), A1/A2; jedes Wort vor einer Übung mit Bedeutung eingeführt. Englische Aufgaben enthalten kein deutsches Wort. Fachbegriffe verb, noun, tense, sentence nur benutzen (aus #470). Keine Datendateien: jede Tatsache steht einmal in ihrer Seite.

**Wiederholungsseite K1:** `recap: englisch/personalpronomen` („Das brauchst du hier“), kompakt: I, you, he, she, it, we, they; Link auf die echte Seite aus #471, sonst auf die Karte. Keine Übung. Andere Voraussetzungen von außen gibt es nicht.

**Selbsteinschätzung** (Skill `lernapps-explainer-self-assessment`, im Commit-Teil): je Seite 2 Übungen, die ohne die Seite verständlich sind.

**Ein späteres Kapitel ergänzen (Inkremente 4 bis 7).** Karte lesen, Seite nach dem Muster der Musterseite anlegen, den Strahl um die neuen Zeichen erweitern (Welle in der Vergangenheit, Bogen wird Welle, Fähnchen since/for, Stoppschild für Zustandsverben, Punktreihe in der Vergangenheit für used to), Poster erweitern, Übungen aus den Mustern mit `mistakes`, Hörtexte mit `regen_audio.py`, `check`, Inhaltsführer nachführen.

**Engagement je Seite** (Einstieg · Wechsel · Belohnung · Geschichte):
- `das-brauchst-du` (Wiederholung K1): kompakt, keine Übung · Tabelle der Pronomen · Kinder wissen, dass sie sie gleich brauchen · Mr Hill hängt den leeren Strahl an die Wand.
- `to-be`: Sophie stellt Karten für den Strahl vor („I am Sophie“): die Kinder ordnen Person ↔ Form · Tabelle lesen, selbst ergänzen, schreiben · sie stellen die Figuren mit be vor · Karte „Wer ist wer?“ hängt am Strahl.
- `have-got`: Ellie zeigt, was sie hat (a red jacket, a brother): Lücke have/has · Szene, Tabelle, Frage schreiben · sie beschreiben Dinge der Figuren · Peters Karte „What has he got?“.
- `simple-present`: Peter spielt jeden Samstag Fußball: Punktreihe lesen (Satz ↔ Gewohnheit) · Tabelle mit -s · sie schreiben Gewohnheiten der vier Kinder · die Reihe von Punkten steht am Strahl.
- `haeufigkeit`: Fähnchen always bis never ordnen · Ordnen, Lücke, Schreiben · sie beschreiben ihre eigene Woche · Amir ist nie zu spät, Peter manchmal.
- `present-progressive`: Szene im Klassenzimmer (Wer macht gerade was?): Satz ↔ Welle · Bau-Karte be + -ing, Tabelle, -ing-Schreibung · sie beschreiben die Szene · Welle über now am Strahl.
- `simple-oder-progressive`: zwei Sätze mit Signalwort-Fähnchen: Punktreihe oder Welle? · Signalwort-Zuordnung, Lücke mit Klammer · sie entscheiden bei Sätzen der Kinder · Rückblick K1: der Strahl hat jetzt Punktreihe und Welle.
- `simple-past`: Sophie erzählt, was gestern war (yesterday, last week): Punkt mit Zeitangabe · Bildung -ed am Strahl, Tabelle, Lücke · sie schreiben, was gestern passiert ist · der Strahl wächst nach links.
- `unregelmaessig`: Karten fallen vom Strahl: Mr Hill zeigt went, saw, ate: sortieren nach Klangmustern · Ordnen, Tabelle, Schreiben · sie bilden die Muster nach (sing → swim) · Kartenset ist das Poster.
- `present-perfect`: Ellie: „Have you ever been to London?“: Bogen bis now · Bau-Karte have + 3. Form, Signalwörter, simple past gegen Bogen · sie entscheiden bei Sätzen der Kinder · Bogen am Strahl; Rückblick K2.
- `will`: Amir überlegt, was nächstes Jahr ist (I think / maybe): Punkt rechts · Form, Entscheidung Vermutung/spontan · sie machen Vorhersagen · Strahl wächst nach rechts.
- `going-to`: Peter plant seinen Geburtstag am 5. Mai: Pfeil ab now · Bau-Karte, Anzeichen ↔ Satz · sie schreiben Pläne der Figuren · Pfeil am Strahl.
- `will-oder-going-to`: Ellies Geburtstag und eine spontane Idee: Pfeil oder Punkt? · Entscheiden mit Begründung, Zuordnung · sie schreiben Pläne und Angebote · Rückblick K3, der Strahl ist fertig (Vergangenheit, jetzt, Zukunft).

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [x] Load skill `lernapps-explainer`.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Musterseite K1 `simple-present` (immer-oder-jetzt/simple-present): Zeichnungen (Zeitstrahl-SVG mit now, Punktreihe und Fähnchen; Szene Peter spielt Fußball; Figuren aus millbrook-klassenzimmer.svg von #470), alle Abschnitte (einstieg, neu, uebung mit mindestens vier Übungen und mistakes, anwenden, weiter), Diktat und Nachsprechen mit bf_emma via regen_audio.py, Tabelle Klassenzimmer-Poster · Zeitformen; zeigt das Muster aller Seiten
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [x] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
      Creator: Ja, die anderen Seiten dürfen nach diesem Muster folgen. Update 0.18.3 jetzt (erledigt). Wiederholungsseite personalpronomen bald; Reihenfolge to-be, have-got, simple-present, adverbien-haeufigkeit, present-progressive, simple-oder-progressive. Je Seite ein neuer Schritt, Sätze nicht von Seite zu Seite wiederholen, Diktat und Nachsprechen je höchstens drei ganze Sätze, Grundwortschatz-Abgleich für jede Seite. work regelmäßig pushen, nicht gh-pages anlegen.
- [x] Kapitel 1 Rest: Wiederholungsseite das-brauchst-du (recap personalpronomen) und Seiten to-be, have-got, haeufigkeit (adverbien-haeufigkeit) nach dem Muster, je mit Szene, Übungen, mistakes, Audio
- [x] Kapitel 1 Rest: Seiten present-progressive (Welle, Bau-Karte be + -ing) und simple-oder-progressive (Signalwörter, Rückblick K1) nach dem Muster, je mit Szene, Übungen, mistakes, Audio
- [x] Kapitel 2: Seiten simple-past (Strahl nach links), unregelmaessig (Kartenset der 38 Verben nach Klangmustern, Poster) und present-perfect (Bogen, Bau-Karte have + 3. Form, Rückblick K2) nach dem Muster, je mit Szene, Übungen, mistakes, Audio, Schulkalender · Zeitangaben
- [x] Kapitel 3: Seiten will, going-to (Pfeil, Bau-Karte) und will-oder-going-to (Entscheiden mit Begründung, Rückblick K3, fertiger Strahl) nach dem Muster, je mit Szene, Übungen, mistakes, Audio
- [x] Selbsteinschätzung (Skill lernapps-explainer-self-assessment) je Kapitel und der App; Übungen mit Prüfung, dass sie ohne die Seite verständlich sind
- [x] Sprachprüfung: ein Sub-Agent prüft das Englisch (britisch, keine deutschen Wörter in englischen Aufgaben) und das Deutsche aller Seiten; Funde beheben und unter Notes aufschreiben
<!-- tasks: pages (6 added): the other pages or screens, after the pattern -->
- [x] Update the content guide so that it describes the app as built (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [x] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
