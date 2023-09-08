from manim import *
from src.slide_elements.header_elements import Header_Seperator
from src.slide_elements.footer_elements import Slide_Counter, Footer_Separator
from src.text_elements.titles import SlideTitle
from src.text_elements.bulletpoints import Bulletpoint_Creator
from src.designs.themes.CURRENT import APPLIED_THEME

theme = APPLIED_THEME


class TitledSlide:
    def __init__(self, title: str):
        self.seperator = Header_Seperator()
        self.title = SlideTitle(title)

    def create(self):
        elements = VGroup()
        elements.add(self.seperator.create())
        elements.add(self.title.create())
        return elements





class CoverSlide:
    def __init__(self, title: str, subtitle: str, author: str):
        self.theme = theme.Slide.Cover
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
        elements.add(Text(self.author, weight=self.theme.author_weight, font=self.theme.author_font, color=self.theme.author_color).scale(self.theme.author_size).
                     align_to(elements[2], DOWN + LEFT).shift(DOWN * 0.66))  # Author
        return elements






