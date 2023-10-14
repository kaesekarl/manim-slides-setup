from manim import TexTemplate, TexFontTemplates

base_tex_template = TexTemplate()
base_tex_template.add_to_preamble(
        r"""
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
"""
        )
base_tex_template.add_to_preamble(
        r"""
\usepackage[T1]{fontenc}
\usepackage{avant}
\renewcommand{\familydefault}{\sfdefault}
\usepackage[symbolgreek,defaultmathsizes]{mathastext}
""",
        )
base_tex_template.add_to_preamble(r"\setlength{\parindent}{0pt}")
