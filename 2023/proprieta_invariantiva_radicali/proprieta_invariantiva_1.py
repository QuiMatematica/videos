from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        scale = 1.5
        big_scale = 3.5

        self.wait(.5)

        obiettivo_condizioni_1 = MathTex(r"n, m, p \in \mathbb{N} - \{0\}").scale(scale)
        obiettivo_condizioni_2 = MathTex(r"a \in \mathbb{R}; a \ge 0").scale(scale)
        obiettivo_riga_1 = VGroup(
            obiettivo_condizioni_1,
            obiettivo_condizioni_2
        ).arrange(DOWN)

        obiettivo_riga_2 = MathTex(r"\sqrt[n]{a^m} = \sqrt[n \cdot p]{a^{m \cdot p}").scale(big_scale)

        obiettivo = VGroup(
            obiettivo_riga_1,
            obiettivo_riga_2
        ).arrange(DOWN, buff=1)

        titolo = Title("Proprietà invariantiva")

        radicale_1 = MathTex(r"\sqrt[n]{a^m").scale(big_scale)
        radicale_1[0][0].set_color(YELLOW)
        radicale_1[0][3].set_color(GREEN)
        radicale_1[0][4].set_color(RED)
        self.play(Write(radicale_1))
        self.wait(delay)
        self.next_section()

        self.play(Wiggle(radicale_1[0][0], scale_value=2))
        self.wait(delay)
        self.next_section()

        self.play(Wiggle(radicale_1[0][3], scale_value=2))
        self.play(Wiggle(radicale_1[0][4], scale_value=2))
        self.wait(delay)
        self.next_section()

        self.wait(30)

