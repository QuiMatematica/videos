from manim import *

from qui_matematica.qmath import EqSystem

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        equazione = MathTex(r"y= 2x^2 - 4x + 5").to_edge(UP)

        self.play(Write(equazione))
        self.cut_and_wait()

        asse = VGroup(
            MathTex(r"\text{asse}:", color=YELLOW),
            MathTex(r"x = {{ -\dfrac{b}{2a} }}")
        ).arrange(RIGHT)

        vertice = VGroup(
            MathTex(r"\text{vertice}: ", color=YELLOW),
            EqSystem(MathTex(r"x_V = 1"), MathTex(r"y_V = {{ a x_V^2 + b x_V + c }}"))
        ).arrange(RIGHT)

        fuoco = VGroup(
            MathTex(r"\text{fuoco}:", color=YELLOW),
            EqSystem(MathTex(r"x_F = 1"), MathTex(r"y_F = {{ y_V + \dfrac{1}{4a} }}"))
        ).arrange(RIGHT)

        direttrice = VGroup(
            MathTex(r"\text{direttrice}:", color=YELLOW),
            MathTex(r"y = {{ y_V - \dfrac{1}{4a} }}")
        ).arrange(RIGHT)

        gruppo = VGroup(
            VGroup(vertice, asse).arrange(DOWN, aligned_edge=LEFT, buff=1),
            VGroup(fuoco, direttrice).arrange(DOWN, aligned_edge=LEFT, buff=1)
        ).arrange(RIGHT, buff=.5).shift(.5 * DOWN)

        self.play(
            Write(asse[0]),
            Write(vertice[0]),
            Write(fuoco[0]),
            Write(direttrice[0]),
        )
        self.cut_and_wait()

        # ASSE

        self.play(Write(asse[1]))
        self.cut_and_wait()

        asse_1 = MathTex(r"-\dfrac{-4}{2 \cdot 2}").move_to(asse[1][1]).shift(.2 * RIGHT)
        self.play(Transform(asse[1][1], asse_1))

        asse_2 = MathTex(r"1").move_to(asse[1][1]).shift(- .5 * RIGHT)
        self.play(Transform(asse[1][1], asse_2))
        self.cut_and_wait()

        # ASCISSA FUOCO E VERTICE

        self.play(Write(vertice[1].bracket))
        self.play(Write(vertice[1].eqs[0]))
        self.play(Write(fuoco[1].bracket))
        self.play(Write(fuoco[1].eqs[0]))
        self.cut_and_wait()

        # ORDINATA VERTICE

        self.play(Write(vertice[1].eqs[1]))
        self.cut_and_wait()

        vertice_1 = MathTex(r"2 \cdot 1^2 - 4 \cdot 1 + 5").move_to(vertice[1].eqs[1][1]).shift(.1 * RIGHT)
        self.play(Transform(vertice[1].eqs[1][1], vertice_1))
        self.wait(1)

        vertice_2 = MathTex(r"3").move_to(vertice[1].eqs[1][1]).shift(1.55 * LEFT)
        self.play(Transform(vertice[1].eqs[1][1], vertice_2))
        self.cut_and_wait()

        # ORDINATA FUOCO

        self.play(Write(fuoco[1].eqs[1]))
        self.cut_and_wait()

        fuoco_1 = MathTex(r"3 + \dfrac{1}{8}").move_to(fuoco[1].eqs[1][1]).shift(.28 * LEFT)
        self.play(Transform(fuoco[1].eqs[1][1], fuoco_1))
        self.wait(1)

        fuoco_2 = MathTex(r"\dfrac{25}{8}").move_to(fuoco[1].eqs[1][1]).shift(.28 * LEFT)
        self.play(Transform(fuoco[1].eqs[1][1], fuoco_2))
        self.cut_and_wait()

        # DIRETTRICE

        self.play(Write(direttrice[1]))
        self.cut_and_wait()

        direttrice_1 = MathTex(r"3 - \dfrac{1}{8}").move_to(direttrice[1][1]).shift(.28 * LEFT)
        self.play(Transform(direttrice[1][1], direttrice_1))
        self.wait(1)

        direttrice_2 = MathTex(r"\dfrac{23}{8}").move_to(direttrice[1][1]).shift(.28 * LEFT)
        self.play(Transform(direttrice[1][1], direttrice_2))

        self.wait(30)
