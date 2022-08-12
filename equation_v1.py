from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.add(ImageMobject("img/paper.jpg").scale(3))

        equation = VGroup(
            MathTex(r"(2x + 1)^2 -3(2x - 1)(2x + 1) = -2(2x + 1)(2x - 3)"),
            MathTex(r"4x^2 +4x +1 -3(4x^2 - 1) = -2(4x^2 -6x + 2x - 3)"),
            MathTex(r"4x^2 +4x +1 -12x^2 + 3 = -8x^2 +12x -4x +6"),
            MathTex(r"-8x^2 +4x +4 = -8x^2 +8x +6"),
            MathTex(r"-8x^2 +4x +8x^2 -8x = 6 -4"),
            MathTex(r"-4x = 2"),
            MathTex(r"x = \dfrac{2}{-4}"),
            MathTex(r"x = -\dfrac{1}{2}")
        ).set_color(BLACK).scale(.7).arrange(DOWN, buff=0.40)

        for s in equation:
            self.play(Write(s))
            self.wait(delay)
            self.next_section()

        self.wait(60)
