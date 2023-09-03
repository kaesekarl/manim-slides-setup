from manim import *
from manim_presentation import Slide
from src.constants import colors


theme = colors.DarkTheme()
config.background_color = theme.Background().color


class Scene1(Slide):
    def construct(self):
        text = Text("Hello world!")
        self.add(text)
