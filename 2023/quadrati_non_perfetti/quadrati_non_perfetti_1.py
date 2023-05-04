from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 2

        self.wait(1)

        riga_1 = Tex("$n$ quadrato perfetto").scale(scale)
        riga_2 = MathTex(r"\sqrt{n} \in \mathbb{Z}").scale(scale)
        riga_3 = Tex("36 quadrato perfetto").scale(scale)
        riga_4 = MathTex(r"\sqrt{36} = 6 \in \mathbb{Z}").scale(scale)

        gruppo_1 = VGroup(riga_1, riga_2).arrange(DOWN)
        gruppo_2 = VGroup(riga_3, riga_4).arrange(DOWN)

        gruppo = VGroup(gruppo_1, gruppo_2).arrange(DOWN, buff=2)

        self.play(Write(riga_1))
        self.wait(delay)
        self.next_section()
        self.play(Write(riga_2))
        self.wait(delay)
        self.next_section()
        self.play(Write(riga_3))
        self.wait(delay)
        self.next_section()
        self.play(Write(riga_4))

        self.wait(30)