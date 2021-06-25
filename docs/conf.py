#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import oci
import sys
import pkg_resources
import sphinx_rtd_theme

from sphinx.domains.python import PythonDomain

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "autodocsumm",
    "sphinx.ext.autosectionlabel"
]

# Automatically generate stub pages for the .. autosummary:: directive when combined with :toctree:
autosummary_generate = True

# Add contents table
autodoc_default_options = {
    "autosummary": True
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "oci"
copyright = "2016, {}, Oracle".format(datetime.datetime.now().year)
author = "Oracle"

try:
    release = pkg_resources.get_distribution("oci").version
except pkg_resources.DistributionNotFound:
    print("To build the documentation, The distribution information of oci")
    print("Has to be available.  Either install the package into your")
    print("development environment or run 'setup.py develop' to setup the")
    print("metadata.  A virtualenv is recommended!")
    sys.exit(1)
del pkg_resources
version = ".".join(release.split(".")[:3])

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'oci vCURRENT_VER'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = html_title

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

html_search_language = language

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "ocidoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "oci.tex", "oci Documentation",
     "Oracle", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "oci", "oci Documentation",
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "oci", "oci Documentation",
     author, "oci", "One line description of project.",
     "Miscellaneous"),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


class PatchedPythonDomain(PythonDomain):
    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if 'refspecific' in node and fromdocname.startswith('api/'):
            # This for api/* and defined tags. These have a data type of dict(str, dict(str, object)) but if
            # Sphinx auto-linking tries to link "object" to the "object" property in CreateMultipartUploadDetails
            # (which is incorrect).
            #
            # This prevents any non-explicit link (e.g. just plain "object") from being linked across, but if I was
            # explicit like "oci.object_storage.models.CreateMultipartUploadDetails.object" that **should** still
            # produce a link
            if node['reftarget'] == 'object' and not node['refexplicit']:
                del node['refspecific']
        return super(PatchedPythonDomain, self).resolve_xref(env, fromdocname, builder, typ, target, node, contnode)


def setup(sphinx):
    sphinx.override_domain(PatchedPythonDomain)


rst_epilog = """
.. |OciSdkVersion| replace:: {version}
""".format(version=oci.__version__)
