from manim import *


class Grid_Helper:
    def __init__(self):
        self.grid = VGroup()
        self.grid.add(self.create_grid())

    def create_grid(self):
        grid = VGroup()
        # Horizontal and vertical lines with coordinates and colored x and y axis
        for i in range(-10, 11):
            if i == 0:
                grid.add(Line(LEFT * 10, RIGHT * 10, color=RED, stroke_width=2))
                grid.add(Line(UP * 10, DOWN * 10, color=GREEN, stroke_width=2))
            else:
                grid.add(Line(LEFT * 10 + UP * i, RIGHT * 10 + UP * i, color=GREY_B, stroke_width=1))
                grid.add(Line(LEFT * 10 + DOWN * i, RIGHT * 10 + DOWN * i, color=GREY_B, stroke_width=1))
                grid.add(Line(UP * 10 + LEFT * i, DOWN * 10 + LEFT * i, color=GREY_B, stroke_width=1))
                grid.add(Line(UP * 10 + RIGHT * i, DOWN * 10 + RIGHT * i, color=GREY_B, stroke_width=1))

            # numbers on the edge of the screen
            if i != 0:
                grid.add(Text(str(i)).next_to(UP * i, LEFT * 0.5).scale(0.5))
                grid.add(Text(str(i)).next_to(LEFT * i, DOWN * 0.5).scale(0.5))

        return grid

