with open('scripts/build_msultimate_docs.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'it["href"]' in line or "it['href']" in line or '"href":' in line or "'href':" in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(max(0, i-15), min(len(lines), i+15)):
            print(f"  {j+1}: {lines[j]}", end="")
        print("\n" + "="*50 + "\n")
