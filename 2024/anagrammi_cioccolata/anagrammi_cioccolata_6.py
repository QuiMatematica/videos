from manim import *

DELAY = 30
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3
CARDS_BUFF = .2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        formula = MathTex(
            r"\dfrac{P_4}{P_2} {{ = \dfrac{4!}{2!} }} = \dfrac{4 \cdot 3 \cdot 2 \cdot 1}{2 \cdot 1} {{ = \dfrac{24}{2} }} = 12",
            color=YELLOW).scale(1.5)

        for _i in range(5):
            self.play(Write(formula[_i]))
            self.cut_and_wait()

        self.wait(30)
