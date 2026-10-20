// Build the client-side search index from the documents the site builder emits.
//
//   node build-index.mjs <documents.json> <out-index.json>
//
// One MiniSearch index over every post and every page in the corpus. The
// browser loads it on demand, when someone actually searches.
import fs from "node:fs";
import MiniSearch from "minisearch";

const [, , docsPath, outPath] = process.argv;
if (!docsPath || !outPath) {
  console.error("usage: node build-index.mjs <documents.json> <out-index.json>");
  process.exit(1);
}

const docs = JSON.parse(fs.readFileSync(docsPath, "utf8"));
console.log("documents: %d", docs.length);

const excerpt = (text, n = 260) => {
  const t = (text || "").replace(/\s+/g, " ").trim();
  return t.length > n ? t.slice(0, n) + "…" : t;
};

const index = new MiniSearch({
  fields: ["text", "title", "author"],
  storeFields: ["path", "pid", "title", "kind", "site", "author", "ts", "excerpt"],
  searchOptions: { boost: { title: 3, author: 2 }, prefix: true, fuzzy: 0.2 }
});

index.addAll(
  docs.map((d) => ({
    id: d.id,
    text: d.text,
    title: d.title,
    author: d.author,
    path: d.path,
    pid: d.pid || null,
    kind: d.kind,
    site: d.site,
    ts: d.ts,
    excerpt: excerpt(d.text)
  }))
);

const json = JSON.stringify(index.toJSON());
fs.writeFileSync(outPath, json);
console.log(`index bytes: ${(json.length / 1e6).toFixed(1)} MB`);
