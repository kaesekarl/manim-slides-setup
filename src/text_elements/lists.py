from src.designs.themes import APPLIED_THEME, FallbackDictWrapper
from manim import *

theme = FallbackDictWrapper(APPLIED_THEME, "Text Lists")


class Bulletpoint_Creator:
    def __init__(self, *args, size=None):
        self.theme = theme
        self.bulletpoints = [*args]
        if size is None:
            self.size = self.theme["Bulletpoints size"]

    def create(self, *bulletpoints, size=None):
        if len(bulletpoints) == 0:
            bulletpoints = self.bulletpoints
        if size is None:
            size = self.size

        elements = VGroup()
        for bulletpoint in bulletpoints:
            elements.add(Text(f"• {bulletpoint}", font=self.theme["Bulletpoints text_font"]).scale(size))
        elements.arrange(DOWN, buff=self.theme["Bulletpoints point_spacing"])
        for element in elements:
            element.align_on_border(LEFT, buff=0.5)

        return elements


class Numbered_List_Creator:
    def __init__(self, *args, size=None):
        self.theme = theme
        self.bulletpoints = [*args]
        if size is None:
            self.size = self.theme["Numbered size"]

    def create(self, *bulletpoints, size=None):
        if len(bulletpoints) == 0:
            bulletpoints = self.bulletpoints
        if size is None:
            size = self.size

        elements = VGroup()
        for i, bulletpoint in enumerate(bulletpoints):
            elements.add(Text(f"{i+1}. {bulletpoint}", font=self.theme["Numbered text_font"]).scale(size))
        elements.arrange(DOWN, buff=self.theme["Numbered point_spacing"])
        for element in elements:
            element.align_on_border(LEFT, buff=0.5)

        return elements

