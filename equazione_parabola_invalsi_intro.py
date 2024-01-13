import math

from manim import *

from qui_matematica.axes.parable import parable_from_coefficients

DELAY = 30


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        domanda = Tex(r"Qual è l'equazione \\ della parabola rappresentata \\ in figura?")

        r1 = Tex("A) $y = x^2 - x - 2$")
        r2 = Tex("B) $y = x^2 + x - 2$")
        r3 = Tex("C) $x = y^2 + y - 2$")
        r4 = Tex("D) $y = (x + 2)(x - 1) - 2$")
        r5 = Tex("E) $y = x^2 + x + 2$")

        risposte = VGroup(r1, r2, r3, r4, r5).arrange(DOWN, aligned_edge=LEFT)

        VGroup(domanda, risposte).arrange(DOWN, buff=1).shift(3.5 * LEFT)

        self.play(Write(domanda))

        x_min = -2
        x_max = 3
        y_min = -3
        y_max = 4

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1).shift(3.5 * RIGHT)

        self.play(Create(riferimento))

        a_coefficient = 1
        b_coefficient = -1
        c_coefficient = -2
        parabola = parable_from_coefficients(riferimento, a_coefficient, b_coefficient, c_coefficient, color=RED)
        self.play(Create(parabola))

        for _i in range(5):
            self.play(Write(risposte[_i]))

        self.wait(30)
