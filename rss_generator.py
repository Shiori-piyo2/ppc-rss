import requests
from bs4 import BeautifulSoup

print("PPC RSS")

url = "https://www.ppc.go.jp/"

r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

items = []

for link in links:
    title = link.get_text(strip=True)

    if len(title) < 10:
        continue

    if len(items) >= 10:
        break

    items.append(title)

with open("feed.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('<channel>\n')
    f.write('<title>PPC RSS</title>\n')

    for item in items:
        f.write('<item>\n')
        f.write(f'<title>{item}</title>\n')
        f.write('</item>\n')

    f.write('</channel>\n')
    f.write('</rss>\n')
