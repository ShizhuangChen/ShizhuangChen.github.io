# Markdown Generator

Batch generator for the site's content: turns structured tables (TSV) or
BibTeX into Jekyll content Markdown (`_publications/`, `_talks/`). It follows
a **source -> artifact** workflow — **edit the table, re-run the script, and
commit the regenerated Markdown; never hand-edit the generated `.md` files**
(they are overwritten on the next run).

## Layout

| Directory | Contents |
|---|---|
| `data/` | Source tables: `publications.tsv` (papers), `talks.tsv` (talks), `*.bib` (for BibTeX import) |
| `scripts/` | Command-line generators: `publications.py`, `talks.py`, `pubsFromBib.py` |
| `notebooks/` | Interactive Jupyter counterparts of the scripts (`publications.ipynb`, ...), handy for debugging/demos |

## Publications: `data/publications.tsv`

Edit the table, **one paper per row**. The header is fixed (fields separated
by **TAB**, not spaces):

```
pub_date	title	venue	excerpt	citation	url_slug	paper_url	slides_url	category
```

| Field | Description |
|---|---|
| `pub_date` | Date, format `YYYY-MM-DD` (required) |
| `title`, `venue`, `citation` | Paper title, journal/conference, recommended citation text (required) |
| `excerpt` | Abstract / short description; may be blank |
| `url_slug` | Becomes the file base name and the permalink tail; letters, digits, hyphens only (required). Generates `YYYY-MM-DD-<url_slug>.md` with page link `/publication/YYYY-MM-DD-<url_slug>` |
| `paper_url`, `slides_url` | Download links for the paper / slides; may be blank |
| `category` | One of `books` / `manuscripts` / `conferences`. If the header lacks this column (old 8-column layout), defaults to `manuscripts` |

**Generate** (run from the `markdown_generator/` folder):

```bash
cd markdown_generator
python3 scripts/publications.py data/publications.tsv
```

Output lands in the repo's `_publications/`, one `.md` per data row. Review,
then `git add` and commit.

## Talks: `data/talks.tsv`

Same idea; header (TAB-separated):

```
title	type	url_slug	venue	date	location	talk_url	description
```

- `title`, `url_slug`, `date` (`YYYY-MM-DD`) are required; `type` defaults to
  `Talk`.
- Generates `YYYY-MM-DD-<url_slug>.md` with page link
  `/talks/YYYY-MM-DD-<url_slug>`.

**Generate**:

```bash
python3 scripts/talks.py data/talks.tsv
```

Output lands in the repo's `_talks/`.

## BibTeX bulk import (optional)

1. Put `pubs.bib` (journal articles) and `proceedings.bib` (conference
   papers) into `markdown_generator/data/` (the `notebooks/OrcidToBib.ipynb`
   notebook can export these from ORCID).
2. To change source files, venue fields, or citation prefixes, adjust the
   `publist` dictionary at the top of `scripts/pubsFromBib.py`.
3. Generate (requires `pybtex`: `pip install pybtex`):

```bash
python3 scripts/pubsFromBib.py
```

Output lands in `_publications/`.

## Notes

- **Never hand-edit artifacts**: `.md` files under `_publications/` and
  `_talks/` are script output; manual edits get overwritten on the next run.
- **Scripts only write, never delete**: removing a row from a table does not
  remove the corresponding `.md` — clean it up with `git rm` yourself.
- **Hand-writing a single entry is allowed**: create
  `_publications/YYYY-MM-DD-xxx.md` directly, but don't mix it with
  batch-generated content (risk of duplicates).
- **Front matter must be complete**: CI builds with
  `bundle exec jekyll build --strict_front_matter`; missing fields fail the
  build.
- Prefer the `.py` scripts under `scripts/` for batch generation (zero
  dependencies, CI-friendly); the `.ipynb` notebooks under `notebooks/` are
  for interactive debugging.
- The sample rows in the tables ("Paper Title Number 1", ...) are placeholder
  content to replace with your real data.
