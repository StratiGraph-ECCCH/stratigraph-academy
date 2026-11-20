# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'StratiGraph Academy'
copyright = '2026, Consiglio Nazionale delle Ricerche (CNR) — Istituto di Scienze del Patrimonio Culturale'
author = 'Emanuel Demetrescu'

release = '1.6'
version = '1.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    # the pages written since this became the ecosystem manual are markdown,
    # like the rest of the ecosystem's documentation
    'myst_parser',
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
myst_enable_extensions = ['deflist', 'colon_fence', 'fieldlist', 'substitution']
myst_heading_anchors = 3

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    # reusable RST snippets, pulled in with `.. include::`, never pages
    '_includes/**',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Il marchio, vendorizzato da `stratigraph-brand` con il suo
# `docs-theme/sync-brand-docs.sh`, come lo vendorizzano le applicazioni: un
# manuale letto in trincea non ha una CDN. Chiaro e scuro seguono
# l'impostazione di sistema di chi legge; i contrasti sono misurati nel
# marchio. Per cambiare un colore si cambia lì, e si ridà il sync.
# EPUB non conosce il tipo di un .woff2 e, con -W, la sua lamentela
# («unknown mimetype … ignoring») ferma la pubblicazione: i caratteri del
# marchio servono alla pagina web, non al libro.
suppress_warnings = ['epub.unknown_project_files']

html_css_files = [
    'brand/stratigraph-theme.css',
    'brand/sphinx-rtd-bridge.css',
]

# L'interruttore delle due facce: chiaro, scuro, come il sistema. Senza
# scelta esplicita vale il sistema di chi legge, che è il modo di serie.
html_js_files = ['brand/brand-theme-toggle.js']

# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True

# -- AI Act Article 50 transparency footer -----------------------------
# A short notice appended to every page via ``rst_epilog``, pointing to
# the project's AI usage policy at extendedmatrix.org/ai-usage/.
rst_epilog = """
.. include:: /_includes/ai_usage_notice.rst
"""
