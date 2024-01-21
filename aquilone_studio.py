import math

from manim import *

DELAY = 1

SQRT_3 = math.sqrt(3)
SQRT_3_DIV_2 = SQRT_3 / 2

ANGLE_RADIUS = 1
VALUE_ANGLE_RADIUS = 1.4


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

        ac_line = Line(a_coords, c_coords, color=LIGHT_GREY, z_index=-1)
        self.play(Create(ac_line))
        tic1 = Text(r"//").set_color(BLUE).scale(.5).move_to(ab_line).rotate(ab_line.get_angle())
        tic2 = Text(r"//").set_color(BLUE).scale(.5).move_to(bc_line).rotate(bc_line.get_angle())
        tic3 = Text(r"//").set_color(BLUE).scale(.5).move_to(ac_line).rotate(ac_line.get_angle())
        self.play(Write(tic1), Write(tic2), Write(tic3))

        cad_angle = get_angle_group(d_dot, a_dot, c_dot, YELLOW)
        self.play(Create(cad_angle))
        cad_angle_value = MathTex(r"15^{\circ}", color=YELLOW)
        cad_angle_value.move_to(
            Angle.from_three_points(
                d_dot.get_center(), a_dot.get_center(), c_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Write(cad_angle_value))

        misura_lato = MathTex(r"12", color=RED)\
            .move_to(da_line.get_center())\
            .shift(.30 * DOWN)\
            .rotate(PI + da_line.get_angle(), about_point=da_line.get_center())
        self.play(Write(misura_lato))
        self.cut_and_wait()

        o_dot = Dot(ORIGIN)
        o_label = MathTex("O").next_to(o_dot, UR, buff=.05)
        self.play(Create(o_dot), Write(o_label))
        self.cut_and_wait()

        ao_line = Line(a_dot.get_center(), o_dot.get_center())
        self.play(Create(ao_line))
        self.cut_and_wait()

        bao_angle = get_angle_group(o_dot, a_dot, b_dot, BLUE)
        cao_angle = get_angle_group(c_dot, a_dot, o_dot, BLUE)
        self.play(Create(bao_angle), Create(cao_angle))
        self.cut_and_wait()

        cao_angle_value = MathTex(r"30^{\circ}", color=BLUE)
        cao_angle_value.move_to(
            Angle.from_three_points(
                c_dot.get_center(), a_dot.get_center(), o_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        bao_angle_value = MathTex(r"30^{\circ}", color=BLUE)
        bao_angle_value.move_to(
            Angle.from_three_points(
                o_dot.get_center(), a_dot.get_center(), b_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(
            Write(cao_angle_value),
            Write(bao_angle_value)
        )
        self.cut_and_wait()

        self.play(
            FadeOut(bao_angle), FadeOut(bao_angle_value),
            FadeOut(ac_line), FadeOut(tic3)
        )
        dao_angle = get_angle_group(d_dot, a_dot, o_dot, GREEN)
        dao_angle_value = MathTex(r"45^{\circ}", color=GREEN)
        dao_angle_value.move_to(
            Angle.from_three_points(
                d_dot.get_center(), a_dot.get_center(), o_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(
            ReplacementTransform(VGroup(cao_angle, cad_angle), dao_angle),
            ReplacementTransform(VGroup(cao_angle_value, cad_angle_value), dao_angle_value),
        )
        self.cut_and_wait()

        do_line = Line(d_dot.get_center(), o_dot.get_center())
        self.play(Create(do_line))
        self.cut_and_wait()

        tilde1 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(YELLOW).scale(2).move_to(ao_line).rotate(ao_line.get_angle())
        tilde2 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(YELLOW).scale(2).move_to(do_line).rotate(do_line.get_angle())
        self.play(Write(tilde1), Write(tilde2))
        self.cut_and_wait()

        ado_angle = get_angle_group(o_dot, d_dot, a_dot, GREEN)
        ado_angle_value = MathTex(r"45^{\circ}", color=GREEN)
        ado_angle_value.move_to(
            Angle.from_three_points(
                o_dot.get_center(), d_dot.get_center(), a_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Create(ado_angle), Write(ado_angle_value))
        aod_angle = get_angle_group(a_dot, o_dot, d_dot, BLUE)
        aod_angle_value = MathTex(r"90^{\circ}", color=BLUE)
        aod_angle_value.move_to(
            Angle.from_three_points(
                a_dot.get_center(), o_dot.get_center(), d_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Create(aod_angle), Write(aod_angle_value))
        self.cut_and_wait()

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.shift(3.5 * RIGHT))

        formule = [
            MathTex(r"\overline{AD} {{ = }} \overline{AO} {{ \cdot }} \sqrt{2}"),
            MathTex(r"12 {{ = }} \overline{AO} {{ \cdot }} \sqrt{2}"),
            MathTex(r"\overline{AO} {{ = }} \dfrac{12}{\sqrt{2} }"),
            MathTex(r"\overline{AO} {{ = }} \dfrac{12}{2}\sqrt{2}"),
            MathTex(r"\overline{AO} {{ = }} 6\sqrt{2}"),
        ]
        formule[0].move_to(7 * RIGHT)
        self.play(Write(formule[0]))
        for _i in range(1, len(formule)):
            self.wait(1)
            formule[_i].move_to(formule[_i - 1])
            self.play(TransformMatchingTex(formule[_i - 1], formule[_i]))

        self.play(
            FadeOut(dao_angle), FadeOut(dao_angle_value),
            FadeOut(ado_angle), FadeOut(ado_angle_value),
            FadeOut(tilde1), FadeOut(tilde2)
        )
        ao_measure = MathTex(r"6\sqrt{2}", color=RED)\
            .move_to(ao_line.get_center())\
            .shift(.30 * DOWN)\
            .rotate(ao_line.get_angle(), about_point=ao_line.get_center())
        self.play(Write(ao_measure))
        self.play(FadeOut(formule[-1]))
        self.cut_and_wait()

        ado_triangle = Polygon(
            a_dot.get_center(), d_dot.get_center(), o_dot.get_center(),
            color=BLUE_E, fill_color=BLUE_E, fill_opacity=.5, z_index=-3)
        self.play(Create(ado_triangle))

        formule = [
            MathTex(r"{{ \mathcal{A}_{ADO} = }} \dfrac{1}{2} \cdot {{ \overline{AO} }} ^2"),
            MathTex(r"{{ \mathcal{A}_{ADO} = }} \dfrac{1}{2} \cdot {{ (6\sqrt{2}) }} ^2"),
            MathTex(r"{{ \mathcal{A}_{ADO} = }} \dfrac{1}{2} \cdot {{ 72 }}"),
            MathTex(r"{{ \mathcal{A}_{ADO} = }} 36"),
        ]
        formule[0].move_to(7 * RIGHT)
        formule[0][0][:4].set_color(BLUE)
        self.play(Write(formule[0]))
        for _i in range(1, len(formule)):
            self.wait(1)
            formule[_i][0][:4].set_color(BLUE)
            formule[_i].move_to(formule[_i - 1])
            self.play(TransformMatchingTex(formule[_i - 1], formule[_i]))
        area1 = formule[-1]
        self.play(area1.animate.shift(3 * UP))
        self.cut_and_wait()

        bo_line = Line(b_dot.get_center(), o_dot.get_center())
        co_line = Line(c_dot.get_center(), o_dot.get_center())
        self.play(Create(bo_line))
        self.play(Create(co_line))
        self.cut_and_wait()

        abo_triangle = Polygon(
            a_dot.get_center(), b_dot.get_center(), o_dot.get_center(),
            color=GREEN_E, fill_color=GREEN_E, fill_opacity=.5, z_index=-3)
        bco_triangle = Polygon(
            b_dot.get_center(), c_dot.get_center(), o_dot.get_center(),
            color=GREEN_E, fill_color=GREEN_E, fill_opacity=.5, z_index=-3)
        self.play(
            Create(abo_triangle), Create(bco_triangle), FadeOut(tic1), FadeOut(tic2)
        )
        self.cut_and_wait()

        aob_angle = get_angle_group(b_dot, o_dot, a_dot, GREEN)
        aob_angle_value = MathTex(r"120^{\circ}", color=GREEN)
        aob_angle_value.move_to(
            Angle.from_three_points(
                b_dot.get_center(), o_dot.get_center(), a_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Create(aob_angle), Write(aob_angle_value))
        self.cut_and_wait()

        h_dot = Dot((a_dot.get_center() + b_dot.get_center()) / 2)
        h_label = MathTex("H").next_to(h_dot, LEFT, buff=.05)
        oh_line = Line(o_dot.get_center(), h_dot.get_center())
        self.play(Write(h_label), Create(h_dot), Create(oh_line))

        aoh_angle = get_angle_group(h_dot, o_dot, a_dot, GREEN)
        aoh_angle_value = MathTex(r"60^{\circ}", color=GREEN)
        aoh_angle_value.move_to(
            Angle.from_three_points(
                h_dot.get_center(), o_dot.get_center(), a_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        boh_angle = get_angle_group(b_dot, o_dot, h_dot, GREEN)
        boh_angle_value = MathTex(r"60^{\circ}", color=GREEN)
        boh_angle_value.move_to(
            Angle.from_three_points(
                b_dot.get_center(), o_dot.get_center(), h_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(
            FadeOut(aob_angle), FadeOut(aob_angle_value),
            Create(aoh_angle), Write(aoh_angle_value),
            Create(boh_angle), Write(boh_angle_value),
        )
        self.cut_and_wait()

        formule1 = [
            MathTex(r"\overline{OH} = {{ \dfrac{1}{2} \cdot }} \overline{AO}"),
            MathTex(r"\overline{OH} = {{ \dfrac{1}{2} \cdot }} 6\sqrt{2}"),
            MathTex(r"\overline{OH} = {{ 3\sqrt{2} }}"),
        ]
        formule1[0].move_to(7 * RIGHT)
        self.play(Write(formule1[0]))
        for _i in range(1, len(formule1)):
            self.wait(1)
            formule1[_i].move_to(formule1[_i - 1])
            self.play(TransformMatchingTex(formule1[_i - 1], formule1[_i]))
        self.cut_and_wait()

        formule2 = [
            MathTex(r"\overline{AH} = {{ \dfrac{ \sqrt{3} }{2} \cdot }} \overline{AO}"),
            MathTex(r"\overline{AH} = {{ \dfrac{ \sqrt{3} }{2} \cdot }} 6\sqrt{2}"),
            MathTex(r"\overline{AH} = {{ 3\sqrt{6} }}"),
        ]
        formule2[0].next_to(formule1[-1], DOWN)
        self.play(Write(formule2[0]))
        for _i in range(1, len(formule2)):
            self.wait(1)
            formule2[_i].move_to(formule2[_i - 1])
            self.play(TransformMatchingTex(formule2[_i - 1], formule2[_i]))
        self.play(formule2[-1].animate.next_to(formule1[-1], DOWN))
        self.cut_and_wait()

        formule3 = [
            MathTex(r"\overline{AB} = {{ 2 \cdot }} \overline{AH}"),
            MathTex(r"\overline{AB} = {{ 2 \cdot }} 3 {{\sqrt{6} }}"),
            MathTex(r"\overline{AB} = {{ 6 }} \sqrt{6}"),
        ]
        formule3[0].next_to(formule2[-1], DOWN)
        self.play(Write(formule3[0]))
        for _i in range(1, len(formule3)):
            self.wait(1)
            formule3[_i].move_to(formule3[_i - 1])
            self.play(TransformMatchingTex(formule3[_i - 1], formule3[_i]))
        self.cut_and_wait()

        formule4 = [
            MathTex(r"\mathcal{A}_{ABO} = {{ \dfrac{1}{2} \cdot }} \overline{AB} {{ \cdot }} \overline{OH}"),
            MathTex(r"\mathcal{A}_{ABO} = {{ \dfrac{1}{2} \cdot }} 6\sqrt{6} {{ \cdot }} 3\sqrt{2}"),
            MathTex(r"\mathcal{A}_{ABO} = {{ 18\sqrt{3} }}"),
        ]
        formule4[0].next_to(formule3[-1], DOWN)
        formule4[0][0][:4].set_color(GREEN)
        self.play(Write(formule4[0]))
        for _i in range(1, len(formule4)):
            self.wait(1)
            formule4[_i][0][:4].set_color(GREEN)
            formule4[_i].move_to(formule4[_i - 1])
            self.play(TransformMatchingTex(formule4[_i - 1], formule4[_i]))
        self.play(
            FadeOut(h_dot), FadeOut(h_label), FadeOut(oh_line),
            FadeOut(aoh_angle), FadeOut(aoh_angle_value),
            FadeOut(boh_angle), FadeOut(boh_angle_value),
            FadeIn(aob_angle), FadeIn(aob_angle_value),
            FadeOut(formule1[-1]), FadeOut(formule2[-1]), FadeOut(formule3[-1]),
        )
        area2 = formule4[-1]
        self.play(area2.animate.next_to(area1, DOWN))
        self.cut_and_wait()

        boc_angle = get_angle_group(c_dot, o_dot, b_dot, GREEN)
        boc_angle_value = MathTex(r"120^{\circ}", color=GREEN)
        boc_angle_value.move_to(
            Angle.from_three_points(
                c_dot.get_center(), o_dot.get_center(), b_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Create(boc_angle), Write(boc_angle_value))
        area3 = MathTex(r"\mathcal{A}_{BCO} = 18\sqrt{3}").next_to(area2, DOWN)
        area3[0][:4].set_color(GREEN)
        self.play(Write(area3))
        self.cut_and_wait()

        cdo_triangle = Polygon(c_dot.get_center(), d_dot.get_center(), o_dot.get_center(),
                               color=YELLOW, fill_color=YELLOW, fill_opacity=.5, z_index=-3)
        self.play(Create(cdo_triangle))
        self.cut_and_wait()

        cod_angle = get_angle_group(d_dot, o_dot, c_dot, YELLOW)
        cod_angle_value = MathTex(r"30^{\circ}", color=YELLOW)
        cod_angle_value.move_to(
            Angle.from_three_points(
                d_dot.get_center(), o_dot.get_center(), c_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(Create(cod_angle), Write(cod_angle_value))
        self.cut_and_wait()

        k_dot = Dot((c_dot.get_center() + d_dot.get_center())/2)
        k_label = MathTex("K").next_to(k_dot, DR, buff=.05)
        ok_line = Line(o_dot.get_center(), k_dot.get_center())
        self.play(Create(k_dot), Write(k_label), Create(ok_line))

        cok_angle = get_angle_group(k_dot, o_dot, c_dot, YELLOW)
        cok_angle_value = MathTex(r"15^{\circ}", color=YELLOW).scale(.5)
        cok_angle_value.move_to(
            Angle.from_three_points(
                k_dot.get_center(), o_dot.get_center(), c_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        dok_angle = get_angle_group(d_dot, o_dot, k_dot, YELLOW)
        dok_angle_value = MathTex(r"15^{\circ}", color=YELLOW).scale(.5)
        dok_angle_value.move_to(
            Angle.from_three_points(
                d_dot.get_center(), o_dot.get_center(), k_dot.get_center(),
                radius=VALUE_ANGLE_RADIUS).get_midpoint()
        )
        self.play(
            FadeOut(cod_angle), FadeOut(cod_angle_value),
            Create(cok_angle), Write(cok_angle_value),
            Create(dok_angle), Write(dok_angle_value),
        )
        self.cut_and_wait()

        formule1 = [
            MathTex(r"\overline{OK} = {{ \overline{CO} }} \cdot {{ \cos 15^\circ }}"),
            MathTex(r"\overline{OK} = {{ 6\sqrt{2} }} \cdot {{ \dfrac{\sqrt{6} + \sqrt{2} }{4} }}"),
            MathTex(r"\overline{OK} = {{ \dfrac{12\sqrt{3} + 12 }{4} }}"),
            MathTex(r"\overline{OK} = {{ 3(\sqrt{3} + 1) }}"),
        ]
        formule1[0].move_to(7 * RIGHT)
        self.play(Write(formule1[0]))
        self.cut_and_wait()

        cos_15 = MathTex(r"\cos 15^\circ &= \cos(45^\circ - 30^\circ) = \\",
                         r"&= \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ = \\",
                         r"&= \dfrac{\sqrt{2}}{2} \cdot \dfrac{\sqrt{3}}{2} + \dfrac{\sqrt{2}}{2} \cdot \dfrac{1}{2} = \\",
                         r"&= \dfrac{\sqrt{6} + \sqrt{2}}{4}").shift(3.5 * RIGHT).add_background_rectangle(buff=.5, opacity=.9)
        cos_15_surr = SurroundingRectangle(cos_15, buff=0)
        self.play(Write(cos_15), Create(cos_15_surr))
        self.cut_and_wait()

        self.play(FadeOut(cos_15_surr), FadeOut(cos_15))
        for _i in range(1, len(formule1)):
            self.wait(1)
            formule1[_i].move_to(formule1[_i - 1])
            self.play(TransformMatchingTex(formule1[_i - 1], formule1[_i]))
        self.cut_and_wait()

        formule2 = [
            MathTex(r"\overline{CK} = {{ \overline{CO} }} \cdot {{ \sin 15^\circ }}"),
            MathTex(r"\overline{CK} = {{ 6\sqrt{2} }} \cdot {{ \dfrac{\sqrt{6} - \sqrt{2} }{4} }}"),
            MathTex(r"\overline{CK} = {{ \dfrac{12\sqrt{3} - 12 }{4} }}"),
            MathTex(r"\overline{CK} = {{ 3(\sqrt{3} - 1) }}"),
        ]
        formule2[0].next_to(formule1[-1], DOWN)
        self.play(Write(formule2[0]))
        for _i in range(1, len(formule2)):
            self.wait(1)
            formule2[_i].move_to(formule2[_i - 1])
            self.play(TransformMatchingTex(formule2[_i - 1], formule2[_i]))
        self.cut_and_wait()

        formule3 = [
            MathTex(r"\overline{CD} = {{ 2 \cdot }} \overline{CK}"),
            MathTex(r"\overline{CD} = {{ 2 \cdot }} 3(\sqrt{3} - 1)"),
            MathTex(r"\overline{CD} = {{ 6(\sqrt{3} - 1) }}"),
        ]
        formule3[0].next_to(formule2[-1], DOWN)
        self.play(Write(formule3[0]))
        for _i in range(1, len(formule3)):
            self.wait(1)
            formule3[_i].move_to(formule3[_i - 1])
            self.play(TransformMatchingTex(formule3[_i - 1], formule3[_i]))
        self.cut_and_wait()

        formule4 = [
            MathTex(r"\mathcal{A}_{CDO} = {{ \dfrac{1}{2} }} \cdot {{ \overline{CD} }} \cdot {{ \overline{OK} }}"),
            MathTex(r"\mathcal{A}_{CDO} = {{ \dfrac{1}{2} }} \cdot {{ 6(\sqrt{3} - 1) }} \cdot {{ 3(\sqrt{3} + 1) }}"),
            MathTex(r"\mathcal{A}_{CDO} = {{ \dfrac{1}{2} }} \cdot {{ 18(3 - 1) }}"),
            MathTex(r"\mathcal{A}_{CDO} = {{ 18 }}"),
        ]
        formule4[0].next_to(formule3[-1], DOWN)
        formule4[0][0][:4].set_color(YELLOW)
        self.play(Write(formule4[0]))
        for _i in range(1, len(formule4)):
            self.wait(1)
            formule4[_i][0][:4].set_color(YELLOW)
            formule4[_i].move_to(formule4[_i - 1])
            self.play(TransformMatchingTex(formule4[_i - 1], formule4[_i]))
        self.play(
            FadeOut(k_dot), FadeOut(k_label), FadeOut(ok_line),
            FadeOut(cok_angle), FadeOut(cok_angle_value),
            FadeOut(dok_angle), FadeOut(dok_angle_value),
            FadeIn(cod_angle), FadeIn(cod_angle_value),
            FadeOut(formule1[-1]), FadeOut(formule2[-1]), FadeOut(formule3[-1]),
        )
        area4 = formule4[-1]
        self.play(area4.animate.next_to(area3, DOWN))
        self.cut_and_wait()

        somma = Line(ORIGIN, area2.width * RIGHT).next_to(area4, DOWN)
        self.play(Create(somma))
        area = MathTex(r"\mathcal{A} = 54 + 36\sqrt{3}").next_to(somma, DOWN)
        self.play(Write(area))

        self.wait(30)
