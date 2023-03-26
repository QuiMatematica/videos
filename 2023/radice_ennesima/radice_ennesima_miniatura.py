from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        l1 = MathTex(r"\sqrt[n]{a} = b")
        l1[0][0:3].set_color(YELLOW)
        l1[0][3].set_color(BLUE)
        l1[0][5].set_color(RED)
        l2 = MathTex(r"b^n = a")
        l2[0][1].set_color(YELLOW)
        l2[0][3].set_color(BLUE)
        l2[0][0].set_color(RED)

        gruppo = VGroup(l1, l2).scale(5).arrange(DOWN, buff=1.8)
        self.add(gruppo)

        self.wait(30)
