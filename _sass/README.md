# `_sass`

SCSS sources for the site theme, compiled to `assets/css/main.css` on build
(`sass.style: compressed` in `_config.yml`).

- `theme/`, `layout/`, `include/`, `vendor/` — Minimal Mistakes SCSS modules
- `_themes.scss` — theme variants (`default`, `air`, `sunrise`, `mint`, `dirt`,
  `contrast`)

Part of the **theme layer** — usually only touched for a site-wide look-and-feel
change. `assets/css/main.css` is a generated artifact; do not edit it directly.