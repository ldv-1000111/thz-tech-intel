project = "Terahertz Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"

extensions = ["sphinx_revealjs"]

# ── HTML — sphinx_rtd_theme (what HPE HOWTO was written for) ──
html_theme = "sphinx_rtd_theme"
html_title = "THZ Tech Intel"

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

html_static_path  = ["_static"]
templates_path    = ["_templates"]

# Option A per HOWTO: base + components + rtd-theme (no layout.css)
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
