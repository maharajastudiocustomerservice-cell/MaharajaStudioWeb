with open('msultimate-core-docs.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="cat-callbacks"' in line:
        print(f"Line {i+1}:")
        for j in range(i, min(len(lines), i + 40)):
            print(f"{j+1}: {lines[j]}", end="")
        break

