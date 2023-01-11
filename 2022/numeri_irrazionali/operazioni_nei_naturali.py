from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        scala_testi = 1.5

        titolo = Tex(r"$\mathbb{N}$: numeri naturali", color=YELLOW).scale(scala_testi).to_edge(UP)
        self.play(Write(titolo))
        self.wait(delay)
        self.next_section()

        operazioni = VGroup(
            MathTex(r"2 + 3 = 5"),
            MathTex(r"2 \cdot 3 = 6"),
            MathTex(r"2 - 3 = \, ?"),
            MathTex(r"2 : 3 = \, ?")).scale(scala_testi).arrange(DOWN)

        for _i in operazioni:
            self.play(Write(_i, run_time=.5))

        self.wait(5)
        self.next_section()

        titolo2 = Tex(r"$\mathbb{Z}$: numeri interi", color=YELLOW).scale(scala_testi).move_to(titolo)
        sottrazione = MathTex(r"2 - 3 = -1").scale(scala_testi).move_to(operazioni[2])

        self.play(Transform(titolo, titolo2), Transform(operazioni[2], sottrazione))

        self.wait(5)
        self.next_section()

        titolo3 = Tex(r"$\mathbb{Q}$: numeri razionali", color=YELLOW).scale(scala_testi).move_to(titolo)
        divisione = MathTex(r"2 : 3 = 2/3").scale(scala_testi).move_to(operazioni[3])

        self.play(Transform(titolo, titolo3), Transform(operazioni[3], divisione))

        self.wait(5)
        self.next_section()
