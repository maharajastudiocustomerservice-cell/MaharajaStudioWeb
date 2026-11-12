with open('scripts/build_msultimate_docs.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for fn in ['parse_directory_table', 'resolve_href']:
    m = re.search(r'def\s+' + fn + r'\b', text)
    if m:
        print(f"--- {fn} ---")
        print(text[m.start():m.start()+800])
