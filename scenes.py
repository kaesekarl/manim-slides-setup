from manim import *
from manim_presentation import Slide
from src.designs.themes.CURRENT import APPLIED_THEME
import src.network_creator.DFA_network as DFA
import src.designs.layouts.kazut as kazut
import src.slide_elements.footer_elements as footer_elements


theme = APPLIED_THEME
layout = kazut

config.background_color = theme.Background.color


class Scene1(Slide):
    def construct(self):
        page = layout.
        self.play(Create(page))
        self.wait(2)




with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
