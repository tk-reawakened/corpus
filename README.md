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

This is a historical archive of a public forum, and it contains what that forum contained:
the handles people posted under, their email addresses where they posted them, their
member-profile details (join date, occupation, interests, age band, location) and their
posts. **The same pages are already public on the Wayback Machine**, at the link given on
every entry — nothing here was collected from anywhere else, and no message or address
was gathered that the forum itself did not already publish. No working credentials or
passwords are included.

One exception was made, because it was a re-identification risk rather than archive
content: **two phone numbers** that a member posted in a forum signature in 2003 are
redacted in the corpus, and the marker `[redacted: phone number]` is left in their place
so the loss is visible rather than silent. Search for `redacted` to see every redaction.

If you are one of the people in here and would like something removed, open an issue on
this repository and it will be taken out.

## Licence and copyright

The writing, artwork, game descriptions, help text and everything else in `corpus/` remain
the property of their original authors. They are reproduced here for historical
preservation, research and engine-compatibility work, exactly as the Wayback Machine
reproduces them. This includes the official RPG Toolkit v2 User's Guide and the TK3 help
system, which are part of the archive and the most useful reference material in it.

The site generator in `site/` is MIT licensed.

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
