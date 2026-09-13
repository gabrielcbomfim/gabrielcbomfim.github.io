from pathlib import Path
import re

root = Path('.')
mail = '<a href="mailto:carneirogabriel10@gmail.com">E-mail</a>'
pattern = re.compile(r'(<a\s+href="https://www\.linkedin\.com/in/gabrielcbomfim/[^">]*">[^<]*</a>)', re.I)

updated = []
for p in root.rglob('index.html'):
    text = p.read_text(encoding='utf-8')
    if 'mailto:' in text:
        continue
    if 'linkedin.com/in/gabrielcbomfim/' not in text:
        continue
    new_text = pattern.sub(r'\1 | ' + mail, text, count=1)
    p.write_text(new_text, encoding='utf-8')
    updated.append(str(p.relative_to(root)))

print(f'updated {len(updated)}')
for item in updated:
    print(item)
