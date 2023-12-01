from manim import *

from qui_matematica.axes.parable import parable_from_coefficients

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        x_min = -10
        x_max = 10
        y_min = -6
        y_max = 6

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1)

        self.play(Create(riferimento))
        self.cut_and_wait()

        fuoco = Dot(riferimento.c2p(0, 3), color=YELLOW)
        fuoco_label = MathTex(r"F(0, 3)", color=YELLOW).next_to(fuoco, RIGHT, buff=.2)
        self.play(Create(fuoco), Write(fuoco_label))
        self.cut_and_wait()

        direttrice = Line(start=riferimento.c2p(x_min, -3), end=riferimento.c2p(x_max, -3), color=YELLOW)
        direttrice_label = MathTex(r"d: y = -3", color=YELLOW).next_to(direttrice.get_start(), DOWN, buff=.2).shift(1.1 * RIGHT)
        self.play(Create(direttrice), Write(direttrice_label))
        self.cut_and_wait()

        a_coefficient = 1/12
        parabola = parable_from_coefficients(riferimento, a_coefficient, color=RED)
        self.play(Create(parabola))
        self.cut_and_wait()

        self.wait(30)
