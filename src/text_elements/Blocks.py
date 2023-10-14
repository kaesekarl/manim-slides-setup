from manim import LEFT, ORIGIN, RIGHT, Text, VGroup, SurroundingRectangle, DOWN, Tex
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper

theme = FallbackDictWrapper(APPLIED_THEME, "Text Blocks")


class ColorBlock:
    def __init__(self, title, text, color, pos=ORIGIN, size=None, text_color=None):
        self.title = title
        self.text = text
        self.color = color
        self.pos = pos

        if size is None:
            self.size = theme["size"]
        else:
            self.size = size
        if text_color is None:
            self.text_color = theme["text_color"]
        else:
            self.text_color = text_color

        self.rect_width = theme["rect_width"]
        self.rect_height = theme["rect_height"]

    def create(self):
        elements = VGroup()
        backgrounds = VGroup()

        title = (Tex(self.title, color=self.text_color, tex_template=theme.no_default()["Tex_Templates base"])
                 .scale(self.size)
                 .set_z_index(10))
        text = (Tex(self.text, color=self.text_color, tex_template=theme.no_default()["Tex_Templates base"])
                .scale(self.size*0.75)
                .next_to(title, DOWN, aligned_edge=LEFT)
                .shift(ORIGIN).set_z_index(10))

        elements.add(title, text)

        title_background = (SurroundingRectangle(title, color=self.color,
                                                 stroke_opacity=theme["header_stroke_opacity"],
                                                 fill_color=self.color,
                                                 fill_opacity=theme["header_opacity"],
                                                 corner_radius=[0.2, 0, 0.2, 0])
                            .set_z_index(1))
        text_background = (SurroundingRectangle(text, color=self.color,
                                                stroke_opacity=theme["body_stroke_opacity"],
                                                fill_color=self.color,
                                                fill_opacity=theme["body_opacity"],
                                                corner_radius=0.2)
                            .set_z_index(1))
        elements_background = (SurroundingRectangle(elements, color=self.color,
                                                    stroke_opacity=theme["block_stroke_opacity"],
                                                    fill_color=self.color,
                                                    fill_opacity=theme["block_opacity"],
                                                    corner_radius=0.2)
                               .set_z_index(1))
        backgrounds.add(text_background, title_background, elements_background)

        elements += backgrounds
        return elements.move_to(self.pos)





