# `_layouts`

Liquid page templates — the skeleton that wraps a page's content. Content types are
mapped to layouts via `defaults` in `_config.yml`:

| File                   | Used for                                                   |
|------------------------|------------------------------------------------------------|
| `default.html`         | Base layout                                                |
| `single.html`          | Posts, pages, teaching, publications, portfolio            |
| `archive.html`         | List pages that iterate over a collection                  |
| `talk.html`            | Talks                                                      |
| `cv-layout.html`       | CV page                                                    |
| `splash.html`          | Splash / landing pages                                     |
| `compress.html`        | HTML compression pipeline                                  |

Part of the **theme layer**; normally you don't edit these.