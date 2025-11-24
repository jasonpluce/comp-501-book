"""
Sphinx configuration file.

Copyright (C) 2025 Nicholas M. Synovic.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "COMP 501 Book"
copyright = "2025, Loyola University Chicago Computer Science Department"  # noqa: A001
author = "Loyola University Chicago Computer Science Department"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton"
]

templates_path = ["_templates"]
exclude_patterns = []

# sphinx.ext.todo options
todo_include_todos = True

# Sphinx auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Sphinx BibTex settings
bibtex_bibfiles = ["refs.bib"]
bibtex_default_style = "unsrt"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Sphinx Book Theme Settings
html_theme_options = {
    "repository_url": "https://github.com/NicholasSynovic/comp-501-book",
    "use_repository_button": True,
    "show_navbar_depth": 0,
    "max_navbar_depth": 2,
    "collapse_navbar": False,
    "use_sidenotes": True,
}
html_title = project
# html_logo = "_static/images/headshot.png"
# html_favicon = "_static/favicon.png"
