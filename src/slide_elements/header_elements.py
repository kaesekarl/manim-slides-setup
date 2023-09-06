from manim import *
from src.designs.themes.CURRENT import APPLIED_THEME
import src.constants as constants

theme = APPLIED_THEME


class Header_Seperator:
    def __init__(self):
        self.theme = theme.Slide.Header.Seperator


    def create(self):
        seperator = DashedLine(
                start=constants.SLIDE_WIDTH/2 * LEFT,
                end=constants.SLIDE_WIDTH/2 * RIGHT,
                color=self.theme.color
                )
        seperator = seperator.to_edge(UP, buff=self.theme.buff)

        return seperator




