from manim import *
from src.text_elements.label import TexLabel
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper
from copy import copy

theme = FallbackDictWrapper(APPLIED_THEME, "Text")


class VertexLabel(TexLabel):
    def __init__(self, string=None, color=theme["color"], font=None, size=None, position=None, shift=ORIGIN):
        super().__init__(string, color, font, size, position, shift)


class Vertex:
    def __init__(self, name, color=theme["color"], variety=None, position=ORIGIN, scale=1, label_color=theme["color"], **kwargs):
        self.name = name
        self.color = color
        self.position = position
        self.variety = variety
        self.scale = scale

        self.vertex_label = VertexLabel()
        self.label_pos = kwargs.pop("label_pos", position)
        self.label_color = label_color


    def node(self, pos: np.ndarray = None, vertex_scale=1):
        if pos is None:
            pos = self.position
        if self.variety is None:
            raise Exception("Vertex variety not set")
        if self.color is None:
            return copy(self.variety.move_to(pos).scale(vertex_scale))
        return copy(self.variety.set_color(self.color).move_to(pos).scale(vertex_scale))

    def label(self, string=None, pos: np.ndarray = None, scale=1, color=None):
        if pos is None:
            pos = self.position
        if string is None:
            string = self.name
        if color is None:
            color = self.label_color

        return copy(self.vertex_label.label(string, color, pos).scale(scale))



