from manim import *
from src.designs.themes.CURRENT import APPLIED_THEME
import src.constants as constants

theme = APPLIED_THEME


class Footer_Separator:
    def __init__(self):
        self.theme = theme.Slide.Footer.Separator

    def create(self):
        seperator = DashedLine(
            start=constants.SLIDE_WIDTH / 2 * LEFT,
            end=constants.SLIDE_WIDTH / 2 * RIGHT,
            color=self.theme.color,
            dashed_ratio=self.theme.dashed_ratio,
            dash_length=self.theme.dash_length,
        )
        seperator = seperator.to_edge(DOWN, buff=self.theme.buff)
        return seperator

