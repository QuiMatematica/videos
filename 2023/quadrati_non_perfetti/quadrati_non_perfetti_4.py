from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 3

        self.wait(1)

        riga_1 = MathTex(r"\sqrt{30} = {{ \sqrt{30} }}").scale(scale)
        riga_2 = MathTex(r"30 = 2^1 \cdot 3^1 \cdot 5^1").scale(scale)

        VGroup(riga_1, riga_2).arrange(DOWN, buff=1)

        domanda = Tex("?").scale(scale).move_to(riga_1[1])

        self.play(Write(riga_1[0]))
        self.play(Write(domanda))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_2))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(domanda), FadeIn(riga_1[1]))
        self.wait(30)

