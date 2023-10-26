from manim import *

__all__ = [
    "Vanish",
    "UnVanish"
        ]


class Vanish(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        temp = self.mobject.copy()
        temp.set_opacity(1-alpha)
        temp.scale(1 + 0.7*alpha)
        return temp


class UnVanish(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        temp = self.mobject.copy()
        temp.set_opacity(alpha)
        temp.scale(1/(1 + 0.7*alpha))
        return temp



