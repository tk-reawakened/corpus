# tk-corpus schema

Every file is YAML frontmatter + Markdown body. Same envelope for every kind, so one query layer works across all of it. Built by `tools/build-tk-corpus.py`; raw captures are never modified.

## Common envelope (all kinds)

```yaml
kind: forum-thread | game | file | doc | blog | member | review | code | page | download   # (discord-month lives only in tk-corpus-private/)
id: "<site-or-board>/<native id>"        # identity; filenames end with it
site: "toolkitzone.com"
title: ""
original_url: ""                          # the canonical live URL
written: ISO | null                       # when authored (NOT when captured)
date_confidence: exact | day | year | unknown
captured: ["2005..."]                     # Wayback timestamps of the captures used
source_captures: [{path, captured, sha256, wayback_url}]
author: ""                                # creator / thread starter
repliers: []                              # everyone else who posted or commented
authors: []                               # everyone, in order of appearance
complete: true | false | null
gaps: []                                  # {reason: never-captured | not-fetched | capture-failed | quarantined | may-continue}
links: [{url, status, local}]             # status: captured | not-fetched | never-captured | capture-failed | external
duplicate_of: "<site>/<id>"              # the same page captured under another URL
converter_version: ""
```

Body: `# title`, the content as Markdown, then comments/replies as `### author · date · #id` blocks (the same shape as forum posts), so "everything by X" is one grep for every kind.

## Redaction

The published corpus is de-identified. These are removed from every file, with a
`(redacted: …)` marker left in place so the loss is visible rather than silent:

| Removed | Marker |
|---|---|
| Real names (the `Name` field of a profile, the `Real Name` field of a member site, and any later mention of them) | `(redacted: name)` |
| Email addresses | `(redacted: email)` |
| Phone numbers | `(redacted: phone number)` |
| Street addresses | `(redacted: address)` |
| The `f_location` field | `(redacted: location)` |
| The `f_age` field | dropped entirely |

The **handles stay** — `author`, `authors`, `repliers` and `handle` are how these people
knew each other, and they are the community. The rules live in `tools/redact.py` and the
list of names in `data/real-names.txt`; `tools/verify-redaction.py` checks a built corpus
against them and is the gate before publishing.

## Per-kind fields (added to the envelope)

| kind | sources | extra frontmatter | body |
|---|---|---|---|
| forum-thread (done) | 6 forum skins | board, forum, thread_id, posts_present, pages_total, posts_per_page | posts |
| game | toolkitzone `games.php`, mysticsoftware `games.php`, rpgtoolkit.net games | led_by, members, website, status, last_updated, toolkit_era, downloads[], screenshots[] | description, then comments |
| file | toolkitzone `fileman.php` / `files.php` | file_id, category, uploader, download_count, artifact (local zip path + sha256) | description |
| doc | toolkitzone `library.php`, mysticsoftware articles/help/tutorials, tk3 help | doc_id, section | article text, then comments |
| blog | toolkitzone `blog.php` | blog_author, entry_id | entry, then comments |
| member | toolkitzone `community.php?user`, rpgtoolkit.net `member/<name>`, acforum profiles | handle, joined, location, titles/roles, real_name when public | profile text |
| review / code | mysticsoftware `reviews.php`, `code.php` | reviewer, game, rating, resource_type | text |
| page | everything else (static pages) | none | cleaned page text |
| download | every captured binary (zip, exe, dll, mid, pdf, …) | f_size_bytes, f_path | size, capture date, archive path, Wayback link |

`download` is the artifact itself, where `file`/`game` are a site's database
entry for it: `tk-corpus/downloads/aljo.afraid.org/littlemanzip--<hash>.md`
points at `wayback/aljo.afraid.org/games/littleman/LittleMan.zip`.

## How the article is found (the page kinds)

`tools/extract-article.py` pulls the article out of a 1997-2010 page before it
is written down. It is generic - no per-site rules - and deterministic:

1. The HTML becomes a small tree that tracks, per block, the text inside links
   and the text outside them.
2. Blocks that carry no prose next to a block that does are site furniture
   (nav bars, sidebars, footers) and are dropped; blocks whose links are all
   navigation words are dropped; blocks with download links are kept, because
   on a game page the download table *is* the article.
3. What is left is rendered to Markdown, then the line-level clean-up drops
   decorative images, icon rows, breadcrumbs, login widgets, "no news created"
   empty states and legal footers.
4. The title is the page's own heading, never the site's `<title>` (that is the
   site name on most of these pages); the breadcrumb is kept aside because for
   a member or a game it carries the name.

Fields observed in samples: toolkitzone games (Led By, Other Members, Web Site, Last Updated, Status, Description); library/blog (title, "By X", date, then `Comments (N)` with author + timestamp each); rpgtoolkit.net member (handle, roles, join year, name, age, country, occupation, website). Not yet inspected in detail: toolkitzone `files.php`/`community.php` field blocks.

## Standardization rules

1. Site chrome is removed by the generic extractor in `tools/extract-article.py` (a tree walk, not a per-site marker list), so a new host needs no new rules; label/value pairs become frontmatter keys (`Led By` → `led_by`) and their values keep the original text.
2. Dates are normalized per format (`June 6, 2005, 9:26 am`, `2.43pm, October 27th, 2009`, etc.); unparseable ones stay raw with `date_confidence: unknown`. Impossible times (acforum shows `26:18`) keep the raw string and are flagged, never guessed.
3. Identity is the site-native id; same thing on several sites is linked later via `duplicate_of` / the games index, not merged here.
4. Idempotent: same captures in, byte-identical files out.
5. The same page is often captured under many URLs (session ids, `page=`
   parameters). Those entities are kept (the URL is evidence) but carry
   `duplicate_of`, so a reader can follow the one that matters.

## Public vs private

`tk-corpus/` is built only from publicly available sources (Wayback captures) and is the part that can be released. Discord is not public: it is converted into `tk-corpus-private/` (`tools/build-tk-discord.py`), never into `tk-corpus/`, and the public search db and people pages are built without it. `build-tk-index.py --private` builds a combined index inside `tk-corpus-private/_index/` only.
