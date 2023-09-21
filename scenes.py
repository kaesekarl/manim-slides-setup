from manim import *
from manim_presentation import Slide
from src.designs.themes.CURRENT import APPLIED_THEME
import src.network_creator.DFA_network as DFA
from src.designs.layouts.kazut import *
import src.slide_elements.footer_elements as footer_elements

from copy import deepcopy


theme = APPLIED_THEME
SLIDE_HEIGHT = 8
SLIDE_WIDTH = SLIDE_HEIGHT * 16 / 9


config.background_color = theme.Background.color


class Scene1(Slide):
    def construct(self):
        page = Kazut_TitledSlide.WithFooter("Ur Mama", 6, 9, True).create()
        self.add(page)
        self.wait(1)

        # background = Rectangle(width=SLIDE_WIDTH, height=SLIDE_HEIGHT, color=BLACK, fill_opacity=1)
        # text = Text(r"Ich hab gehört Brüning stinkt nach Maggi", color=WHITE, font="Consolas")
        # self.play(FadeIn(background), page.animate.scale(1.5), FadeIn(text), run_time=2)
        # self.wait(1)

        verts = [
                DFA.State("A", LEFT * 2),
                DFA.State("B", RIGHT * 2 + UP * 2),
                DFA.State("C", RIGHT * 2 + DOWN * 2),
                ]
        edges = [
                DFA.CurvedEdge(verts[0], verts[1], "a"),
                DFA.CurvedEdge(verts[1], verts[0], "b"),
                DFA.Loop(verts[0], "a"),
                DFA.CurvedEdge(verts[1], verts[2], "a"),
                DFA.CurvedEdge(verts[2], verts[0], "b"),
                ]
        verts1, edges1 = verts[:2], edges[:3]
        verts2, edges2 = verts[2:], edges[3:]
        g = DFA.Graph_Creator(verts1, edges1, 0.8).create()
        g2 = DFA.Graph_Creator(verts2, edges2, 0.8).create()
        self.play(Create(g))
        self.play(TransformFromCopy(g, g2))



        self.wait(1)



with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
