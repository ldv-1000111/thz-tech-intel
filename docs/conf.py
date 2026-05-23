project = "Teradar Technology Intelligence"
copyright = "2025, Teradar"
author = "Teradar"
release = "1.0"

extensions = ["sphinx_revealjs"]

html_theme = "furo"
html_title = "Teradar Technology Intelligence"

html_theme_options = {
    "sidebar_hide_name": False,
}

# reveal.js global settings
revealjs_theme = "black"
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "slideNumber": True,
    "transition": "slide",
    "hash": True,
}
revealjs_css_files = ["custom.css"]
revealjs_static_path = ["_static"]
