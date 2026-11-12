import os, re
from pathlib import Path

# Let's inspect all tables in MSUltimate docs
doc_dir = Path("assets/Documentations")
for root, dirs, files in os.walk(doc_dir):
    for f in files:
        if f.lower() == "index.md":
            p = Path(root) / f
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                c = fp.read()
            if "Attribute Directory" in c or "| Attribute |" in c:
                # check rows
                for line in c.splitlines():
                    if line.strip().startswith("|") and not re.match(r"^\|?[\s:\-|]+\|?$", line.strip()) and "| attribute |" not in line.lower():
                        cells = [x.strip() for x in line.strip().split("|")[1:-1]]
                        # search for any markdown link in cells
                        links = []
                        for cell in cells:
                            m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cell)
                            if m:
                                links.append((m.group(1), m.group(2)))
                        # print if no link in cell 0
                        m0 = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cells[0]) if cells else None
                        if not m0 and cells:
                            print(f"{p.name} in {p.parent.name}: cell0='{cells[0]}' -> other links: {links}")
                            break
