"""Zeigt englische Sätze, die auf einer Seite mehr als einmal vorkommen (Text, Poster, Merke, Übungen, Meldungen).

Aufruf im Ordner der App:  python3 .agents/skills/app-content/scripts/pruefe_doppelte.py
Regel: Die Lösung einer Übung steht nicht wörtlich im Text darüber oder in einer anderen Übung derselben Seite.
Ein Satz, der zweimal vorkommt, ist ein Hinweis, kein Fehler: Hörsatz und Übung, `target` und seine `examples`
oder `accepted` zählen nicht doppelt; prüfe, ob der zweite Treffer die Lösung einer anderen Übung verrät.
"""
import collections
import glob
import re
import sys


def norm(s):
    s = re.sub(r"\(([^|()]+)\|[^()]*\)", r"\1", s)          # (a|b) -> a
    s = re.sub(r"\[([^|\]\[]+)(?:\|[^\]]*)?\]", r"\1", s)   # [a] -> a
    return re.sub(r"[^a-z' ]", " ", s.lower().replace("’", "'")).split()


def main():
    total = 0
    for f in sorted(glob.glob("src/*/*.yaml")):
        if f.endswith("chapter.yaml"):
            continue
        seen = collections.defaultdict(list)
        for no, line in enumerate(open(f, encoding="utf-8").read().split("\n"), 1):
            if re.match(r"\s*(- )?(audio|id|type|language|languages|form|mode|distractors|links|url|title|alt|caption|source|licence|image|hint|explanation|info|message|scope|description|competencies):", line):
                continue
            body = re.sub(r"^\s*(- )?[a-z]+: ", "", line)
            body = re.sub(r"^\s*- ", "", body)
            for part in re.split(r"(?<=[.?!])\s+|\s·\s|,\s(?=[A-Z])|\|", body):
                w = norm(part)
                if len(w) >= 4 and re.search(r"[a-z]", part) and not re.search(r"[äöüß]", part):
                    seen[" ".join(w)].append(no)
        dup = {k: v for k, v in seen.items() if len(v) > 1}
        if dup:
            print(f)
            for k, v in dup.items():
                print(f"   Zeilen {v}: {k}")
                total += 1
    print("Doppelte:", total)


main()
