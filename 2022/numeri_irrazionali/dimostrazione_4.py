from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        scala = 1.1

        # equivalenza = MathTex(r"a^2 = 2 b^2")
        primi_fra_loro = Tex(r"$a$ e $b$ primi fra loro", color=YELLOW)
        caso_1 = Tex(r"1) $a$ multiplo di 2 e $b$ non multiplo di 2")
        caso_2 = Tex(r"2) $b$ multiplo di 2 e $a$ non multiplo di 2")
        caso_3 = Tex(r"3) $a$ e $b$ non multipli di 2")

        group = VGroup(primi_fra_loro, caso_1, caso_2, caso_3).scale(scala).arrange(DOWN, buff=.4)

        for _s in group:
            self.play(Write(_s))
            self.wait(delay)
            self.next_section()



