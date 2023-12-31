from copy import deepcopy, copy

from manim import VGroup, Circle, Triangle, Arrow, CurvedArrow, TangentLine, TAU, ORIGIN, UP, LEFT, np

from src.DFA_Creator.Vertex import Vertex
from src.DFA_Creator.Edge import Edge, EdgeLabel

from src.designs.themes import APPLIED_THEME, FallbackDictWrapper

theme = FallbackDictWrapper(APPLIED_THEME, "Text")

__all__ = [
        "State",
        "Start_State",
        "Accept_State",
        "Start_Accept_State",
        "DirectEdge",
        "CurvedEdge",
        "Loop",
        "Graph_Creator"
        ]


class Start_State(Vertex):
    def __init__(self, name, position=ORIGIN, color=theme["color"], variety=None, scale=1, label_color=None):
        super().__init__(name, color, variety, position, scale, label_color)
        self.label_pos = ORIGIN
        self.label_color = color
        self.variety = VGroup(Circle(), Triangle(fill_opacity=1).rotate(-0.18).scale(0.15).shift(UP * 0.7 + LEFT * 0.7))



class Accept_State(Vertex):
    def __init__(self, name, position=ORIGIN, color=theme["color"], variety=None, scale=1, label_color=None):
        super().__init__(name, color, variety, position, scale, label_color)
        self.label_pos = ORIGIN
        self.label_color = color
        self.variety = VGroup(Circle(), Circle().scale(0.85))


class Start_Accept_State(Vertex):
    def __init__(self, name, position=ORIGIN, color=theme["color"], variety=None, scale=1, label_color=None):
        super().__init__(name, color, variety, position, scale, label_color)
        self.label_pos = ORIGIN
        self.label_color = color
        self.variety = VGroup(Circle(), Triangle(fill_opacity=1).rotate(-0.18).scale(0.15).shift(UP * 0.7 + LEFT * 0.7), Circle().scale(0.85))


class State(Vertex):
    def __init__(self, name, position=ORIGIN, color=theme["color"], variety=None, scale=1, label_color=None):
        super().__init__(name, color, variety, position, scale, label_color)
        self.label_pos = ORIGIN
        self.label_color = color
        self.variety = VGroup(Circle())


class DirectEdge(Edge):
    def __init__(self, start: Vertex, end: Vertex, name: str, color=theme["color"]):
        super().__init__(start, end, name, color=color, edge_type=Arrow)
        self.start = start
        self.end = end
        self.name = name
        self.label_color = color


class CurvedEdge(Edge):
    def __init__(self, start: Vertex, end: Vertex, name: str, arc=TAU/6, color=theme["color"]):
        super().__init__(start, end, name, color=color, edge_type=CurvedArrow)
        self.start = start
        self.end = end
        self.name = name
        self.label_color = color
        self.arc = arc


    def edge(self, start=None, end=None, start_pos=None, end_pos=None, color=None, arc=None):
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
        if arc is None:
            arc = self.arc
        start_pos, end_pos = start.node()[0].point_from_proportion(start_pos), end.node()[0].point_from_proportion(end_pos)
        return CurvedArrow(start_pos, end_pos, angle=-arc).set_color(color)


class Loop:
    def __init__(self, vertex: Vertex, name: str, color=theme["color"], pos=None, arc=TAU/2):
        self.vertex = vertex
        self.name = name
        self.color = color
        self.pos = pos
        self.arc = arc
        self.edge_label = EdgeLabel(relative_position=0.6)

    def edge(self, vertex=None, name=None, pos=None,color=None, arc=None):
        if vertex is None:
            vertex = self.vertex
        if color is None:
            color = self.color
        if arc is None:
            arc = self.arc
        if pos is None:
            pos = self.pos
            if self.pos is None:
                pos = 0.25
        pos1, pos2 = pos-0.08 if pos-0.08 > 0 else pos-0.08+1, pos+0.08 if pos+0.08 < 1 else pos+0.08-1
        pos1, pos2 = vertex.node()[0].point_from_proportion(pos1), vertex.node()[0].point_from_proportion(pos2)
        return CurvedArrow(pos1, pos2, angle=arc).set_color(color)

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
        _perp = np.array([_perp[1], -_perp[0], 0])
        position += _perp * distance

        return copy(self.edge_label.label(string, color, position))



class Graph_Creator:
    """
    Creates a graph from a list of vertices and edges
    """
    def __init__(self, vertices: list, edges: list, vertex_scale=None):
        self.vertices = copy(vertices)
        self.edges = copy(edges)
        self.vertex_scale = vertex_scale

    def create(self, vertex_scale=None) -> VGroup:
        """
        Creates an Automata Graph from the vertices and edges specified in the constructor
        :param vertex_scale: Scale the size of all vertices
        :return: VGroup containing all vertices and edges as well as their labels
        """
        if vertex_scale is None:
            vertex_scale = self.vertex_scale
        graph = VGroup()
        for vertex in self.vertices:
            if vertex_scale is not None:
                graph.add(vertex.node(vertex_scale=vertex_scale))
            else:
                graph.add(vertex.node())
            graph.add(vertex.label())
        for edge in self.edges:
            graph.add(edge.edge())
            graph.add(edge.label())
        return graph

    def create_vertices(self, vertex_scale=None) -> VGroup:
        """
        Creates only the vertices of the graph
        :param vertex_scale: Scale the size of all vertices
        :return: VGroup containing all vertices and their labels
        """
        graph = VGroup()
        for vertex in self.vertices:
            if vertex_scale is not None:
                graph.add(vertex.node(vertex_scale=vertex_scale))
            else:
                graph.add(vertex.node())
            graph.add(vertex.label())
        return graph


