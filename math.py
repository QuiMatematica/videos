from abc import ABC

from manim import *


class EqSystem(VMobject, ABC):

    def __init__(self, *equation_texs, **kwargs):
        super().__init__(**kwargs)
        eqs = VGroup()
        for tex in equation_texs:
            eqs.add(tex)
        eqs.arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\{")
        bracket.scale(2)
        bracket.stretch_to_fit_height(eqs.height + 2 * MED_SMALL_BUFF)
        bracket.next_to(eqs, LEFT, MED_SMALL_BUFF)
        self.add(bracket, eqs)
        self.center()
