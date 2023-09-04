from manim import *
from src.text_elements.Label import Label


class VertexLabel(Label):
    def __init__(self, string=None, color=None, font=None, size=None, position=ORIGIN, shift=ORIGIN, tex=True):
        super().__init__(string, color, font, size, position, shift, tex)


class Vertex:
    def __init__(self, name, color=None, variety=None, position=ORIGIN, scale=1, label_color=None):
        self.name = name
        self.color = color
        self.position = position
        self.variety = variety
        self.scale = scale

        self.vertex_label = VertexLabel()
        self.label_pos = ORIGIN
        self.label_color = label_color


    def node(self, pos: np.ndarray = None, scale=1):
        if pos is None:
            pos = self.position
        if self.variety is None:
            raise Exception("Vertex variety not set")
        if self.color is None:
            return self.variety.copy().move_to(pos).scale(scale)
        return self.variety.copy().set_color(self.color).move_to(pos).scale()

    def label(self, string=None, pos: np.ndarray = None, scale=1, color=None):
        if pos is None:
            pos = self.label_pos
        if string is None:
            string = self.name
        if color is None:
            color = self.label_color

        return self.vertex_label.label(string, color=color).copy().shift(pos).scale(scale)
