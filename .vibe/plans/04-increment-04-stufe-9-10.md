---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 1
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 3 }
---

# Increment: increment-04-stufe-9-10

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-24. Explore, Plan, Code, Commit.*

## Goal

Jugendliche der Klassen 9-10 ordnen alle Zeitformen auf dem Zeitstrahl ein, drücken mit dem past perfect progressive aus, wie lange etwas vor einem Zeitpunkt der Vergangenheit schon dauerte, sprechen mit used to und would über frühere Gewohnheiten und wählen in einem Sachtext für jede Handlung die passende Zeit und begründen sie. Die Lesestücke sind reale Fälle mit Daten und Quellen (keine erfundenen Kinder).

## Key decisions

<!-- One line each: decision and reason. Your own choice without the creator: mark "(guess)". -->

## Notes

<!-- New competencies by chapter (ids of the strand), didactic approach, scope, sources and licences, open questions. -->

**Karte** (`https://lernapps.net/apps/map/englisch.json`, Strang `grammatik`, gelesen 2026-11-24): drei Bausteine im Band 9-10, alle Lücken, alle Voraussetzungen in der App geübt (keine Wiederholungsseite, kein `ahead`): `past-perfect-progressive` (Schritt 1; requires past-perfect, present-perfect-progressive), `used-to` (1; simple-past), `zeiten-ueberblick` (1; zeitenfolge-temporalsaetze, present-perfect-progressive, present-fuer-zukunft). Kapitel 7 `ueberblick` „Alle Zeiten im Überblick“, drei Seiten in der Reihenfolge des Issues: `past-perfect-progressive`, `used-to`, `zeiten-ueberblick`.

**Form (Stufe 9-10, Abschnitt 8):** Je Seite ein Lesestück von 300 bis 600 Wörtern, ein realer Fall mit Daten und Quellen (kein erfundenes Kind, keine Sophie-Szene, sachlicher Ton, Anrede „du“), Vokabelblock davor, Aufgaben in drei Stufen (Verstehen, Belegen mit Zeile, Meinung/Entscheidung), Schreibauftrag; Hörsätze nur wenige kurze (nicht das Lesestück). Keine Figuren-Einführung im Seitentext.

**Lesestücke (eigene Texte nach geöffneten Quellen; keine Sätze aus Quellen):**
- `past-perfect-progressive`: Sachtext zum Bau des Eiffelturms: Baubeginn 28. Januar 1887, Fertigstellung 31. März 1889, Eröffnung der Ausstellung 6. Mai, für Besucher geöffnet 15. Mai 1889. Past perfect progressive: „The workers had been building for more than two years when the tower opened.“ Entscheidung: welche Zeit für die Dauer vor dem Ereignis. Quelle: <https://en.wikipedia.org/wiki/Eiffel_Tower> (geöffnet 2026-11-24, Antwort 200; Infobox: Construction started 28 January 1887, Completed 31 March 1889, Opening 15 May 1889; Ausstellung 6 Mai).
- `used-to`: Sachtext zur Concorde: früher, heute nicht mehr: Studien ab 1954, Vertrag 1962, Erstflug 2. März 1969, Linienflüge ab 21. Januar 1976, schnellster Linienflug New York–London in 2 Stunden 52 Minuten 59 Sekunden am 7. Februar 1996, letzter Linienflug 24. Oktober 2003, 20 gebaut, 18 stehen in Museen. Used to und would für frühere Gewohnheiten (Punktreihe in der Vergangenheit, heute vorbei). Quelle: <https://en.wikipedia.org/wiki/Concorde> (geöffnet, Antwort 200).
- `zeiten-ueberblick`: Sachtext (eigene Fassung) über Eiffelturm und Concorde zusammen oder über einen dritten geprüften Fall: alle Zeiten, Kinder markieren und begründen; die Übersicht aller Zeichen wird zum Werkzeug (Tabelle „Klassenzimmer-Poster · Alle Zeitformen“). Quellen wie oben. (guess: keine VOA-/Wikinews-Texte, weil sie für die Zeitenübung nicht gezielt genug sind und Rechtepflichten bringen; die erlaubten Quellen bleiben offen; ob `en.wikinews.org` und `learningenglish.voanews.com` über den Proxy erreichbar sind, ist ungeprüft.)
- Grammatikfakten: <https://en.wikipedia.org/wiki/Uses_of_English_verb_forms>, <https://en.wikipedia.org/wiki/Used_to>, <https://en.wikipedia.org/wiki/Habitual_aspect> (geöffnet, 200), schon im Inhaltsführer teils vermerkt.

**Zeichen:** past perfect progressive: Welle, die in der Vergangenheit bis zu einem Punkt reicht (Bogen unter der Welle), Fähnchen for/since/when; used to: Punktreihe in der Vergangenheit, grau und gestrichelt, wo sie endet (heute nicht mehr); Überblick: der ganze Strahl mit allen Zeichen als Werkzeug (Übersicht der 13 Zeichen). Farben wie bisher.

**Didaktik je Seite:** past-perfect-progressive: Dauer vor einem Zeitpunkt der Vergangenheit; Fehler: simple past statt ppp, had been vergessen, since mit Dauer, Zustandsverb mit -ing. used-to: used to (nicht would bei Zuständen), would nur bei wiederholten Handlungen; Fehler: „use to“ in Verneinung/Frage (didn't use to) liegt bei do/did (#473), nur Hinweis; „would“ für Zustände; „used to“ für Einmaliges. zeiten-ueberblick: für jede Handlung des Textes die Zeit wählen und begründen; Fehler: present perfect mit Zeitpunkt, simple past ohne Bezug, past perfect ohne Reihenfolge.

**Umfang:** drin: die drei Bausteine; Zeitformen in Bejahung und, wo nötig, Verneinung mit Hilfsverb. Nicht drin: Fragen/Verneinung mit do/did (#473), Passiv (#480), Bedingungssätze und indirekte Rede (#481), Aussprache (#482).

**Neu gegenüber Stufe 7-8:** (1) Lesestück 300 bis 600 Wörter, realer Fall mit Daten und Quelle (Sachtext statt Figurenszene), (2) die Überblicksseite: Werkzeug „Alle Zeitformen“ (`table` mit 13 Zeichen: Zeichen · Form · Signalwort · Beispiel) und Markieren im Text über `matching` (Satz des Sachtexts ↔ Zeichen), `single-choice` mit Begründung („Warum diese Zeit?“) und `language-task` write; kein Komponenten-Bedarf (Blöcke der Laufzeit reichen, `prefer-built-in-block`). Der Hinweis `explainer-text-load` ist bei Lesestück-Seiten bewusst.

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
      Creator: Ja, passt so (Eiffelturm und Concorde sind gute reale Fälle; Fakten und Daten gegen die Quellen prüfen, keine Sätze übernehmen). Weiter mit Musterseite past-perfect-progressive, Lerner-Check, dann melden.

### Answers

<!-- The creator's answers, in their words, one bullet each. -->

- Auftrag der Ersteller:in (über die Orchestrator-Session): „Starte das Stufe-9-10-Inkrement `increment/04-stufe-9-10` auf eigenem Branch von aktuellem `main`: Kapitel 7 „Alle Zeiten im Überblick“ (9-10). Ablauf wie bei den 7-8-Inkrementen (Plan-Checkpoint, Musterseite, Gesamtcheck und Sprachprüfung mit Sub-Agenten, Vorschau-PR, nicht mergen). Beachte `konventionen.md` (keine Figuren-Einführung im Seitentext, Vokabelblock, Hörurteile bestätigt der Orchestrator). Tooling vorher auf den neuesten Stand (`update`).“
- Konzept und Regeln: Abschnitte 7 und 8 der `konventionen.md` (Stufe 9-10: Lesestück 300 bis 600 Wörter, realer oder realistischer Fall mit Daten, Quellen und einer Entscheidung, keine erfundenen Kinder, sachlich; Quellen mit geöffneter Lizenzseite; Hörtexte nur kurze Sätze; alle Regeln aus Abschnitt 7).
- Bausteine: `issues/472.md`, Kapitel 7 (past-perfect-progressive, used-to, zeiten-ueberblick). Zeichen und Begriffe wie bisher (Strahl, Punkt, Punktreihe, Welle, Bogen, Pfeil, Fähnchen, Bau-Karte).
- Workflow: `lernapps update` (tooling 0.19.0, app-templates 0.20.0 erledigt), Branch `increment/04-stufe-9-10`, Checkpoints an die Orchestrator-Session, Vorschau-Pull-Request, nichts nach `main`, kein Katalogeintrag.

## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [x] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [x] (skipped: keine neue Komponente und keine interaktive Übung) Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [x] Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, bestätigt, so bauen. Weiter mit der Musterseite.

### Content method

<!-- One line each: the guide's patterns, figures and components used, and where; anything new, what it does and
cannot. Something new goes into the guide in the slice that adds it. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

Muster der Stufe 7-8 (Inhaltsführer, Abschnitt „Stufe 7-8: Seite mit Lesestück“) gilt weiter, mit den Unterschieden der Stufe 9-10: Abschnitte `einstieg` (Vorwissens-Frage vom Zeitstrahl aus), `lesestueck` (Titel nennt die Sorte, z. B. „Sachtext: Der Eiffelturm“; Vokabelblock davor, höchstens eine Wörterliste; Text 300 bis 600 Wörter in 3 bis 5 `text`-Blöcken mit nummerierten Zeilen `**[1]**`; reale Daten, eigene Sätze, Quelle im Inhaltsführer unter „Sources“ und als `links` nur, wo sie genau zur Frage passt), `neu` (Zeichen, Bau-Karte, Merke; kein Satz des Lesestücks wörtlich), `uebung` (Verstehen, Belegen mit Zeile als `multiple-choice`/`single-choice`, Bilden und Korrektur mit `language-task`, Entscheidung mit Begründung: `single-choice` mit `info` je Option; höchstens etwa 25 Items; mindestens vier Übungen mit eigener Rückmeldung), `anwenden` (`speaking-task` mit 3 kurzen Sätzen, `open-task` als Schreibauftrag mit `scope`), `weiter`. Kein Vorstellen von Figuren, keine Altersangaben, keine Sophie-Szene (9-10: reale Fälle). Keine Links zur Lernlandkarte (Vorlage verbietet sie). Zeichnungen `zeitstrahl-<seite>.svg` mit den Farben des Inhaltsführers; neu: Welle bis zu einem Punkt der Vergangenheit (past perfect progressive), graue Punktreihe, die heute endet (used to), ganzer Strahl mit allen 13 Zeichen als Werkzeug (zeiten-ueberblick). Hörsätze: natürliche, ganze Sätze, nicht das Lesestück, 3 plus 3 je Seite, Fuzzy-Prüfung 0 Treffer, `regen_audio.py` mit Fehllaut-Schnitt, Hörliste im Inhaltsführer; die Hörurteile bestätigt der Orchestrator. `scope` je Seite (open-task). Selbsteinschätzung: 2 allein verständliche Übungen je Seite.

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
- [x] Slice 1 (ich, Muster): Kapitel 7 ueberblick (chapter.yaml, in app.yaml), Seite past-perfect-progressive: Lesestück Eiffelturm 300 bis 600 Wörter nach den geprüften Daten, Vokabelblock, Zeichen, Übungen in drei Stufen, Hörsätze, open-task; Lesestück-9-10-Muster im Inhaltsführer
- [x] Slice 2 (Sub-Agent A, eigenes Worktree): Seite used-to (Lesestück Concorde, graue Punktreihe in der Vergangenheit)
- [x] Slice 3 (Sub-Agent B, eigenes Worktree): Seite zeiten-ueberblick (Sachtext, Tabelle aller Zeichen, Markieren und Begründen)
<!-- tasks: slices (3 added): one per competency, as written in Plan -->
- [x] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
      Creator: Ja, used-to (Concorde) und zeiten-ueberblick dürfen nach diesem Muster in zwei Sub-Agenten gebaut werden. Die Hörurteile für die 6 neuen Sätze bestätige ich in Namen der Ersteller:in.
- [ ] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
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
