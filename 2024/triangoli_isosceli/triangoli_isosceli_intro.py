import math

from manim import *

DELAY = 30

ANGLE_RADIUS = .9


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        ab_len = 3
        dab_amp = 41 * DEGREES
        cad_amp = 82 * DEGREES
        cab_amp = cad_amp + dab_amp

        ad_len = (ab_len / 2) / math.cos(dab_amp)
        ac_len = (ad_len / 2) / math.cos(cad_amp)

        a_coordinates = ORIGIN
        b_coordinates = a_coordinates + ab_len * RIGHT
        c_coordinates = a_coordinates + ac_len * math.cos(cab_amp) * RIGHT + ac_len * math.sin(cab_amp) * UP
        d_coordinates = a_coordinates + (ab_len / 2) * RIGHT + ad_len * math.sin(dab_amp) * UP

        a_point = Dot(a_coordinates)
        b_point = Dot(b_coordinates)
        c_point = Dot(c_coordinates)
        d_point = Dot(d_coordinates)

        # abc_triangle_vertices = VGroup(a_point, b_point, c_point, d_point).move_to(ORIGIN)

        ab_line = Line(start=a_coordinates, end=b_coordinates)
        bc_line = Line(start=b_coordinates, end=c_coordinates)
        ca_line = Line(start=c_coordinates, end=a_coordinates)
        cd_line = Line(start=c_coordinates, end=d_coordinates)
        ad_line = Line(start=a_coordinates, end=d_coordinates)
        bd_line = Line(start=b_coordinates, end=d_coordinates)

        abc_triangle_lines = VGroup(ab_line, bc_line, ca_line)

        abc_triangle = VGroup(
            a_point, b_point, c_point, d_point,
            ab_line, bc_line, ca_line, cd_line, ad_line, bd_line,
        ).move_to(ORIGIN)

        self.play(Create(abc_triangle_lines))

        a_label = MathTex("A").next_to(a_point, DOWN, buff=.1)
        b_label = MathTex("B").next_to(b_point, DOWN, buff=.1)
        c_label = MathTex("C").next_to(c_point, UP, buff=.1)

        self.play(
            Create(a_point), Create(b_point), Create(c_point),
            Write(a_label), Write(b_label), Write(c_label)
        )
        self.cut_and_wait()

        d_label = MathTex("D").next_to(d_point, UP, buff=.1)
        self.play(Create(d_point), Write(d_label))
        self.cut_and_wait()

        tic1 = Tex("//").set_color(GREEN).scale(.7).move_to(ca_line).rotate(ca_line.get_angle())
        tic2 = Tex("//").set_color(GREEN).scale(.7).move_to(cd_line).rotate(cd_line.get_angle())
        self.play(Write(tic1), Write(tic2))
        self.cut_and_wait()

        self.play(Create(ad_line))

        tic1 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(ad_line).rotate(ad_line.get_angle())
        tic2 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(bd_line).rotate(bd_line.get_angle())
        self.play(Write(tic1), Write(tic2))
        self.cut_and_wait()

        c_angle = Angle(ca_line, cd_line, radius=ANGLE_RADIUS, color=YELLOW, z_index=-1)
        c_angle_fill = Sector(
            start_angle=ca_line.get_angle(),
            angle=cd_line.get_angle() - ca_line.get_angle(),
            outer_radius=ANGLE_RADIUS,
            arc_center=c_point.get_center(),
            fill_color=YELLOW, fill_opacity=.5,
            z_index=-1
        )
        self.play(Create(c_angle), Create(c_angle_fill))
        c_angle_value = MathTex(r"16^{\circ}", color=YELLOW)
        c_angle_value.next_to(c_angle, UR).shift(.5 * LEFT).shift(.05 * UP)
        self.play(Write(c_angle_value))

        b_angle = Angle(bc_line, ab_line.reverse_direction(), radius=ANGLE_RADIUS, color=RED, z_index=-1)
        b_angle_fill = Sector(
            start_angle=bc_line.get_angle(),
            angle=ab_line.get_angle() - bc_line.get_angle(),
            outer_radius=ANGLE_RADIUS,
            arc_center=b_point.get_center(),
            fill_color=RED, fill_opacity=.5,
            z_index=-1
        )
        self.play(Create(b_angle), Create(b_angle_fill))
        question = Tex("?", color=RED).next_to(b_angle, LEFT, buff=.1)
        self.play(Write(question))

        self.wait(30)
