import math

from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        a = 1
        b = -2
        c = -3

        x_min = -3
        x_max = 5
        y_min = -5
        y_max = 5

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        colore_fuoco_direttrice = GREEN
        colore_parabola = YELLOW

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().shift(3*RIGHT).shift(.5 * DOWN)
        self.add(riferimento)

        fuoco = Dot(riferimento.coords_to_point(1, -15/4), color=colore_fuoco_direttrice)
        direttrice = Line(start=riferimento.coords_to_point(x_min, -17/4),
                          end=riferimento.coords_to_point(x_max, -17/4),
                          color=colore_fuoco_direttrice)
        asse = DashedLine(start=riferimento.coords_to_point(1, y_max),
                          end=riferimento.coords_to_point(1, y_min), color=colore_parabola)

        vertice = Dot(riferimento.coords_to_point(1, -4), color=colore_parabola)
        intersezione_asse_x_1 = Dot(riferimento.coords_to_point(-1, 0), color=colore_parabola)
        intersezione_asse_x_2 = Dot(riferimento.coords_to_point(3, 0), color=colore_parabola)
        intersezione_asse_y = Dot(riferimento.coords_to_point(0, -3), color=colore_parabola)

        equazione = MathTex(r"y = x^2 - 2x - 3", color=colore_parabola).shift(3*RIGHT).shift(3.2*UP)
        delta = MathTex(r"\Delta = 16").next_to(equazione, DOWN).shift(2 * RIGHT)
        self.add(equazione)
        self.add(asse)
        self.add(vertice)
        self.add(delta)
        self.add(intersezione_asse_x_1, intersezione_asse_x_2)

        testo = VGroup(
            Tex("INTERSEZIONE ASSE y:"),
            MathTex(r"\begin{cases} y = x^2 - 2x - 3 \\ x = 0 \\ \end{cases}"),
            MathTex(r"y = 0^2 - 2 \cdot 0 - 3 = -3")
            ).arrange(DOWN, buff=.5).shift(3 * LEFT)
        # self.add(testo)

        self.play(Write(testo[0]))
        self.cut_and_wait()
        self.play(Write(testo[1]))
        self.cut_and_wait()
        self.play(Write(testo[2]))
        # self.cut_and_wait()
        # self.play(Write(testo[3]))
        # self.cut_and_wait()
        # self.play(Write(testo[4]))
        self.cut_and_wait()
        self.play(Create(intersezione_asse_y))
        self.play(Flash(intersezione_asse_y))
        self.play(Flash(intersezione_asse_y))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
