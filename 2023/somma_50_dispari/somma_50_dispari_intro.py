from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)
        somma = VGroup(
            MathTex(r"1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 \,+"),
            MathTex(r"+\, 21 + 23 + 25 + 27 + 29 + 31 + 33 + 35 \,+"),
            MathTex(r"+\, 37 + 39 + 41 + 43 + 45 + 47 + 49 + 51 \,+"),
            MathTex(r"+\, 53 + 55 + 57 + 59 + 61 + 63 + 65 + 67 \,+"),
            MathTex(r"+\, 69 + 71 + 73 + 75 + 77 + 79 + 81 + 83 \,+"),
            MathTex(r"+\, 85 + 87 + 89 + 91 + 93 + 95 + 97 + 99 ="),
            MathTex(r"= \,\,?").scale(2)
        ).scale(1.5).arrange(DOWN)
        somma[0].match_width(somma[1])
        self.play(Write(somma, run_time=3))
        self.wait(30)
