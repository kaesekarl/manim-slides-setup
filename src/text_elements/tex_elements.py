from manim import TexTemplate, TexFontTemplates

base_tex_template = TexFontTemplates.urw_avant_garde
base_tex_template.add_to_preamble(r"\usepackage{amssymb}")
base_tex_template.add_to_preamble(r"\usepackage{amsmath}")
base_tex_template.add_to_preamble(r"\usepackage{amsfonts}")
base_tex_template = base_tex_template.add_to_preamble(r"\setlength{\parindent}{0pt}")

