from manim import *
from src.text_elements.tex_elements import tex_template


class Label:
    def __init__(self, string, color: str = None, font=None, size=None, position=ORIGIN):

        self.string: str = string
        self.color: str = color
        self.font: str = font
        self.size: float = 1
        self.position: np.ndarray = position

    def label(self, string, color: str = None, tex=None):
        if string is None:
            string = self.string
        if string.__len__() == 0:
            return VGroup()
        if color is None:
            color = self.color

        return Text(string, font=self.font).move_to(self.position).scale(self.size).set_color(color)


class TexLabel(Label):
    def __init__(self, string, color: str = None, font=None, size=None, position=ORIGIN, shift=ORIGIN):
        super().__init__(string, color, font, size, position)

    def label(self, string, color: str = None, pos=None):
        if pos is None:
            pos = self.position
        if string is None:
            string = self.string
        if string.__len__() == 0:
            return VGroup()
        if color is None:
            color = self.color

        return MathTex(string, color=self.color, tex_template=tex_template).move_to(pos).scale(self.size)





