from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        equation = VGroup(
            MathTex(r"(2x + 1)^2 -3(2x - 1)(2x + 1) = -2(2x + 1)(2x - 3)"),
            MathTex(r"4x^2 +4x +1 -3(4x^2 - 1) = -2(4x^2 -6x + 2x - 3)"),
            MathTex(r"4x^2 +4x +1 -12x^2 + 3 = -8x^2 +12x -4x +6"),
            MathTex(r"-8x^2 +4x +4 = -8x^2 +8x +6"),
            MathTex(r"4x +4 = 8x +6"),
            MathTex(r"2x +2 = 4x +3"),
            MathTex(r"2 - 3 = 4x - 2x"),
            MathTex(r"-1 = 2x"),
            MathTex(r"-\dfrac{1}{2} = x"),
            MathTex(r"x = -\dfrac{1}{2}")
        ).scale(.7).arrange(DOWN)

        for s in equation:
            self.play(Write(s))
            self.wait(delay)
            self.next_section()

        new_part = VGroup(*[equation[_i] for _i in range(4, 10)])
        self.play(new_part.animate.set_color(RED).shift(3*RIGHT))

        old_part = VGroup(
            MathTex(r"-8x^2 +4x +8x^2 -8x = 6 -4"),
            MathTex(r"-4x = 2"),
            MathTex(r"x = \dfrac{2}{-4}"),
            MathTex(r"x = -\dfrac{1}{2}")
        ).set_color(GREEN).scale(.7).arrange(DOWN)
        old_part.move_to(new_part).shift(6*LEFT)

        self.play(Write(old_part))

        self.wait(60)
