#!/usr/bin/env python3
"""Render ledger/ledger.md (+ prior_work_facts.tsv) as a read-only Markdown view with real tables.

Usage (from repo root):  python ledger/render_ledger.py
Output: build/ledger_view.md  (generated; never edit, never read by the agent or QA scripts)
The ledger itself is unchanged. Registers stay pipe-delimited, one row per line.
"""
import argparse, csv, re
from pathlib import Path

DEFAULT_HEADERS = {
    "decision_log": ["Date", "Gate / topic", "Decision", "Approver"],
    "change_log": ["Date", "Entry"],
}

def esc(c):
    c = c.strip().replace("|", "\\|")
    return re.sub(r"<(/?\w+)>", r"`<\1>`", c) or " "

def table(header, rows):
    n = max([len(header)] + [len(r) for r in rows])
    header = header + [f"Col{i+1}" for i in range(len(header), n)]
    out = ["| " + " | ".join(esc(h) for h in header) + " |",
           "|" + "|".join(["---"] * n) + "|"]
    for r in rows:
        r = r + [""] * (n - len(r))
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    return out

def render_block(tag, body):
    header, rows, text = None, [], []
    for l in body:
        s = l.strip()
        if not s:
            continue
        if s.startswith("#"):
            if header is None and "|" in s:
                header = [c.strip() for c in s.lstrip("# ").split("|")]
            else:
                text.append(f"*{s.lstrip('# ').strip()}*")
        elif "|" in s and tag != "ledger_rules":
            rows.append([c.strip() for c in s.split("|")])
        else:
            text.append(s if s.startswith("- ") else f"- {s}" if ":" in s and tag not in ("status",) else s)
    text = [re.sub(r"<(/?\w+)>", r"`<\1>`", x) for x in text]
    out = [f"## {tag.replace('_', ' ').title()}", ""]
    if tag == "status":
        out += [f"- {t}" if not t.startswith("- ") else t for t in text]
    else:
        out += text + ([""] if text and (rows or header) else [])
    if header is None and rows:
        header = DEFAULT_HEADERS.get(tag, [])
    if tag == "decision_log":  # a stray "|" inside a decision: keep the last field as approver
        rows = [r[:2] + [" / ".join(r[2:-1]), r[-1]] if len(r) > 4 else r for r in rows]
    if rows:
        out += table(header or [], rows)
    elif header:
        out += table(header, [])
        out += ["", "*(no entries yet)*"]
    return out + [""]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default="ledger/ledger.md")
    ap.add_argument("--facts", default="ledger/prior_work_facts.tsv")
    ap.add_argument("--out", default="build/ledger_view.md")
    a = ap.parse_args()
    t = Path(a.ledger).read_text(encoding="utf-8")
    t = re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", t, flags=re.S)
    out = ["# Ledger view (generated, read-only)", "",
           f"Source: `{a.ledger}`. Edit the ledger, never this file. Re-run `python ledger/render_ledger.py` to refresh.", ""]
    for m in re.finditer(r"<(\w+)>\r?\n(.*?)\r?\n</\1>", t, re.S):
        tag, body = m.group(1), m.group(2).splitlines()
        if tag == "prior_work_facts" and Path(a.facts).exists():
            with open(a.facts, encoding="utf-8", newline="") as f:
                rows = list(csv.reader(f, delimiter="\t"))
            out += ["## Prior Work Facts", ""]
            if len(rows) > 1:
                out += table(rows[0], rows[1:]) + [""]
            else:
                out += table(rows[0] if rows else ["(empty)"], []) + ["", "*(no entries yet)*", ""]
            continue
        out += render_block(tag, body)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote", a.out)

main()
