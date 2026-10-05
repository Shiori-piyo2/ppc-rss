from datetime import datetime

print("PPC RSS")

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>PPC Test Feed</title>
<link>https://www.ppc.go.jp/</link>
<description>Test</description>

<item>
<title>PPCテスト {datetime.now()}</title>
<link>https://www.ppc.go.jp/</link>
</item>

</channel>
</rss>
"""
    )
