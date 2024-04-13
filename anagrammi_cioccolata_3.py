import itertools

from manim import *

DELAY = 1
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3
CARDS_BUFF = SMALL_BUFF


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        titolo = Title("Permutazioni", color=RED).scale(2)
        titolo.underline.set_color(RED)
        self.play(Write(titolo))

        formula_generica = MathTex(r"P_n {{ = n! }}").scale(2)
        formula_esempio = MathTex(r"P_4 {{ = 4! }} = 4 \cdot 3 \cdot 2 \cdot 1 {{ = 24 }}").scale(2)

        VGroup(formula_generica, formula_esempio).arrange(DOWN, buff=1)

        for _i in formula_generica:
            self.play(Write(_i))
            self.cut_and_wait()

        for _i in formula_esempio:
            self.play(Write(_i))
            self.cut_and_wait()

        self.wait(30)
