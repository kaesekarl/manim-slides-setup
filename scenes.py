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
        page = Kazut_TitledSlide.WithFooter("DFA", 2, 3, True).create()
        self.play(Create(page))
        self.wait(1)

        background = Rectangle(width=SLIDE_WIDTH, height=SLIDE_HEIGHT, color=BLACK, fill_opacity=1)
        self.play(FadeIn(background), page.animate.scale(1.5))
        self.wait(1)


with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
