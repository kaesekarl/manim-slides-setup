# Python Imports
from copy import deepcopy
from dataclasses import dataclass

# Manim Imports
from manim import *
from manim_presentation import Slide

# Tool Imports
import src.DFA_Creator as DFA
from src.utils.display_grid import Grid_Helper

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

        self.play(FadeIn(g))
        # self.play(TransformFromCopy(g1, g2))
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

        self.wait(1)


class Scene4(Slide):
    def construct(self):
        sl = layout.TitledSlide.WithFooter("Jahaha moin", 6, 9, with_total=True).create()
        def_block = layout.Text_Blocks.Cyan_ColorBlock(r"Definition: $\mathbb{N}$", r"Hier kommt eine Definition von $$\sum^n_{i=0} i = \frac{n (n+1)}{2}$$ "
                                                                                    r"hin", ORIGIN).create()
        self.add(def_block, sl)
        self.wait()
        self.play(layout.Vanish(sl))

        l = layout.Numbered_List_Creator("Bulletpoint 1", "Bulletpoint 2", "Bulletpoint 3").create()

        self.play(Write(l), layout.UnVanish(sl))
        self.wait(1)


class Scene5(Slide):
    def construct(self):
        self.add(Grid_Helper().grid)
        self.wait(1)




with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene4()
    scene.render()
