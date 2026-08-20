# `_publications`

Publications collection. Each item is one Markdown file with YAML front matter.

Key front matter fields:

| Field     | Notes                                                        |
|-----------|--------------------------------------------------------------|
| `title`   | Paper title                                                   |
| `collection` | Must be `publications`                                    |
| `category`| One of `books` / `manuscripts` / `conferences` — groups the paper under the matching heading on `_pages/publications.html` (headings defined in `_config.yml` under `publication_category`) |
| `permalink` | Item URL                                                  |
| `excerpt` | Short description shown in list views                         |
| `date`    | Publication date                                              |
| `venue`   | Journal / venue                                               |
| `paperurl`| Link to the paper PDF (files in `/files/`)                    |
| `citation`| Recommended citation string                                   |

## Two ways to maintain this collection

**1. Hand-written Markdown entries** (like the current files) — fine for a one-off
addition.

**2. Generated from a TSV (bulk / recurring updates):** edit
`markdown_generator/data/publications.tsv` and rerun

```bash
python3 markdown_generator/scripts/publications.py markdown_generator/data/publications.tsv
```

BibTeX batch import is also supported via
`markdown_generator/scripts/pubsFromBib.py`.

Do **not** mix hand-written and script-generated entries for the same papers, or you
will get duplicates.