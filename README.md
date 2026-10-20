# TK Corpus — the RPG Toolkit community archive

RPG Toolkit was a game-making tool for Windows in the late 1990s and 2000s. It had a
community: **toolkitzone.com**, **mysticsoftware.net**, **rpgtoolkit.net**,
**rpgtoolkit.com**, and the Aljo Productions site among them. Most of that community is
gone. This repository holds what the Wayback Machine still has of it, written out as
Markdown so it can be read and searched instead of being a pile of captured HTML.

**Browse it:** <https://tk-reawakened.github.io/corpus/>

```
corpus/            the archive itself: one Markdown file per page, thread, profile or download
site/              the generator that turns corpus/ into the website
SCHEMA.md          what a corpus file looks like
```

## What is in it

| Kind | Entries | What it is |
|---|---:|---|
| `forum-thread` | 3,653 | Every captured thread with all its replies in order, by post, with authors and dates |
| `page` | 8,120 | Everything else that was a page: home pages, news entries, personal member sites |
| `member` | 937 | Member profiles: handle, join date, rank, occupation, interests, bio |
| `file` | 829 | The toolkitzone.com file database: plugins, method packs, resources |
| `game` | 537 | Game profiles from toolkitzone.com and mysticsoftware.net |
| `download` | 446 | The binaries the archive recovered, with size, hash and provenance |
| `blog` | 399 | Community blogs |
| `doc` | 280 | News, tutorials, articles and help documents |
| `code` | 254 | RPG Code submissions: menus, methods, plugins |
| `review` | 125 | Game reviews from mysticsoftware.net |

Roughly 15,600 files, 53 MB of Markdown, 35,000 searchable posts and pages.

The **games themselves** are not here — they are in
[`tk-reawakened/ludotheque`](https://github.com/tk-reawakened/ludotheque). The **engine
rebuild** this archive supports is in
[`tk-reawakened/rpgtoolkit-reawakened`](https://github.com/tk-reawakened/rpgtoolkit-reawakened).

## How it was made

**Everything here was captured by the Internet Archive's Wayback Machine, and every page is
still publicly readable there** — the same content, at the link given on every entry. Nothing
was gathered from private sources, from the forums' own servers, or from anybody directly.
This is a copy of material that was already available to anyone, reorganised so it can be
read and searched instead of being a pile of captured HTML.

1. The Wayback Machine's CDX index was read for every host, giving the full list of URLs
   that were ever captured.
2. Each URL was fetched and stored byte-for-byte, with a manifest recording the capture
   timestamp, the SHA-256 of every file and the source URL.
3. A converter walks the captures and writes one Markdown file per page, thread, profile
   or download, with the page's metadata in YAML frontmatter. The converter pulls the
   *article* out of each page: these are 1997-2010 pages, and rendering them whole keeps
   the navigation, the login widget, the sidebars and the footer, and loses the page's own
   heading in the site's `<title>`.
4. `site/build.py` turns the Markdown into the website.

Every file carries its own provenance: the original URL, the Wayback timestamp, the
SHA-256 of the capture, and a link back to the archived page. Nothing here was written
by hand; the only authored parts are the site generator and this README.

## Personal data

This is a historical archive of a public forum. **The handles stay** — "Xorlak", "Zorlac",
"Vampz" are how these people knew each other, and they are the community. What does not
stay is the material that points at somebody outside the forum:

| Removed | How |
|---|---|
| Real names | The names people published in their profile's *Name* field, or as *Real Name* on their own site. Removed from the profile field and from every later mention of them in a post. |
| Email addresses | Everywhere, in every file. |
| Phone numbers | Everywhere, in the formats these forums used. |
| Street addresses | Everywhere. |
| Location | The member profile's *Location* field (`f_location`) is blanked. |
| Age | The member profile's age band (`f_age`) is dropped entirely. |

Each removal leaves a marker in place — `(redacted: email)`, `(redacted: name)` — so the
loss is visible rather than silent, and so you can tell a redaction from a gap in the
capture. Search for `redacted` to see every one of them.

The rules live in the archive's own build — `tools/redact.py` and `data/real-names.txt` —
so they can be reviewed and extended without touching this repository.

**This was an automated pass, and it is not a guarantee.** The redaction is pattern
matching, not judgement: it removes the categories of self-identifying information these
profiles and posts actually use, and it caught most of them. But a real name that only
ever appeared inside a post, a phone number written in an unusual way, or a personal
detail told as a story would not be recognised as what it is. **Some of these pages did
contain self-identifying information, and some of it is still here.**

So the honest description of this repository is *a de-identified copy of pages that were
already public*, not a guaranteed-anonymised archive. The original pages are still on the
Wayback Machine, linked from every entry, and nothing here was collected from anywhere
else — no message was gathered that the forum itself did not publish.

If you are one of the people in here and would like something removed, open an issue on
this repository and it will be taken out.

## Please do not crawl this

This is a research copy, not a mirror to index or copy in bulk. The canonical copies of
these pages are on the Wayback Machine, and every entry here links to the one it came
from. The site asks search engines not to index it and asks well-behaved crawlers to stay
away (`robots.txt`, and a `noindex` tag on every page) — that is a request, not a lock, so
the real courtesy is simply not to take the whole thing.

If you are researching this material and want the corpus, ask: open an issue on this
repository and it will be made available to you directly.

## Licence and copyright

The writing, artwork, game descriptions, help text and everything else in `corpus/` remain
the property of their original authors. They are reproduced here for historical
preservation, research and engine-compatibility work, exactly as the Wayback Machine
reproduces them. This includes the official RPG Toolkit v2 User's Guide and the TK3 help
system, which are part of the archive and the most useful reference material in it.

The site generator in `site/` is MIT licensed (see `site/LICENSE`). The corpus itself is
not covered by a licence: the material in `corpus/` belongs to its original authors, as
described above.

## Building the site

```bash
pip install pyyaml
npm install                       # for the search index (MiniSearch)
python3 site/build.py             # -> _site/
node site/build-index.mjs _site/search/documents.json _site/search/index.json
```

Then serve `_site/` with any static server, for example `python3 -m http.server -d _site`.
The GitHub Pages workflow does exactly this on every push to `main`.

## The schema

See [SCHEMA.md](SCHEMA.md). Every file is YAML frontmatter plus a Markdown body, the same
envelope for every kind, so one query layer works across all of it. A file can also be
read on its own: it is plain Markdown, and the frontmatter says where it came from.
