"""Prüft, ob ein Hörsatz (Diktat, Nachsprechen) einem Satz derselben Seite (fast) wörtlich gleicht.

Aufruf im Ordner der App:  python3 .agents/skills/app-content/scripts/pruefe_hoersaetze.py [--strict]

Regel: Ein Hörsatz unterscheidet sich von jedem Satz derselben Seite (Einstieg, Poster, Merke, Bildtexte, Übungen:
target, cue, source, Optionen, Meldungen) in mehr als Name, Adverb, Zeitangabe oder einem Wort. Der Abgleich entfernt
Namen, Häufigkeits- und Zeitwörter und vergleicht die übrigen Wörter. Gemeldet wird: gleiche Wortfolge, höchstens ein
Wort verschieden, Wortfolge eines Satzes steckt in dem anderen (ab drei Wörtern), oder Ähnlichkeit ab 0,8.
"""
import difflib
import glob
import json
import re
import sys

NAMES = {"sophie", "ellie", "peter", "amir", "mr", "mrs", "hill", "parker", "parkers", "millbrook"}
ADV = {"always", "usually", "often", "sometimes", "never", "now", "today", "tomorrow", "yesterday", "ago", "soon",
       "already", "just", "ever", "yet", "every", "day", "saturday", "saturdays", "week", "last", "next", "two", "days",
       "moment", "at", "the", "probably", "maybe", "also", "again", "here", "so", "on", "july", "may", "october", "in"}
STRICT = "--strict" in sys.argv


def tokens(s):
    s = re.sub(r"[\[\]()·|]", " ", s.lower().replace("’", "'"))
    t = re.findall(r"[a-z]+(?:'[a-z]+)?", s)
    return [w for w in t if w not in NAMES and w not in ADV]


def sentences(text):
    out = []
    for part in re.split(r"[.!?;:„“\"|\n]+", text):
        part = re.sub(r"[\[\]()·|]", " ", part).strip()
        if len(part.split()) >= 4:
            out.append(part)
            for clause in re.split(r",| and | but | so ", part):
                if len(clause.split()) >= 4:
                    out.append(clause.strip())
    return out


def page_texts():
    pages = {}
    for f in sorted(glob.glob("src/*/*.yaml")):
        if f.endswith("chapter.yaml"):
            continue
        raw = open(f, encoding="utf-8").read()
        audio_files = set(re.findall(r"audio: (\S+\.mp3)", raw))
        body = "\n".join(l for l in raw.split("\n") if not re.match(r"\s*(- )?audio:", l))
        # Hörsätze selbst (target/text unter audio:) herausnehmen
        for m in re.finditer(r"audio: \S+\.mp3\n\s+(?:target|text): (.*)", raw):
            body = body.replace(m.group(1), "", 1)
        for img in set(re.findall(r"images/([\w-]+\.svg)", raw)):
            svg = open("src/images/" + img, encoding="utf-8").read()
            body += "\n" + "\n".join(re.findall(r">([^<>]+)</text>", svg)) + "\n" + "\n".join(re.findall(r"<title>([^<]+)</title>", svg))
        pages[f] = (audio_files, body)
    return pages


def main():
    texts = json.load(open(".agents/skills/app-content/scripts/audio-texte.json", encoding="utf-8"))
    by_name = {k.split("/")[-1]: v for k, v in texts.items()}
    hits = 0
    for f, (files, body) in page_texts().items():
        sents = sentences(body)
        for name in sorted(files):
            a = by_name.get(name)
            if a is None:
                print("FEHLT in audio-texte.json:", name)
                continue
            ta = tokens(a)
            for s in sents:
                ts = tokens(s)
                if not ta or not ts:
                    continue
                ratio = difflib.SequenceMatcher(None, ta, ts).ratio()
                same_len_diff = len(ta) == len(ts) and sum(x != y for x, y in zip(ta, ts)) <= 1 and len(ta) >= 3
                contained = (len(ta) >= 3 and " ".join(ta) in " ".join(ts)) or (len(ts) >= 3 and " ".join(ts) in " ".join(ta))
                if ta == ts or same_len_diff or contained or ratio >= (0.7 if STRICT else 0.8):
                    print(f"{f}\n   Hörsatz: {a}\n   ähnlich: {s}   (Ähnlichkeit {ratio:.2f})")
                    hits += 1
                    break
    # keine zwei gleichen Hörsätze in der App
    seen = {}
    for k, v in texts.items():
        seen.setdefault(v.lower(), []).append(k)
    for v, ks in seen.items():
        if len(ks) > 1:
            print("DOPPELT:", v, ks)
            hits += 1
    print("Treffer:", hits)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
