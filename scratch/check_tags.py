import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'<span class="tag">([^<]+,[^<]+)</span>', c)
    if m:
        print(f'{f}: {len(m)} multi-target tags')
        for sample in m[:3]:
            print(f'   - {sample}')

