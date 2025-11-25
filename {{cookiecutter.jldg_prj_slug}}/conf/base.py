# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import date


# -- General configuration ---------------------------------------------------

copyright = f"{date.today().year}"

extensions = ['myst_parser',
              "sphinx_design",
              'nbsphinx',
              'sphinxcontrib.email',
              'sphinxcontrib.plantuml',
              ]


# -- Options for MyST -------------------------------------------------

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
myst_title_to_header = False
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
email_automode = True
master_doc = "index"
html_theme = 'alabaster'
html_static_path = ['static_free']
latex_engine = 'xelatex'
myst_words_per_minute = 30


# -- Options for PDF output -------------------------------------------------

latex_listoffigures_in_preamble =  r'''
        \renewcommand{\sphinxtableofcontents}{%
          \pagenumbering{roman}%
          \begingroup
            \parskip \z@skip
            \sphinxtableofcontentshook
            \tableofcontents
            \pagebreak%
            \vspace{0pt}
            \listoffigures
            \vfill
          \endgroup
          % before resetting page counter, let's do the right thing.
          \if@openright\cleardoublepage\else\clearpage\fi
          \pagenumbering{arabic}%
        }
'''


def set_latex_language(language, latex_elements):
    if language == 'en':
        latex_elements['preamble'] += "\n\\setmainlanguage{english}\n"
    elif language == 'de':
        latex_elements['preamble'] += "\n\\setmainlanguage{ngerman}\n"
    else:
        latex_elements['preamble'] += "\n\\setmainlanguage{english}\n"


# -- Options for PlantUML -------------------------------------------------

plantuml_output_format= 'png'
plantuml_latex_output_format = 'eps'
plantuml_batch_size = 100
