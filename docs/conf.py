# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re
import datetime
import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
source_dir = os.path.join(os.path.dirname(__file__), '..', 'biosimulators_ibiosim')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# -- Project information -----------------------------------------------------
source_base_url = 'https://github.com/biosimulators/BioSimulators_iBioSim/blob/dev/'
project = 'BioSimulators-iBioSim'
copyright = '{}, BioSimulators Team'.format(datetime.datetime.now().year)
author = 'BioSimulators Team'

# The short X.Y version
filename = os.path.join(source_dir, '_version.py')
verstrline = open(filename, 'rt').read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
version = mo.group(1)

# The full version, including alpha/beta/rc tags
release = '.'.join(version.split('.')[0:3])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode',
    'sphinx.ext.napoleon',
    'sphinxprettysearchresults',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set 'language' from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

show_authors = False
pygments_style = 'sphinx'

# -- napoleon options -----------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- linkcode options -----------------------------------------------------


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    rel_filename = info['module'].replace('.', '/')
    if os.path.isfile(os.path.join(os.path.dirname(__file__), '..', rel_filename + '.py')):
        return source_base_url + '{}.py'.format(rel_filename)
    else:
        return source_base_url + '{}/__init__.py'.format(rel_filename)

# -- Options for HTML output -------------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_theme_options = {
    'github_user': 'biosimulators',
    'github_repo': 'BioSimulators_iBioSim',
    'github_banner': True,
    'github_button': True,
    'description': 'BioSimulators-compliant interface to iBioSim',
    'fixed_sidebar': True,
    'show_powered_by': False,
    'show_relbars': False,
    'extra_nav_links': {
        'BioSimulators': 'https://biosimulators.org',
        'runBioSimulations': 'https://run.biosimulations.org',
        'BioSimulations': 'https://biosimulations.org',
    }
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}
