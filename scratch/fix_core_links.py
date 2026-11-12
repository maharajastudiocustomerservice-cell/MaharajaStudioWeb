from bs4 import BeautifulSoup

with open('msultimate-core-docs.html', 'r', encoding='utf-8') as fp:
    html_text = fp.read()

soup = BeautifulSoup(html_text, 'html.parser')

all_sections = {sec['id']: sec for sec in soup.find_all('section', class_='docs-section')}

replacements_count = 0

for tr in soup.find_all('tr', attrs={'data-cat-row': True}):
    a = tr.find('a')
    if a:
        href = a.get('href', '')
        label = a.get_text(strip=True)
        if href.startswith('#cat-') or href == '' or href == '#':
            clean_label = label.replace('[', '').replace(']', '').strip().lower()
            candidate = None
            for sid, sec in all_sections.items():
                title = sec.get('data-doc-title', '')
                if clean_label == title.replace('[', '').replace(']', '').strip().lower():
                    candidate = sid
                    break
                slug_candidate = clean_label.replace(' ', '-').replace('_', '-')
                if sid == slug_candidate or sid.replace('-', '') == clean_label:
                    candidate = sid
                    break
            if candidate:
                a['href'] = f"#{candidate}"
                replacements_count += 1
                print(f"Fixed {label}: {href} -> #{candidate}")
            else:
                print(f"WARNING: Could not find section for {label}")

with open('msultimate-core-docs.html', 'w', encoding='utf-8') as fp:
    fp.write(str(soup))

print(f"\nTotal links updated in msultimate-core-docs.html: {replacements_count}")
