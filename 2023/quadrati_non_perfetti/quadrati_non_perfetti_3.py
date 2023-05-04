from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 3

        self.wait(1)

        riga_1 = MathTex(r"\sqrt{17} = {{ \sqrt{17} }}").scale(scale)
        riga_2 = MathTex(r"17 = 17^1").scale(scale)

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

