#!/usr/bin/env python3
"""Mechanical consistency checks for Assignment 3 drafts. Python 3, standard library only.
Usage: python qa_checks.py --ledger ledger/ledger.md --drafts drafts [--sources a1.txt a2.txt] [--expect A1,A2,...]
Exit code 1 if any BLOCKING issue. Reports only; never edits files."""
import re, sys, glob, os, argparse

TAG = re.compile(r"\[(?:D|C|E|A|F|R|L)(?::[^\]]*)?\]|\[J\]")
HDR = re.compile(r"<!--\s*section=(\S+)\s+cap=(\d+)\s*-->")

def block(txt, name):
    m = re.search(r"<%s>(.*?)</%s>" % (name, name), txt, re.S)
    rows = []
    if m:
        for l in m.group(1).splitlines():
            l = l.strip()
            if l and not l.startswith("#") and "|" in l:
                rows.append([c.strip() for c in l.split("|")])
    return rows

def words(t):
    return re.findall(r"[A-Za-z0-9]+(?:[-'’./%][A-Za-z0-9]+)*", t)

def norm_tokens(t):
    return re.findall(r"[a-z0-9]+", t.lower())

def ngrams(toks, n):
    return {" ".join(toks[i:i+n]) for i in range(len(toks) - n + 1)}

def load_drafts(folder):
    out = {}
    for f in sorted(glob.glob(os.path.join(folder, "*.md"))):
        raw = open(f, encoding="utf-8").read()
        m = HDR.search(raw)
        if not m:
            out[os.path.basename(f)] = dict(id=None, cap=None, raw=raw, body=raw, file=f)
            continue
        body = HDR.sub("", raw)
        out[m.group(1)] = dict(id=m.group(1), cap=int(m.group(2)), raw=raw, body=body, file=f)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--drafts", required=True)
    ap.add_argument("--sources", nargs="*", default=[])
    ap.add_argument("--expect", default="")
    ap.add_argument("--strip", default="", help="write tag-stripped copies to this folder")
    a = ap.parse_args()
    led = open(a.ledger, encoding="utf-8").read()
    issues = []
    def add(sev, sec, chk, det): issues.append((sev, sec, chk, det))

    maturity = {r[0]: r for r in block(led, "maturity")}
    portfolio = block(led, "portfolio")
    figures = {r[0]: r for r in block(led, "figures")}
    assumptions = {r[0] for r in block(led, "assumptions")}
    evidence = {r[0] for r in block(led, "evidence")}
    glossary = block(led, "glossary")
    vocab = {}
    m = re.search(r"<allowed_vocabulary>(.*?)</allowed_vocabulary>", led, re.S)
    if m:
        for l in m.group(1).splitlines():
            if ":" in l: k, v = l.split(":", 1); vocab[k.strip()] = [x.strip() for x in v.split(";")]

    drafts = load_drafts(a.drafts)

    # 1 missing sections
    if a.expect:
        for s in [x.strip() for x in a.expect.split(",") if x.strip()]:
            if s not in drafts:
                add("BLOCKING", s, "missing_section", "no draft file with this section id")

    clean = {}
    for k, d in drafts.items():
        if d["id"] is None:
            add("BLOCKING", k, "header", "missing <!-- section=ID cap=N --> header"); continue
        body = re.sub(r"<appendix>.*?</appendix>", "", d["body"], flags=re.S)
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        clean[k] = body
        # 2 cap
        n = len(words(TAG.sub("", body)))
        if n > d["cap"]:
            add("BLOCKING", k, "word_cap", "%d words > cap %d" % (n, d["cap"]))
        # 3 placeholders
        for pat in [r"\[(?:X|N|TBD)[^\]]*\]%?", r"\bTBD\b", r"\bXX+\b", r"\{\{", r"<fill", r"lorem ipsum", r"\[\d+\s*[–-]\s*\d+\]"]:
            for mm in re.finditer(pat, body, re.I):
                add("BLOCKING", k, "placeholder", mm.group(0)[:40])
        # 4 untagged numeric claims
        text = body
        for sent in re.split(r"(?<=[.!?])\s+|\n+", text):
            s = sent.strip()
            if not s or s.startswith(("|---", "#", "<")): continue
            if TAG.search(s): continue
            for mm in re.finditer(r"(?<![A-Za-z0-9.])(\d[\d,.]*)\s*(%|k\b|K\b|m\b|hours|days|months|weeks|years|USD|analyst-days)?|\$\s?\d", s):
                tok = mm.group(0)
                has_unit = ("%" in tok) or ("$" in tok) or bool(mm.group(2) if mm.lastindex and mm.lastindex >= 2 else False)
                try: val = float(mm.group(1).replace(",", "")) if mm.lastindex else 0
                except Exception: val = 0
                if has_unit or val > 20:
                    add("BLOCKING", k, "untagged_claim", s[:90]); break
        # 5 undefined IDs
        for mm in re.finditer(r"\[(E|A|F):([^\]]+)\]", d["body"]):
            kind, ref = mm.group(1), mm.group(2).strip()
            pool = evidence if kind == "E" else assumptions if kind == "A" else set(figures)
            if ref not in pool:
                add("BLOCKING", k, "undefined_id", "%s:%s not in ledger" % (kind, ref))
        # 6 terminology
        for r in glossary:
            if len(r) >= 2:
                for bad in [x.strip() for x in r[1].split(";") if x.strip()]:
                    if re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(bad), body):
                        add("WARNING", k, "terminology", "'%s' -> use '%s'" % (bad, r[0]))
        # 9 ratings / classifications vs ledger
        for mm in re.finditer(r"\[R:([A-Za-z]+)=([A-Za-z]+)\]", d["body"]):
            dim, rt = mm.groups()
            led_rt = maturity.get(dim, [None, None])[1]
            if led_rt is None: add("BLOCKING", k, "rating_not_in_ledger", "%s=%s" % (dim, rt))
            elif led_rt != rt: add("BLOCKING", k, "rating_mismatch", "%s: text %s vs ledger %s" % (dim, rt, led_rt))
        pf = {r[0]: r for r in portfolio}
        for mm in re.finditer(r"\[L:([A-Za-z0-9]+)=([A-Za-z ]+)\]", d["body"]):
            oid, cl = mm.group(1), mm.group(2).strip()
            led_cl = pf.get(oid, [None] * 4)[3]
            if led_cl is None: add("BLOCKING", k, "opportunity_not_in_ledger", oid)
            elif led_cl != cl: add("BLOCKING", k, "classification_mismatch", "%s: text %s vs ledger %s" % (oid, cl, led_cl))
        # figure value mismatch: [F:ID] must be adjacent to the ledger value
        for mm in re.finditer(r"([^\[\]\n]{0,40})\[F:([^\]]+)\]", d["body"]):
            fid = mm.group(2).strip()
            if fid in figures:
                val = figures[fid][1]
                if val and val not in mm.group(1) and val not in d["body"][max(0, mm.start()-60):mm.end()+60]:
                    add("BLOCKING", k, "figure_mismatch", "%s expected '%s' near tag" % (fid, val))

    # 7 repetition across sections
    keys = [k for k in clean]
    gr = {k: ngrams(norm_tokens(TAG.sub("", clean[k])), 8) for k in keys}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            sh = gr[keys[i]] & gr[keys[j]]
            if len(sh) >= 2:
                add("WARNING", "%s/%s" % (keys[i], keys[j]), "repetition", "%d shared 8-word phrases, e.g. '%s'" % (len(sh), sorted(sh)[0]))

    # 8 verbatim overlap with sources
    if a.sources:
        src = set()
        for f in a.sources:
            src |= ngrams(norm_tokens(open(f, encoding="utf-8", errors="ignore").read()), 10)
        for k in keys:
            sh = gr10 = ngrams(norm_tokens(TAG.sub("", clean[k])), 10) & src
            if sh:
                add("BLOCKING", k, "verbatim_reuse", "%d shared 10-word phrases, e.g. '%s'" % (len(sh), sorted(sh)[0]))

    # 10-12 portfolio rules
    if portfolio:
        n = len(portfolio)
        if not (5 <= n <= 7): add("BLOCKING", "ledger", "portfolio_size", "%d opportunities (need 5-7)" % n)
        for r in portfolio:
            r = r + [""] * (8 - len(r))
            oid, cl, dimr = r[0], r[3], r[6]
            if vocab.get("classification") and cl and cl not in vocab["classification"]:
                add("BLOCKING", "ledger", "vocabulary", "%s classification '%s'" % (oid, cl))
            if cl == "Quick Win" and dimr == "Low":
                add("BLOCKING", "ledger", "quick_win_low_dependency", "%s is Quick Win but dependency rated Low" % oid)
            elif cl == "Quick Win" and dimr == "Medium":
                add("WARNING", "ledger", "quick_win_medium_dependency", "%s Quick Win with Medium dependency: needs explicit rationale" % oid)

    if a.strip:
        os.makedirs(a.strip, exist_ok=True)
        for k, d in drafts.items():
            if d["id"]:
                body = TAG.sub("", d["body"]); body = re.sub(r"[ \t]+\n", "\n", body)
                open(os.path.join(a.strip, os.path.basename(d["file"])), "w", encoding="utf-8").write(body)

    blocking = [i for i in issues if i[0] == "BLOCKING"]
    for sev, sec, chk, det in issues:
        print("%-8s %-10s %-26s %s" % (sev, sec, chk, det))
    print("\n%d blocking, %d warnings, %d drafts checked" % (len(blocking), len(issues) - len(blocking), len(drafts)))
    sys.exit(1 if blocking else 0)

if __name__ == "__main__":
    main()
