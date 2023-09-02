# Here are some added colors
# path: src/constants/colors.py
from manim.utils.color import Color
from manim.utils.color import *


def color_creator_hex(hex_string: str) -> Color:
    """
    Creates a Color object from a hex string.
    :param hex_string: Hex string of the color.
    :return: returns a Color object.
    """

    new_color = Color()
    new_color.hex = hex_string
    return new_color


dark_blue = color_creator_hex("2a2e34")  # ZUT_BLUE_DARK
light_blue = color_creator_hex("#6daddf")  # ZUT_BLUE_LIGHT
tan = color_creator_hex("#f3eee1")  # ZUT_TAN

text =  WHITE
text_muted = tan

background = dark_blue
acc_1 = light_blue
