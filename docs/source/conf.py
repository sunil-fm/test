import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))

project = "Documentation"
copyright = "2024, Jonathan Arias Busto"
author = "Jonathan Arias Busto"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",  # Optional: for summary tables
]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_mock_imports = []  # Mock external dependencies if needed

# Napoleon settings (Google/NumPy docstrings)
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_extra_path = [".nojekyll"]  # Alternative to manual touch in workflow
