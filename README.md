# WBes — Wissen Baum Engineering Solutions · Internal HR Dashboard

Flask + Jinja2 + HTML5 + CSS3 + vanilla JavaScript. No frontend frameworks.

## Project structure

```
WBes/
├── app.py                # Flask entry point (GET / and GET /styleguide)
├── requirements.txt
├── templates/
│   ├── base.html         # Base layout (loads tokens → base → components CSS)
│   ├── index.html        # Phase 0 smoke-test page
│   └── styleguide.html   # Phase 1A design-system reference page
└── static/
    ├── css/
    │   ├── tokens.css      # Design tokens (locked palette, spacing, radius, shadows, motion)
    │   ├── base.css        # Reset, document defaults, typography, reduced-motion
    │   ├── components.css  # Reusable components (buttons, inputs, cards, badges, tables, ...)
    │   └── styleguide.css  # Demo-only helpers for /styleguide (not part of the system)
    └── js/
        └── main.js         # Minimal Phase 0 script
```

## Design system (Phase 1A)

- **Locked brand palette:** `#FFB6A6` `#FFEBD3` `#9BCEC1` `#67A2C5` `#45A9A9` `#98E8DE`
  (no purple/violet/indigo, no additional accent hues).
- Neutrals (white / light gray / dark gray / near-black) for backgrounds, borders, text.
- All tints and shades are derived from the locked palette via `color-mix()`.
- Component classes: `.btn` (`--primary` / `--secondary` / `--ghost`), `.input` / `.select`,
  `.card` (`--compact` / `--interactive`), `.badge` (`--success` / `--info` / `--warning` /
  `--attention` / `--neutral`), `.table` + `.table-container`, `.filter-bar` / `.filter-field`,
  `a`, `.icon-btn`, `.empty-state`.
- Typography: `.page-title`, `.section-title`, `.card-title`, `.text-body`,
  `.text-secondary`, `.text-muted`, `.text-small`, `.form-label`.
- Motion: subtle transitions only; `prefers-reduced-motion` is respected.

## Running

```
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5000
```

Routes: `/` (Dashboard) · `/candidates` (+ `/candidates/<id>` placeholder detail) · `/styleguide` (design-system reference).
