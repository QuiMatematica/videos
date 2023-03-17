from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 2

        self.wait(1)

        radice_quadrata = MathTex(r"\sqrt[4]{16} = 2 \,\,\Longleftrightarrow\,\, 2^4 = 16")
        radice_quadrata[0][:3].set_color(YELLOW)
        radice_quadrata[0][10].set_color(YELLOW)
        radice_quadrata[0][3:5].set_color(GREEN)
        radice_quadrata[0][12:].set_color(GREEN)
        radice_quadrata[0][6].set_color(RED)
        radice_quadrata[0][9].set_color(RED)

        radice_cubica = MathTex(r"\sqrt[5]{32} = 2 \,\,\Longleftrightarrow\,\, 2^5 = 32")
        radice_cubica[0][:3].set_color(YELLOW)
        radice_cubica[0][10].set_color(YELLOW)
        radice_cubica[0][3:5].set_color(GREEN)
        radice_cubica[0][12:].set_color(GREEN)
        radice_cubica[0][6].set_color(RED)
        radice_cubica[0][9].set_color(RED)

        VGroup(radice_quadrata, MathTex("x"), radice_cubica).scale(scale).arrange(DOWN)

        self.play(Write(radice_quadrata))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_cubica))

        self.wait(30)
