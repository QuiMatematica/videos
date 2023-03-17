from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 2

        self.wait(1)

        pari = MathTex(r"n \text{ pari:}")
        pari[0][0].set_color(YELLOW)

        radice_quadrata = MathTex(r"\sqrt[n]{a} = b \,\,\Longleftrightarrow\,\, b^n = a")
        radice_quadrata[0][:3].set_color(YELLOW)
        radice_quadrata[0][9].set_color(YELLOW)
        radice_quadrata[0][3].set_color(GREEN)
        radice_quadrata[0][11].set_color(GREEN)
        radice_quadrata[0][5].set_color(RED)
        radice_quadrata[0][8].set_color(RED)

        ce_radice_quadrata = MathTex(r"a \ge 0 \quad b \ge 0")
        ce_radice_quadrata[0][0].set_color(GREEN)
        ce_radice_quadrata[0][3].set_color(RED)

        dispari = MathTex(r"n \text{ dispari:}")
        dispari[0][0].set_color(YELLOW)

        radice_cubica = MathTex(r"\sqrt[n]{a} = b \,\,\Longleftrightarrow\,\, b^n = a")
        radice_cubica[0][:3].set_color(YELLOW)
        radice_cubica[0][9].set_color(YELLOW)
        radice_cubica[0][3].set_color(GREEN)
        radice_cubica[0][11].set_color(GREEN)
        radice_cubica[0][5].set_color(RED)
        radice_cubica[0][8].set_color(RED)

        ce_radice_cubica = MathTex(r"a \in \mathbb{R} \quad b \in \mathbb{R}")
        ce_radice_cubica[0][0].set_color(GREEN)
        ce_radice_cubica[0][3].set_color(RED)

        VGroup(pari, radice_quadrata, ce_radice_quadrata, MathTex("x"), dispari, radice_cubica, ce_radice_cubica)\
            .scale(scale).arrange(DOWN)

        self.play(Write(pari))
        self.play(Write(radice_quadrata))
        self.play(Write(ce_radice_quadrata))
        self.wait(delay)
        self.next_section()

        self.play(Write(dispari))
        self.play(Write(radice_cubica))
        self.play(Write(ce_radice_cubica))

        self.wait(30)
