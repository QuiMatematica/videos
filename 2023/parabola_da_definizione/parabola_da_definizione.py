from manim import *

from qui_matematica.axes.parable import parable_from_coefficients

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        x_min = -5
        x_max = 5
        y_min = -6
        y_max = 6

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1).shift(4*LEFT)

        fuoco = Dot(riferimento.c2p(0, 3), color=YELLOW)
        fuoco_label = MathTex(r"F(0, 3)", color=YELLOW).next_to(fuoco, RIGHT, buff=.2)

        direttrice = Line(start=riferimento.c2p(x_min, -3), end=riferimento.c2p(x_max, -3), color=YELLOW)
        direttrice_label = MathTex(r"d: y = {{-3}}", color=YELLOW).next_to(direttrice.get_start(), DOWN, buff=.2).shift(1.1 * RIGHT)

        a_coefficient = 1/12
        parabola = parable_from_coefficients(riferimento, a_coefficient, color=RED)

        self.play(Create(riferimento))
        self.play(Create(fuoco), Write(fuoco_label))
        self.play(Create(direttrice), Write(direttrice_label))
        self.play(Create(parabola))
        self.cut_and_wait()

        x_p = 3.2
        y_p = parabola.underlying_function(x_p)

        punto = Dot(riferimento.c2p(x_p, y_p), color=RED)
        punto_label = MathTex(r"P( {{x}} , y)", color=RED).next_to(punto, RIGHT, buff=.2)
        self.play(Create(punto), Write(punto_label))
        self.cut_and_wait()

        piede = Dot(riferimento.c2p(x_p, -3), color=YELLOW)
        piede_label = MathTex(r"H( {{x}} , {{-3}} )", color=YELLOW).next_to(piede, DR, buff=.1)

        pf = Line(start=punto.get_center(), end=fuoco.get_center(), color=RED, z_index=-1)
        ph = Line(start=punto.get_center(), end=piede.get_center(), color=RED, z_index=-1)
        self.play(Create(pf), Create(ph))

        segno_a = Tex("//", color=RED).scale(.5)
        segno_b = segno_a.copy()
        segno_a.rotate(pf.get_angle()).move_to(pf.get_center())
        segno_b.rotate(ph.get_angle()).move_to(ph.get_center())
        self.play(Create(segno_a), Create(segno_b), Flash(segno_a), Flash(segno_b))
        self.cut_and_wait()

        SCALE = .9

        formule = VGroup(
            MathTex(r"\overline{PF} = \text{d}(P, d)"),
            MathTex(r"\overline{PF} = \overline{PH}"),
            MathTex(r"\sqrt{(x - 0)^2 + (y - 3)^2} = {{ \left| y + 3 \right| }}"),
            MathTex(r"(x - 0)^2 + (y - 3)^2 = (y + 3)^2"),
            MathTex(r"x^2 + y^2 - 6y + 9 = y^2 + 6y + 9"),
            MathTex(r"x^2 = 12y"),
            MathTex(r"12y = x^2"),
            MathTex(r"y = \dfrac{1}{12} x^2")
        ).scale(SCALE).arrange(DOWN).shift(3.5*RIGHT)

        self.play(Write(formule[0]))
        self.cut_and_wait()

        self.play(Create(piede))
        self.play(Write(piede_label[0]))
        clone1 = punto_label[1].copy()
        clone1.target = piede_label[1]
        self.play(MoveToTarget(clone1))
        self.play(Write(piede_label[2]))
        clone2 = direttrice_label[1].copy()
        clone2.target = piede_label[3]
        self.play(MoveToTarget(clone2))
        self.play(Write(piede_label[4]))
        self.add(piede_label)
        self.remove(clone1, clone2)
        self.cut_and_wait()

        self.play(Write(formule[1]))
        self.cut_and_wait()

        self.play(Write(formule[2][0]))
        self.play(Write(formule[2][1]))
        self.cut_and_wait()

        self.play(Write(formule[3]))
        self.cut_and_wait()

        self.play(Write(formule[4]))
        self.cut_and_wait()

        self.play(Write(formule[5]))
        self.cut_and_wait()

        self.play(Write(formule[6]))
        self.cut_and_wait()

        self.play(Write(formule[7]))
        self.cut_and_wait()

        self.wait(30)
