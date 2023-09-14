from manim import *
from manim_presentation import Slide
from src.designs.themes.CURRENT import APPLIED_THEME
import src.network_creator.DFA_network as DFA
from src.designs.layouts.kazut import *
import src.slide_elements.footer_elements as footer_elements


theme = APPLIED_THEME
SLIDE_HEIGHT = 8
SLIDE_WIDTH = SLIDE_HEIGHT * 16 / 9


config.background_color = theme.Background.color


class Scene1(Slide):
    def construct(self):
        page = Kazut_TitledSlide.WithFooter("Ur Mama", 6, 9, True).create()
        self.add(page)
        self.wait(1)

        background = Rectangle(width=SLIDE_WIDTH, height=SLIDE_HEIGHT, color=BLACK, fill_opacity=1)
        text = Text(r"Ich hab gehört Brüning stinkt nach Maggi", color=WHITE, font="Consolas")
        self.play(FadeIn(background), page.animate.scale(1.5), FadeIn(text), run_time=2)
        self.wait(1)

        # verts = dict(
        #         A=DFA.State("A", LEFT * 2),
        #         B=DFA.State("B", RIGHT * 2),
        #         )
        # edges = dict(
        #         A_B=DFA.CurvedEdge(verts["A"], verts["B"], "a"),
        #         B_A=DFA.CurvedEdge(verts["B"], verts["A"], "b"),
        #         A_A=DFA.Loop(verts["A"], "a"),
        #         )
        # g = DFA.Graph_Creator(verts, edges).create(0.8)
        # self.play(FadeIn(g))
        self.wait(1)



with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
