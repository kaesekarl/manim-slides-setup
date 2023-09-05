# Here are some added colors
# path: src/constants/colors.py
from manim.utils.color import *
from dataclasses import dataclass


dark_blue = "#2A2E34"  # ZUT_BLUE_DARK
light_blue = "#6DADDF"
tan = "#f3eee1"  # ZUT_TAN

text =  WHITE
text_muted = tan

background = dark_blue
accent_1 = light_blue


@dataclass
class DarkTheme:

    @dataclass
    class Text:
        color = WHITE
        muted_color = text_muted
        font = "Sans"
        size = 0.5
        line_spacing = 0.2


    @dataclass
    class Background:
        color = background

