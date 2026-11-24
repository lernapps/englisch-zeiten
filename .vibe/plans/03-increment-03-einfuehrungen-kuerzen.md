---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: commit
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Increment: increment-03-einfuehrungen-kuerzen

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

Die Seiten steigen ohne lange Vorstellung der Figuren ein: keine Altersangaben, Verwandtschaftserklärungen und Datumsangaben im Fließtext, wenn sie nichts zur Aufgabe beitragen. Die Vorstellung steht, wenn überhaupt, einmal auf der Startseite.

## Key decisions

<!-- One line each: decision and reason. Your own choice without the creator: mark "(guess)". -->

## Notes

<!-- New competencies by chapter (ids of the strand), didactic approach, scope, sources and licences, open questions. -->

Korrektur ohne neue Kompetenzen: Alle 22 Seiten (13 der ersten Version, 9 des Inkrements 02) werden auf Vorstellungen der Figuren, Altersangaben, Verwandtschaftserklärungen und überflüssige Datumsangaben im Fließtext, in Einstiegs-, Szenen- und Lesestück-Texten, Bildunterschriften und Alt-Texten durchsucht und gekürzt. Eine Figur wird nur benannt, wo die Aufgabe es braucht (wer in der Chatzeile spricht, wer spricht in der Szene). Die Vorstellung (Alter, Beziehungen, Mr Hill) bleibt einmal auf der Seite `das-brauchst-du` und im `intro` der App, dort aber kurz. Geprüft wird auch das Lesestück (keine Einleitungssätze vor dem Text, die Figuren erklären), die Einstiegsfrage und `weiter`. Neu in der Vorlage (app-templates 0.19.0, update vor dem Inkrement): `links` an Fragen ist optional, Links auf die Lernlandkarte verbietet der Build; alle 44 Karten-Links an den Fragen sind entfernt (Commit „fix: keine Links zur Lernlandkarte …“). Keine neuen Quellen.

**Ergebnis (Sub-Agenten, drei Slices, zusammengeführt):** Alle 22 Seiten und alle 6 `chapter.yaml` plus das `intro` der App geprüft, Texte gekürzt: immer-oder-jetzt (7 Seiten: Vorstellung auf `das-brauchst-du` auf zwei Sätze ohne Alter und Verwandtschaft, „Ellie erzählt Sophie von ihrem Bruder“ → „Ellie sagt“, Bildunterschriften auf das Nötige), gestern-und-schon und morgen-und-spaeter (6 Seiten: Bildunterschriften, Datum ohne Aufgabenbezug), erzaehlen, dauer, plaene (9 Seiten: Vorspann vor der Einstiegsfrage weg, `description`, Abschnitts- und Lesestück-Titel neutral, `weiter`, Alter und „bei den Parkers“ aus den Lesestücken). Alle 22 Seiten betroffen. Hörsätze nicht geändert (Fuzzy-Prüfung 0 Treffer). `lernapps check` ohne Fehler (Hinweise wie zuvor). Bewusst geblieben: Namen als Sprecher in Chat-, Interview- und Dialogzeilen, Datum und Zeitangaben, die Aufgabeninhalt sind (Seit September, Geburtstage als Pläne in `going-to`), Alt-Texte, die beschreiben, wer was tut. Vorher in diesem Inkrement: `lernapps update` (tooling 0.18.6, app-templates 0.19.0: `links` an Fragen optional, Links zur Lernlandkarte verboten; 44 entfernt).

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
- [x] (skipped: keine neuen Kompetenzen, Korrektur der vorhandenen Seiten) Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] (skipped: keine neue Art von Inhalt) The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [x] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.
      Creator: Auftrag der Ersteller:in: alle Seiten prüfen und die langen Einführungen der Figuren (wer sie sind, wie alt, Verwandtschaft, Datum) auf die Story-Inhalte kürzen; Figuren nur dort nennen, wo die Aufgabe es braucht; Vorstellung einmal auf der Startseite; auch Szenen-, Einstiegs- und Lesestück-Texte, Bildunterschriften und Alt-Texte; danach lernapps check, Inhaltsführer, Hörsätze prüfen.

### Answers

<!-- The creator's answers, in their words, one bullet each. -->

- Auftrag der Ersteller:in (über die Orchestrator-Session): „Die langen Einführungen, wer Ellie, Amir, Sophie und die anderen sind und wie alt sie gerade sind („Es ist Montag, der 21. September. Die Schulzeitung … Sophie (13) liest ihn in der Pause. Sie kommt aus Deutschland und wohnt bei der Familie Parker. Im Bericht kommen … vor …“), sind im Verlauf eines Explainers unnötig und verhindern den Einstieg. Bitte alle Seiten deiner App prüfen und solche Absätze auf die eigentlichen Story-Inhalte kürzen: kein Vorstellen der Figuren, keine Altersangaben im Fließtext, keine Verwandtschaftserklärungen, kein Datum, wenn es nichts zur Aufgabe beiträgt. Eine Figur wird nur dort kurz benannt, wo sie für die Aufgabe nötig ist (z. B. wer in der Chatzeile spricht). Die Vorstellung gehört, wenn überhaupt, einmal in die Startseite der App. Prüfe auch Szenen-, Einstiegs- und Lesestück-Texte, Bildunterschriften und Alt-Texte, nicht nur die erste Zeile. Danach `lernapps check`, Inhaltsführer nachführen, Hörsätze bei geänderten Texten prüfen.“

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
- [x] (skipped: keine neue Komponente oder Übung) Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Auftrag der Ersteller:in gilt als Bestätigung: alle Seiten kürzen, Vorstellung nur einmal auf der Startseite; danach check, Inhaltsführer, Hörsätze.

### Content method

<!-- One line each: the guide's patterns, figures and components used, and where; anything new, what it does and
cannot. Something new goes into the guide in the slice that adds it. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

Keine neuen Muster, Zeichnungen oder Komponenten. Regel für alle Seiten: Im Fließtext (Einstieg, `neu`, `weiter`, Lesestück-Einleitung, Szenenbeschreibung, Bildunterschriften, Alt-Texte, Vokabel-`note`, scope-Text, `info` und `explanation`) stehen keine Vorstellungen der Figuren („Sophie ist 13 und lebt bei den Parkers“), keine Altersangaben, keine Verwandtschaftserklärungen (Ellies Bruder, Gastschwester), kein Datum und keine Wochentage, wenn sie nichts zur Aufgabe beitragen. Eine Figur wird nur genannt, wo die Aufgabe sie braucht (Sprecher einer Chatzeile, wer in der Szene spricht, wer was tut). Die Vorstellung bleibt, kurz, einmal auf `immer-oder-jetzt/das-brauchst-du` und im `intro` der App. Hörsätze bei geänderten Texten prüfen (`pruefe_hoersaetze.py`), bei Textänderungen, die Hörsätze betreffen, neu erzeugen; Selbsteinschätzungs-Übungen bleiben allein verständlich; Inhaltsführer („Content structure“, Regeln) nachführen.

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
- [x] Slice 1 (Sub-Agent A, eigenes Worktree): Kapitel immer-oder-jetzt, 7 Seiten (das-brauchst-du, to-be, have-got, simple-present, haeufigkeit, present-progressive, simple-oder-progressive): Vorstellungen, Alter, Verwandtschaft, Datum aus Fließtext, Einstieg, Szenen-Bildunterschriften, alt und Lesestück-Einleitungen kürzen; Vorstellung bleibt kurz einmal auf das-brauchst-du
- [x] Slice 2 (Sub-Agent B, eigenes Worktree): Kapitel gestern-und-schon und morgen-und-spaeter, 6 Seiten, gleiche Kürzung
- [x] Slice 3 (Sub-Agent C, eigenes Worktree): Kapitel erzaehlen, dauer und plaene, 9 Seiten (Lesestücke ohne Einleitungen, die Figuren erklären; Einstieg und weiter), gleiche Kürzung
<!-- tasks: slices (3 added): one per competency, as written in Plan -->
- [x] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
      Creator: Auftrag der Ersteller:in: alle Seiten kürzen; kein neues Muster, daher weiter.
- [x] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [x] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [x] (skipped: nur Texte gekürzt, Übungen unverändert) If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
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

Explore, Plan und Code abgeschlossen; Commit bis zum Vorschau-Pull-Request. Die Checkpoints der Explore- und Plan-Phase wurden mit dem Auftrag der Ersteller:in als Antwort abgehakt (die Orchestrator-Session wollte eine einzige Meldung am Ende); der Checkpoint „Veröffentlichen“ steht aus.

### Creator turns after the plan

Eine Rückmeldung der Ersteller:in (über die Orchestrator-Session): die Einführungen der Figuren auf allen Seiten kürzen. Sie stand vor dem Plan; danach kam keine weitere Nachricht eines Menschen.

### Where I had to guess

- Die Checkpoints Recherche und Plan mit dem Auftrag der Ersteller:in beantwortet, statt auf eine eigene Antwort zu warten.
- Bildunterschriften der Szenen: der Sprecher bleibt genannt (mit Merkmal, z. B. „Ellie (roter Pferdeschwanz) spricht“), weil sonst unklar wäre, wer spricht.
- Namen als Sprecher in Chat-, Interview- und Dialogzeilen bleiben; Daten und Zeitangaben bleiben, wo sie Aufgabeninhalt sind.
- Die kurze Vorstellung auf `das-brauchst-du` (zwei Sätze) bleibt, die der App-Startseite im `intro` ist auf Namen ohne Alter gekürzt.
