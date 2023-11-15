import math

from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        x_min = -3
        x_max = 10 + x_min
        y_min = -2
        y_max = 12 + y_min

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).set_color(BLUE).shift(4 * LEFT)
        x_label = riferimento.get_x_axis_label(Tex("$x$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        y_label = riferimento.get_y_axis_label(Tex("$y$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        self.play(Create(riferimento))
        self.add(x_label, y_label)
        self.cut_and_wait()

        asse = DashedLine(start=riferimento.c2p(2, 10),
                          end=riferimento.c2p(2, -2),
                          color=YELLOW)
        asse_label = MathTex("a", color=YELLOW).next_to(asse.get_start(), DL, buff=.1)
        self.play(Create(asse), Write(asse_label))
        self.cut_and_wait()

        vertice = Dot(riferimento.c2p(2, 3), color=YELLOW)
        vertice_label = MathTex("V", color=YELLOW).next_to(vertice, DR, buff=.1)
        self.play(Create(vertice), Write(vertice_label))
        self.cut_and_wait()

        fuoco = Dot(riferimento.c2p(2, 4), color=GREEN)
        fuoco_label = MathTex("F", color=GREEN).next_to(fuoco, UR, buff=.1)
        self.play(Create(fuoco), Write(fuoco_label))
        self.cut_and_wait()

        direttrice = Line(start=riferimento.c2p(-3, 2),
                          end=riferimento.c2p(7, 2),
                          color=GREEN)
        direttrice_label = MathTex("d", color=GREEN).next_to(direttrice.get_start(), DR, buff=.1)
        self.play(Create(direttrice), Write(direttrice_label))
        self.cut_and_wait()

        a = 1/4
        b = -1
        c = 4
        x_min_parabola = x_min
        x_max_parabola = x_max

        parabola = riferimento.plot(lambda x: a * x**2 + b * x + c,
                                    x_range=[x_min_parabola, x_max_parabola],
                                    color=YELLOW)
        self.play(Create(parabola))
        self.cut_and_wait()

        gruppo = VGroup(riferimento, x_label, y_label, asse, asse_label, vertice, vertice_label, fuoco, fuoco_label,
                        direttrice, direttrice_label, parabola)

        freccia = MathTex(r"\Longrightarrow", color=RED).scale(3)
        self.play(Write(freccia))
        self.cut_and_wait()

        colore_coefficienti = BLUE
        equazione = MathTex(r"y = a x^2 + bx + c", color=YELLOW).scale(1.3).shift(4*RIGHT)
        equazione[0][2].set_color(colore_coefficienti)
        equazione[0][6].set_color(colore_coefficienti)
        equazione[0][9].set_color(colore_coefficienti)
        self.play(Write(equazione))
        self.cut_and_wait()

        eq_arc = Arc(radius=4, angle=PI)
        # self.add(eq_arc)
        pr_arc = Arc(radius=4, start_angle=PI, angle=PI)

        self.play(MoveAlongPath(equazione, eq_arc), MoveAlongPath(gruppo, pr_arc))

        punto_di_domanda = Tex("?", color=RED).scale(4).next_to(freccia, UP)
        self.play(Write(punto_di_domanda))

        self.wait(30)
