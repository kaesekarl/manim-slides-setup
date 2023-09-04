from Vertex import Vertex
from src.text_elements.Label import Label
from manim import *


class EdgeLabel(Label):
    def __init__(self, string=None, color=None, font=None, size=None, relative_position=0.5, distance=0.5, tex=True, **kwargs):
        super().__init__(string, color, font, size, tex=tex)
        self.relative_position = relative_position
        self.distance = distance





class Edge:
    def __init__(self, start: Vertex, end: Vertex, start_pos=None, end_pos=None, color=None, label=None, name=None):
        self.start: Vertex = start
        self.end: Vertex = end
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.edge_label = label
        self.name = name

    def closest_points_on_vertices(self, v1=None, v2=None):
        if v1 is None:
            v1 = self.start
        if v2 is None:
            v2 = self.end

        if v1 is None or v2 is None:
            raise Exception("Both vertices must be set")
        v1_center = v1.node()[0].get_center()
        v2_center = v2.node()[0].get_center()
        ang1 = np.arctan2(v2_center[1] - v1_center[1], v2_center[0] - v1_center[0])
        ang2 = np.arctan2(v1_center[1] - v2_center[1], v1_center[0] - v2_center[0])

        for ang in [ang1, ang2]:
            if ang < 0:
                ang += np.pi * 2
            ang /= np.pi * 2

        return ang1, ang2

    def edge(self, start=None, end=None, start_pos=None, end_pos=None, color=None):
        if start is None:
            start = self.start
        if end is None:
            end = self.end
        if color is None:
            color = self.color
        if start_pos is None:
            start_pos = self.start_pos
            if self.start_pos is None:
                start_pos = self.closest_points_on_vertices()[0]
        if end_pos is None:
            end_pos = self.end_pos
            if self.end_pos is None:
                end_pos = self.closest_points_on_vertices()[1]
        return Line(start_pos, end_pos).set_color(color)

    def label(self, string=None, rel_pos=None, distance=None, color=None):
        if string is None:
            string = self.name
        if rel_pos is None:
            rel_pos = self.edge_label.relative_position
        if distance is None:
            distance = self.edge_label.distance
        if color is None:
            color = self.color
        pos = self.edge()[0].point_from_proportion(rel_pos)
        return EdgeLabel(string, color=color, position=pos).label(string)

