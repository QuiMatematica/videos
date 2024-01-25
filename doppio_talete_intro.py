import math

from manim import *

DELAY = 1


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(1)

        a_coord = [-6, -2, 0]
        b_coord = [-1, -1, 0]
        c_coord = [-5, 2, 0]

        a_dot = Dot(a_coord)
        b_dot = Dot(b_coord)
        c_dot = Dot(c_coord)

        a_label = MathTex("A").next_to(a_dot, LEFT)
        b_label = MathTex("B").next_to(b_dot, RIGHT)
        c_label = MathTex("C").next_to(c_dot, UP)

        ab_line = Line(a_coord, b_coord)
        bc_line = Line(b_coord, c_coord)
        ca_line = Line(c_coord, a_coord)

        abc_dots = VGroup(a_dot, b_dot, c_dot)
        abc_labels = VGroup(a_label, b_label, c_label)
        abc_edges = VGroup(ab_line, bc_line, ca_line)

        self.play(Create(abc_dots), Write(abc_labels), Create(abc_edges))
        self.cut_and_wait()

        p_coords = (b_dot.get_center() - a_dot.get_center()) / 3 + a_dot.get_center()
        p_dot = Dot(p_coords)
        p_label = MathTex("P").next_to(p_dot, DOWN)
        self.play(Create(p_dot), Write(p_label))
        self.cut_and_wait()

        dato0 = MathTex(r"AP = \dfrac{1}{3} \cdot AB")
        dato1 = MathTex(r"CO = \dfrac{1}{3} \cdot CP")
        dato2 = Tex(r"$AC$ = 968 cm")
        dato3 = Tex(r"$CE$ = ?")

        dati = VGroup(
            dato0, dato1, dato2, dato3
        ).arrange(DOWN).move_to(3.5 * RIGHT)

        self.play(Write(dato0))
        self.cut_and_wait()

        cp_line = Line(c_dot.get_center(), p_dot.get_center())
        self.play(Create(cp_line))

        o_coords = (p_dot.get_center() - c_dot.get_center()) / 3 + c_dot.get_center()
        o_dot = Dot(o_coords)
        o_label = MathTex("O").next_to(o_dot, RIGHT)
        self.play(Create(o_dot), Write(o_label))
        self.cut_and_wait()

        self.play(Write(dato1))
        self.cut_and_wait()

        d_coord = line_intersection([b_dot.get_center(), c_dot.get_center()], [a_dot.get_center(), o_dot.get_center()])
        d_dot = Dot(d_coord)
        d_label = MathTex("D").next_to(d_dot, UR)
        ad_line = Line(a_dot.get_center(), d_dot.get_center())

        self.play(Create(ad_line))
        self.play(Create(d_dot), Write(d_label))
        self.cut_and_wait()

        e_coord = line_intersection([a_dot.get_center(), c_dot.get_center()], [b_dot.get_center(), o_dot.get_center()])
        e_dot = Dot(e_coord)
        e_label = MathTex("E").next_to(e_dot, UL)
        be_line = Line(b_dot.get_center(), e_dot.get_center())

        self.play(Create(be_line))
        self.play(Create(e_dot), Write(e_label))
        self.cut_and_wait()

        self.play(Write(dato2))
        self.cut_and_wait()

        self.play(Write(dato3))
        self.cut_and_wait()

        self.wait(30)
