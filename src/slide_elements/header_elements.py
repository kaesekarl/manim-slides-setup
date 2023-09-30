from manim import *
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper
import src.constants as constants

theme = APPLIED_THEME


class Header_Seperator:
    def __init__(self):
        self.theme = FallbackDictWrapper(theme, "Slide Header Seperator")

    def create(self):
        seperator = Line(
                start=constants.SLIDE_WIDTH/2 * LEFT,
                end=constants.SLIDE_WIDTH/2 * RIGHT,
                color=self.theme["color"],
                )
        seperator = seperator.to_edge(UP, buff=self.theme["buff"])
        return seperator


class SlideTitle:
    def __init__(self, text=None):
        self.text = text
        self.theme = FallbackDictWrapper(theme, "Slide Header Title")

    def create(self, title: str = None):
        if title is None:
            title = self.text
        title = Text(title, color=self.theme["color"], font=self.theme["font"])
        title = title.scale(self.theme["size"]).to_corner(UL, buff=self.theme["buff"])
        return title

