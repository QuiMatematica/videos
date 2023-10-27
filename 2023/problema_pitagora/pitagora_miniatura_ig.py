from manim import *
import math


class Video(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def construct(self):
        ac = 21
        bc = 28
        ab = 35

        abc_scale = 3 / ab

        cos_a = ac / ab
        sin_a = bc / ab
        ah = ac * cos_a
        ch = ac * sin_a

        abc = Polygon([0, 0, 0], [ab, 0, 0], [ah, ch, 0]).scale(abc_scale)
        abc_vertices = abc.get_vertices()
        ac_side = Line(abc_vertices[2], abc_vertices[0])
        bc_side = Line(abc_vertices[2], abc_vertices[1])
        c_right_angle = RightAngle(ac_side, bc_side, length=.3, color=BLUE)
        a_label = MathTex("A").next_to(abc_vertices[0], (DOWN + LEFT) * .7)
        b_label = MathTex("B").next_to(abc_vertices[1], (DOWN + RIGHT) * .7)
        c_label = MathTex("C").next_to(abc_vertices[2], UP)

        gruppo_triangolo = VGroup(abc, c_right_angle, a_label, b_label, c_label)

        dato_1_con_cm = MathTex(r"BC = AC + 7 \text{ cm}")
        dato_2_con_cm = MathTex(r"AB = AC + BC - 14 \text{ cm}")
        richiesta = MathTex(r"2P = \,\,?")
        gruppo_dati_con_cm = VGroup(dato_1_con_cm, dato_2_con_cm, richiesta).arrange(DOWN, aligned_edge=LEFT)

        VGroup(gruppo_triangolo, gruppo_dati_con_cm).scale(2.2).arrange(DOWN, buff=2)

        self.play(Create(abc))
        self.play(Create(c_right_angle))
        self.play(Write(a_label), Write(b_label), Write(c_label))

        self.play(Write(dato_1_con_cm))
        self.play(Write(dato_2_con_cm))
        self.play(Write(richiesta))
        self.wait(15)

