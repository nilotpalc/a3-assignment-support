#!/usr/bin/env python3
"""Extract marks and word caps from worksheet/rubric text and check sums and cross-document agreement.
Usage: python req_check.py --ws worksheet.txt --rb rubric.txt   (text from pdftotext -layout)"""
import argparse, re, sys
EXPECT = {"A": 25, "B": 30, "C": 20, "D": 25}

def marks_from_ws_summary(t):
    i = t.find("Participant-Facing Scoring Summary")
    seg = t[i:] if i >= 0 else t
    out = {}
    for m in re.finditer(r"^\s*([A-D]\d(?:\.\d)?)\.\s+.*?\s{2,}(\d+)\s*$", seg, re.M):
        out[m.group(1)] = int(m.group(2))
    return out

def marks_from_ws_headings(t):
    out = {}
    for m in re.finditer(r"^\s*([A-D]\d)\.\s+.*?-\s*(\d+)\s*marks", t, re.M):
        out[m.group(1)] = int(m.group(2))
    for m in re.finditer(r"^\s*(D4\.[12])\s+.*?-\s*(\d+)\s*marks", t, re.M):
        out[m.group(1)] = int(m.group(2))
    return out

def marks_from_rb(t):
    out = {}
    for m in re.finditer(r"^\s*([A-D]\d(?:\.\d)?)\.?\s+.{3,80}?\s{2,}(\d+)\s{2,}", t, re.M):
        out.setdefault(m.group(1), int(m.group(2)))
    return out

def caps(t):
    res = []
    for m in re.finditer(r"Response budget:\s*(.{0,160})", t):
        res.append(re.sub(r"\s+", " ", m.group(1)).strip())
    return res

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ws", required=True); ap.add_argument("--rb", required=True)
    a = ap.parse_args()
    ws = open(a.ws, encoding="utf-8", errors="ignore").read(); rb = open(a.rb, encoding="utf-8", errors="ignore").read()
    s1 = marks_from_ws_summary(ws); s2 = marks_from_ws_headings(ws); s3 = marks_from_rb(rb)
    ok = True
    print("WS summary criteria:", len(s1), " WS headings:", len(s2), " RB criteria:", len(s3))
    for part, exp in EXPECT.items():
        tot = sum(v for k, v in s1.items() if k.startswith(part) and k not in ("D4.1", "D4.2"))
        print("Part %s total (WS summary) = %d (expected %d)" % (part, tot, exp)); ok &= tot == exp
    print("Content total =", sum(v for k, v in s1.items() if k not in ("D4.1", "D4.2")), "(expected 100)")
    for k in sorted(set(s1) | set(s2) | set(s3)):
        vals = {"summary": s1.get(k), "heading": s2.get(k), "rubric": s3.get(k)}
        present = {v for v in vals.values() if v is not None}
        flag = "" if len(present) <= 1 else "  <-- DISAGREE"
        if flag: ok = False
        print("%-5s %s%s" % (k, vals, flag))
    print("\nResponse budgets stated in worksheet (compare manually with the register):")
    for c in caps(ws): print(" -", c)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
