from src.slide_elements.header_elements import Header_Seperator, SlideTitle
from src.slide_elements.footer_elements import Slide_Counter, Footer_Separator

from manim import VGroup


class TitledSlide:

    def __init__(self, title: str):
        self.header_seperator = Header_Seperator()
        self.title = SlideTitle(title)

    def create(self):
        elements = VGroup()
        elements.add(self.header_seperator.create())
        elements.add(self.title.create())
        return elements.set_z_index(10)

    class WithFooter:

        def __init__(self, title: str, counter: int, total: int, with_total: bool = False):
            self.header_seperator = Header_Seperator()
            self.footer_seperator = Footer_Separator()
            self.title = SlideTitle(title)
            self.slide_counter = Slide_Counter(counter, total, with_total)

        def create(self):
            elements = VGroup()
            elements.add(self.header_seperator.create())
            elements.add(self.title.create())
            elements.add(self.footer_seperator.create())
            elements.add(self.slide_counter.create())
            return elements.set_z_index(10)

