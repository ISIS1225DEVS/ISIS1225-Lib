# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# basic project information
project = "DISClib"
copyright = "2023, Uniandes, DISC, ISIS-1225 Devs"
author = "ISIS1225 Devs DISC"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions to use
# install them with: pip install...
extensions = [
    "sphinx.ext.autodoc",
    # "sphinx.ext.autodoc.typehints",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "autoapi.extension",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx_copybutton",
    "sphinx_favicon",
    "sphinx_gitstamp",
    "sphinx-prompt",
    "myst_parser",
    # "docxsphinx",
    "nbsphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# internationalization options
locale_dirs = ["locale/"]
gettext_compact = False

# autoapi configuration
autoapi_dirs = [
    "../DISClib/",
]

# myst_parser configuration
source_suffix = {
    ".rst": "restructuredtext",
    # ".txt": "markdown",
    ".md": "markdown",
}

# myst extensions to enable
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


# favicon configuration
favicons = [
   {
      "sizes": "16x16",
      "href": "https://secure.example.com/favicon/favicon-16x16.png",
   },
   {
      "sizes": "32x32",
      "href": "https://secure.example.com/favicon/favicon-32x32.png",
   },
   {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "apple-touch-icon-180x180.png",  # use a local file in _static
   },
]

# gitstamp configuration
# Date format for git timestamps
gitstamp_fmt = "%Y-%m-%d %H:%M:%S %z"

# default role for `sphinx.ext.intersphinx`
language = "es"

# docxsphinx configuration
# "docx_template" need *.docx or *.dotx template file name. default is None.
# docx_template = "template.docx"

# -- Options for HTML output -------------------------------------------------
# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   "da", "de", "en", "es", "fi", "fr", "hu", "it", "ja"
#   "nl", "no", "pt", "ro", "ru", "sv", "tr", "zh"
#
html_search_language = "en"

# A dictionary with options for the search language support, empty by default.
# "ja" uses this config value.
# "zh" user can custom change `jieba` dictionary path.
#
html_search_options = {"type": "default"}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
html_search_scorer = "scorer.js"


# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# prefered theme
html_theme = "renku"
# html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"

html_static_path = ["_static"]
