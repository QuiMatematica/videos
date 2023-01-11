from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        scala = 1.1

        caso_1 = Tex(r"3) $a$ e $b$ non multipli di 2", color=YELLOW)
        l1 = MathTex(r"a^2 = {{ \dots }}")
        l3 = MathTex(r"b^2 = {{ \dots }}")
        l4 = MathTex(r"a^2 {{ = 2 }} b^2")
        l5 = MathTex(r"\dots {{ = 2 }} \cdot {{ \dots }}")
        l6 = Tex(r"Assurdo.")

        group = VGroup(caso_1, l1, l3, l4, l5, l6).scale(scala).arrange(DOWN, buff=.4)

        self.play(Write(caso_1))
        self.wait(delay)
        self.next_section()

        self.play(Write(l1))
        self.wait(delay)
        self.next_section()

        self.play(Write(l3))
        self.wait(delay)
        self.next_section()

        self.play(Write(l4))
        self.wait(delay)
        self.next_section()

        self.play(l1[1].copy().animate.move_to(l5[0]).shift(.15*DOWN))
        self.play(l4[1].copy().animate.move_to(l5[1]))
        self.play(Write(l5[2]), l3[1].copy().animate.move_to(l5[3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(l6))
        self.wait(delay)
        self.next_section()
