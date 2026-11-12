import urllib.request
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

print("Fetching publisher page...")
html = fetch("https://assetstore.unity.com/publishers/120284")
print("Length:", len(html))

# Look for reviews or package ids in html
package_ids = re.findall(r'/packages/[^"\']+/(\d+)', html)
print("Found package IDs:", set(package_ids))

# Check for review text or JSON in page
if 'reviews' in html.lower():
    print("Page mentions reviews!")

# Also try known packages for reviews
known_packages = ['303666', '338916', '329676', '327233', '347520', '344724']
for pid in set(package_ids + known_packages):
    # Try review API endpoint
    api_url = f"https://assetstore.unity.com/api/v1/packages/{pid}/reviews"
    res = fetch(api_url)
    if "Error" not in res and len(res) > 20:
        print(f"Reviews for {pid}:", res[:500])
    
    # Also fetch the package page to look for reviews
    pkg_html = fetch(f"https://assetstore.unity.com/packages/slug/{pid}")
    # Extract JSON-LD or review elements
    reviews = re.findall(r'"reviewBody":\s*"([^"]+)"', pkg_html)
    authors = re.findall(r'"author":\s*\{\s*"@type":\s*"Person",\s*"name":\s*"([^"]+)"', pkg_html)
    if reviews:
        print(f"Found JSON-LD reviews for {pid}:", list(zip(authors, reviews)))
    else:
        # Check for review tags
        rev_texts = re.findall(r'<div class="[^"]*review[^"]*">.*?</div>', pkg_html, re.DOTALL)
        if rev_texts:
            print(f"Found HTML reviews for {pid}: {len(rev_texts)}")

