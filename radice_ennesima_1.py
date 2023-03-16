from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.wait(1)

        radice_quadrata = MathTex(r"\sqrt{a} = b \,\,\Longleftrightarrow\,\, b^2 = a").scale(2.5)
        radice_quadrata[0][:2].set_color(YELLOW)
        radice_quadrata[0][8].set_color(YELLOW)
        radice_quadrata[0][2].set_color(GREEN)
        radice_quadrata[0][10].set_color(GREEN)
        radice_quadrata[0][4].set_color(RED)
        radice_quadrata[0][7].set_color(RED)
        self.play(Write(radice_quadrata))
        self.wait(delay)
        self.next_section()

        radice_cubica = MathTex(r"\sqrt[3]{a} = b \,\,\Longleftrightarrow\,\, b^3 = a").scale(2.5)
        radice_cubica[0][:3].set_color(YELLOW)
        radice_cubica[0][9].set_color(YELLOW)
        radice_cubica[0][3].set_color(GREEN)
        radice_cubica[0][11].set_color(GREEN)
        radice_cubica[0][5].set_color(RED)
        radice_cubica[0][8].set_color(RED)

        group = VGroup(radice_quadrata.copy(), radice_cubica).arrange(DOWN)
        self.play(radice_quadrata.animate.move_to(group[0]))
        self.play(Write(radice_cubica))
        self.wait(delay)
        self.next_section()

        radice_quarta = MathTex(r"\sqrt[4]{a} = b \,\,\Longleftrightarrow\,\, b^4 = a").scale(2.5)
        radice_quarta[0][:3].set_color(YELLOW)
        radice_quarta[0][9].set_color(YELLOW)
        radice_quarta[0][3].set_color(GREEN)
        radice_quarta[0][11].set_color(GREEN)
        radice_quarta[0][5].set_color(RED)
        radice_quarta[0][8].set_color(RED)

        group = VGroup(radice_quadrata.copy(), radice_cubica.copy(), radice_quarta).arrange(DOWN)
        self.play(radice_quadrata.animate.move_to(group[0]), radice_cubica.animate.move_to(group[1]))
        self.play(Write(radice_quarta))
        self.wait(delay)
        self.next_section()

        radice_quinta = MathTex(r"\sqrt[5]{a} = b \,\,\Longleftrightarrow\,\, b^5 = a").scale(2.5)
        radice_quinta[0][:3].set_color(YELLOW)
        radice_quinta[0][9].set_color(YELLOW)
        radice_quinta[0][3].set_color(GREEN)
        radice_quinta[0][11].set_color(GREEN)
        radice_quinta[0][5].set_color(RED)
        radice_quinta[0][8].set_color(RED)

        group = VGroup(radice_quadrata.copy(), radice_cubica.copy(), radice_quarta.copy(), radice_quinta).arrange(DOWN)
        self.play(radice_quadrata.animate.move_to(group[0]), radice_cubica.animate.move_to(group[1]),
                  radice_quarta.animate.move_to(group[2]))
        self.play(Write(radice_quinta))
        self.wait(delay)
        self.next_section()

        radice_ennesima = MathTex(r"\sqrt[n]{a} = b \,\,\Longleftrightarrow\,\, b^n = a").scale(2.5)
        radice_ennesima[0][:3].set_color(YELLOW)
        radice_ennesima[0][9].set_color(YELLOW)
        radice_ennesima[0][3].set_color(GREEN)
        radice_ennesima[0][11].set_color(GREEN)
        radice_ennesima[0][5].set_color(RED)
        radice_ennesima[0][8].set_color(RED)

        self.play(Transform(radice_quadrata, radice_ennesima),
                  Transform(radice_cubica, radice_ennesima),
                  Transform(radice_quarta, radice_ennesima),
                  Transform(radice_quinta, radice_ennesima))
        self.wait(delay)
        self.next_section()

        radice_quadrata = MathTex(r"\sqrt{a} = b \,\,\Longleftrightarrow\,\, b^2 = a").scale(2.5)
        radice_quadrata[0][:2].set_color(YELLOW)
        radice_quadrata[0][8].set_color(YELLOW)
        radice_quadrata[0][2].set_color(GREEN)
        radice_quadrata[0][10].set_color(GREEN)
        radice_quadrata[0][4].set_color(RED)
        radice_quadrata[0][7].set_color(RED)
        radice_quadrata.next_to(radice_ennesima, DOWN)
        self.play(Write(radice_quadrata))
        self.wait(delay)
        self.next_section()

        radice_cubica = MathTex(r"\sqrt[3]{a} = b \,\,\Longleftrightarrow\,\, b^3 = a").scale(2.5)
        radice_cubica[0][:3].set_color(YELLOW)
        radice_cubica[0][9].set_color(YELLOW)
        radice_cubica[0][3].set_color(GREEN)
        radice_cubica[0][11].set_color(GREEN)
        radice_cubica[0][5].set_color(RED)
        radice_cubica[0][8].set_color(RED)
        radice_cubica.next_to(radice_ennesima, DOWN)
        self.play(Unwrite(radice_quadrata))
        self.play(Write(radice_cubica))
        self.wait(delay)
        self.next_section()

        self.play(Unwrite(radice_cubica))
        self.wait(delay)
        self.next_section()

        self.wait(30)

