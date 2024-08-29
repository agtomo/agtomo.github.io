# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Akshay Gaikwad'
copyright = '2024, Akshay Gaikwad'
author = 'Akshay Gaikwad'
html_title = 'My research webpage'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


html_sidebars = {
    '**': [
        'about.html',
        # 'language.html',
        'navigation.html',
        # 'relations.html',
    ]
}

html_theme_options = {
    'fixed_sidebar': True,
    'show_powered_by': False,
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme = 'classic'
# html_theme = 'sphinxdoc'
# html_theme = 'scrolls'
# html_theme = 'agogo'
# html_theme = 'traditional'
# html_theme = 'nature'
# html_theme = 'haiku'
# html_theme = 'pyramid'
# html_theme = 'bizstyle'
# html_theme = 'epub'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_material'


# Customize the theme options (if needed)
# html_theme_options = {
#     'search_bar': False,  # This ensures the search box is not added automatically
# }


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# intl
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional