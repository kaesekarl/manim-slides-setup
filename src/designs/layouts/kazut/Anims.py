from manim import *

__all__ = [
    "Vanish",
    "UnVanish"
        ]


class Vanish(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.mobject.set_opacity(1 - alpha).scale(1 + 0.3*alpha)


class UnVanish(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.mobject.set_opacity(alpha).scale(1 - (1/1.3 * alpha))



