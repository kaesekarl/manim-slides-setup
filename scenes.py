from manim import *
from manim_presentation import Slide
from src.constants import colors
import src.network_creator.DFA_network as DFA


theme = colors.DarkTheme()
config.background_color = theme.Background().color


class Scene1(Slide):
    def construct(self):
        temp = UP * 2
        verts = dict(
                q_0=DFA.Start_State("q_0", position=rotate_vector(temp, TAU/3)),
                q_1=DFA.State("q_1", position=rotate_vector(temp, 0)),
                q_a=DFA.Accept_State("q_a", position=rotate_vector(temp, 2*TAU/3)),
                )
        edges = dict(
                e1=DFA.DirectEdge(verts["q_0"], verts["q_1"], "0"),
                e2=DFA.DirectEdge(verts["q_1"], verts["q_a"], "1"),
                e3=DFA.CurvedEdge(verts["q_0"], verts["q_a"], "1"),
                e4=DFA.CurvedEdge(verts["q_a"], verts["q_0"], "1"),
                e5=DFA.Loop(verts["q_1"], "0"),
                )
        graph = DFA.Graph_Creator(verts, edges).create(0.75).shift(DOWN)
        for i, j in zip(graph[::2], graph[1::2]):

            self.play(Create(i), Create(j), run_time=0.5)
        self.wait(2)


with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
