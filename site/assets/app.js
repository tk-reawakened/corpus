/* TK Corpus - search.
 *
 * The index is one MiniSearch index over every post and every page in the
 * corpus, built at publish time by site/build-index.mjs. It is loaded once,
 * on demand, when the visitor actually searches.
 */
(function () {
  "use strict";

  var input = document.getElementById("qq");
  var results = document.getElementById("results");
  var stat = document.getElementById("stat");
  var kindSel = document.getElementById("kind");
  if (!input || !results) return;

  var ms = null;
  var loading = null;

  var FIELDS = ["text", "title", "author"];
  var STORE_FIELDS = ["path", "pid", "title", "kind", "site", "author", "ts", "excerpt"];

  function loadIndex() {
    if (ms) return Promise.resolve(ms);
    if (loading) return loading;
    stat.textContent = "loading the index…";
    loading = fetch("index.json")
      .then(function (r) {
        if (!r.ok) throw new Error("index " + r.status);
        return r.text();
      })
      .then(function (text) {
        var MiniSearch = window.MiniSearch;
        ms = MiniSearch.loadJSON(text, { fields: FIELDS, storeFields: STORE_FIELDS });
        stat.textContent = "";
        return ms;
      })
      .catch(function (err) {
        stat.textContent = "the search index could not be loaded (" + err.message + ")";
        throw err;
      });
    return loading;
  }

  function entryUrl(path, pid) {
    var u = "e/" + path.replace(/\.md$/, ".html");
    return pid ? u + "#p-" + encodeURIComponent(pid) : u;
  }

  function excerpt(text, terms) {
    var t = (text || "").replace(/\s+/g, " ").trim();
    if (t.length > 240) {
      var low = t.toLowerCase();
      var at = -1;
      for (var i = 0; i < terms.length && at < 0; i++) {
        at = low.indexOf(terms[i].toLowerCase());
      }
      var start = at > 60 ? at - 60 : 0;
      t = (start ? "…" : "") + t.slice(start, start + 240) + (t.length > start + 240 ? "…" : "");
    }
    return t;
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function highlight(text, terms) {
    var out = escapeHtml(text);
    terms.forEach(function (term) {
      if (term.length < 2) return;
      var re = new RegExp("(" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return out;
  }

  function run(q) {
    results.innerHTML = "";
    if (!q) {
      stat.textContent = ms ? stat.dataset.count || "" : "";
      return;
    }
    var terms = q.split(/\s+/).filter(Boolean);
    loadIndex()
      .then(function (index) {
        var kind = kindSel ? kindSel.value : "";
        var opts = { prefix: true, fuzzy: 0.1, boost: { title: 3, author: 2 }, combineWith: "AND" };
        if (kind) opts.filter = function (r) { return r.kind === kind; };
        var hits = index.search(q, opts);
        if (!hits.length) {          // nothing with every term: fall back to any of them
          opts.combineWith = "OR";
          hits = index.search(q, opts);
        }
        stat.textContent = hits.length + " hit" + (hits.length === 1 ? "" : "s");
        if (!hits.length) {
          results.innerHTML = '<p class="empty">Nothing found.</p>';
          return;
        }
        results.innerHTML = hits.slice(0, 200).map(function (h) {
          var m = [];
          if (h.author) m.push(escapeHtml(h.author));
          if (h.ts) m.push(escapeHtml(h.ts));
          if (h.kind) m.push(escapeHtml(h.kind));
          if (h.site) m.push(escapeHtml(h.site));
          return '<div class="hit"><a href="' + escapeHtml(entryUrl(h.path, h.pid)) + '">' +
            highlight(h.title || "(untitled)", terms) + "</a> " +
            '<span class="m">' + m.join(" · ") + "</span>" +
            '<span class="x">' + highlight(h.excerpt || "", terms) + "</span></div>";
        }).join("");
        if (hits.length > 200) {
          results.innerHTML += '<p class="empty">Showing the first 200 of ' + hits.length + ' hits.</p>';
        }
      })
      .catch(function () {});
  }

  function currentQuery() {
    return new URLSearchParams(window.location.search).get("q") || "";
  }

  input.value = currentQuery();

  var timer = null;
  input.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(function () { run(input.value.trim()); }, 250);
  });
  if (kindSel) {
    kindSel.addEventListener("change", function () { run(input.value.trim()); });
  }
  var form = document.getElementById("q");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var u = new URL(window.location.href);
      u.searchParams.set("q", input.value.trim());
      if (kindSel && kindSel.value) u.searchParams.set("kind", kindSel.value);
      window.history.replaceState({}, "", u);
      run(input.value.trim());
    });
  }
  if (input.value) run(input.value.trim());
})();
