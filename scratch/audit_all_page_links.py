from bs4 import BeautifulSoup
import glob

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    
    # Collect all IDs in this document
    all_ids = {tag['id'] for tag in soup.find_all(id=True)}
    
    broken_same_page = []
    category_self_loops = []
    
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        if not href or href == '#':
            continue
        if href.startswith('#'):
            target_id = href[1:]
            if target_id not in all_ids:
                broken_same_page.append((text, href))
            # Check if this link is on an attribute name (e.g. [Something]) but links to a category (#cat-...)
            if text.startswith('[') and text.endswith(']') and href.startswith('#cat-'):
                category_self_loops.append((text, href))
    
    if broken_same_page:
        print(f"{f}: {len(broken_same_page)} BROKEN same-page hash links:")
        for t, h in broken_same_page[:5]:
            print(f"   '{t}' -> '{h}'")
    if category_self_loops:
        print(f"{f}: {len(category_self_loops)} attribute names linking to categories instead of sections:")
        for t, h in category_self_loops[:5]:
            print(f"   '{t}' -> '{h}'")
