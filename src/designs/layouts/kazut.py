from manim import VGroup, DashedLine, Text, LEFT, UP, DOWN
from src.slide_elements.header_elements import Header_Seperator, SlideTitle
from src.slide_elements.footer_elements import Slide_Counter, Footer_Separator
from src.designs.themes.CURRENT import APPLIED_THEME

_theme = APPLIED_THEME
__all__ = ["TitledSlide",
           "CoverSlide"]


class TitledSlide:

    def __init__(self, title: str):
        self.header_seperator = Header_Seperator()
        self.title = SlideTitle(title)

    def create(self):
        elements = VGroup()
        elements.add(self.header_seperator.create())
        elements.add(self.title.create())
        return elements

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
            return elements


class CoverSlide:

    def __init__(self, title: str, subtitle: str, author: str):
        self.theme = _theme.Slide.Cover
        self.title = title
        self.subtitle = subtitle
        self.author = author

    def create(self):
        elements = VGroup()
        elements.add(DashedLine(color=self.theme.separator_color, start=[-6, 1, 0], end=[6, 1, 0], dashed_ratio=0.5, dash_length=0.07))  # Underline of Title
        elements.add(Text(self.title, weight=self.theme.title_weight, font=self.theme.title_font, color=self.theme.title_color).scale(self.theme.title_size).
                     align_to(elements[0], LEFT + UP).shift(UP * 0.66))  # Title
        elements.add(Text(self.subtitle, weight=self.theme.subtitle_weight, font=self.theme.subtitle_font, color=self.theme.subtitle_color).scale(
                self.theme.subtitle_size).
                     align_to(elements[0], DOWN + LEFT).shift(DOWN))  # Subtitle
        elements.add(
            Text(self.author, weight=self.theme.author_weight, font=self.theme.author_font, color=self.theme.author_color).scale(self.theme.author_size).
            align_to(elements[2], DOWN + LEFT).shift(DOWN * 0.66))  # Author
        return elements
