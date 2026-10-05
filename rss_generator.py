import requests

print("PPC RSS")

r = requests.get("https://www.ppc.go.jp/")
r.raise_for_status()

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(
        """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>PPC RSS</title>
<link>https://www.ppc.go.jp/</link>
<description>PPC RSS</description>

<item>
<title>PPCトップページ取得成功</title>
<link>https://www.ppc.go.jp/</link>
</item>

</channel>
</rss>
"""
    )
