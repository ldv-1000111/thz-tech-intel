# THZ Tech Intel

A Sphinx documentation site with embedded reveal.js presentations,
hosted on Read the Docs.

## Live Site

- **Docs:** https://terahertz-technology-intelligence.readthedocs.io/en/latest/
- **Scoreboard slides:** https://terahertz-technology-intelligence.readthedocs.io/en/latest/slides/scoreboard.html

## Structure

```
├── .readthedocs.yaml          # RTD build config (runs both builders)
└── docs/
    ├── conf.py                # Sphinx config (html + revealjs)
    ├── requirements.txt       # Python dependencies
    ├── _static/
    │   └── custom.css         # Brand styles for reveal.js
    ├── index.rst              # Docs home
    ├── overview.rst           # Technology overview
    ├── competitive.rst        # Competitive analysis (Teradar/Arbe/Mobileye)
    └── slides/
        ├── index.rst          # Presentations index
        └── scoreboard.rst     # reveal.js scoreboard presentation
```

## What gets built on Read the Docs

| URL | Content |
|-----|---------|
| `/en/latest/` | Normal Sphinx/Furo docs |
| `/en/latest/competitive/` | Full competitive analysis |
| `/en/latest/slides/` | Presentations index |
| `/en/latest/slides/scoreboard.html` | reveal.js scoreboard |

## Local development

```bash
pip install -r docs/requirements.txt

# Build normal docs
sphinx-build -b html docs _build/html

# Build slides
sphinx-build -b revealjs docs _build/slides

# Open slides
open _build/slides/slides/scoreboard.html
```

## Adding more slides

Create a new `.rst` file under `docs/slides/` with a `.. revealjs-slide::` directive
at the top, then add it to `docs/slides/index.rst` toctree.

## Adding more analysis

Add `.rst` files to `docs/` and reference them in `docs/index.rst` toctree.

## Tech stack

- [Sphinx](https://www.sphinx-doc.org/) 7+
- [sphinx-revealjs](https://sphinx-revealjs.readthedocs.io/) 3.2.1
- [reveal.js](https://revealjs.com/) 5.2.1 (bundled)
- [Furo](https://pradyunsg.me/furo/) theme
- Hosted on [Read the Docs](https://readthedocs.org/)
