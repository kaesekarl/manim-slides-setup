from src.text_elements.Blocks import ColorBlock
from src.designs.themes import APPLIED_THEME, FallbackDictWrapper

__all__ = ["Red_ColorBlock",
           "Orange_ColorBlock",
           "Yellow_ColorBlock",
           "Green_ColorBlock",
           "Cyan_ColorBlock",
           "Blue_ColorBlock",
           "Purple_ColorBlock"
           ]

theme = FallbackDictWrapper(APPLIED_THEME, "Text Blocks")



class Red_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Red color"], pos, size, text_color)


class Orange_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Orange color"], pos, size, text_color)


class Yellow_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Yellow color"], pos, size, text_color)


class Green_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Green color"], pos, size, text_color)


class Cyan_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Cyan color"], pos, size, text_color)


class Blue_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Blue color"], pos, size, text_color)


class Purple_ColorBlock(ColorBlock):
    def __init__(self, title, text, pos, size=None, text_color=None):
        super().__init__(title, text, theme["Purple color"], pos, size, text_color)
