from manim import *

from qui_matematica.axes.parable import parable_from_coefficients

DELAY = 30

WRONG_COLOR = RED
PARABOLA_COLOR = RED


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        domanda = Tex(r"Qual è l'equazione \\ della parabola rappresentata \\ in figura?")

        r1 = Tex("A) $y = x^2 - x - 2$")
        r2 = Tex("B) $y = x^2 + x - 2$")
        r3 = Tex("C) $x = y^2 + y - 2$")
        r4 = Tex("D) $y = (x + 2)(x - 1) - 2$")
        r5 = Tex("E) $y = x^2 + x + 2$")

        risposte = VGroup(r1, r2, r3, r4, r5).arrange(DOWN, aligned_edge=LEFT)

        VGroup(domanda, risposte).arrange(DOWN, buff=1).shift(3.5 * LEFT)

        self.add(domanda)

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

        self.add(riferimento)

        a_coefficient = 1
        b_coefficient = -1
        c_coefficient = -2
        parabola = parable_from_coefficients(riferimento, a_coefficient, b_coefficient, c_coefficient, color=PARABOLA_COLOR)
        self.add(parabola)

        self.add(risposte)

        asse = DashedLine(start=riferimento.c2p(.5, y_max),
                          end=riferimento.c2p(.5, y_min),
                          color=YELLOW)
        self.play(Create(asse))
        self.cut_and_wait()

        self.play(Create(Line(start=risposte[2].get_left(), end=risposte[2].get_right(), color=WRONG_COLOR)))
        self.cut_and_wait()

        intersezione_asse_y = Dot(riferimento.c2p(0, -2), color=PARABOLA_COLOR)
        # coordinate_int_asse_y = MathTex("(0, -2)", color=PARABOLA_COLOR).next_to(intersezione_asse_y, LEFT)
        self.play(Create(intersezione_asse_y), Flash(intersezione_asse_y))
        self.cut_and_wait()

        self.play(Create(Line(start=risposte[4].get_left(), end=risposte[4].get_right(), color=WRONG_COLOR)))
        self.cut_and_wait()

        r4b = MathTex(r"y = x^2 - x + 2x - 2 - 2")
        r4b.move_to(r4[0][2:].get_center())
        r4b.shift((r4[0][2:].get_left() - r4b.get_left()) * RIGHT)
        self.play(ReplacementTransform(r4[0][2:], r4b))
        self.wait(1)

        r4c = MathTex(r"y = x^2 + x - 4")
        r4c.move_to(r4[0][2:].get_center())
        r4c.shift((r4[0][2:].get_left() - r4c.get_left()) * RIGHT)
        self.play(ReplacementTransform(r4b, r4c))
        self.cut_and_wait()

        self.play(Create(Line(start=risposte[3].get_left(), end=r4c.get_right(), color=WRONG_COLOR)))
        self.cut_and_wait()

        self.play(
            Flash(r1[0][6]),
            Flash(r2[0][6]),
        )
        self.cut_and_wait()

        vertice = Dot(riferimento.c2p(.5, -2.25), color=PARABOLA_COLOR)
        self.play(Create(vertice), Flash(vertice))
        self.cut_and_wait()

        vertice_negativo = MathTex(r"x_V {{ > 0 }}").next_to(riferimento, DOWN, buff=.75)
        self.play(Write(vertice_negativo))
        self.cut_and_wait()

        coeff_disc = MathTex(r"-\dfrac{b}{2a} {{ > 0 }}").move_to(vertice_negativo)
        self.play(TransformMatchingTex(vertice_negativo, coeff_disc))
        self.cut_and_wait()

        self.play(Create(Line(start=risposte[1].get_left(), end=risposte[1].get_right(), color=WRONG_COLOR)))

        self.wait(30)
