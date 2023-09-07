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
        class Bulletpoints:
            color = WHITE
            font = "Sans"
            size = 0.5
            point_spacing = 0.4
            line_spacing = 0.2

    @dataclass
    class Slide:
        background = background

        @dataclass
        class Header:

            @dataclass
            class Seperator:
                color = accent_1
                buff = 1.0
                stroke_width = 2
                dashed_ratio = 0.5
                dash_length = 0.07

        @dataclass
        class Title:
            color = WHITE
            font = "Sans"
            size = 0.65
            line_spacing = 0.2

    @dataclass
    class CoverSlide:
        separator_color = accent_1

        title_color = WHITE
        title_font = "Sans"
        title_size = 0.9
        title_weight = "BOLD"

        subtitle_color = WHITE
        subtitle_font = "Sans"
        subtitle_size = 0.5
        subtitle_weight = "BOLD"

        author_color = text_muted
        author_font = "Sans"
        author_size = 0.33
        author_weight = "BOLD"

    @dataclass
    class Background:
        color = background

