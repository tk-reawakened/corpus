#!/usr/bin/env python3
"""Check the generated site for links that do not resolve."""
import collections
import os
import re
import sys
from html.parser import HTMLParser

SITE = sys.argv[1] if len(sys.argv) > 1 else "_site"
HREF = re.compile(r'(?:href|src)="([^"]+)"')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ("href", "src"):
            if d.get(k):
                self.urls.append(d[k])


broken = collections.Counter()
examples = {}
total = 0
for root, dirs, files in os.walk(SITE):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
    for name in files:
        if not name.endswith(".html"):
            continue
        p = os.path.join(root, name)
        txt = open(p, encoding="utf-8", errors="replace").read()
        lp = Links()
        lp.feed(txt)
        for u in lp.urls:
            if u.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            total += 1
            u = u.split("#")[0].split("?")[0]
            if not u:
                continue
            target = os.path.normpath(os.path.join(root, u))
            if os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                broken[u] += 1
                examples.setdefault(u, p)

print("internal links checked: %d" % total)
print("broken targets: %d distinct, %d links" % (len(broken), sum(broken.values())))
for u, c in broken.most_common(30):
    print("  %-60s %5d   e.g. %s" % (u[:60], c, examples[u][-70:]))
