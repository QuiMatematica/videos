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
        self.wait(.6)

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

        abc_triangle = VGroup(
            ab_line, bc_line, ca_line, a_point, b_point, c_point,
            a_label, b_label, c_label
        )
        self.add(abc_triangle)

        right_angle = Polygon(
            b_coordinates,
            b_coordinates + DL * INC_ANGLE_BORDER,
            b_coordinates + DL * INC_ANGLE_BORDER + DR * INC_ANGLE_BORDER,
            b_coordinates + DR * INC_ANGLE_BORDER,
            color=RED, fill_color=RED, fill_opacity=.6, z_index=-2)
        self.add(right_angle)
        self.wait(1.04 - .6)

        bh_line = Line(start=b_coordinates, end=h_coordinates, color=BH_COLOR, z_index=-1)

        bh = VGroup(
            bh_line, h_point, h_label
        )
        self.add(bh)

        right_angle = Polygon(
            h_coordinates,
            h_coordinates + RIGHT * ANGLE_BORDER,
            h_coordinates + RIGHT * ANGLE_BORDER + UP * ANGLE_BORDER,
            h_coordinates + UP * ANGLE_BORDER,
            color=RED, fill_color=RED, fill_opacity=.6, z_index=-2)
        self.add(right_angle)
        self.wait(1.80 - 1.04)

        tesi = MathTex(r"ABC \text{ isoscele} \Longleftrightarrow BH \cong \dfrac{1}{2} AC")
        tesi.next_to(abc_triangle, DOWN)

        self.play(Write(tesi), run_time=3.60 - 1.80)

        self.wait(30)