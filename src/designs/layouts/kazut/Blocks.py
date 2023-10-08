from manim import LEFT, RIGHT, Text, VGroup, SurroundingRectangle, DOWN, Tex
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper

theme = FallbackDictWrapper(APPLIED_THEME, "Text Blocks")


class ColorBlock:
    def __init__(self, title, text, color, pos, text_color=None):
        self.title = title
        self.text = text
        self.color = color
        self.pos = pos
        if text_color is None:
            self.text_color = theme["text_color"]
        else:
            self.text_color = text_color

    def create(self):
        elements = VGroup()
        backgrounds = VGroup()

        title = (Tex(self.title, color=self.text_color, tex_template=theme.no_default()["Tex_Templates base"])
                 .scale(0.6)
                 .set_z_index(10))
        text = (Tex(self.text, color=self.text_color, tex_template=theme.no_default()["Tex_Templates base"])
                .scale(0.5)
                .next_to(title, DOWN, aligned_edge=LEFT)
                .shift(RIGHT * 0.2).set_z_index(10))

        elements.add(title, text)

        title_background = (SurroundingRectangle(title, color=self.color, stroke_opacity=0.8, fill_color=self.color, fill_opacity=0.5, corner_radius=0.2)
                            .set_z_index(1))
        text_background = (SurroundingRectangle(text, color=self.color, stroke_opacity=0.8, fill_color=self.color, fill_opacity=0.1, corner_radius=0.2)
                            .set_z_index(1))
        backgrounds.add(text_background, title_background)

        elements += backgrounds
        return elements





