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
    "default_mode": "dark",
    "light_css_variables": {
        "color-background-primary":   "#080808",
        "color-background-secondary": "#0f0f0f",
        "color-foreground-primary":   "#cccccc",
        "color-brand-primary":        "#1BEA9A",
        "color-brand-content":        "#1BEA9A",
        "color-sidebar-background":   "#0f0f0f",
        "font-stack":                 "'Inter', sans-serif",
        "font-stack--monospace":      "'DM Mono', monospace",
    },
    "dark_css_variables": {
        "color-background-primary":   "#080808",
        "color-background-secondary": "#0f0f0f",
        "color-foreground-primary":   "#cccccc",
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
            "html": "<span style='font-family:Syne,sans-serif;font-weight:800;font-size:0.8rem;letter-spacing:.12em;color:#1BEA9A;text-transform:uppercase;'>TERADAR</span>",
            "class": "",
        },
    ],
}

html_static_path = ["_static"]

# Load order: base → layout → components → rtd-theme (Furo overrides last)
html_css_files = [
    "https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@600;700;800&family=Inter:wght@300;400;500&display=swap",
    "base.css",
    "layout.css",
    "components.css",
    "rtd-theme.css",
]

# ── reveal.js ───────────────────────────────────────────────
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
