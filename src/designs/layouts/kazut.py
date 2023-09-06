from manim import *
from src.slide_elements.header_elements import Header_Seperator
from src.text_elements.titles import SlideTitle


class TitledSlide:
    def __init__(self, title: str):
        self.seperator = Header_Seperator()
        self.title = SlideTitle(title)

    def create(self):
        elements = VGroup()
        elements.add(self.seperator.create())
        elements.add(self.title.create())
        return elements

