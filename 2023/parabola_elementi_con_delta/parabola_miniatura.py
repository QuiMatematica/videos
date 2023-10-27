import math

from manim import *

DELAY = 0


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

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
                           y_length=y_length).add_coordinates().shift(3*RIGHT).shift(.8 * DOWN)
        self.add(riferimento)

        x_min_parabola = (-b - math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)
        x_max_parabola = (-b + math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)

        parabola = riferimento.plot(lambda x: a * x**2 + b * x + c,
                                    x_range=[x_min_parabola, x_max_parabola],
                                    color=colore_parabola)
        self.add(parabola)

        fuoco = Dot(riferimento.coords_to_point(1, -15/4), color=colore_fuoco_direttrice)
        direttrice = Line(start=riferimento.coords_to_point(x_min, -17/4),
                          end=riferimento.coords_to_point(x_max, -17/4),
                          color=colore_fuoco_direttrice)
        asse = DashedLine(start=riferimento.coords_to_point(1, y_max),
                          end=riferimento.coords_to_point(1, y_min), color=colore_parabola)
        self.add(asse)
        self.add(fuoco)

        self.add(direttrice)

        vertice = Dot(riferimento.coords_to_point(1, -4), color=colore_parabola)
        intersezione_asse_x_1 = Dot(riferimento.coords_to_point(-1, 0), color=colore_parabola)
        intersezione_asse_x_2 = Dot(riferimento.coords_to_point(3, 0), color=colore_parabola)
        intersezione_asse_y = Dot(riferimento.coords_to_point(0, -3), color=colore_parabola)
        self.add(vertice, intersezione_asse_x_1, intersezione_asse_x_2, intersezione_asse_y)

        equazione = MathTex(r"y = x^2 - 2x - 3", color=colore_parabola).scale(1.6).shift(3*RIGHT).shift(3*UP)
        self.add(equazione)

        testo = VGroup(
            Tex("Determinare:"),
            Tex("ASSE"),
            Tex("VERTICE"),
            Tex("INTERSEZIONI"),
            Tex("FUOCO"),
            Tex("DIRETTRICE")).scale(1.6).arrange(DOWN, buff=.5, aligned_edge=LEFT).to_edge(UL).shift(.25 * DOWN)
        self.add(testo)

        self.wait(30)
