---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 2 }
---

# Increment: increment-02-erzaehlen-dauer-plaene

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-22. Explore, Plan, Code, Commit.*

## Goal

Jugendliche der Klassen 7-8 erzählen auf Englisch, ordnen Hintergrund, Handlung und Vorvergangenheit, sagen mit since, for und dem present perfect progressive, wie lange etwas schon dauert, und sprechen über feste Pläne und genaue Zeitpunkte in der Zukunft. Jede Seite hat ein Lesestück (Chat, Tagebuch, Interview, Zeitungsartikel), an dem sie die Zeitform erkennen, bevor sie sie bilden.

## Key decisions

<!-- One line each: decision and reason. Your own choice without the creator: mark "(guess)". -->

- `scope` bleibt wie in der ersten Version (ja): jede Seite hat `open-task` und `scope`.
- Lesestücke sind eigene erfundene Texte der Figuren (guess), keine VOA-/Wikinews-/African-Storybook-Texte.
- Randglossar als Vokabelblock (`type: vocabulary`, app-templates ab 0.14) vor dem Lesestück, eine Wörterliste je Seite.
- Der Hinweis `explainer-text-load` bei Lesestück-Seiten ist bewusst (Konventionen Abschnitt 8).

## Notes

<!-- New competencies by chapter (ids of the strand), didactic approach, scope, sources and licences, open questions. -->

**Karte** (`https://lernapps.net/apps/map/englisch.json`, Strang `grammatik`, gelesen 2026-11-22). Alle neun Bausteine liegen im Band 7-8 und sind Lücken (`practisedBy` leer). Ihre Voraussetzungen sind alle in der ersten Version geübt (`simple-past`, `present-progressive`, `present-perfect`, `will-future`, `will-oder-going-to`, `simple-oder-progressive`): keine Wiederholungsseite nötig, kein `ahead`.
- Kapitel 4 `erzaehlen` „Erzählen: Hintergrund, Handlung, vorher“: `past-progressive` (Schritt 1; requires simple-past, present-progressive) · `past-perfect` (1; present-perfect) · `zeitenfolge-temporalsaetze` (2; past-perfect, will-future) · `present-perfect-oder-simple-past` (1; present-perfect).
- Kapitel 5 `dauer` „Seit wann und wie lange?“: `since-for` (1; present-perfect) · `present-perfect-progressive` (2; since-for, present-progressive) · `dynamic-stative` (1; simple-oder-progressive).
- Kapitel 6 `plaene` „Pläne, Fahrpläne und Zeitpunkte“: `present-fuer-zukunft` (1; will-oder-going-to) · `future-progressive-perfect` (1; will-future, present-perfect, present-progressive).
- Seitenreihenfolge nach `requires`: K4 past-progressive, past-perfect, zeitenfolge (nach past-perfect), present-perfect-oder-simple-past; K5 since-for, present-perfect-progressive (nach since-for), dynamic-stative; K6 present-fuer-zukunft, future-progressive-perfect. Neun Seiten, eine Kompetenz je Seite.

**Quellen** (geöffnet 2026-11-22, nur Fakten, keine Sätze, CC BY-SA): <https://en.wikipedia.org/wiki/Past_continuous>, <https://en.wikipedia.org/wiki/Pluperfect> (past perfect: „had arrived before the game began“), <https://en.wikipedia.org/wiki/Uses_of_English_verb_forms> (present perfect progressive, future progressive, future perfect, Gebrauch der Zeiten), <https://en.wikipedia.org/wiki/Stative_verb>, <https://en.wikipedia.org/wiki/Future_perfect>, <https://en.wikipedia.org/wiki/Sequence_of_tenses>. Alle antworteten 200. Nicht verwendet, weil die Konventionen sie ausschließen oder nur als Faktenquelle zulassen: BBC Newsround, Time for Kids, Newsela, CommonLit, DOGOnews, The Conversation, Teen Ink; VOA, Wikinews und African Storybook nur, wenn ein Lesestück einen realen Text übernimmt (siehe nächster Punkt).

**Lesestücke:** Alle neun Lesestücke sind **eigene, erfundene Texte der Figuren** (Chat, Tagebuch, Interview, Zeitungsartikel der Millbrook School), 150 bis 300 Wörter, ohne reale Faktenangaben. Sie stützen sich nicht auf fremde Sätze, darum brauchen sie keine Textquelle; real sind nur die Grammatikfakten der Seiten (Wikipedia, siehe oben). Wo ein Lesestück ein reales Faktum nennt (zum Beispiel ein Datum oder Ort), wird es mit geöffneter Quelle im Inhaltsführer belegt; sonst kein Satz mit realer Behauptung (`Millbrook` und die Parkers sind erfunden). (guess: keine VOA-/Wikinews-Texte übernommen, weil ein ganzer fremder Text die Zeitform nicht gezielt zeigt und Rechtepflichten bringt; die erlaubten Quellen bleiben für spätere Inkremente offen.)

**Figuren (13 bis 14):** Sophie (13 bis 14, sie bleibt in England), Ellie Parker (13), Peter Parker (11), Amir (13), Mr Hill. Sophies Geburtstag 14. Oktober, Amir 12. Oktober, Ellie 10. Juli, Peter 5. Mai bleiben. Aus Sophie (11) wird Sophie (13): zwei Jahre später, gleiches Äußeres (Zeichnungen aus der ersten Version, Peter kleiner, vgl. Notes der ersten Version). Neue Nebenfiguren nur nach Rückfrage; Mrs Parker nur im Text (rote Haare, türkise Strickjacke), nicht gezeichnet. (guess)

**Didaktik je Seite (Lesestück · Zeichen am Strahl · Fehlvorstellung):**
- `past-progressive`: Tagebuch von Sophie über den Schulausflug („It was raining when we arrived“). Die Welle wandert nach links, ein Punkt unterbricht sie. Kinder markieren im Text Hintergrund (Welle) und Handlung (Punkt), bilden dann was + -ing. Fehler: simple past für den Hintergrund („It rained when we arrived“); was/were vergessen; when/while vertauscht.
- `past-perfect`: Chat-Verlauf von Peter und Ellie: der Bus war schon weg. Das past perfect rückt einen Schritt nach links (had + 3. Form). Kinder ordnen zwei Ereignisse und wählen die Zeit des früheren. Fehler: simple past für das frühere Ereignis; had weggelassen; had + 2. Form.
- `zeitenfolge-temporalsaetze`: Interview mit Mr Hill über das Schulfest: when, after, before, as soon as mit simple present für die Zukunft („as soon as the bell rings, we will start“) und mit past perfect („after we had finished“). Fehler: will im Nebensatz; falsche Zeit nach after/before.
- `present-perfect-oder-simple-past`: Zeitungsartikel der Schülerzeitung über die neue Bibliothek: Punkt mit Zeitangabe (simple past) neben Bogen bis now (present perfect). Kinder begründen die Wahl. Fehler: present perfect mit yesterday; simple past, wo das Ergebnis jetzt zählt.
- `since-for`: Interview/Umfrage der Klasse „How long have you…?“. Since markiert den Startpunkt, for die Länge. Fehler: for mit Zeitpunkt, since mit Dauer; simple present („I live here since two years“).
- `present-perfect-progressive`: Chat: Sophie wartet seit einer Stunde auf Ellie. Der Bogen wird zur Welle (have/has been + -ing). Fehler: present perfect statt progressive bei andauernder Handlung; been vergessen; Zustandsverb mit progressive.
- `dynamic-stative`: Dialog Sophie und Amir („I know/like/belong“): Stoppschild für die Welle bei know, like, belong, want, need. Fehler: „I am knowing“, „She is liking“; Ausnahmen (think, have, see) nur als Hinweis.
- `present-fuer-zukunft`: Chat mit Fahrplan der Klassenfahrt: Kalendereintrag (present progressive, Verabredung) und Fahrplan (simple present, Zeiten) liegen auf dem Strahl. Fehler: will für Verabredungen und Fahrpläne; simple present für Verabredungen.
- `future-progressive-perfect`: Interview „Wo bist du nächsten Samstag um acht?“: will be doing spiegelt die Welle in die Zukunft, will have done den Bogen. Fehler: will do statt will be doing; will have + 2. Form.

**Seitenaufbau (Muster Lesestück, neu gegenüber Stufe 5-6):** `einstieg` (Vorwissen-Frage, „Das kannst du danach“), `lesestueck` (Text in Abschnitten mit Randglossar: schwere Wörter am Rand, als Tabelle oder Merke-Kasten unter dem Absatz, weil die Laufzeit kein Randglossar kennt), `neu` (Zeichen, Bau-Karte, Merke), `uebung` (Aufgaben in drei Stufen: Verstehen, Belegen mit Zeile, Meinung; höchstens etwa 25 Items), `anwenden` (Schreib- oder Sprechauftrag), `weiter`.

**Umfang (scope):** drin: die neun Bausteine in der Form der Karte; Zeitformen Bejahung, Verneinung (not, n't) und Frage mit Hilfsverb (was/were, had, have been); Zeit- und Signalwörter: while, when, as, before, after, as soon as, since, for, already, yet, ever, never, by, at this time. Nicht drin: Fragen und Verneinung mit do und did (#473), Bedingungssätze und indirekte Rede (#481), Passiv (#480), Aussprache -s und -ed (#482), die Kapitel 7 (past perfect progressive, used to, Überblick: Stufe 9-10), Konjunktionen allgemein. Datenumfang: alle Verben der ersten Version (38 unregelmäßige) plus Verben aus den Lesestücken, vollständig bei Bedarf im Inhaltsführer; keine neuen Listen.

**Neu gegenüber der ersten Version: Lesestück-Seiten (Skills `lernapps-explainer-design` und `lernapps-exercise-patterns`, `foreign-languages.md`, erneut gelesen).** Die Archetyp-Blöcke reichen aus, keine Komponente (`prefer-built-in-block`): Lesestück = `section` `lesestueck` mit mehreren `text`-Blöcken (nummerierte Zeilen „[1] …“, damit „Belegen mit Zeile“ möglich ist), darunter je Absatz eine kleine `table` „Randglossar“ (Wort · Bedeutung) für die schweren Wörter. Aufgaben in drei Stufen: Verstehen (`single-choice`, `matching`, `true-false` mit Begründung), Belegen (`multiple-choice` oder `single-choice` „In welcher Zeile steht …?“, `language-task` write: „Schreibe den Satz mit …“), Meinung (`open-task` mit Punkten). Hörtext: nur wenige kurze Sätze je Seite (nicht das Lesestück). Bild: nur wo es etwas zeigt (Zeitstrahl und Häufigkeits-/Fahrplan-Tabellen als `table`). Der Text-Check `explainer-text-load` zählt die Wörter des Lesestücks mit (Hinweis, kein Fehler): wenn nötig mit Hinweis leben und im Inhaltsführer begründen.

**Lerner-Check der Musterseite `erzaehlen/past-progressive` (Sub-Agent, Kind 7-8, 1280 und 360 px) und was behoben wurde:** Die Einstiegsfrage fragte nach einem Satz, den die Seite noch nicht erklärt hatte → jetzt Frage vom Zeitstrahl aus (Welle). Glossar stand unter dem Text und enthielt nur 9 Wörter → Vokabelblock „Wörter zum Tagebuch“ vor dem Text mit 17 Einträgen (get off, count, still, flew …). -ing-Regeln (Verdopplung, e fällt weg) fehlten → im Merke mit anderen Verben als in den Übungen; Frage und Verneinung (What were you doing?, wasn't) dort ergänzt. Mehrfachauswahl zu „while“ war mehrdeutig → Frage nach Zeilen mit while, eindeutig. Distraktor „Peter hielt den Schalter schon in der Hand“ war plausibel → Vogelsatz. Übung 3: Satz mit verratendem was singing ersetzt, Tipp gestrichen (dreifache Wiederholung). Übung 4, Satz 3: while my brother cooked schrieb vor den Rest → when the rain started. Übung 5: Mistake für is/are ergänzt. Offene Aufgabe: Satzanfang angeboten, Beispiel vereinfacht. Nicht im Inhalt behebbar (Vorlage): generische Meldung bei freien Antworten, keine Teilprüfung einzelner Zeilen, Mikrofon-Text.
**Update:** tooling 0.18.3 → 0.18.4, app-templates 0.11.0 → 0.14.0 (neuer Vokabelblock `vocabulary`); alle Wörtertabellen der ersten Version (9) sind jetzt Vokabelblöcke (Commit „feat: Vokabelblock statt Wörtertabellen“), `lernapps check` ohne Fehler.

## Explore

<!--
- All content questions belong here; Plan maps the answers onto the app. Ask; write no code.
- Skip what earlier answers or the app already tell. At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Read the README of the archetype's template (its path is in skill `lernapps-app`): what the app can do now.
      Tell the creator what is new, if it matters for this increment.
- [x] Load the content guide `.agents/skills/app-content/SKILL.md` and read the earlier plans in `.vibe/plans/`: what
      the app teaches, how its content is made, what is open.
- [x] Interview, one topic per question, the creator's words under "Answers": which competencies, chapters or rounds,
      for which school years; hurdles and examples; the amount; any change of look and feel or of terms. No answer:
      ask once more, then write your assumption with "(guess)".
- [x] Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [x] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.
      Creator: Ja, passt (neun Seiten, Lesestück je Seite, eigene Texte, Musterseite past-progressive). Glossar als Tabelle unter dem Absatz ist ok, solange es die Regel höchstens eine kurze Wörtertabelle je Seite erfüllt (es ersetzt die Wörter-Tabelle). Weiter zu Plan und Inhaltsmethode. Push von increment/02 und zweiter Vorschau-PR muss die Ersteller:in erlauben; bis dahin lokal arbeiten.

### Answers

<!-- The creator's answers, in their words, one bullet each. -->

- Umfang: „Baue die Kapitel **4 „Erzählen: Hintergrund, Handlung, vorher“, 5 „Seit wann und wie lange?“ und 6 „Pläne, Fahrpläne und Zeitpunkte“** (Stufe 7-8) als Inkrement in dasselbe Repository; Kapitel 7 (9-10) kommt später.“ (Orchestrator-Session in der Rolle der Ersteller:in)
- Form und Konzept: Abschnitt 8 „Höhere Stufen“ in `konventionen.md` (Lesestück als Kern der Seite, 150 bis 300 Wörter, Randglossar, Aufgaben in drei Stufen, höchstens ein Lesestück je Seite, höchstens etwa 25 Items; Sophie 13 bis 14, Chats und kurze Dialoge, ein Bild nur wo es etwas zeigt; eigene Texte nach Fakten; erlaubte Quellen VOA, Wikinews, African Storybook; Gutenberg ausgeschlossen). Die Ersteller:in hat das Konzept bestätigt („passt“).
- Bausteine und Inhalt: `issues/472.md`, Kapitel 4 bis 6 (neun Bausteine). Zeichen und Figuren wie in der ersten Version; der Strahl wächst nach den Beschreibungen des Issues.
- Regeln: alle aus Abschnitt 7 der Konventionen (keine Lösung im Text darüber, nur echte Lernerfehler, eigene Meldung je Fehler, Fuzzy-Prüfung der Hörsätze, Hörliste, Retrospektive nur mit Fakten) und die der ersten Version.
- Look und Begriffe: unverändert (Look der Laufzeit; Strahl, Punkt, Punktreihe, Welle, Bogen, Pfeil, Fähnchen, Bau-Karte; „Ausdruck“); Anrede „du“ (7-8 wie bisher).
- Workflow: `lernapps update`, Branch `increment/02-erzaehlen-dauer-plaene`, Checkpoints an die Orchestrator-Session, Vorschau-Pull-Request offen lassen, nichts nach `main`, kein Katalogeintrag.

## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [x] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [x] Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [x] (skipped: keine neue Komponente und keine interaktive Übung; Skizzen der Seite und des Strahls liegen in .vibe/sketches) Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, Plan bestätigt. Pläne und Commits lokal halten, bis die Ersteller:in den Push erlaubt. Das Lesestück darf die 350 Wörter Erklärtext überschreiten (Abschnitt 8); der Hinweis explainer-text-load ist dann bewusst, im Inhaltsführer nennen. Weiter mit der Musterseite past-progressive.

### Content method

<!-- One line each: the guide's patterns, figures and components used, and where; anything new, what it does and
cannot. Something new goes into the guide in the slice that adds it. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

**Aufbau je Seite (Muster Lesestück):** Abschnitte `einstieg` (Vorwissen-Frage als erste leichte Aufgabe, „Das kannst du danach“), `lesestueck` (Titel nennt die Sorte, z. B. „Sophies Tagebuch“; Text in 2 bis 4 `text`-Blöcken mit nummerierten Zeilen „[1] …“, nach jedem Block eine kurze `table` „Randglossar“: schwere Wörter, Wort · Bedeutung; die einzige Wörtertabelle der Seite), `neu` (Zeichen am Strahl, Bau-Karte, Merke, Zeitformen-Poster; kein Satz des Lesestücks wörtlich), `uebung` (drei Stufen, höchstens etwa 25 Items; mindestens vier Übungen mit eigener Meldung, davon `single-choice` mit `info`/`write` mit `mistakes`), `anwenden` (`speaking-task` und `open-task`), `weiter`. Titel sagen, was der Abschnitt tut. Lesestück 150 bis 300 Wörter (zählen nicht zu den 350 Wörtern Erklärtext; der Check meldet einen Hinweis `explainer-text-load`, bewusst).
**Stufen der Aufgaben:** (1) Verstehen: `single-choice`/`matching`/`true-false` mit Begründung, Fragen zum Inhalt des Lesestücks. (2) Belegen mit Zeile: `single-choice` „In welcher Zeile steht …?“ und `matching` Zeile ↔ Zeichen am Strahl; dazu `language-task` write (`mistakes`) für das Bilden der Zeitform. (3) Meinung: `open-task` (Schreib- oder Sprechauftrag, 2 bis 5 Punkte, `scope` je Seite).
**Zeichen:** Zeitstrahl-SVG je Seite (`zeitstrahl-<seite>.svg`, Farben der ersten Version: now #c0392b, Punkte #2c6fd8, Welle #8e44ad, Bogen #138d75, Pfeil/will #d35400, Hintergrund #f4efe2). Neu: Welle in der Vergangenheit (Hintergrund) mit unterbrechendem Punkt (K4), Punkt vor dem Punkt (past perfect, ein Schritt weiter links), Bogen als Welle (present perfect progressive), Fähnchen since (Startpunkt) und for (Länge, Klammer), Stoppschild an der Welle (Zustandsverben, K5), Kalendereintrag (Punkt in der Zukunft mit Datum) und Fahrplan (Tabelle), Welle über einem Zeitpunkt der Zukunft und Bogen bis zu einem Zeitpunkt der Zukunft (K6). Szenen nur wo sie etwas zeigen (Peter kleiner gezeichnet; Mrs Parker nicht gezeichnet). Bilder der Figuren (Sophie 13 bis 14): gleiche `<g id>`-Zeichnungen wie in der ersten Version.
**Übungsarten je Seite** (mindestens vier mit eigener Meldung; keine `punctuation: hint`, keine `accepted`): past-progressive: Lesestück markieren (`matching` Satz ↔ Welle/Punkt), `language-task` choice (was/were + -ing, when/while), write mit Cue, Korrektur, Satzbau `ordering` nur bei eindeutiger Reihenfolge; past-perfect: `matching` Ereignis ↔ früher/später, choice had + 3. Form, write, Korrektur; zeitenfolge: choice (Zeit im Nebensatz), write, Satzteile verbinden; present-perfect-oder-simple-past: Lesestück-Zeilen sortieren (Punkt oder Bogen), choice mit Signalwort, Korrektur, Begründungsfrage; since-for: choice since/for, `ordering` Startpunkt/Länge, write; present-perfect-progressive: choice have/has been, write, Zustandsverb-Korrektur; dynamic-stative: `matching` Verb ↔ Welle/Stoppschild, choice, Korrektur; present-fuer-zukunft: Fahrplan lesen (`table`), choice Verabredung/Fahrplan, write; future-progressive-perfect: choice will be doing/will have done, write. Jede Übung mit Hörsatz-Regeln der ersten Version (Fuzzy-Prüfung `pruefe_hoersaetze.py`, Hörliste im Inhaltsführer, `regen_audio.py` mit Fehllaut-Schnitt, keine Namen nur für den Klang, nur wenige kurze Sätze je Seite, Lesestück nicht gesprochen).
**Wie ein späterer Agent weitermacht:** Kapitel 7 (Stufe 9-10) nach demselben Muster, Strahl um Welle+Bogen in der Vergangenheit (past perfect progressive) und Punktreihe in der Vergangenheit (used to) erweitern; die Ziele und Wörter stehen im Inhaltsführer.

## Code

<!--
- Build locally on the branch, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first.
-->

### Tasks

- [x] `git switch -c increment/<NN>-<short name>` from `main`. Commit this plan on it.
- [x] Load skill `lernapps-cli`. Update the app as its section "Update" says. Commit the update alone and fix its
      findings before any content. The update replaces the `lernapps-*` skills: read again those you use.
- [x] Load skill `lernapps-explainer` and the content guide.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Slice 1 (ich, Muster): Kapitel 4 `erzaehlen` (chapter.yaml, in app.yaml), Seite `past-progressive` (Kompetenz past-progressive): Lesestück Sophies Tagebuch (150 bis 300 Wörter, nummerierte Zeilen, Randglossar-Tabelle), Strahl-SVG mit Welle in der Vergangenheit, Szene nur wo sie etwas zeigt, Übungen in drei Stufen, Diktat/Nachsprechen, open-task, Hörsätze mit regen_audio.py; neues Lesestück-Muster in den Inhaltsführer
- [x] Slice 2 (Sub-Agent A, eigenes Worktree): Kapitel 4 Rest, Seiten `past-perfect`, `zeitenfolge-temporalsaetze`, `present-perfect-oder-simple-past` nach dem Muster von Slice 1 (nur diese Seitendateien, Bilder, Audio und eigene audio-texte-Datei; chapter.yaml und app.yaml führe ich zusammen)
- [x] Slice 3 (Sub-Agent B, eigenes Worktree): Kapitel 5 `dauer`, Seiten `since-for`, `present-perfect-progressive`, `dynamic-stative` (chapter.yaml des Kapitels und die Seiten; Strahl: Bogen wird Welle, Fähnchen since/for, Stoppschild für Zustandsverben)
- [x] Slice 4 (Sub-Agent C, eigenes Worktree): Kapitel 6 `plaene`, Seiten `present-fuer-zukunft` (Kalender und Fahrplan als table) und `future-progressive-perfect` (Welle und Bogen in die Zukunft)
<!-- tasks: slices (4 added): one per competency, as written in Plan -->
- [x] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
      Creator: Ja, die anderen acht Seiten dürfen nach dem Muster von past-progressive folgen, drei Sub-Agenten sind ok. Vokabelblock-Auftrag mitgeben. Kein Push, bis die Erlaubnis der Ersteller:in vorliegt.
- [x] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [ ] If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
      as it says. Commit.
- [ ] Load skill `lernapps-github`. Push the branch, open the preview pull request and see its checks to green, as it
      says.
- [ ] **Checkpoint:** publish. Show what the increment adds and the preview link. Ask whether it may go online. Stop
      and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: the pull request squash-merged into
      `main`, the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm the new content. Never use a derived address.
- [ ] The app is listed and its entry changes (school years, summary): load skill `lernapps-listing` and write the
      changed entry. Else skip this task.
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it. A push of only `.vibe/` publishes nothing.
- [ ] **Checkpoint:** list. The entry changed: open the pull request to the catalog as skill `lernapps-listing`
      says, without asking first, see it to "bestanden", then show the creator the pull request and its result. The
      entry did not change: tell the creator that the catalog updates the app by itself.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

## Retrospective

<!-- At the end of Commit. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, content guide, messages or answers, and your choice. "None" if none. -->
