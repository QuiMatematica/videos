import math

from manim import *

DELAY = 30


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

        calcolo_delta = MathTex(r"\Delta &= b^2 - 4ac {{ = \\ &= (-2)^2 - 4 \cdot 1 \cdot (-3) }} = \\ &= 16").shift(3*RIGHT)
        cornice_delta = SurroundingRectangle(calcolo_delta, fill_color=BLACK, fill_opacity=.9)

        testo = VGroup(
            Tex("VERTICE:"),
            MathTex(r"x_V = {{ -\dfrac{b}{2a} }} = 1"),
            MathTex(r"y_V &= -\dfrac{\Delta}{4a} {{ = \\ &= -\dfrac{16}{4 \cdot 1} = }} \\ &= -4"),
            MathTex(r"V (1, -4)"),
            ).arrange(DOWN, buff=.5).shift(3 * LEFT)
        # self.add(testo)

        # self.add(cornice_delta)
        # self.add(calcolo_delta)
        self.play(Write(testo[0]))
        self.cut_and_wait()
        self.play(Write(testo[1][0]))
        self.cut_and_wait()
        self.play(Write(testo[1][1]))
        self.cut_and_wait()
        self.play(Write(testo[1][2]))
        self.cut_and_wait()
        self.play(Write(testo[2][0]))
        self.cut_and_wait()
        self.play(Create(cornice_delta))
        self.cut_and_wait()
        self.play(Write(calcolo_delta[0]))
        self.cut_and_wait()
        self.play(Write(calcolo_delta[1]))
        self.cut_and_wait()
        self.play(Write(calcolo_delta[2]))
        self.cut_and_wait()
        self.play(Write(delta))
        self.play(FadeOut(cornice_delta), FadeOut(calcolo_delta))
        self.cut_and_wait()
        self.play(Write(testo[2][1]))
        self.cut_and_wait()
        self.play(Write(testo[2][2]))
        self.cut_and_wait()
        self.play(Write(testo[3]), Create(vertice))
        self.play(Flash(vertice))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
