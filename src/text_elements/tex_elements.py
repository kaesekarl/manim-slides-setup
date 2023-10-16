from manim import TexTemplate, TexFontTemplates

base_tex_template = TexTemplate()
base_tex_template.add_to_preamble(
        r"""
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[T1]{fontenc}
\renewcommand{\familydefault}{\sfdefault}
\usepackage[symbolgreek,defaultmathsizes]{mathastext}
\setlength{\parindent}{0pt}
\usepackage[document]{ragged2e}
""",
        )
