from src.designs.themes import APPLIED_THEME
from manim import *

theme = APPLIED_THEME


class Bulletpoint_Creator:
    def __init__(self, *args, size=None):
        self.theme = theme.Text.Lists.Bulletpoints
        self.bulletpoints = [*args]
        if size is None:
            self.size = self.theme.size

    def create(self, *bulletpoints, size=None):
        if bulletpoints is None:
            bulletpoints = self.bulletpoints
        if size is None:
            size = self.size

        elements = VGroup()
        for bulletpoint in bulletpoints:
            elements.add(Text(f"• {bulletpoint}", font=self.theme.font).scale(size))
        elements.arrange(DOWN, buff=self.theme.point_spacing)
        for element in elements:
            element.align_on_border(LEFT, buff=0.5)

        return elements


class Numbered_List_Creator:
    def __init__(self, *args, size=None):
        self.theme = theme.Text.Lists.Numbered
        self.bulletpoints = [*args]
        if size is None:
            self.size = self.theme.size

    def create(self, *bulletpoints, size=None):
        if bulletpoints is None:
            bulletpoints = self.bulletpoints
        if size is None:
            size = self.size

        elements = VGroup()
        for i, bulletpoint in enumerate(bulletpoints):
            elements.add(Text(f"{i+1}. {bulletpoint}", font=self.theme.font).scale(size))
        elements.arrange(DOWN, buff=self.theme.point_spacing)
        for element in elements:
            element.align_on_border(LEFT, buff=0.5)

        return elements

