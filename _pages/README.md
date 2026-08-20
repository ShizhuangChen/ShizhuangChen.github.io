# `_pages`

Standalone pages and archive pages. Hand-edited Markdown/HTML files with YAML front
matter.

Two kinds of files:

- **Content pages** — `about.md`, `cv.md`, `404.md`, `terms.md`, `markdown.md`, ...
- **Archive pages** (`layout: archive`) — `publications.html`, `talks.html`,
  `teaching.html`, `portfolio.html`, `year-archive.html`, `category-archive.html`,
  `tag-archive.html`. These use Liquid to loop over a collection and render lists.

**Important:** `cv.md` is the source of truth for the CV page. `_data/cv.json` is
generated from it via `bash scripts/update_cv_json.sh` — do **not** edit `cv.json`
directly.