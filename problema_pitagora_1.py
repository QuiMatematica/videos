from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(.5)

        ac = 21
        bc = 28
        ab = 35

        abc_scale = 3 / ab
        text_scale = 1

        cos_a = ac / ab
        sin_a = bc / ab
        ah = ac * cos_a
        ch = ac * sin_a

        abc = Polygon([0, 0, 0], [ab, 0, 0], [ah, ch, 0]).scale(abc_scale).move_to(3.5 * LEFT)
        abc_vertices = abc.get_vertices()
        ac_side = Line(abc_vertices[2], abc_vertices[0])
        bc_side = Line(abc_vertices[2], abc_vertices[1])
        c_right_angle = RightAngle(ac_side, bc_side, length=.3, color=BLUE)
        self.play(Create(abc))
        self.play(Create(c_right_angle))

        a_label = MathTex("A").next_to(abc_vertices[0], (DOWN + LEFT) * .7).scale(text_scale)
        b_label = MathTex("B").next_to(abc_vertices[1], (DOWN + RIGHT) * .7).scale(text_scale)
        c_label = MathTex("C").next_to(abc_vertices[2], UP).scale(text_scale)
        self.play(Write(a_label), Write(b_label), Write(c_label))

        dato_1_cm = MathTex(r"BC = AC + 7 \text{ cm}")
        dato_2_cm = MathTex(r"AB = AC + BC - 14 \text{ cm}")
        richiesta_cm = MathTex(r"2P = \,\,?")
        dati_cm = VGroup(dato_1_cm, dato_2_cm, richiesta_cm).\
            arrange(DOWN, aligned_edge=LEFT).scale(text_scale).move_to(3.5 * RIGHT)
        self.play(Write(dato_1_cm))
        self.play(Write(dato_2_cm))
        self.play(Write(richiesta_cm))

        dato_1 = MathTex(r"\overline{BC} = \overline{AC} + 7")
        dato_2 = MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14")
        richiesta = richiesta_cm.copy()
        dati = VGroup(dato_1, dato_2, richiesta).arrange(DOWN, aligned_edge=LEFT)
        dati.move_to(dati_cm.get_left() + dati.get_center() - dati.get_left())

        self.play(ReplacementTransform(dato_1_cm, dato_1), ReplacementTransform(dato_2_cm, dato_2))

        gruppo_triangolo = VGroup(abc, c_right_angle, a_label, b_label, c_label)

        gruppo_dati = VGroup(dato_1, dato_2, richiesta_cm)

        self.play(gruppo_triangolo.animate.scale(.7).move_to(5*LEFT + 3*UP))
        self.play(gruppo_dati.animate.scale(.7).move_to(3*UP))

        buff_schema = 1.5
        schema_dato_1 = MathTex(r"\overline{BC} = \overline{AC} + 7")
        schema_dato_2 = MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14")
        schema_dati = VGroup(schema_dato_1, schema_dato_2).arrange(RIGHT, buff=buff_schema)
        schema_ac = MathTex(r"\overline{AC}")
        schema_bc = MathTex(r"\overline{BC}")
        schema_ab = MathTex(r"\overline{AB}")
        schema_lati = VGroup(schema_ac, schema_bc, schema_ab).arrange(RIGHT, buff=buff_schema)
        schema_2p = MathTex(r"2P")
        schema = VGroup(schema_dati, schema_lati, schema_2p).arrange(DOWN, buff=buff_schema).shift(DOWN)

        self.add(schema)

        self.wait(30)
