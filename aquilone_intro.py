import math

from manim import *

DELAY = 1

SQRT_3 = math.sqrt(3)
SQRT_3_DIV_2 = SQRT_3 / 2

ANGLE_RADIUS = 1.5


def get_angle_group(a_dot, b_dot, c_dot, angle_color=WHITE):
    angle = Angle.from_three_points(
        a_dot.get_center(), b_dot.get_center(), c_dot.get_center(),
        radius=ANGLE_RADIUS, color=angle_color, z_index=-2
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
        z_index=-2
    )
    angle_lines = VGroup(
        Line(start=b_dot.get_center(), end=angle.get_start()),
        Line(start=b_dot.get_center(), end=angle.get_end())
    ).set_stroke(width=DEFAULT_STROKE_WIDTH / 2).set_color(angle_color).set_z_index(-2)
    return VGroup(angle, angle_fill, angle_lines)


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(1)

        lato = 5.5
        altezza = lato * SQRT_3_DIV_2
        raggio = altezza * 2 / 3

        a_coords = [- lato / 2, - altezza / 3, 0]
        c_coords = [lato / 2, - altezza / 3, 0]
        b_coords = [0, raggio, 0]
        d_coords = [altezza / 3, - lato / 2, 0]

        a_dot = Dot(a_coords)
        b_dot = Dot(b_coords)
        c_dot = Dot(c_coords)
        d_dot = Dot(d_coords)

        label_dist_ratio = 1.1

        a_label = MathTex("A").move_to(a_dot.get_center() * label_dist_ratio)
        b_label = MathTex("B").move_to(b_dot.get_center() * label_dist_ratio)
        c_label = MathTex("C").move_to(c_dot.get_center() * label_dist_ratio)
        d_label = MathTex("D").move_to(d_dot.get_center() * label_dist_ratio)

        ab_line = Line(a_coords, b_coords)
        bc_line = Line(b_coords, c_coords)
        cd_line = Line(c_coords, d_coords)
        da_line = Line(d_coords, a_coords)

        circonferenza = Circle(radius=raggio, z_index=-1, color=LIGHT_GREY).rotate(7 * PI / 6).reverse_direction()

        self.play(Create(a_dot), Create(ab_line), Write(a_label))
        self.play(Create(b_dot), Create(bc_line), Write(b_label))
        self.play(Create(c_dot), Create(cd_line), Write(c_label))
        self.play(Create(d_dot), Create(da_line), Write(d_label))
        self.play(Create(circonferenza, rate_func=linear))
        self.cut_and_wait()

        ac_line = Line(a_coords, c_coords, color=LIGHT_GREY, z_index=-1)
        self.play(Create(ac_line))
        tic1 = Text(r"//").set_color(BLUE).scale(.5).move_to(ab_line).rotate(ab_line.get_angle())
        tic2 = Text(r"//").set_color(BLUE).scale(.5).move_to(bc_line).rotate(bc_line.get_angle())
        tic3 = Text(r"//").set_color(BLUE).scale(.5).move_to(ac_line).rotate(ac_line.get_angle())
        self.play(Write(tic1), Write(tic2), Write(tic3))
        self.cut_and_wait()

        cad_angle = get_angle_group(d_dot, a_dot, c_dot, YELLOW)
        self.play(Create(cad_angle))
        cad_angle_value = MathTex(r"15^{\circ}", color=YELLOW)
        cad_angle_value.next_to(cad_angle, RIGHT, buff=.15).shift(.03 * DOWN)
        # cad_angle_value.move_to(cad_angle[0].get_center() + .40 * UP)
        self.play(Write(cad_angle_value))

        misura_lato = Tex("12 cm", color=RED)\
            .move_to(da_line.get_center())\
            .shift(.30 * DOWN)\
            .rotate(PI + da_line.get_angle(), about_point=da_line.get_center())
        self.play(Write(misura_lato))
        self.cut_and_wait()

        quadrilatero = Polygon(a_dot.get_center(), b_dot.get_center(), c_dot.get_center(), d_dot.get_center(),
                               color=WHITE, fill_color=DARK_BLUE, fill_opacity=1, z_index=-3)
        self.play(Create(quadrilatero))

        domanda = MathTex(r"\mathcal{A} = \,?", color=BLACK).scale(2).move_to(quadrilatero)
        self.play(Write(domanda))

        self.wait(30)
