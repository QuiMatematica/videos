import math

from manim import *

from qui_matematica.qmath import EqSystem

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        equazione = MathTex("y = ax^2 + bx + c").to_edge(UP)
        self.play(Write(equazione))

        x_min = -2
        x_max = 10 + x_min
        y_min = -2
        y_max = 10 + y_min

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).set_color(BLUE).shift(.5 * DOWN).shift(3*LEFT)
        x_label = riferimento.get_x_axis_label(Tex("$x$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        y_label = riferimento.get_y_axis_label(Tex("$y$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        self.play(Create(riferimento))
        self.add(x_label, y_label)
        self.cut_and_wait()

        a = 1/8
        b = -1/2
        c = 1.5

        x_v = -b / (2 * a)
        y_v = a * x_v * x_v + b * x_v + c
        f = 1 / (4 * a)

        asse = DashedLine(start=riferimento.c2p(x_v, y_max),
                          end=riferimento.c2p(x_v, y_min),
                          color=YELLOW)
        asse_label = MathTex("a", color=YELLOW).next_to(asse.get_start(), DL, buff=.1)

        vertice = Dot(riferimento.c2p(x_v, y_v), color=YELLOW)
        vertice_label = MathTex("V", color=YELLOW).next_to(vertice, DR, buff=.1)

        fuoco = Dot(riferimento.c2p(x_v, y_v + f), color=GREEN)
        fuoco_label = MathTex("F", color=GREEN).next_to(fuoco, UR, buff=.1)

        direttrice = Line(start=riferimento.c2p(x_min, y_v - f),
                          end=riferimento.c2p(x_max, y_v - f),
                          color=GREEN)
        direttrice_label = MathTex("d", color=GREEN).next_to(direttrice.get_start(), DR, buff=.1)

        x_min_parabola = (-b - math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)
        if x_min_parabola < x_min:
            x_min_parabola = x_min
        x_max_parabola = (-b + math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)
        if x_max_parabola > x_max:
            x_max_parabola = x_max

        parabola = riferimento.plot(lambda x: a * x**2 + b * x + c,
                                    x_range=[x_min_parabola, x_max_parabola],
                                    color=YELLOW)
        self.play(Create(parabola))
        self.cut_and_wait()

        formula_asse = MathTex(r"\text{asse}: x = {{ -\dfrac{b}{2a} }}")
        formula_asse[0][:5].set_color(YELLOW)

        formula_vertice = VGroup(
            MathTex(r"\text{vertice}: "),
            EqSystem(MathTex(r"x_V = -\dfrac{b}{2a}"), MathTex(r"y_V = -\dfrac{\Delta}{4a}"))
        ).arrange(RIGHT)
        formula_vertice[0].set_color(YELLOW)

        formula_fuoco = VGroup(
            MathTex(r"\text{fuoco}:"),
            EqSystem(MathTex(r"x_F = {{ -\dfrac{b}{2a} }}"), MathTex("y_F = {{ \dfrac{1-\Delta}{4a} }}"))
        ).arrange(RIGHT)
        formula_fuoco[0].set_color(YELLOW)

        formula_direttrice = MathTex(r"\text{direttrice}: y = -\dfrac{1+\Delta}{4a}")
        formula_direttrice[0][:11].set_color(YELLOW)

        gruppo = VGroup(
            formula_asse,
            formula_vertice,
            formula_fuoco,
            formula_direttrice).scale(.8).arrange(DOWN, aligned_edge=LEFT, buff=.2).shift(.5 * DOWN).shift(4*RIGHT)
        # gruppo = VGroup(
        #     VGroup(formula_asse, formula_vertice).arrange(DOWN, aligned_edge=LEFT),
        #     VGroup(formula_fuoco, formula_direttrice).arrange(DOWN, aligned_edge=LEFT)
        # ).arrange(RIGHT, buff=1).shift(DOWN)

        self.play(Write(formula_asse))
        self.play(Create(asse), Write(asse_label))
        self.cut_and_wait()

        self.play(Write(formula_vertice))
        self.play(Create(vertice), Write(vertice_label))
        self.cut_and_wait()

        self.play(Write(formula_fuoco))
        self.play(Create(fuoco), Write(fuoco_label))
        self.cut_and_wait()

        self.play(Write(formula_direttrice))
        self.play(Create(direttrice), Write(direttrice_label))
        self.cut_and_wait()

        senza_delta = Tex(r"senza $\Delta$?").scale(2.5).add_background_rectangle(buff=1, opacity=.9)
        contorno = SurroundingRectangle(senza_delta)
        self.play(Create(contorno), Write(senza_delta))

        self.wait(30)
