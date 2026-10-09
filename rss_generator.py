import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from feedgen.feed import FeedGenerator

print("PPC RSS")

SOURCE_URL = "https://www.ppc.go.jp/information/"

r = requests.get(SOURCE_URL, timeout=30)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

fg = FeedGenerator()
fg.title("個人情報保護委員会 新着情報")
fg.link(href=SOURCE_URL)
fg.description("個人情報保護委員会 新着情報RSS")
fg.language("ja")

count = 0

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

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=article_url)
    fe.guid(article_url, permalink=True)
    fe.description(f'元記事: {article_url}')

    count += 1

    if count >= 15:
        break

fg.rss_file("feed.xml")

print(f"{count} items written")
