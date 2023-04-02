from manim import *

import util


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        quadrato = MathTex(r"99225 = 3^4 \cdot 5^2 \cdot 7^2").scale(2)
        quadrato[0][6].set_color(RED)
        quadrato[0][7].set_color(GREEN)
        quadrato[0][9].set_color(ORANGE)
        quadrato[0][10].set_color(GREEN)
        quadrato[0][12].set_color(YELLOW)
        quadrato[0][13].set_color(GREEN)

        radice = MathTex(r"\sqrt{99225} = 3^2 \cdot 5 \cdot 7 = 315").scale(2)
        radice[0][8].set_color(RED)
        radice[0][9].set_color(GREEN)
        radice[0][11].set_color(ORANGE)
        radice[0][13].set_color(YELLOW)

        VGroup(quadrato, radice).arrange(DOWN, buff=1)

        self.play(Write(quadrato[0][0:5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(quadrato[0][5:]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice[0][:7]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice[0][7:]))

        self.wait(30)
