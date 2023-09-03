from manim import *


class Label:
    def __init__(self, string, color: str = None, font=None, size=None, position=ORIGIN, shift=ORIGIN, tex=False):

        self.string: str = string
        self.color: str = color
        self.font: str = font
        self.size: float = 1
        self.position: np.ndarray = position
        self.tex: bool = tex

    def label(self, string, color: str = None):
        if string is None:
            string = self.string
        if string.__len__() == 0:
            return VGroup()
        if color is None:
            color = self.color
        if self.tex:
            return Tex(string, color=self.color).move_to(self.position).scale(self.size).set_color(self.color)
        return Text(string, color=self.color, font=self.font).move_to(self.position).scale(self.size).set_color(self.color)





