import math

from manim import *

DELAY = 30

ANGLE_RADIUS = .9


def get_angle_group(a_dot, b_dot, c_dot, angle_color=WHITE):
    angle = Angle.from_three_points(
        a_dot.get_center(), b_dot.get_center(), c_dot.get_center(),
        radius=ANGLE_RADIUS, color=angle_color, z_index=-1
    )
    lines = angle.get_lines()

    fill_angle = lines[1].get_angle() - lines[0].get_angle()
    if fill_angle < 0:
        fill_angle = 2 * PI + fill_angle

    angle_fill = Sector(
        start_angle=lines[0].get_angle(),
        angle=fill_angle,
        outer_radius=ANGLE_RADIUS,
        arc_center=b_dot.get_center(),
        fill_color=angle_color, fill_opacity=.5,
        z_index=-1
    )
    angle_lines = VGroup(
        Line(start=b_dot.get_center(), end=angle.get_start()),
        Line(start=b_dot.get_center(), end=angle.get_end())
    ).set_stroke(width=DEFAULT_STROKE_WIDTH / 2).set_color(angle_color).set_z_index(-1)
    return VGroup(angle, angle_fill, angle_lines)


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

        d_label = MathTex("D").next_to(d_point, UP, buff=.1)
        self.play(Create(d_point), Write(d_label))

        tic1 = Tex("//").set_color(GREEN).scale(.7).move_to(ca_line).rotate(ca_line.get_angle())
        tic2 = Tex("//").set_color(GREEN).scale(.7).move_to(cd_line).rotate(cd_line.get_angle())
        self.play(Write(tic1), Write(tic2))

        self.play(Create(ad_line))

        tic1 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(ad_line).rotate(ad_line.get_angle())
        tic2 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(bd_line).rotate(bd_line.get_angle())
        self.play(Write(tic1), Write(tic2))

        c_angle_group = get_angle_group(a_point, c_point, d_point, YELLOW)
        self.play(*[Create(_i) for _i in c_angle_group])

        c_angle_value = MathTex(r"16^{\circ}", color=YELLOW)
        c_angle_value.next_to(c_angle_group[0], UR).shift(.5 * LEFT).shift(.05 * UP)
        self.play(Write(c_angle_value))

        b_angle_group = get_angle_group(c_point, b_point, a_point, RED)
        self.play(*[Create(_i) for _i in b_angle_group])
        question = Tex("?", color=RED).next_to(b_angle_group, LEFT, buff=.1)
        self.play(Write(question))
        self.cut_and_wait()

        # I lati AC e CD sono congruenti, quindi il triangolo ACD è isoscele per definizione,

        acd_triangle = Polygon(
            a_point.get_center(), d_point.get_center(), c_point.get_center(),
            fill_color=BLUE, fill_opacity=.5,
            z_index=-2
        )
        self.play(Create(acd_triangle))
        self.cut_and_wait()

        # e per il teorema dei triangoli isosceli gli angoli CAD e ADC sono congruenti.

        a_angle_group = get_angle_group(d_point, a_point, c_point, GREEN)
        d_angle_group = get_angle_group(c_point, d_point, a_point, GREEN)
        self.play(
            *[Create(_i) for _i in a_angle_group],
            *[Create(_i) for _i in d_angle_group],
        )
        self.cut_and_wait()

        sum_center = 4 * RIGHT + 3 * UP

        target = VGroup(
            get_angle_group(
                Dot(sum_center - [1, 0, 0]),
                Dot(sum_center),
                Dot(sum_center - [math.cos(16 * DEGREES), math.sin(16 * DEGREES), 0])
            ),
            get_angle_group(
                Dot(sum_center - [math.cos(16 * DEGREES), math.sin(16 * DEGREES), 0]),
                Dot(sum_center),
                Dot(sum_center - [math.cos(98 * DEGREES), math.sin(98 * DEGREES), 0])
            ),
            get_angle_group(
                Dot(sum_center - [math.cos(98 * DEGREES), math.sin(98 * DEGREES), 0]),
                Dot(sum_center),
                Dot(sum_center - [-1, 0, 0])
            ),
        )
        a_angle_copy = a_angle_group.copy()
        c_angle_copy = c_angle_group.copy()
        d_angle_copy = d_angle_group.copy()

        self.play(
            c_angle_copy.animate.rotate(target[0][2][0].get_angle() - c_angle_copy[2][0].get_angle()),
            a_angle_copy.animate.rotate(target[1][2][0].get_angle() - a_angle_copy[2][0].get_angle()),
            d_angle_copy.animate.rotate(target[2][2][0].get_angle() - d_angle_copy[2][0].get_angle()),
        )
        self.play(
            c_angle_copy.animate.move_to(target[0]),
            a_angle_copy.animate.move_to(target[1]),
            d_angle_copy.animate.move_to(target[2]),
        )

        formula_1 = MathTex(r"16^{\circ} + x + x = 180^{\circ}").next_to(target, DOWN)
        formula_2 = MathTex(r"2x = 164^{\circ}").next_to(formula_1, DOWN)
        formula_3 = MathTex(r"x = 82^{\circ}").next_to(formula_2, DOWN)

        self.play(Write(formula_1))
        self.cut_and_wait()
        self.play(Write(formula_2))
        self.cut_and_wait()
        self.play(Write(formula_3))
        d_amp = MathTex(r"82^{\circ}", color=GREEN).next_to(d_angle_group, LEFT, buff=.1)
        self.play(Write(d_amp))
        self.cut_and_wait()

        self.play(
            FadeOut(acd_triangle),
            FadeOut(a_angle_group),
            FadeOut(a_angle_copy), FadeOut(c_angle_copy), FadeOut(d_angle_copy),
            FadeOut(formula_1), FadeOut(formula_2), FadeOut(formula_3)
        )

        abd_triangle = Polygon(
            a_point.get_center(), b_point.get_center(), d_point.get_center(),
            fill_color=BLUE, fill_opacity=.5,
            z_index=-2
        )
        self.play(Create(abd_triangle))
        self.cut_and_wait()

        a_angle_group = get_angle_group(b_point, a_point, d_point, RED)
        self.play(*[Create(_i) for _i in a_angle_group])
        self.cut_and_wait()

        target = VGroup(
            VGroup(
                get_angle_group(
                    Dot(ORIGIN - [math.cos(-41 * DEGREES), math.sin(-41 * DEGREES), 0]),
                    Dot(ORIGIN),
                    Dot(ORIGIN - [1, 0, 0])
                ),
                get_angle_group(
                    Dot(ORIGIN - [1, 0, 0]),
                    Dot(ORIGIN),
                    Dot(ORIGIN - [math.cos(41 * DEGREES), math.sin(41 * DEGREES), 0])
                )
            ),
            MathTex(r"\cong"),
            get_angle_group(
                Dot(ORIGIN - [math.cos(-41 * DEGREES), math.sin(-41 * DEGREES), 0]),
                Dot(ORIGIN),
                Dot(ORIGIN - [math.cos(41 * DEGREES), math.sin(41 * DEGREES), 0])
            ),
        ).arrange(RIGHT).move_to(sum_center)

        a_angle_copy = a_angle_group.copy()
        b_angle_copy = b_angle_group.copy()
        d_angle_copy = d_angle_group.copy()

        self.play(
            b_angle_copy.animate.rotate(target[2][2][0].get_angle() - b_angle_copy[2][0].get_angle()),
            a_angle_copy.animate.rotate(target[0][1][2][0].get_angle() - a_angle_copy[2][0].get_angle()),
            d_angle_copy.animate.rotate(target[0][0][2][0].get_angle() - d_angle_copy[2][0].get_angle()),
        )
        self.play(
            b_angle_copy.animate.move_to(target[0][0]),
            a_angle_copy.animate.move_to(target[0][1]),
            d_angle_copy.animate.move_to(target[2]),
            Write(target[1])
        )
        self.cut_and_wait()

        formula_1 = MathTex(r"x + x = 82^{\circ}").next_to(target, DOWN)
        formula_2 = MathTex(r"x = 41^{\circ}").next_to(formula_1, DOWN)
        self.play(Write(formula_1))
        self.cut_and_wait()
        self.play(Write(formula_2))
        self.cut_and_wait()

        risposta = MathTex(r"41^{\circ}", color=RED).next_to(b_angle_group, LEFT, buff=.1)
        self.play(
            FadeOut(abd_triangle),
            FadeOut(a_angle_group),
            FadeOut(question),
        )
        self.play(Write(risposta))

        self.wait(30)

