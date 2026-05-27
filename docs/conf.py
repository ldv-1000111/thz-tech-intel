project = "Terahertz Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"
version = "1.0"

extensions = ["sphinx_revealjs"]

# ── Custom HPE theme ──────────────────────────────────────────
html_theme      = "hpe"
html_theme_path = ["_themes"]
html_title      = "THZ Tech Intel"

html_theme_options = {}

html_static_path = ["_static"]

# CSS served from _static (copied there at build time via theme)
html_css_files = []

# last updated date in footer
html_last_updated_fmt = "%B %Y"

# ── reveal.js (slides) ───────────────────────────────────────
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
