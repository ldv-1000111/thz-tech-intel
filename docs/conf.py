project = "Terahertz Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"

extensions = ["sphinx_revealjs"]

# ── HTML (Furo) ──────────────────────────────────────────────
html_theme = "furo"
html_title = "THZ Tech Intel"

html_theme_options = {
    "sidebar_hide_name": False,
    "default_mode": "light",
    "footer_icons": [
        {
            "name": "Teradar",
            "url": "https://teradar.com",
            "html": "<span style='font-weight:700;font-size:0.8rem;letter-spacing:.05em;'>TERADAR</span>",
            "class": "",
        },
    ],
}

html_static_path = ["_static"]

# HPE CSS stack — load order matters
html_css_files = [
    "https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;600;700&family=Source+Code+Pro:wght@400;600&display=swap",
    "base.css",
    "layout.css",
    "components.css",
    "rtd-theme.css",
]

# ── reveal.js (keep Teradar dark slides) ─────────────────────
revealjs_theme = "black"
revealjs_script_conf = {
    "controls":             True,
    "progress":             True,
    "slideNumber":          True,
    "transition":           "fade",
    "backgroundTransition": "fade",
    "hash":                 True,
    "center":               True,
}
revealjs_css_files   = ["custom.css"]
revealjs_static_path = ["_static"]
