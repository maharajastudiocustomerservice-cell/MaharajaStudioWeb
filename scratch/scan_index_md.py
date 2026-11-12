import os, re

for root, dirs, files in os.walk('assets/Documentations'):
    for f in files:
        if f.lower() == 'index.md':
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            if 'Attribute Directory' in c or '| Attribute |' in c:
                lines = c.splitlines()
                for i, line in enumerate(lines):
                    if '| Attribute |' in line or '| attribute |' in line.lower():
                        print(f"{p}:")
                        print("  Header:", line)
                        for sample in lines[i+2:i+5]:
                            if sample.strip():
                                print("   Sample:", sample[:100])
                        break
