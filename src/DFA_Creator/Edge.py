from src.DFA_Creator.Vertex import Vertex
from src.text_elements.Label import TexLabel
from manim import *
from copy import copy


class EdgeLabel(TexLabel):
    def __init__(self, edge: VMobject = None, string=None, color=None, relative_position=0.5, distance=0.3, **kwargs):
        position = kwargs.pop("position", None)
        self.relative_position = relative_position
        self.distance = distance
        super().__init__(string, color, font=None, position=position)



class Edge:
    def __init__(self, start: Vertex, end: Vertex, name=None, start_pos=None, end_pos=None, color=None, edge_type=Line):
        self.start: Vertex = start
        self.end: Vertex = end
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.name = name
        self.edge_label = EdgeLabel()
        self.edge_type = edge_type

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

        if ang1 < 0:
            ang1 += TAU
        ang1 /= TAU
        if ang2 < 0:
            ang2 += TAU
        ang2 /= TAU

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
                start_pos = self.closest_points_on_vertices(start, end)[0]
        if end_pos is None:
            end_pos = self.end_pos
            if self.end_pos is None:
                end_pos = self.closest_points_on_vertices(start, end)[1]
        start_pos, end_pos = start.node()[0].point_from_proportion(start_pos), end.node()[0].point_from_proportion(end_pos)
        return self.edge_type(start_pos, end_pos, buff=0).set_color(color)

    def label(self, string=None, rel_pos=None, distance=None, color=None):
        if string is None:
            string = self.name
        if rel_pos is None:
            rel_pos = self.edge_label.relative_position
        if distance is None:
            distance = self.edge_label.distance
        if color is None:
            color = self.color
        position = self.edge().point_from_proportion(rel_pos)
        _perp = TangentLine(self.edge(), rel_pos).get_unit_vector()
        _perp = - np.array([_perp[1], -_perp[0], 0])
        position += _perp * distance

        return copy(self.edge_label.label(string, color, position))

