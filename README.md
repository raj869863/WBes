# WBes — Wissen Baum Engineering Solutions · Internal HR Dashboard

Flask + Jinja2 + HTML5 + CSS3 + vanilla JavaScript. No frontend frameworks.

## Project structure

```
(project root = Air_ui)
├── app.py · config.py · requirements.txt · .env.example
├── routes/       # Flask blueprints — dashboard & candidates implemented;
│                 # calendar / interviews / jobs / activity are placeholders
├── services/     # service layer placeholders (future business logic)
├── providers/    # data provider placeholders (future Airtable / MySQL / mock)
├── integrations/ # external integration placeholders (future n8n / Google)
├── mock/         # mock data: candidates, interviews, activity (jobs placeholder)
├── templates/    # base.html + partials/ (sidebar, status_badge, ...) + page folders
├── static/
│   ├── css/      # tokens, main, shell, components (+ pages/ per-page styles)
│   ├── js/       # main.js (+ pages/ per-page scripts)
│   └── images/
└── tests/        # unittest smoke tests
```

Architecture (target): `routes → services → providers → Airtable/MySQL`,
with `services → integrations → n8n/Google`. Templates never touch data
sources directly.

## Design system (Phase 1A)

- **Locked brand palette:** `#FFB6A6` `#FFEBD3` `#9BCEC1` `#67A2C5` `#45A9A9` `#98E8DE`
  (no purple/violet/indigo, no additional accent hues).
- Neutrals (white / light gray / dark gray / near-black) for backgrounds, borders, text.
- All tints and shades are derived from the locked palette via `color-mix()`.
- Component classes: `.btn` (`--primary` / `--secondary` / `--ghost` / `--sm`), `.input` / `.select`,
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

Routes: `/` and `/dashboard` (Dashboard) · `/candidates` (+ `/candidates/<id>`
placeholder detail) · `/styleguide` (design-system reference).
Calendar, Interviews, Jobs/JDs and Activity pages are not built yet.

## Tests

```
python -m unittest discover -s tests -t .
```
