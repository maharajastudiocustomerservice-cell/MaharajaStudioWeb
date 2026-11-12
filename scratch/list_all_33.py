from bs4 import BeautifulSoup

with open('msultimate-core-docs.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp.read(), 'html.parser')

all_section_ids = {sec['id']: sec for sec in soup.find_all('section', class_='docs-section')}

for tr in soup.find_all('tr', attrs={'data-cat-row': True}):
    a = tr.find('a')
    if a:
        href = a.get('href', '')
        label = a.get_text(strip=True)
        if href.startswith('#cat-') or href == '' or href == '#':
            # Let's find the matching section ID in the document
            clean_label = label.replace('[', '').replace(']', '').strip().lower()
            # Find candidate section
            candidate = None
            for sid, sec in all_section_ids.items():
                title = sec.get('data-doc-title', '')
                if clean_label == title.replace('[', '').replace(']', '').strip().lower():
                    candidate = sid
                    break
                # Also try slug matching
                slug_candidate = clean_label.replace(' ', '-').replace('_', '-')
                if sid == slug_candidate:
                    candidate = sid
                    break
            print(f"{label}: current href='{href}' -> target section: #{candidate}")
