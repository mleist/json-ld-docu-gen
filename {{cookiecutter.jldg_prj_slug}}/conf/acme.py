# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from conf.base import *

# -- Options for HTML output -------------------------------------------------

html_logo = 'static_free/Logo_acme.png'
html_show_copyright = False
html_show_sourcelink = False
html_theme_options = {
    'font_family': 'Montserrat,Helvetica,Arial,sans-serif',
    'logo_name': False,
    'show_powered_by': False,
    'link_hover': '#942193',
    'link': '#942193',
    'sidebar_hr': '#005493',
    'sidebar_link': '#929000',
    'sidebar_list': '#929000',
    'sidebar_link_underscore': '#942193',
    'note_bg': '#D3EBE5',
    'note_border': '#005493',
    'warn_bg': '#FFFC79',
    'warn_border': '#FFFB00',
    'pre_bg': '#EBEBEB',
}


# -- Options for PDF output -------------------------------------------------

latex_logo = 'static_free/Logo_acme.png'

latex_elements = {
    'papersize': 'a4paper',
    'extraclassoptions': 'oneside',
    'cmappkg': r'''
        \usepackage{cmap}
        \usepackage{xcolor}
        \definecolor{ACME_yellow}{cmyk}{0.01, 0.11, 0.89, 0.01}
        \definecolor{ACME_orange}{cmyk}{0, 0.63, 0.88, 0}
        \definecolor{ACME_silver}{cmyk}{0.06, 0.04, 0.03, 0}
        \definecolor{ACME_black}{cmyk}{0, 0, 0, 1}
        \definecolor{ACME_1}{cmyk}{0.96, 0.60, 0.03, 0.08}
        \definecolor{ACME_2}{cmyk}{0.49, 0.91, 0, 0.01}
        ''',
    'sphinxsetup': r'''
        TitleColor=ACME_1,
        noteBgColor=ACME_silver,
        warningBgColor=ACME_silver,
        cautionBgColor=ACME_silver,
        attentionBgColor=ACME_silver,
        dangerBgColor=ACME_orange,
        errorBgColor=ACME_yellow,      
        hmargin={18.56mm,18.56mm},
        vmargin={18.56mm,18.56mm},
        marginpar=0.0mm
        ''',
    'maketitle': r'''
        {
            \begingroup % for PDF information dictionary
               \def\endgraf{ }\def\and{\& }%
               \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
               \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
            \endgroup
            \thispagestyle{empty}
          \begin{flushright}
            \sphinxlogo
            \vspace{6cm}
            \py@HeaderFamily
            {\Huge \@title }\par
            \vspace{25pt}
            {\Large \@author }\par
            \vspace{25pt}
            {{ env.docname }}
          \end{flushright}
          \@thanks
          \setcounter{footnote}{0}
          \let\thanks\relax\let\maketitle\relax
          %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
        }''',
    'preamble': r'''
        \setmainfont{Montserrat-Regular.ttf}[
           BoldFont       = Montserrat-Bold.ttf,
           ItalicFont     = Montserrat-Italic.ttf,
           BoldItalicFont = Montserrat-BoldItalic.ttf
        ]
        \setmonofont{FiraCode-Regular.ttf}

        \setcounter{page}{0}
        \makeatletter
        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyhead[OL]{{\small\@title}}
            \fancyhead[OR]{{\small\rightmark}}
            \fancyfoot[OR]{{\thepage}}
            \fancyfoot[LO]{{\color{ACME_yellow}\small\py@release}}
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0pt}
            }
        \fancypagestyle{plain}{
            \fancyhf{}
            \fancyhead[OL]{{\small\@title}}
            \fancyhead[OR]{{\small\rightmark}}
            \fancyfoot[OR]{{\thepage}}
            \fancyfoot[LO]{{\color{ACME_yellow}\small\py@release}}
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0pt}
            }
        \fancypagestyle{empty}{
            \fancyhf{}
            \fancyfoot[LO]{{\color{white} \py@release \releaseinfo \hspace{2pt} \--- \hspace{2pt}\@date }}
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0pt}
            \ThisULCornerWallPaper{1}{background3.pdf}
            }
        \ChRuleWidth{0mm}
        \ChNumVar{\Huge\color{white}\colorbox{ACME_2}}
        \ChNameVar{\Huge\color{black}\colorbox{green}}
        \ChTitleVar{\Huge\color{black}}
        \definecolor{TitleColor}{named}{ACME_2}
        \definecolor{InnerLinkColor}{named}{ACME_1}
        \definecolor{OuterLinkColor}{named}{ACME_1}
        \newcommand\crule[3][black]{\textcolor{#1}{\rule{#2}{#3}}}
        \usepackage[titles]{tocloft}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{0.75cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
        \renewcommand{\DOCH}{%
            \raggedleft
            \CTV{\@chapapp}\space \CTV\thechapter
            \par\nobreak
            \vskip 40\p@}
        \renewcommand{\DOTI}[1]{%
            \CTV\raggedleft\mghrulefill{\RW}\par\nobreak
            \vskip 5\p@
            \CTV\FmTi{#1}\par\nobreak
            \mghrulefill{\RW}\par\nobreak
            \vskip 40\p@}
        \renewcommand{\DOTIS}[1]{%
            \CTV\raggedleft\mghrulefill{\RW}\par\nobreak
            \vskip 5\p@
            \CTV\FmTi{#1}\par\nobreak
            \mghrulefill{\RW}\par\nobreak
            \vskip 40\p@}
            ''',
    'fncychap': r'\usepackage[Sonny]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    'extrapackages': r'''
        \usepackage{isodate}
        \usepackage{xltxtra}
        \usepackage[titles]{tocloft}
        \usepackage{isodate}
        \usepackage{xcolor}
        \usepackage{graphicx}
        \usepackage[document]{ragged2e}
        \usepackage{lastpage}
        \usepackage{wallpaper}
        \usepackage{eso-pic}
        ''',
    'shorthandoff': r'''
        \ifdefined\shorthandoff
          \ifnum\catcode`\=\string=\active\shorthandoff{=}\fi
          \ifnum\catcode`\"=\active\shorthandoff{"}\fi
        \fi
        ''',
}
latex_show_urls = 'no'
latex_additional_files = [
    'static_free/background3.pdf',
]


# -- Options for PlantUML -------------------------------------------------

plantuml = '/usr/bin/plantuml -DPLANTUML_LIMIT_SIZE=8192 -config /docs/conf/acme_plantuml.cfg '
plantuml_output_format = 'svg_img'
plantuml_latex_output_format = 'eps'
