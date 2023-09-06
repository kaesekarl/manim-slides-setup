from manim import *
from src.designs.themes.CURRENT import APPLIED_THEME

theme = APPLIED_THEME


class SlideTitle:
    def __init__(self, text=None):
        self.text = text
        self.theme = theme.Slide.Title

    def create(self, title: str = None):
        if title is None:
            title = self.text
        title = Text(title, color=self.theme.color, font=self.theme.font)
        title = title.scale(self.theme.size).to_corner(UL, buff=0.45)
        return title







