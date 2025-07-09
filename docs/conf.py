import os
import sys

sys.path.insert(0, os.path.abspath("../jl"))

project = "jl"
author = "Mr Moo"
copyright = "2023, redandgreen.co.uk"
release = "0.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "m2r2",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

source_suffix = [".rst", ".md"]
master_doc = "index"

autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False

