from manim import *
from manim_presentation import Slide
from src.designs.themes.CURRENT import APPLIED_THEME
import src.network_creator.DFA_network as DFA
import src.designs.layouts.kazut as kazut


theme = APPLIED_THEME
layout = kazut

config.background_color = theme.Background().color


class Scene1(Slide):
    def construct(self):
        test = layout.TitledSlide("Test").create()
        self. play(Create(test))


with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
