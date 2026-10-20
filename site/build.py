#!/usr/bin/env python3
"""Build the TK Corpus site: every corpus entry as an HTML page, plus the
browse indexes and the documents the search index is made from.

usage:
    build.py [--corpus DIR] [--out DIR]

    --corpus DIR   the corpus markdown (default: ../corpus)
    --out DIR      where the site is written (default: ../_site)

The markdown renderer is deliberately small and dependency-free: the corpus is
machine-generated, so its markdown is a known, narrow shape (headings, bold,
italic, links, images, lists, blockquotes, code fences, horizontal rules).
Frontmatter is read with PyYAML, which is the only dependency.
"""
import argparse
import collections
import datetime
import glob
import html
import json
import os
import re
import sys
import unicodedata

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))

# where the raw Markdown lives, for the "Raw Markdown" link on every entry page
REPO_BLOB = os.environ.get(
    "TK_CORPUS_REPO_BLOB", "https://github.com/tk-reawakened/corpus/blob/main/corpus/")

KINDS = [
    ("forum-thread", "Forum threads", "forums", "Every captured thread, with all its replies in order."),
    ("page", "Pages", "pages", "Everything else that was a page: home pages, news entries, member sites."),
    ("game", "Games", "games", "Game profiles from toolkitzone.com and mysticsoftware.net."),
    ("file", "Files", "files", "The toolkitzone.com file database: plugins, method packs, resources."),
    ("doc", "Documents", "docs", "News, tutorials, articles and help documents."),
    ("blog", "Blogs", "blogs", "Community blogs."),
    ("member", "Members", "members", "Member profiles, with join date, occupation and interests."),
    ("review", "Reviews", "reviews", "Game reviews from mysticsoftware.net."),
    ("code", "Code", "code", "RPG Code submissions: menus, methods, plugins."),
    ("download", "Downloads", "downloads", "The binaries the archive recovered, with size and provenance."),
]

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


# ---------------------------------------------------------------- markdown

def esc(s):
    return html.escape(s or "", quote=False)


def inline(text):
    """markdown inline -> html (the corpus's own markdown, nothing exotic)"""
    spans = []

    def stash(m):
        spans.append("<code>%s</code>" % esc(m.group(1)))
        return "\x00%d\x00" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = esc(text)
    # autolinks before anything else eats the brackets
    text = re.sub(r"&lt;(https?://[^\s&]+)&gt;", r'<a href="\1" rel="nofollow">\1</a>', text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
                  lambda m: '<img src="%s" alt="%s" loading="lazy">' % (m.group(2), m.group(1)), text)
    text = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)",
                  lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1) or m.group(2)), text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)
    return text


def md_to_html(text):
    """the corpus's markdown -> html"""
    out = []
    lines = (text or "").split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        # fenced code
        m = re.match(r"^```(\w*)\s*$", line)
        if m:
            i += 1
            buf = []
            while i < n and not re.match(r"^```\s*$", lines[i]):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
            continue
        if not line.strip():
            i += 1
            continue
        if re.match(r"^\s*---+\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            anchor = ""
            pm = re.match(r"^###\s+(.+?)\s+·\s+(.+?)\s+·\s+#(\S+)\s*$", m.group(2))
            if pm:
                anchor = ' id="p-%s"' % esc(pm.group(3))
            out.append("<h%d%s>%s</h%d>" % (lvl, anchor, inline(m.group(2)), lvl))
            i += 1
            continue
        if re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append("<li>%s</li>" % inline(re.sub(r"^\s*[-*+]\s+", "", lines[i])))
                i += 1
            out.append("<ul>%s</ul>" % "".join(items))
            continue
        if re.match(r"^\s*&gt;|^\s*>", line) or re.match(r"^\s*>", line):
            buf = []
            while i < n and re.match(r"^\s*>", lines[i]):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf)))
            continue
        # paragraph - the corpus puts one block per line, so a line is a paragraph
        if not re.match(r"^\s*(#{1,6}\s|[-*+]\s|>|```)", line):
            out.append("<p>%s</p>" % inline(line.strip()))
        i += 1
    return "\n".join(out)


# ---------------------------------------------------------------- helpers

def slug(s, n=60):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return (s[:n].rstrip("-") or "unknown")


def load(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        t = f.read()
    m = FM.match(t)
    if not m:
        return {}, t
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, t[m.end():]


def readme_of(fm, body):
    """the corpus body without its first '# title' line"""
    lines = body.split("\n")
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        lines = lines[i + 1:]
    return "\n".join(lines).strip()


def fm_value(fm, key):
    v = fm.get(key)
    if v is None:
        return None
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v)


# ---------------------------------------------------------------- templates

def page(title, body, depth=0, extra=""):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="stylesheet" href="%sassets/style.css">
%s</head>
<body>
<header class="top">
  <a class="brand" href="%s">TK&nbsp;Corpus</a>
  <nav>
    <a href="%sbrowse/">Browse</a>
    <a href="%speople/">People</a>
    <a href="%sgames/">Games</a>
    <a href="%sabout/">About</a>
  </nav>
</header>
<main>
%s
</main>
<footer class="foot">
  <p>Recovered from the Wayback Machine, %d entries. Public domain sources; see
  <a href="%sabout/">About &amp; provenance</a>.</p>
</footer>
</body>
</html>
""" % (esc(title), "../" * depth, extra, "../" * depth, "../" * depth, "../" * depth,
       "../" * depth, "../" * depth, body, TOTAL["entries"], "../" * depth)


TOTAL = {"entries": 0}


def entry_url(rel):
    """corpus/<kind>/<site>/<file>.md -> e/<kind>/<site>/<file>.html"""
    return "e/" + rel[:-3] + ".html" if rel.endswith(".md") else "e/" + rel


def meta_table(fm):
    rows = []
    order = [("kind", "Kind"), ("site", "Site"), ("author", "Author"),
             ("written", "Written"), ("updated", "Updated"), ("captured", "Captured"),
             ("board", "Board"), ("forum", "Forum"), ("handle", "Handle"),
             ("reviewer", "Reviewer"), ("submitted_by", "Submitted by"),
             ("original_url", "Original URL")]
    for k, label in order:
        v = fm.get(k)
        if v in (None, "", [], {}):
            continue
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        if k == "original_url":
            cell = '<a href="%s" rel="nofollow">%s</a>' % (esc(str(v)), esc(str(v)))
        else:
            cell = esc(str(v))
        rows.append("<tr><th>%s</th><td>%s</td></tr>" % (label, cell))
    extra = {}
    for k, v in sorted(fm.items()):
        if k.startswith("f_"):
            extra[k[2:].replace("_", " ").title()] = v
    for k, v in sorted(extra.items()):
        rows.append("<tr><th>%s</th><td>%s</td></tr>" % (esc(k), esc(str(v))))
    if not rows:
        return ""
    return '<table class="meta">%s</table>' % "".join(rows)


def render_entry(rel, fm, body):
    kind = fm.get("kind", "page")
    site = fm.get("site", "")
    title = fm.get("title") or "(untitled)"
    url = entry_url(rel)
    h = []
    h.append('<article class="entry">')
    h.append("<h1>%s</h1>" % inline(str(title)))
    h.append('<p class="crumbs"><a href="../browse/kind/%s/">%s</a> · %s</p>' % (
        esc(kind), esc(kind), esc(str(site))))
    h.append(meta_table(fm))
    caps = fm.get("source_captures") or []
    if caps:
        links = []
        for c in caps:
            if isinstance(c, dict) and c.get("wayback_url"):
                links.append('<a href="%s" rel="nofollow">%s</a>' % (
                    esc(c["wayback_url"]), esc(str(c.get("captured") or "capture"))))
        if links:
            h.append('<p class="src">Wayback: %s</p>' % " · ".join(links))
    if fm.get("duplicate_of"):
        h.append('<p class="note">This page was also captured under another URL — '
                 'the same content is filed under <code>%s</code>.</p>' % esc(str(fm["duplicate_of"])))
    h.append('<div class="body">%s</div>' % md_to_html(readme_of(fm, body)))
    h.append('<p class="raw">Raw Markdown: <a href="%s">%s</a></p>' % (
        esc(REPO_BLOB + rel), esc(rel)))
    h.append("</article>")
    return page(str(title), "\n".join(h), depth=2)


def list_page(title, intro, items, depth=1, kind=None):
    h = ["<h1>%s</h1>" % esc(title)]
    if intro:
        h.append("<p class=\"intro\">%s</p>" % inline(intro))
    if not items:
        h.append("<p class=\"empty\">Nothing here yet.</p>")
    else:
        h.append('<ul class="entries">')
        for it in items:
            h.append("<li>%s</li>" % it)
        h.append("</ul>")
    return page(title, "\n".join(h), depth=depth)


def link_entry(rel, fm, extra=""):
    title = fm.get("title") or "(untitled)"
    bits = []
    if fm.get("author"):
        bits.append(esc(str(fm["author"])))
    if fm.get("written"):
        bits.append(esc(str(fm["written"])[:10]))
    if fm.get("site"):
        bits.append(esc(str(fm["site"])))
    return '<a href="%s">%s</a> <span class="m">%s</span>%s' % (
        "../" * 1 + entry_url(rel), esc(str(title)), " · ".join(bits), extra)


# ---------------------------------------------------------------- build

def build(corpus, out):
    files = sorted(glob.glob(os.path.join(corpus, "*", "*", "*.md")) +
                   glob.glob(os.path.join(corpus, "*", "*.md")))
    entries = []
    for path in files:
        rel = os.path.relpath(path, corpus)
        fm, body = load(path)
        if not fm:
            continue
        entries.append((rel, fm, body))
    TOTAL["entries"] = len(entries)
    print("entries: %d" % len(entries))

    for sub in ("e", "browse/kind", "browse/site", "browse/year", "people", "games",
                "assets", "search", "about"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)

    # ---- one page per entry
    for rel, fm, body in entries:
        p = os.path.join(out, entry_url(rel))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(render_entry(rel, fm, body))

    by_kind = collections.defaultdict(list)
    by_site = collections.defaultdict(list)
    by_year = collections.defaultdict(list)
    people = collections.defaultdict(lambda: {"items": [], "posts": 0, "sites": set(), "first": None})
    games = []
    search_docs = []

    for rel, fm, body in entries:
        kind = fm.get("kind", "page")
        by_kind[kind].append((rel, fm))
        by_site[str(fm.get("site", ""))].append((rel, fm))
        written = str(fm.get("written") or "")
        if written:
            by_year[written[:4]].append((rel, fm))
        # people
        for a in ([fm.get("author")] if fm.get("author") else []) + list(fm.get("authors") or []):
            if not a or not plausible_name(str(a)):
                continue
            p = people[str(a)]
            p["items"].append((rel, fm))
            p["posts"] += int(fm.get("posts_present") or 1)
            p["sites"].add(str(fm.get("site", "")))
            if written and (not p["first"] or written < p["first"]):
                p["first"] = written
        if kind == "game":
            games.append((rel, fm))

        # ---- search documents: one per post, one per page
        chunks = split_chunks(body)
        for pid, author, ts, text in chunks:
            search_docs.append({
                "id": len(search_docs),
                "path": rel,
                "pid": pid,
                "kind": kind,
                "site": str(fm.get("site", "")),
                "title": str(fm.get("title") or ""),
                "author": author or str(fm.get("author") or ""),
                "ts": ts,
                "text": text,
            })

    # ---- browse by kind
    for kind, label, folder, desc in KINDS:
        items = by_kind.get(kind, [])
        rows = []
        for rel, fm in sorted(items, key=lambda x: (str(x[1].get("written") or ""), x[0])):
            rows.append("<li>%s</li>" % link_entry(rel, fm))
        body = list_page(label, desc, rows, depth=2)
        os.makedirs(os.path.join(out, "browse/kind", kind), exist_ok=True)
        with open(os.path.join(out, "browse/kind", kind, "index.html"), "w", encoding="utf-8") as f:
            f.write(body)

    # ---- browse by site
    for site, items in sorted(by_site.items()):
        rows = ["<li>%s</li>" % link_entry(rel, fm) for rel, fm in sorted(items)]
        body = list_page(site, "%d entries" % len(items), rows, depth=3)
        os.makedirs(os.path.join(out, "browse/site", slug(site)), exist_ok=True)
        with open(os.path.join(out, "browse/site", slug(site), "index.html"), "w", encoding="utf-8") as f:
            f.write(body)

    # ---- browse by year
    for year, items in sorted(by_year.items()):
        rows = ["<li>%s</li>" % link_entry(rel, fm) for rel, fm in sorted(items)]
        body = list_page(year, "%d entries" % len(items), rows, depth=3)
        os.makedirs(os.path.join(out, "browse/year", year), exist_ok=True)
        with open(os.path.join(out, "browse/year", year, "index.html"), "w", encoding="utf-8") as f:
            f.write(body)

    # ---- people
    plist = []
    for name, p in sorted(people.items(), key=lambda kv: (-kv[1]["posts"], kv[0].lower())):
        sl = slug(name)
        rows = []
        seen = set()
        for rel, fm in sorted(p["items"], key=lambda x: (str(x[1].get("written") or ""), x[0])):
            if rel in seen:
                continue
            seen.add(rel)
            rows.append("<li>%s</li>" % link_entry(rel, fm))
        when = ("First dated item: %s" % p["first"][:10]) if p["first"] else "No dated items"
        body = list_page(name, "%d entries · %s" % (len(p["items"]), when), rows, depth=2)
        with open(os.path.join(out, "people", sl + ".html"), "w", encoding="utf-8") as f:
            f.write(body)
        plist.append('<li><a href="people/%s.html">%s</a> <span class="m">%d entries</span></li>' % (
            sl, esc(name), len(p["items"])))
    with open(os.path.join(out, "people/index.html"), "w", encoding="utf-8") as f:
        f.write(list_page("People", "%d people" % len(people), plist, depth=1))

    # ---- games
    bytitle = collections.defaultdict(list)
    for rel, fm in games:
        bytitle[norm_title(fm.get("title"))].append((rel, fm))
    grows = []
    multi = []
    for t, items in sorted(bytitle.items()):
        for rel, fm in items:
            grows.append("<tr><td><a href=\"%s\">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                entry_url(rel), esc(str(fm.get("title") or "")),
                esc(str(fm.get("site") or "")),
                esc(str(fm.get("f_led_by") or fm.get("author") or "")),
                esc(str(fm.get("f_status") or "")),
                esc(str(fm.get("f_toolkit_version") or ""))))
        if t and len({fm.get("site") for _, fm in items}) > 1:
            multi.append("<li>%s</li>" % esc(t))
    body = ["<h1>Games</h1>",
            '<p class="intro">%d game profiles. Games whose title appears on more than one site '
            'are listed at the bottom - they are the same game.</p>' % len(games),
            '<table class="games"><tr><th>Game</th><th>Site</th><th>Led by</th><th>Status</th>'
            '<th>Toolkit</th></tr>', "".join(grows), "</table>",
            "<h2>Same title on more than one site</h2>",
            "<ul>%s</ul>" % ("".join(multi) or "<li>(none)</li>")]
    with open(os.path.join(out, "games/index.html"), "w", encoding="utf-8") as f:
        f.write(page("Games", "\n".join(body), depth=1))

    # ---- search documents for the index builder
    with open(os.path.join(out, "search", "documents.json"), "w", encoding="utf-8") as f:
        json.dump(search_docs, f)
    print("search documents: %d" % len(search_docs))

    # ---- home + about
    write_home(out, by_kind, by_site, people, games)
    write_about(out, by_kind)
    write_browse(out, by_kind, by_site, by_year)

    # ---- static assets
    for name in os.listdir(os.path.join(HERE, "assets")):
        src = os.path.join(HERE, "assets", name)
        if os.path.isfile(src):
            with open(src, "rb") as f:
                data = f.read()
            with open(os.path.join(out, "assets", name), "wb") as f:
                f.write(data)

    print("wrote %s" % out)


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def plausible_name(name):
    """not every author field holds a person (some hold a date, some a label)"""
    n = name.strip()
    if len(n) < 2 or len(n) > 40:
        return False
    if n.lower() in ("none", "null", "n/a", "unknown", "password", "username"):
        return False
    if re.match(r"^\d{1,4}[-/: ]\d{1,4}", n):          # a date
        return False
    if re.match(r"^(mon|tue|wed|thu|fri|sat|sun)", n, re.I):   # a day
        return False
    if n.count(" ") > 3:
        return False
    return True


POST = re.compile(r"^### (.+?) · (.+?) · #(\S+)\s*$", re.M)


def split_chunks(body):
    """-> [(post id, author, ts, text)] : one per post, plus the page's own text"""
    out = []
    ms = list(POST.finditer(body))
    intro = body[:ms[0].start()] if ms else body
    intro = re.sub(r"^# .*$", "", intro, count=1, flags=re.M).strip()
    if intro:
        out.append((None, None, None, intro))
    for i, h in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        out.append((h.group(3), h.group(1).strip(), h.group(2).strip(), body[h.end():end].strip()))
    return out


def write_browse(out, by_kind, by_site=None, by_year=None):
    rows = []
    for kind, label, folder, desc in KINDS:
        rows.append("<tr><td><a href=\"kind/%s/\">%s</a></td><td>%d</td><td>%s</td></tr>" % (
            esc(kind), esc(label), len(by_kind.get(kind, [])), esc(desc)))
    body = [
        "<h1>Browse</h1>",
        '<p class="intro">Three ways in: by kind, by site, or by year.</p>',
        "<h2>By kind</h2>",
        '<table class="kinds"><tr><th>Kind</th><th>Entries</th><th>What it is</th></tr>',
        "".join(rows), "</table>",
        '<p><a href="site/">All sites</a> · <a href="year/">All years</a></p>',
    ]
    with open(os.path.join(out, "browse/index.html"), "w", encoding="utf-8") as f:
        f.write(page("Browse", "\n".join(body), depth=1))
    if by_site:
        srows = ["<li><a href=\"%s/\">%s</a> <span class=\"m\">%d entries</span></li>" % (
            slug(s), esc(s), len(v)) for s, v in sorted(by_site.items())]
        with open(os.path.join(out, "browse/site/index.html"), "w", encoding="utf-8") as f:
            f.write(list_page("Sites", "%d sites" % len(by_site), srows, depth=2))
    if by_year:
        yrows = ["<li><a href=\"%s/\">%s</a> <span class=\"m\">%d entries</span></li>" % (
            esc(y), esc(y), len(v)) for y, v in sorted(by_year.items())]
        with open(os.path.join(out, "browse/year/index.html"), "w", encoding="utf-8") as f:
            f.write(list_page("Years", "%d years" % len(by_year), yrows, depth=2))


def write_home(out, by_kind, by_site, people, games):
    rows = []
    for kind, label, folder, desc in KINDS:
        n = len(by_kind.get(kind, []))
        rows.append("<tr><td><a href=\"browse/kind/%s/\">%s</a></td><td>%d</td><td>%s</td></tr>" % (
            esc(kind), esc(label), n, esc(desc)))
    body = [
        "<h1>The RPG Toolkit community archive</h1>",
        '<p class="lead">%d pages, forum threads, game profiles, plugins and documents, '
        'recovered from the Wayback Machine and written out as Markdown. '
        'The games themselves live in <a href="https://github.com/tk-reawakened/ludotheque">ludotheque</a>.</p>' % TOTAL["entries"],
        "<table class=\"kinds\"><tr><th>Kind</th><th>Entries</th><th>What it is</th></tr>",
        "".join(rows), "</table>",
        "<h2>Start here</h2>",
        '<ul class="start">',
        '<li><a href="browse/site/">Browse by site</a> — %d sites</li>' % len(by_site),
        '<li><a href="browse/year/">Browse by year</a></li>',
        '<li><a href="people/">Browse by person</a> — %d people</li>' % len(people),
        '<li><a href="games/">The games</a> — %d profiles</li>' % len(games),
        "</ul>",
        "<h2>Search</h2>",
        '<p>Type in the box on any page. The search covers every post and every page in the corpus.</p>',
        '<form class="search" action="search/" method="get"><input type="search" name="q" '
        'placeholder="e.g. pea shooter, RNG, dark age" autocomplete="off"><button>Search</button></form>',
    ]
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page("TK Corpus", "\n".join(body), depth=0))
    os.makedirs(os.path.join(out, "search"), exist_ok=True)
    scripts = ('<script src="../assets/minisearch.js" defer></script>\n'
               '<script src="../assets/app.js" defer></script>')
    with open(os.path.join(out, "search/index.html"), "w", encoding="utf-8") as f:
        f.write(page("Search", """
<h1>Search the corpus</h1>
<form class="search" id="q" onsubmit="return false"><input type="search" id="qq"
 placeholder="e.g. pea shooter, RNG, dark age" autocomplete="off"><button>Search</button></form>
<div id="scope"><label>Kind <select id="kind">
<option value="">all kinds</option>
%s
</select></label> <span id="stat"></span></div>
<div id="results"></div>
""" % "".join('<option value="%s">%s</option>' % (k, l) for k, l, _f, _d in KINDS), depth=1, extra=scripts))


def write_about(out, by_kind):
    rows = []
    for kind, label, _f, _d in KINDS:
        n = len(by_kind.get(kind, []))
        if n:
            rows.append("<tr><td>%s</td><td>%d</td></tr>" % (esc(label), n))
    body = [
        "<h1>About this archive</h1>",
        "<h2>What it is</h2>",
        "<p>RPG Toolkit was a game-making tool for Windows in the late 1990s and 2000s, and "
        "it had a lively community: toolkitzone.com, mysticsoftware.net, rpgtoolkit.net, "
        "rpgtoolkit.com and the Aljo Productions site among them. Most of that community is "
        "gone. This repository holds what the Wayback Machine still has of it, written out as "
        "Markdown so it can be read and searched instead of being a pile of captured HTML.</p>",
        "<p>The engine rebuild that this archive supports lives in "
        "<a href=\"https://github.com/tk-reawakened/rpgtoolkit-reawakened\">rpgtoolkit-reawakened</a>. "
        "The recovered games live in <a href=\"https://github.com/tk-reawakened/ludotheque\">ludotheque</a>.</p>",
        "<h2>How it was made</h2>",
        "<ol>",
        "<li>The Wayback Machine's CDX index was read for every host, giving the full list of "
        "URLs that were ever captured.</li>",
        "<li>Each URL was fetched from the archive and stored byte-for-byte, with a manifest "
        "recording the capture timestamp, the SHA-256 of every file and the source URL.</li>",
        "<li>A converter walks the captures and writes one Markdown file per page, thread, "
        "profile or download, with the page's metadata in YAML frontmatter.</li>",
        "<li>The site you are reading is generated from those files.</li>",
        "</ol>",
        "<h2>What is in it</h2>",
        '<table class="kinds"><tr><th>Kind</th><th>Entries</th></tr>', "".join(rows), "</table>",
        "<h2>Personal data</h2>",
        "<p>This is a historical archive of a public forum, and it contains what that forum "
        "contained: the handles people posted under, their email addresses where they posted "
        "them, their member-profile details (join date, occupation, interests) and their "
        "posts. The same pages are already public on the Wayback Machine, at the links given "
        "on every entry. Nothing here was collected from anywhere else, and no address or "
        "message was gathered that the forum itself did not already publish. No credentials "
        "or working passwords are included.</p>",
        "<p>If you are one of the people in here and would like something removed, open an "
        "issue on the repository and it will be taken out.</p>",
        "<h2>Licence and copyright</h2>",
        "<p>The writing, artwork, game descriptions and everything else in <code>corpus/</code> "
        "remain the property of their original authors. They are reproduced here for "
        "historical preservation, research and engine compatibility work, exactly as the "
        "Wayback Machine reproduces them. The site generator in <code>site/</code> is MIT.</p>",
    ]
    with open(os.path.join(out, "about/index.html"), "w", encoding="utf-8") as f:
        f.write(page("About", "\n".join(body), depth=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", default=os.path.join(os.path.dirname(HERE), "corpus"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(HERE), "_site"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    build(a.corpus, a.out)


if __name__ == "__main__":
    main()
