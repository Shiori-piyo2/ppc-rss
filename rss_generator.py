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

if "個人情報保護委員会" in title:
    continue

if "改正法" in title:
    continue

if "年次報告" in title:
    continue

if "上半期報告" in title:
    continue

if "個人情報を考える週間" in title:
    continue
    if len(title) < 10:
        continue
    ng_words = [
        "フッターへ移動します",
        "ホーム",
        "委員会について",
        "個人情報保護委員会について",
        "委員長・委員・幹部紹介"
    ]

    if title in ng_words:
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
