from manim import *

DELAY = 30

SCALE = 3


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        radicali = VGroup(
            MathTex(r"\sqrt{2}").scale(SCALE),
            MathTex(r"\sqrt[4]{3}").scale(SCALE),
            MathTex(r"\sqrt[3]{4}").scale(SCALE)
        ).arrange(RIGHT, buff=SCALE)

        righe = VGroup(
            radicali,
            Tex("in ordine crescente").scale(SCALE)
        ).arrange(DOWN, buff=2)

        for _i in range(3):
            self.play(Write(radicali[_i]))
            self.cut_and_wait()

        self.play(Write(righe[1]))
        self.wait(30)
