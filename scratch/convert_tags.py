import glob, re

files = [
    'msultimate-core-docs.html',
    'msultimate-component-docs.html',
    'msultimate-hierarchy-docs.html',
    'msultimate-toolbox-docs.html'
]

pattern = re.compile(r'<span class="tag">([^<]+,[^<]+)</span>')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    def replacer(match):
        targets_str = match.group(1)
        parts = [p.strip() for p in targets_str.split(',') if p.strip()]
        tags_html = "".join(f'<span class="tag">{p}</span>' for p in parts)
        return f'<div class="tag-group">{tags_html}</div>'
    
    new_content, count = pattern.subn(replacer, content)
    if count > 0:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f"Updated {f}: {count} replacements")
    else:
        print(f"No matches in {f}")
