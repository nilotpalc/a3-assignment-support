"""G8 assembly: approved drafts -> build/A3_assembled.md (full) and build/A3_main_body.md (Parts A-D only).
Presentation only: no wording changes. Public evidence tags become "(En)", course-note tags become
"(course notes, Module n)", internal tags are removed, section titles follow the worksheet verbatim."""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "drafts")
B = os.path.join(ROOT, "build")

PARTS = [
    ("Part A: Organisational AI Maturity Assessment - 25 marks", [
        ("A1. Define the assessment scope and evidence base - 3 marks", ["A1"]),
        ("A2. Six-Dimension AI Maturity Assessment - 14 marks", ["A2_table", "A2"]),
        ("A3. Industry / peer benchmark - 4 marks", ["A3"]),
        ("A4. Weakest-dimension diagnosis and readiness priorities - 4 marks", ["A4"]),
    ]),
    ("Part B: AI Opportunity Portfolio and Sequencing - 30 marks", [
        ("B1. Build a 5-7 opportunity portfolio - 10 marks", ["B1"]),
        ("B2. Classify Quick Wins, Strategic Bets and Moonshots - 8 marks", ["B2"]),
        ("B3. Sequence the portfolio and select the top three - 8 marks", ["B3"]),
        ("B4. Cross-functional compound-value check - 4 marks", ["B4"]),
    ]),
    ("Part C: Competitive AI Positioning - 20 marks", [
        ("C1. Five-source competitive intelligence scan - 8 marks", ["C1"]),
        ("C2. AI-enhanced Five Forces scan - 5 marks", ["C2_table", "C2"]),
        ("C3. Lead / follow / wait positioning for the top three opportunities - 4 marks", ["C3"]),
        ("C4. Proprietary-data moat / flywheel test - 3 marks", ["C4"]),
    ]),
    ("Part D: Workforce Impact and Role Redesign - 25 marks", [
        ("D1. Select the workforce focus - 3 marks", ["D1"]),
        ("D2. Task triage: Decompose -> Classify -> Redesign - 8 marks", ["D2"]),
        ("D3. Redesign the role and redeploy capacity - 5 marks", ["D3"]),
        ("D4. Capability and organisational redesign response - 5 marks", ["D4"]),
        ("D5. Human-AI collaboration evidence plan - 4 marks", ["D5"]),
    ]),
]

INTERNAL = re.compile(r"\[(?:D|A|F|R|L)(?::[^\]]*)?\]|\[J\]")
CITE_RUN = re.compile(r"(?:\[(?:E|C):[^\]]+\]\s*)+")


def cites(run):
    out = []
    for kind, ref in re.findall(r"\[(E|C):([^\]]+)\]", run):
        ref = ref.strip()
        if kind == "E":
            out.append(ref)
        else:
            m = re.fullmatch(r"M(\d)", ref)
            out.append("course notes, Module %s" % m.group(1) if m else "course notes")
    return "(" + "; ".join(dict.fromkeys(out)) + ")"


def clean(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<appendix>.*?</appendix>", "", text, flags=re.S)
    text = re.sub(r"(?m)^#{2,4} .*\n", "", text)  # draft headings replaced by worksheet titles
    text = INTERNAL.sub("", text)
    text = CITE_RUN.sub(lambda m: " " + cites(m.group(0)) + " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r" +([.,;:)|])", r"\1", text)
    text = re.sub(r"\( +", "(", text)
    text = re.sub(r"\|(?=[^ |\n-])", "| ", text)  # keep a space after table pipes
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def appendix_blocks():
    found = []
    for f in sorted(os.listdir(D)):
        if f.endswith(".md"):
            for m in re.finditer(r"<appendix>(.*?)</appendix>", open(os.path.join(D, f), encoding="utf-8").read(), re.S):
                found.append((f[:-3], m.group(1).strip()))
    return found


def evidence_rows():
    led = open(os.path.join(ROOT, "ledger", "ledger.md"), encoding="utf-8").read()
    body = re.search(r"<evidence>(.*?)</evidence>", led, re.S).group(1)
    used = {}
    for f in sorted(os.listdir(D)):
        if f.endswith(".md"):
            sec = f[:-3].split("_")[0]
            for ref in re.findall(r"\[E:([^\]]+)\]", open(os.path.join(D, f), encoding="utf-8").read()):
                used.setdefault(ref.strip(), set()).add(sec)
    rows = []
    for line in body.splitlines():
        c = [x.strip() for x in line.split("|")]
        if len(c) >= 7 and re.fullmatch(r"E\d+", c[0]):
            rows.append((c[0], c[2], c[1], c[3], c[4].replace(" ; ", "<br>"), ", ".join(sorted(used.get(c[0], []))) or "Not cited", c[6]))
    return rows


def main_body():
    out = ["# Assignment 3: AI Opportunity Portfolio with Maturity Assessment, Competitive Analysis, and Workforce Impact Scan\n",
           "Nilotpal Choudhury | AIBP Course 3\n"]
    for part, secs in PARTS:
        out.append("\n## %s\n" % part)
        for title, files in secs:
            out.append("\n### %s\n" % title)
            for f in files:
                body = clean(open(os.path.join(D, f + ".md"), encoding="utf-8").read())
                if f == "D4":
                    body = body.replace("**D4.1 Role family:**", "#### D4.1 Emerging AI capability / role family - 2 marks\n\n**D4.1 Role family:**", 1)
                    body = body.replace("**D4.2 Framework selected:**", "#### D4.2 Role-redesign framework - 3 marks\n\n**D4.2 Framework selected:**", 1)
                out.append("\n" + body)
    return "".join(out)


CHECKLIST = [
    "My assessment scope is clear and my claims do not exceed the evidence I can credibly access.",
    "All six maturity dimensions are rated using the Course 3 sub-dimensions and evidence.",
    "I have distinguished self-assessment from industry/peer benchmarking.",
    "My portfolio contains 5-7 distinct opportunities and does not force every problem into GenAI.",
    "Quick Win / Strategic Bet / Moonshot classifications match readiness and time/uncertainty.",
    "My top-three sequence is consistent with Part A maturity constraints.",
    "Competitive claims are publicly sourced or marked Not evidenced / Not applicable.",
    "I have applied all five competitive-intelligence signal categories without inventing unavailable evidence.",
    "Lead / follow / wait positions are initiative-specific and use data moat, regulatory clarity/risk and readiness.",
    "My workforce analysis focuses on tasks and role redesign rather than assuming job elimination.",
    "I completed at least 15 representative tasks in the task-triage table.",
    "Released capacity is deliberately redeployed to higher-value human/augmented work.",
    "The selected organisational redesign framework matches Part A maturity.",
    "The human-AI evidence plan compares Human alone / AI alone / Human + AI.",
    "Assumptions, anonymisation and hypothetical elements are clearly labelled.",
    "AI assistance, if used, is disclosed and I remain responsible for the final submission.",
]
DECL = [
    "The analysis and judgement in this submission are my own.",
    "Organisational facts are accurate to the best of my knowledge; estimates, assumptions, anonymisation and hypothetical elements are clearly labelled.",
    "I have not fabricated benchmark, competitor, patent, hiring, product, filing or other competitive-intelligence evidence.",
    "I have not disclosed confidential, personal or proprietary information that I am not authorised to share.",
    "Where I used AI assistance, I have disclosed it above and remain responsible for the final submission.",
]


def end_matter():
    o = ['\n<div class="pagebreak"></div>\n\n## Submission Checklist\n\n']
    o += ["- [ ] %s\n" % x for x in CHECKLIST]
    o.append("\n## Competitive / Benchmark Evidence Reference Log\n\n"
             "| Evidence ID | Organisation / topic | Source title / source type | Date | URL / location if shareable | Used in section |\n|---|---|---|---|---|---|\n")
    for r in evidence_rows():
        o.append("| %s | %s | %s | %s | %s | %s |\n" % r[:6])
    o.append("\n## Academic Integrity and AI-Assistance Disclosure\n\n"
             "| Disclosure field | Your response |\n|---|---|\n"
             "| Did you use an AI tool while preparing this assignment? | [ ] No [ ] Yes |\n"
             "| If yes, name the tool(s) and describe how they were used | |\n"
             "| What did you independently verify or materially revise? | |\n")
    o.append("\n## Honour Declaration\n\n")
    o += ["- [ ] %s\n" % x for x in DECL]
    o.append("\n| Name | Date | Signature / typed acknowledgement |\n|---|---|---|\n| | | |\n")
    o.append("\n## Optional Evidence Appendix\n\n")
    blocks = appendix_blocks()
    if blocks:
        for sec, txt in blocks:
            o.append("### Appendix %s\n\n%s\n\n" % (sec, clean(txt)))
    else:
        o.append("No optional evidence appendix material is included.\n")
    return "".join(o)


if __name__ == "__main__":
    mb = main_body()
    open(os.path.join(B, "A3_main_body.md"), "w", encoding="utf-8").write(mb)
    open(os.path.join(B, "A3_assembled.md"), "w", encoding="utf-8").write(mb + end_matter())
    print("evidence rows:", [(r[0], r[5], r[6]) for r in evidence_rows()])
    print("appendix blocks:", len(appendix_blocks()))
