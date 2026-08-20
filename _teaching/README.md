# `_teaching`

Teaching experience collection. One file per course / experience, **hand-written**.

Front matter: `title`, `collection` (`teaching`), `type` (e.g. `"Undergraduate
course"`), `venue`, `date`, `location`. Items are rendered with `layout: single`
(defaults from `_config.yml`) and appear on `_pages/teaching.html`.

Entries also feed the Teaching section of `/cv/`: when you add or change a teaching
item, run

```bash
bash scripts/update_cv_json.sh
```

to regenerate `_data/cv.json`.