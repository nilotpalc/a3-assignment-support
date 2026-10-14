#!/usr/bin/env python3
"""Verify that each fact in prior_work_facts.tsv appears exactly in its source text.
Usage: python fact_check.py --facts ledger/prior_work_facts.tsv --a1 a1.txt --a2 a2.txt
Source text: produce with pdftotext. Normalises case, ligatures, quotes, whitespace and hyphens (digits and symbols must match exactly)."""
import argparse, csv, re, sys

def norm(t):
    t = t.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("–", "-").replace("—", "-").replace("‑", "-")
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    # remove all whitespace and hyphens so line-wrapped words and hyphenated compounds match; digits stay exact
    return re.sub(r"[\s\-]+", "", t).lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--facts", required=True); ap.add_argument("--a1", required=True); ap.add_argument("--a2", required=True)
    a = ap.parse_args()
    src = {"A1": norm(open(a.a1, encoding="utf-8", errors="ignore").read()),
           "A2": norm(open(a.a2, encoding="utf-8", errors="ignore").read())}
    miss = 0; n = 0; ph = 0
    with open(a.facts, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if not row.get("id"): continue
            n += 1
            if row["status"].strip() == "placeholder": ph += 1
            ok = norm(row["exact_text"]) in src.get(row["doc"].strip(), "")
            if not ok:
                miss += 1; print("MISS", row["id"], row["doc"], row["section"], "|", row["exact_text"][:80])
    print("%d facts checked, %d misses, %d placeholders flagged" % (n, miss, ph))
    sys.exit(1 if miss else 0)

if __name__ == "__main__":
    main()
