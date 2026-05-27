project = "Terahertz Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"

extensions = ["sphinx_revealjs"]

# ── HTML — Furo with HPE style override (Option A from HOWTO) ──
html_theme = "furo"
html_title = "THZ Tech Intel"

html_theme_options = {
    "sidebar_hide_name": False,
    "default_mode": "light",
}

html_static_path  = ["_static"]
templates_path    = ["_templates"]

# Option A: base + components + rtd-theme only (no layout.css)
html_css_files = [
    "css/base.css",
    "css/components.css",
    "css/rtd-theme.css",
]

# ── reveal.js (slides keep Teradar dark theme) ───────────────
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
