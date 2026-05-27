project = "Terahertz Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"

extensions = ["sphinx_revealjs"]

# ── HTML (Furo dark — matches thz-fmcw-dsp-complete-reference style) ──
html_theme = "furo"
html_title = "THZ Tech Intel"

html_theme_options = {
    "sidebar_hide_name": False,
    "default_mode": "dark",
}

html_static_path = ["_static"]

# Only load custom.css for reveal.js slides — no docs CSS overrides
html_css_files = [
    "hide-ads.css",
]

# ── reveal.js ─────────────────────────────────────────────────
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
