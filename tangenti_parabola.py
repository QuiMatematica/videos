from manim import *

from qui_matematica.qmath import EqSystem

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        scale_factor = .7

        x_min = -2
        x_max = 9 + x_min
        y_min = -4
        y_max = 10 + y_min

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1).move_to(3.5*LEFT)
        self.add(riferimento)
        self.cut_and_wait()

        equazione_parabola = MathTex(r"y=x^2 - 4x + 3", color=YELLOW).to_edge(UP).shift(3.5*RIGHT)
        self.play(Write(equazione_parabola))
        self.cut_and_wait()

        equazione_asse = MathTex(r"\text{asse: } x = \dfrac{-b}{2a} = \dfrac{4}{2} = {{ 2 }}").next_to(equazione_parabola, DOWN, buff=1)
        self.play(Write(equazione_asse))
        self.cut_and_wait()

        asse = DashedLine(start=riferimento.coords_to_point(2, 6), end=riferimento.coords_to_point(2, -4), color=YELLOW)
        self.play(Create(asse))
        self.cut_and_wait()

        coordinate_vertice = VGroup(
            MathTex(r"x_V = {{ 2 }}"),
            MathTex(r"y_V = x_V^2 - 4x_V + 3 ="),
            MathTex(r"= {{ 2 }} ^2 - 4 \cdot {{ 2 }} + 3 ="),
            MathTex(r"= -1")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(equazione_asse, DOWN, buff=1)
        coordinate_vertice[2].shift(.8*RIGHT)
        coordinate_vertice[3].shift(.8*RIGHT)
        clone1 = equazione_asse[1].copy()
        clone1.target = coordinate_vertice[0][1]
        self.play(Write(coordinate_vertice[0][0]), MoveToTarget(clone1))
        self.add(coordinate_vertice[0])
        self.remove(clone1)
        self.play(Write(coordinate_vertice[1]))
        clone1 = coordinate_vertice[0][1].copy()
        clone1.target = coordinate_vertice[2][1]
        clone2 = coordinate_vertice[0][1].copy()
        clone2.target = coordinate_vertice[2][3]
        self.play(
            Write(coordinate_vertice[2][0]),
            Write(coordinate_vertice[2][2]),
            Write(coordinate_vertice[2][4]),
            MoveToTarget(clone1),
            MoveToTarget(clone2)
        )
        self.add(coordinate_vertice)
        self.remove(clone1, clone2)
        self.play(Write(coordinate_vertice[3]))
        self.cut_and_wait()

        vertice = Dot(riferimento.coords_to_point(2, -1), color=YELLOW)
        vertice_label = MathTex("V", color=YELLOW).next_to(vertice, DR, buff=.1)
        self.play(Create(vertice), Write(vertice_label), Flash(vertice))
        self.cut_and_wait()

        self.play(FadeOut(equazione_asse), FadeOut(coordinate_vertice))

        intersezioni_asse_x = VGroup(
            EqSystem(MathTex(r"y= {{ x^2 - 4x + 3 }}"), MathTex(r"y = {{ 0 }}")),
            MathTex(r"x^2 - 4x + 3 {{ = }} 0"),
            MathTex(r"(x-1)(x-3) = 0"),
            MathTex(r"x = 1 \lor x = 3")
        ).arrange(DOWN).next_to(equazione_parabola, DOWN, buff=1)
        self.play(Write(intersezioni_asse_x[0]))
        clone1 = intersezioni_asse_x[0].eqs[0][1].copy()
        clone1.target = intersezioni_asse_x[1][0]
        clone2 = intersezioni_asse_x[0].eqs[1][1].copy()
        clone2.target = intersezioni_asse_x[1][2]
        self.play(Write(intersezioni_asse_x[1][1]), MoveToTarget(clone1), MoveToTarget(clone2))
        self.add(intersezioni_asse_x[1])
        self.remove(clone1, clone2)
        self.play(Write(intersezioni_asse_x[2]))
        self.play(Write(intersezioni_asse_x[3]))

        int_x_1 = Dot(riferimento.coords_to_point(1, 0), color=YELLOW)
        int_x_2 = Dot(riferimento.coords_to_point(3, 0), color=YELLOW)
        self.play(Create(int_x_1), Create(int_x_2), Flash(int_x_1), Flash(int_x_2))
        self.cut_and_wait()

        self.play(FadeOut(intersezioni_asse_x))

        intersezioni_asse_y = VGroup(
            EqSystem(MathTex(r"y=x^2 - 4x + 3"), MathTex(r"x=0")),
            MathTex(r"y = 3")
        ).arrange(DOWN).next_to(equazione_parabola, DOWN, buff=1)
        for linea in intersezioni_asse_y:
            self.play(Write(linea))

        int_y = Dot(riferimento.coords_to_point(0, 3), color=YELLOW)
        self.play(Create(int_y), Flash(int_y))
        self.cut_and_wait()

        simmetria = DashedLine(start=riferimento.coords_to_point(0, 3), end=riferimento.coords_to_point(4, 3))
        punto = Dot(riferimento.coords_to_point(4, 3), color=YELLOW)
        self.play(Create(simmetria))
        self.play(Create(punto))
        self.play(FadeOut(simmetria))
        self.cut_and_wait()

        self.play(FadeOut(intersezioni_asse_y))
        parabola = riferimento.plot(lambda x: x ** 2 - 4*x + 3, x_range=[-.64, 4.64], color=YELLOW)
        self.play(Create(parabola))
        self.cut_and_wait()

        punto_p = Dot(riferimento.coords_to_point(2, -2), color=GREEN)
        self.play(Create(punto_p))

        coordinate_punto_p = MathTex(r"P(2, -2)", color=GREEN).add_background_rectangle().next_to(punto_p, DR, buff=.1)
        self.play(Write(coordinate_punto_p))
        self.cut_and_wait()

        fascio_di_rette_1 = MathTex(r"y - y_P = m(x - x_P)").next_to(equazione_parabola, DOWN, buff=1)
        fascio_di_rette_2 = MathTex(r"y + 2 = m(x - 2)").next_to(fascio_di_rette_1, DOWN)
        fascio_di_rette_3 = MathTex(r"y + 2 = mx - 2m").next_to(fascio_di_rette_2, DOWN)
        fascio_di_rette_4 = MathTex(r"y = mx - 2m - 2").next_to(fascio_di_rette_3, DOWN)
        self.play(Write(fascio_di_rette_1))
        self.play(Write(fascio_di_rette_2))
        self.cut_and_wait()

        self.play(Write(fascio_di_rette_3))
        self.cut_and_wait()

        self.play(Write(fascio_di_rette_4))
        self.cut_and_wait()

        intersezione_fascio = EqSystem(
            MathTex(r"y= {{ x^2 - 4x + 3 }}"),
            MathTex(r"y = {{ mx - 2m - 2 }}")
        ).next_to(fascio_di_rette_4, DOWN, buff=1)
        clone1 = equazione_parabola.copy()
        clone1.target = intersezione_fascio.eqs[0]
        clone2 = fascio_di_rette_4.copy()
        clone2.target = intersezione_fascio.eqs[1]
        self.play(Write(intersezione_fascio.bracket), MoveToTarget(clone1), MoveToTarget(clone2))
        self.add(intersezione_fascio)
        self.remove(clone1, clone2)
        self.play(FadeOut(fascio_di_rette_1), FadeOut(fascio_di_rette_2), FadeOut(fascio_di_rette_3), FadeOut(fascio_di_rette_4))
        self.play(intersezione_fascio.animate.next_to(equazione_parabola, DOWN, buff=1))

        equazione_risolvente_1 = MathTex(r"x^2 - 4x + 3 {{ = }} mx - 2m - 2").next_to(intersezione_fascio, DOWN, buff=1)
        equazione_risolvente_2 = MathTex(r"x^2 - {{ (m + 4) }} x + {{ 2m + 5 }} = 0").next_to(equazione_risolvente_1, DOWN)
        clone1 = intersezione_fascio.eqs[0][1].copy()
        clone1.target = equazione_risolvente_1[0]
        clone2 = intersezione_fascio.eqs[1][1].copy()
        clone2.target = equazione_risolvente_1[2]
        self.play(Write(equazione_risolvente_1[1]), MoveToTarget(clone1), MoveToTarget(clone2))
        self.add(equazione_risolvente_1)
        self.remove(clone1, clone2)
        self.play(Write(equazione_risolvente_2))
        self.play(FadeOut(intersezione_fascio), FadeOut(equazione_risolvente_1))
        self.play(equazione_risolvente_2.animate.next_to(equazione_parabola, DOWN, buff=1))
        self.cut_and_wait()

        delta_1 = MathTex(r"\Delta = 0").next_to(equazione_risolvente_2, DOWN, buff=1)
        self.play(Write(delta_1))
        self.cut_and_wait()

        delta_2 = MathTex(r"b^2 - 4ac = 0").next_to(delta_1, DOWN)
        self.play(Write(delta_2))
        self.cut_and_wait()

        delta_3 = MathTex(r"{{ (m + 4) }} ^2 - 4( {{ 2m + 5 }} ) = 0").next_to(delta_2, DOWN)
        clone1 = equazione_risolvente_2[1].copy()
        clone1.target = delta_3[0]
        clone2 = equazione_risolvente_2[3].copy()
        clone2.target = delta_3[2]
        self.play(Write(delta_3[1]), Write(delta_3[3]), MoveToTarget(clone1), MoveToTarget(clone2))
        self.add(delta_3)
        self.remove(clone1, clone2)
        self.cut_and_wait()

        delta_4 = MathTex(r"m^2 + 8m + 16 - 8m - 20 = 0").next_to(delta_3, DOWN)
        self.play(Write(delta_4))
        self.cut_and_wait()

        delta_5 = MathTex(r"m^2 - 4 = 0").next_to(delta_4, DOWN)
        self.play(Write(delta_5))
        self.cut_and_wait()

        delta_6 = MathTex(r"m = -2 \lor m = 2").next_to(delta_5, DOWN)
        self.play(Write(delta_6))
        self.play(FadeOut(equazione_risolvente_2),
                  FadeOut(delta_1),
                  FadeOut(delta_2),
                  FadeOut(delta_3),
                  FadeOut(delta_4),
                  FadeOut(delta_5)
                  )
        self.play(delta_6.animate.next_to(equazione_parabola, DOWN, buff=1))
        self.cut_and_wait()

        fascio_di_rette_4.next_to(delta_6, DOWN, buff=1)
        self.play(Write(fascio_di_rette_4))
        self.cut_and_wait()

        equazione_retta_1 = MathTex(r"m = -2: y = -2x + 2").next_to(fascio_di_rette_4, DOWN, buff=1)
        equazione_retta_1[0][5:].set_color(RED)
        equazione_retta_2 = MathTex(r"m = 2: y = 2x - 6").next_to(equazione_retta_1, DOWN)
        equazione_retta_2[0][4:].set_color(RED)
        self.play(Write(equazione_retta_1))
        self.play(Write(equazione_retta_2))

        retta_1 = riferimento.plot(lambda x: -2 * x + 2, x_range=[-2, 3], color=RED)
        retta_2 = riferimento.plot(lambda x: 2 * x - 6, x_range=[1, 6], color=RED)
        self.play(Create(retta_1), Create(retta_2))

        self.wait(30)
