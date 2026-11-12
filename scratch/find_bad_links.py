from bs4 import BeautifulSoup
import glob

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    
    bad_links = []
    # Find all table rows in data-cat-explorer or cat tables
    for tr in soup.find_all('tr', attrs={'data-cat-row': True}):
        a = tr.find('a')
        if a:
            href = a.get('href', '')
            label = a.get_text(strip=True)
            if href.startswith('#cat-') or href == '' or href == '#':
                bad_links.append((label, href))
    
    if bad_links:
        print(f"{f}: {len(bad_links)} BAD category-looping table links! E.g.:")
        for l, h in bad_links[:8]:
            print(f"   {l} -> {h}")
    else:
        # Check if there are any data-cat-row at all
        rows = soup.find_all('tr', attrs={'data-cat-row': True})
        if rows:
            print(f"{f}: All {len(rows)} category table links are valid and specific!")
