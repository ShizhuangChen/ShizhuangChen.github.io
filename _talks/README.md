# `_talks`

Talks collection. Each item is one Markdown file with YAML front matter.

Key front matter fields: `title`, `collection` (`talks`), `type`, `permalink`, `venue`,
`date`, `location`.

A talk's front matter is reused in several places: the list page (`_pages/talks.html`),
the single page, the CV (`_pages/cv.md`), and the talkmap (`talkmap.ipynb`).

## Two ways to maintain this collection

**1. Hand-written Markdown entries** — fine for a one-off addition.

**2. Generated from a TSV (bulk / recurring updates):** edit
`markdown_generator/data/talks.tsv` and rerun

```bash
python3 markdown_generator/scripts/talks.py markdown_generator/data/talks.tsv
```

When `_talks/` changes, the CI workflow `.github/workflows/scrape_talks.yml`
automatically reruns the talkmap notebook and commits the update.