import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from email.utils import formatdate

print("PPC RSS")

SOURCE_URL = "https://www.ppc.go.jp/information/"

r = requests.get(SOURCE_URL, timeout=30)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

items = []

for link in soup.select("div.news-text a"):

    title = link.get_text(strip=True)

    if len(title) < 15:
        continue

    if "年次報告" in title:
        continue

    if "上半期報告" in title:
        continue

    if "個人情報を考える週間" in title:
        continue

    href = link.get("href")

    if not href:
        continue

    article_url = urljoin(SOURCE_URL, href)

    items.append({
        "title": title,
        "link": article_url
    })

    if len(items) >= 15:
        break

with open("feed.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('<channel>\n')

    f.write('<title>個人情報保護委員会 新着情報</title>\n')
    f.write('<link>https://www.ppc.go.jp/information/</link>\n')
    f.write('<description>個人情報保護委員会 新着情報RSS</description>\n')
    f.write(f'<lastBuildDate>{formatdate(usegmt=True)}</lastBuildDate>\n')

    for item in items:

        f.write('<item>\n')
        f.write(f'<title><![CDATA[{item["title"]}]]></title>\n')
        f.write(f'<link>{item["link"]}</link>\n')
        f.write(f'<guid isPermaLink="true">{item["link"]}</guid>\n')

        f.write(
            f'<description><![CDATA['
            f'<p><a href="{item["</p>'
            f']]></description>\n'
        )

        f.write('</item>\n')

    f.write('</channel>\n')
    f.write('</rss>\n')

print(f"{len(items)} items written")
