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

    accent_1 = "#6DADDF"

    @dataclass
    class Text:
        color = WHITE
        muted_color = text_muted
        font = "Sans"
        size = 0.5
        line_spacing = 0.2

        @dataclass
        class Title:
            color = WHITE
            font = "Sans"
            size = 1
            line_spacing = 0.2

    @dataclass
    class Slide:
        background = background

        @dataclass
        class Header:

            @dataclass
            class Seperator:
                color = accent_1
                buff = 0.5
                stroke_width = 2

        @dataclass
        class Title:
            color = WHITE
            font = "Sans"
            size = 0.65
            line_spacing = 0.2




    @dataclass
    class Background:
        color = background

