# `_data`

Site-wide data files consumed by Liquid templates. Everything here is hand-edited
**except** `cv.json`, which is a generated artifact.

| File              | Purpose                                                       |
|-------------------|---------------------------------------------------------------|
| `navigation.yml`  | Top navigation bar (`site.data.navigation`)                   |
| `ui-text.yml`     | Multilingual UI strings (includes a `zh` locale)              |
| `authors.yml`     | Author definitions for multi-author layouts                   |
| `cv.json`         | JSON Resume data rendered on `/cv-json/` (**generated, do not hand-edit**) |
| `comments/`       | Staticman comment storage                                     |

To regenerate `cv.json` after editing its source (`_pages/cv.md`):

```bash
bash scripts/update_cv_json.sh
```