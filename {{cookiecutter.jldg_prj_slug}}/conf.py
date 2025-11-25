# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.append(os.path.abspath('.'))

from conf.acme import *
# from conf.private.ks import *

# include listoffigures
# latex_elements['preamble'] += latex_listoffigures_in_preamble

# -- Project information -----------------------------------------------------

project = '{{cookiecutter.jldg_prj_name}}'
author = 'markus@lei.st'
release = '0.01'
language = 'de'

set_latex_language(language, latex_elements)
