from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        scale = 2

        self.wait(1)

        radice_quadrata = MathTex(r"\sqrt{a} = b \,\,\Longleftrightarrow\,\, b^2 = a")
        radice_quadrata[0][:2].set_color(YELLOW)
        radice_quadrata[0][8].set_color(YELLOW)
        radice_quadrata[0][2].set_color(GREEN)
        radice_quadrata[0][10].set_color(GREEN)
        radice_quadrata[0][4].set_color(RED)
        radice_quadrata[0][7].set_color(RED)

        ce_radice_quadrata = MathTex(r"{{ a \ge 0 }} \quad {{ b \ge 0 }}")
        ce_radice_quadrata[0][0].set_color(GREEN)
        ce_radice_quadrata[2][0].set_color(RED)

        radice_cubica = MathTex(r"\sqrt[3]{a} = b \,\,\Longleftrightarrow\,\, b^3 = a")
        radice_cubica[0][:3].set_color(YELLOW)
        radice_cubica[0][9].set_color(YELLOW)
        radice_cubica[0][3].set_color(GREEN)
        radice_cubica[0][11].set_color(GREEN)
        radice_cubica[0][5].set_color(RED)
        radice_cubica[0][8].set_color(RED)

        ce_radice_cubica = MathTex(r"{{ a \in \mathbb{R} }} \quad {{ b \in \mathbb{R} }}")
        ce_radice_cubica[0][0].set_color(GREEN)
        ce_radice_cubica[2][0].set_color(RED)

        VGroup(radice_quadrata, ce_radice_quadrata, MathTex("x"), radice_cubica, ce_radice_cubica).scale(scale).arrange(DOWN)
        self.play(Write(radice_quadrata))
        self.wait(delay)
        self.next_section()

        b_quadro = MathTex(r"{{ b^2 }} \ge 0").scale(scale)
        b_quadro[0][0].set_color(RED)
        b_quadro[0][1].set_color(YELLOW)
        b_quadro.move_to(ce_radice_quadrata[0])
        self.play(Write(b_quadro))
        self.wait(delay)
        self.next_section()

        b_quadro_a = MathTex(r"{{ b^2 }} = {{ a }} \ge 0").scale(scale)
        b_quadro_a[0][0].set_color(RED)
        b_quadro_a[0][1].set_color(YELLOW)
        b_quadro_a[2][0].set_color(GREEN)
        b_quadro_a.move_to(ce_radice_quadrata[0])
        self.play(TransformMatchingTex(b_quadro, b_quadro_a))
        self.wait(delay)
        self.next_section()

        a = MathTex(r"{{ a }} \ge 0").scale(scale)
        a[0][0].set_color(GREEN)
        a.move_to(ce_radice_quadrata[0])
        self.play(TransformMatchingTex(b_quadro_a, a))
        self.wait(delay)
        self.next_section()

        self.play(Write(ce_radice_quadrata[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_cubica))
        self.play(Write(ce_radice_cubica[0]))
        self.play(Write(ce_radice_cubica[2]))
        self.wait(delay)
        self.next_section()

        self.wait(30)
