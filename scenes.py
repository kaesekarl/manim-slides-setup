from manim import *
from manim_presentation import Slide
from src.constants import colors
import src.network_creator.DFA_network as DFA


theme = colors.DarkTheme()
config.background_color = theme.Background().color


class Scene1(Slide):
    def construct(self):
        verts = dict(
                q_0=DFA.Start_State("q_0", position=LEFT*2),
                q_1=DFA.State("q_1", position=UP*2),
                q_a=DFA.Accept_State("q_a", position=RIGHT*2),
                )
        edges = dict(
                e1=DFA.DirectEdge(verts["q_0"], verts["q_1"], r"0"),
                e2=DFA.DirectEdge(verts["q_1"], verts["q_a"], r"1"),
                e3=DFA.CurvedEdge(verts["q_0"], verts["q_a"], r"a"),
                e4=DFA.CurvedEdge(verts["q_a"], verts["q_0"], r"b"),
                e5=DFA.Loop(verts["q_1"], r"1"),
                )
        graph = DFA.Graph_Creator(verts, edges).create(vertex_scale=0.75)
        self.play(Create(graph.shift(DOWN)))
        self.wait(2)


with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = Scene1()
    scene.render()
