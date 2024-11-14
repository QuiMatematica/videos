import math

from manim import *

DELAY = 1
X_RADIUS = config["frame_x_radius"]
Y_RADIUS = config["frame_y_radius"]
SCALE = 1
BH_COLOR = YELLOW
ANGLE_BORDER = .4
INC_ANGLE_BORDER = ANGLE_BORDER / math.sqrt(2)


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        bh_len = 4
        b_coordinates = ORIGIN + UP * (1 + bh_len/2)
        a_coordinates = b_coordinates + DL * bh_len
        c_coordinates = b_coordinates + DR * bh_len
        h_coordinates = b_coordinates + DOWN * bh_len

        ab_line = Line(start=a_coordinates, end=b_coordinates)
        bc_line = Line(start=b_coordinates, end=c_coordinates)
        ca_line = Line(start=c_coordinates, end=a_coordinates)

        a_point = Dot(a_coordinates)
        b_point = Dot(b_coordinates)
        c_point = Dot(c_coordinates)
        h_point = Dot(h_coordinates, color=BH_COLOR)

        a_label = MathTex("A").next_to(a_point, DL, buff=SMALL_BUFF)
        b_label = MathTex("B").next_to(b_point, UP, buff=SMALL_BUFF)
        c_label = MathTex("C").next_to(c_point, DR, buff=SMALL_BUFF)
        h_label = MathTex("H", color=BH_COLOR).next_to(h_point, DOWN, buff=SMALL_BUFF)

        right_angle = Polygon(
            b_coordinates,
            b_coordinates + DL * INC_ANGLE_BORDER,
            b_coordinates + DL * INC_ANGLE_BORDER + DR * INC_ANGLE_BORDER,
            b_coordinates + DR * INC_ANGLE_BORDER,
            color=RED, fill_color=RED, fill_opacity=.6, z_index=-2)

        abc_triangle = VGroup(
            ab_line, bc_line, ca_line, a_point, b_point, c_point,
            a_label, b_label, c_label, right_angle
        )
        self.add(abc_triangle)

        bh_line = Line(start=b_coordinates, end=h_coordinates, color=BH_COLOR, z_index=-1)

        right_angle = Polygon(
            h_coordinates,
            h_coordinates + RIGHT * ANGLE_BORDER,
            h_coordinates + RIGHT * ANGLE_BORDER + UP * ANGLE_BORDER,
            h_coordinates + UP * ANGLE_BORDER,
            color=RED, fill_color=RED, fill_opacity=.6, z_index=-2)

        bh = VGroup(
            bh_line, h_point, h_label, right_angle
        )
        self.add(bh)

        tesi = MathTex(r"ABC \text{ isoscele} \Longleftrightarrow BH \cong \dfrac{1}{2} AC")
        tesi.next_to(abc_triangle, DOWN)
        self.add(tesi)
        self.cut_and_wait()

        testo = VGroup(abc_triangle, bh, tesi)

        self.play(testo.animate.scale(.5).to_edge(UL))
        self.cut_and_wait()

        titolo = Tex("Prima parte", color=YELLOW).to_edge(UP).shift(2*RIGHT)

        ipotesi_tesi = MathTex(
            r"\text{ipotesi: }&ABC \text{ rettangolo} \\",
            r"&ABC \text{ isoscele} \\",
            r"\text{tesi: }&BH \cong \dfrac{1}{2} AC"
        ).next_to(titolo, DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(titolo))
        self.play(Write(ipotesi_tesi))
        self.cut_and_wait()

        p1 = MathTex(r"ABC \text{ isoscele } \Longrightarrow BH \text{ mediana}")
        p2 = MathTex(r"ABC \text{ rettangolo } \Longrightarrow BH \cong \dfrac{1}{2} AC")

        dimostrazione = VGroup(p1, p2).arrange(DOWN).shift(2*DOWN)
        self.play(Write(p1))
        self.cut_and_wait()

        self.play(Write(p2))
        self.cut_and_wait()

        self.play(
            FadeOut(dimostrazione),
            FadeOut(titolo),
            FadeOut(ipotesi_tesi)
        )

        titolo = Tex("Seconda parte", color=YELLOW).to_edge(UP).shift(2*RIGHT)

        ipotesi_tesi = MathTex(
            r"\text{ipotesi: }&ABC \text{ rettangolo} \\",
            r"& BH \cong \dfrac{1}{2} AC \\",
            r"\text{tesi: }&ABC \text{ isoscele}"
        ).next_to(titolo, DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(titolo))
        self.play(Write(ipotesi_tesi))
        self.cut_and_wait()

        p1 = MathTex(r"ABC \text{ rettangolo } \Longrightarrow \overline{AC} \cdot \overline{BH} = 2A_{ABC}")
        p2 = MathTex(r"ABC \text{ rettangolo } \Longrightarrow \overline{AB} \cdot \overline{BC} = 2A_{ABC}")
        p3 = MathTex(r"{{ \overline{AC} }} \cdot {{ \overline{BH} }} = {{ \overline{AB} \cdot \overline{BC} }}")

        dimostrazione = VGroup(p1, p2, p3).arrange(DOWN).shift(2*DOWN)
        self.play(Write(p1))
        self.cut_and_wait()

        self.play(Write(p2))
        self.cut_and_wait()

        self.play(Write(p3))
        self.cut_and_wait()

        self.play(FadeOut(p1), FadeOut(p2), p3.animate.move_to(p2))

        p3b = MathTex(r"{{ \overline{AC} }} \cdot \dfrac{1}{2} {{ \overline{AC} }} = {{ \overline{AB} \cdot \overline{BC} }}").move_to(p3)
        self.play(TransformMatchingTex(p3, p3b))
        self.cut_and_wait()
        p4 = MathTex(r"{{ \overline{AC}^2 }} = 2 \cdot {{ \overline{AB} \cdot \overline{BC} }}").move_to(p3)
        self.play(TransformMatchingTex(p3b, p4))
        self.cut_and_wait()
        p5 = MathTex(r"{{ \overline{AB}^2 }} + {{ \overline{BC}^2 }} = 2 \cdot {{ \overline{AB} \cdot \overline{BC} }}").move_to(p3)
        self.play(TransformMatchingTex(p4, p5))
        self.cut_and_wait()
        p6 = MathTex(r"{{ \overline{AB}^2 }} - 2 \cdot {{ \overline{AB} \cdot \overline{BC} }} + {{ \overline{BC}^2 }} = 0").move_to(p3)
        self.play(TransformMatchingTex(p5, p6))
        self.cut_and_wait()
        p7 = MathTex(r"( {{ \overline{AB} }} - {{ \overline{BC} }} )^2 {{ = 0 }}").move_to(p3)
        self.play(TransformMatchingTex(p6, p7))
        self.cut_and_wait()
        p8 = MathTex(r"{{ \overline{AB} }} - {{ \overline{BC} }} = 0").move_to(p3)
        self.play(TransformMatchingTex(p7, p8))
        self.cut_and_wait()
        p9 = MathTex(r"{{ \overline{AB} }} = {{ \overline{BC} }} ").move_to(p3)
        self.play(TransformMatchingTex(p8, p9))
        self.cut_and_wait()
        p10 = MathTex(r"{{ \overline{AB} }} = {{ \overline{BC} }} \Longrightarrow ABC \text{ isoscele}").move_to(p3)
        self.play(TransformMatchingTex(p9, p10))
        self.cut_and_wait()

        self.wait(30)
