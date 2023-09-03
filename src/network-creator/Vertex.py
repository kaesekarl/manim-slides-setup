from manim import *
from src.text_elements.Label import Label


class VertexLabel(Label):
    pass


class Vertex:
    def __init__(self, id, color=WHITE, position=ORIGIN):
        self.id = id
        self.color = color
        self.label = VertexLabel()
        self.position = position

    def vertex(self, pos: np.ndarray = None):
        if pos is None:
            pos = self.position
        return None
