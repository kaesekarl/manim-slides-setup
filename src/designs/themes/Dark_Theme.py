# Here are some added colors
# path: src/constants/colors.py
from manim.utils.color import *
from dataclasses import dataclass

# Fonts
_text_font = "Sans"
_title_font = "Sans"

# Colors
dark_blue = "#2A2E34"  # ZUT_BLUE_DARK
light_blue = "#6DADDF"
tan = "#f3eee1"  # ZUT_TAN

text = WHITE
text_muted = tan

background = dark_blue
accent_1 = light_blue

DarkTheme = dict(
    # Fonts
    text_font="Sans",
    title_font="Sans",

    # Colors
    dark_blue="#2A2E34", # same as background
    light_blue="#6DADDF",
    tan="#F3EEE1",

    # Accents
    accent_1="6DADDF",

    Text=dict(
        color=WHITE,
        muted_color=text_muted,
        font=_text_font,
        size=0.5,
        line_spacing=0.2,

        Lists=dict(
            Bulletpoints=dict(
                    point_spacing=0.4,
                    ),

            Numbered=dict(
                    point_spacing=0.4,
                    ),
                ),
        Title=dict(
                color=WHITE,
                font=_title_font,
                size=1,
                line_spacing=0.2,
                ),
            ),
    Slide=dict(
        background=background,

        Header=dict(
            Seperator=dict(
                color=accent_1,
                buff=0.8,
                stroke_width=2,
                ),

            Title=dict(
                color=WHITE,
                font=_title_font,
                size=0.65,
                line_spacing=0.2,
                buff=0.35,
                ),
            ),
        Footer=dict(
            Seperator=dict(
                color=accent_1,
                buff=0.8,
                stroke_width=2,
                ),

            Counter=dict(
                color=text_muted,
                font=_text_font,
                size=0.5,
                weight="NORMAL",
                buff=0.25,
                ),
            ),
        Cover=dict(
            separator_color=accent_1,

            title_color=WHITE,
            title_font=_title_font,
            title_size=0.9,
            title_weight="BOLD",

            subtitle_color=WHITE,
            subtitle_font=_title_font,
            subtitle_size=0.5,
            subtitle_weight="BOLD",

            author_color=text_muted,
            author_font=_text_font,
            author_size=0.33,
            author_weight="BOLD",
            ),
        ),
    Background=dict(
        color="#2A2E34", # same as dark_blue
        ),
    )


# @dataclass
# class DarkTheme:
#     accent_1 = "#6DADDF"
#
#     @dataclass
#     class Text:
#         color = WHITE
#         muted_color = text_muted
#         font = _text_font
#         size = 0.5
#         line_spacing = 0.2
#
#         @dataclass
#         class Lists:
#             @dataclass
#             class Bulletpoints:
#                 color = WHITE
#                 font = _text_font
#                 size = 0.5
#                 point_spacing = 0.4
#                 line_spacing = 0.2
#
#             @dataclass
#             class Numbered:
#                 color = WHITE
#                 font = _text_font
#                 size = 0.5
#                 point_spacing = 0.4
#                 line_spacing = 0.2
#
#         @dataclass
#         class Title:
#             color = WHITE
#             font = _title_font
#             size = 1
#             line_spacing = 0.2
#
#     @dataclass
#     class Slide:
#         background = background
#
#         @dataclass
#         class Header:
#             @dataclass
#             class Seperator:
#                 color = accent_1
#                 buff = 0.8
#                 stroke_width = 2
#
#             @dataclass
#             class Title:
#                 color = WHITE
#                 font = _title_font
#                 size = 0.65
#                 line_spacing = 0.2
#                 buff = 0.35
#
#         @dataclass
#         class Footer:
#             @dataclass
#             class Seperator:
#                 color = accent_1
#                 buff = 0.8
#                 stroke_width = 2
#
#             @dataclass
#             class Counter:
#                 color = text_muted
#                 font = _text_font
#                 size = 0.5
#                 weight = "NORMAL"
#                 buff = 0.25
#
#         @dataclass
#         class Cover:
#             separator_color = accent_1
#
#             title_color = WHITE
#             title_font = _title_font
#             title_size = 0.9
#             title_weight = "BOLD"
#
#             subtitle_color = WHITE
#             subtitle_font = _title_font
#             subtitle_size = 0.5
#             subtitle_weight = "BOLD"
#
#             author_color = text_muted
#             author_font = _text_font
#             author_size = 0.33
#             author_weight = "BOLD"
#
#     @dataclass
#     class Background:
#         color = background
