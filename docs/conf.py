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
    "light_css_variables": {
        # force dark even if system is light
        "color-background-primary":   "#080808",
        "color-background-secondary": "#0f0f0f",
        "color-foreground-primary":   "#f0f0f0",
        "color-brand-primary":        "#1BEA9A",
        "color-brand-content":        "#1BEA9A",
        "color-sidebar-background":   "#0f0f0f",
        "font-stack":                 "'Inter', sans-serif",
        "font-stack--monospace":      "'DM Mono', monospace",
    },
    "dark_css_variables": {
        "color-background-primary":   "#080808",
        "color-background-secondary": "#0f0f0f",
        "color-foreground-primary":   "#f0f0f0",
        "color-brand-primary":        "#1BEA9A",
        "color-brand-content":        "#1BEA9A",
        "color-sidebar-background":   "#0f0f0f",
        "font-stack":                 "'Inter', sans-serif",
        "font-stack--monospace":      "'DM Mono', monospace",
    },
    "footer_icons": [
        {
            "name": "Teradar",
            "url": "https://teradar.com",
            "html": "<strong style='color:#1BEA9A;font-family:Syne,sans-serif;font-weight:800;letter-spacing:.1em;'>TERADAR</strong>",
            "class": "",
        },
    ],
}

html_static_path = ["_static"]
html_css_files = [
    "https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@600;700;800&family=Inter:wght@300;400;500&display=swap",
    "teradar-docs.css",
]

# ── reveal.js ───────────────────────────────────────────────
revealjs_theme = "black"
revealjs_script_conf = {
    "controls":     True,
    "progress":     True,
    "slideNumber":  True,
    "transition":   "fade",
    "hash":         True,
    "center":       True,
    "backgroundTransition": "fade",
}
revealjs_css_files   = ["custom.css"]
revealjs_static_path = ["_static"]
