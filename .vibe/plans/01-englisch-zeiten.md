---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: explore
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
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
- [ ] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.

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

- [ ] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [ ] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [ ] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [ ] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [ ] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [ ] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [ ] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [ ] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [ ] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
<!-- tasks: pattern: the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
<!-- tasks: pages: the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
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
