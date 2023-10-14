# Python Imports
from copy import deepcopy
from dataclasses import dataclass

# Manim Imports
from manim import *
from manim_presentation import Slide

# Tool Imports
import src.DFA_Creator as DFA

# Presentation Imports
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper
from src.designs.layouts import APPLIED_LAYOUT

theme = FallbackDictWrapper(APPLIED_THEME)
layout = APPLIED_LAYOUT

SLIDE_HEIGHT = 8
SLIDE_WIDTH = SLIDE_HEIGHT * 16 / 9

config.background_color = theme["Background color"]


class Scene1(Slide):
    def construct(self):
        page = layout.TitledSlide.WithFooter("Jahaha moin", 6, 9, with_total=True).create()
        self.add(page)
        self.wait(1)

        A = DFA.Start_Accept_State("A", LEFT * 2)       # 0:2
        B = DFA.State("B", RIGHT * 3.5 + UP * 2)          # 2:4
        C = DFA.Accept_State("C", RIGHT * 2 + DOWN * 2) # 4:6

        a_b = DFA.CurvedEdge(A, B, "a")     # 6:8
        b_a = DFA.CurvedEdge(B, A, "b")     # 8:10
        a_a = DFA.Loop(A, "a")                  # 10:12
        b_c = DFA.DirectEdge(B, C, "a")     # 12:14
        c_a = DFA.DirectEdge(C, A, "b")     # 14:16

        g = DFA.Graph_Creator([A, B, C], [a_b, b_a, a_a, b_c, c_a], 0.8).create()

        g1 = g[0:4] + g[6:12] # vertices (with labels) + edges (with labels)
        g2 = g[4:6] + g[12:16] # vertices (with labels) + edges (with labels)

        self.play(FadeIn(g1))
        self.play(TransformFromCopy(g1, g2))
        self.wait(1)


class Scene2(Slide):
    def construct(self):
        cover = layout.CoverSlide("Jahaha moin", "Der allerechte Hase", "Das heißt Red").create()
        self.wait(1)
        self.add(cover)
        self.wait(1)
        self.pause()
        self.remove(cover)
        self.wait(1)


class Scene3(Slide):
    def construct(self):
        sl = layout.TitledSlide.WithFooter("Jahaha moin", 6, 9, with_total=True).create()
        self.add(sl)
        self.wait(1)

        title = r"Title, der diesmal etwas länger ist"
        text = r"Text, der hier auch mal in mehreren Zeilen stattfindet Text, der hier auch mal in mehreren Zeilen stattfindet Text, " \
                r"der hier auch mal in mehreren Zeilen stattfindet Text, der hier auch mal in mehreren Zeilen stattfindet Text, " \
                r"der hier auch mal in mehreren Zeilen stattfindet Text, der hier auch mal in mehreren Zeilen stattfindet Text "

        block_list = ([layout.Red_ColorBlock, layout.Orange_ColorBlock, layout.Yellow_ColorBlock, layout.Green_ColorBlock, layout.Cyan_ColorBlock,
                       layout.Blue_ColorBlock,
                      layout.Purple_ColorBlock])
        blocks = [b(title, text, ORIGIN).create() for b in block_list]

        for b in blocks:
            self.play(FadeIn(b))
            self.wait(1)
            self.play(FadeOut(b))

        self.wait(1)


class Scene4(Slide):
    def construct(self):
        pass


with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene3()
    scene.render()
