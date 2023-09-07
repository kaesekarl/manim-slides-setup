from src.designs.themes.CURRENT import APPLIED_THEME
from manim import *

theme = APPLIED_THEME


class Bulletpoint_Creator:
    def __init__(self, *args):
        self.theme = theme.Text.Bulletpoints
        self.bulletpoints = [*args]

    def create(self):
        elements = VGroup()
        for bulletpoint in self.bulletpoints:
            elements.add(Text(f"• {bulletpoint}", font=self.theme.font).scale(self.theme.size))
        elements.arrange(DOWN, buff=self.theme.point_spacing)
        for element in elements:
            element.align_on_border(LEFT, buff=0.5)

        return elements
