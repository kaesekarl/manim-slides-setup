from manim import *
from manim_presentation import Slide
import src.constants.colors as cols

config.background_color = cols.background


class Scene1(Slide):
    def construct(self):
        text = Text("Hello world!")
        self.add(text)
