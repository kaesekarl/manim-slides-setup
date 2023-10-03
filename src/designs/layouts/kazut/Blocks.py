from manim import LEFT, Text, VGroup, SurroundingRectangle, DOWN
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper

theme = FallbackDictWrapper(APPLIED_THEME, "Text Blocks")


class ColorBlock:
    def __init__(self, title, text, color, text_color=None):
        self.title = title
        self.text = text
        self.color = color
        if text_color is None:
            self.text_color = theme["text_color"]
        else:
            self.text_color = text_color

    def create(self):
        elements = VGroup()



        return elements





