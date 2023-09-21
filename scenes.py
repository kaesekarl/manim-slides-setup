# Python Imports
from copy import deepcopy

# Manim Imports
from manim import *
from manim_presentation import Slide

# Tool Imports
import src.DFA_Creator.interface as DFA

# Presentation Imports
from src.designs.themes.CURRENT import APPLIED_THEME
from src.designs.layouts.CURRENT import APPLIED_LAYOUT

theme = APPLIED_THEME
layout = APPLIED_LAYOUT

SLIDE_HEIGHT = 8
SLIDE_WIDTH = SLIDE_HEIGHT * 16 / 9

config.background_color = theme.Background.color


class Scene1(Slide):
    def construct(self):
        page = layout.TitledSlide.WithFooter("Jahaha moin", 6, 9, with_total=True).create()
        self.add(page)
        self.wait(1)

        # background = Rectangle(width=SLIDE_WIDTH, height=SLIDE_HEIGHT, color=BLACK, fill_opacity=1)
        # text = Text(r"Ich hab gehört Brüning stinkt nach Maggi", color=WHITE, font="Consolas")
        # self.play(FadeIn(background), page.animate.scale(1.5), FadeIn(text), run_time=2)
        # self.wait(1)

        verts = [
                DFA.Start_State("A", LEFT * 2),
                DFA.State("B", RIGHT * 2 + UP * 2),
                DFA.Accept_State("C", RIGHT * 2 + DOWN * 2),
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
