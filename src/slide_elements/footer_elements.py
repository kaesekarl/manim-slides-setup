from manim import *
from src.designs.themes.CURRENT import APPLIED_THEME
import src.constants as constants

theme = APPLIED_THEME


class Footer_Separator:
    def __init__(self):
        self.theme = theme.Slide.Footer.Seperator

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


class Slide_Counter:
    def __init__(self, counter: int, total: int, with_total: bool = False):
        self.theme = theme.Slide.Footer.Counter
        self.counter = counter
        self.total = total
        self.with_total = with_total

    def create(self, counter: int = None):
        if counter is None:
            counter = self.counter
        if self.with_total:
            counter = f"{counter}/{self.total}"
        elements = Text(str(counter), weight=self.theme.weight, font=self.theme.font, color=self.theme.color).scale(self.theme.size)
        elements = elements.to_corner(DR, buff=self.theme.buff)
        return elements

    def increment(self, amount=1):
        self.counter += amount
