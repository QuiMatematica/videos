import math

from manim import *

DELAY = 1

LATO = 5

ABCD_LABEL_BUFF = .1
EFGH_LABEL_BUFF = .12

RAD_3_DIV_2 = math.sqrt(3) / 2
UN_MEZZO = 1 / 2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        quadrato = Square(side_length=LATO).shift(.5 * UP)
        self.play(Create(quadrato))
        center = quadrato.get_center()

        vertici = quadrato.get_vertices()
        a_label = MathTex("A").next_to(vertici[2], DL, buff=ABCD_LABEL_BUFF)
        b_label = MathTex("B").next_to(vertici[3], DR, buff=ABCD_LABEL_BUFF)
        c_label = MathTex("C").next_to(vertici[0], UR, buff=ABCD_LABEL_BUFF)
        d_label = MathTex("D").next_to(vertici[1], UL, buff=ABCD_LABEL_BUFF)

        abcd_labels = VGroup(a_label, b_label, c_label, d_label)
        self.play(Write(abcd_labels))

        brace_lato = Brace(mobject=Line(start=vertici[2], end=vertici[3]), buff=.6, color=YELLOW)
        self.play(Create(brace_lato))
        misura_lato = Tex("1", color=YELLOW).next_to(brace_lato, DOWN, buff=.15)
        self.play(Write(misura_lato))

        arco_bd = Arc(arc_center=vertici[2], radius=LATO, start_angle=0, angle=PI / 2)
        self.play(Create(arco_bd))
        arco_ca = Arc(arc_center=vertici[3], radius=LATO, start_angle=PI / 2, angle=PI / 2)
        self.play(Create(arco_ca))
        arco_db = Arc(arc_center=vertici[0], radius=LATO, start_angle=PI, angle=PI / 2)
        self.play(Create(arco_db))
        arco_ac = Arc(arc_center=vertici[1], radius=LATO, start_angle=3 * PI / 2, angle=PI / 2)
        self.play(Create(arco_ac))

        e_point = Dot(point=vertici[3] + RAD_3_DIV_2 * LATO * LEFT + UN_MEZZO * LATO * UP)
        e_label = MathTex("E").next_to(e_point, LEFT, buff=EFGH_LABEL_BUFF)
        f_point = Dot(point=vertici[0] + RAD_3_DIV_2 * LATO * DOWN + UN_MEZZO * LATO * LEFT)
        f_label = MathTex("F").next_to(f_point, DOWN, buff=EFGH_LABEL_BUFF)
        g_point = Dot(point=vertici[1] + RAD_3_DIV_2 * LATO * RIGHT + UN_MEZZO * LATO * DOWN)
        g_label = MathTex("G").next_to(g_point, RIGHT, buff=EFGH_LABEL_BUFF)
        h_point = Dot(point=vertici[2] + RAD_3_DIV_2 * LATO * UP + UN_MEZZO * LATO * RIGHT)
        h_label = MathTex("H").next_to(h_point, UP, buff=EFGH_LABEL_BUFF)

        efgh_points = VGroup(e_point, f_point, g_point, h_point)
        efgh_labels = VGroup(e_label, f_label, g_label, h_label)
        self.play(Create(efgh_points), Write(efgh_labels))
        self.cut_and_wait()

        o_point = Dot(center)
        o_label = MathTex("O").next_to(o_point, DL, buff=ABCD_LABEL_BUFF)
        self.play(Create(o_point), Write(o_label))
        self.cut_and_wait()

        oe = Line(start=o_point.get_center(), end=e_point.get_center())
        of = Line(start=o_point.get_center(), end=f_point.get_center())
        og = Line(start=o_point.get_center(), end=g_point.get_center())
        oh = Line(start=o_point.get_center(), end=h_point.get_center())
        self.play(Create(VGroup(oe, of, og, oh)))
        self.cut_and_wait()

        circles = [Circle(arc_center=_v, radius=LATO, color=WHITE, fill_color=BLUE, fill_opacity=1) for _v in vertici]
        squares = [Square(side_length=LATO).move_to(_v) for _v in vertici]

        regions = []
        for _i in range(4):
            _j = _i + 2
            if _j > 3:
                _j = _j - 4
            regions.append(Intersection(circles[_j], squares[_i], color=WHITE, fill_color=BLUE, fill_opacity=1))
        self.play(Create(regions[0]))

        for _i in range(1, 4):
            clone = regions[_i - 1].copy()
            self.play(Rotate(clone, angle=PI / 2, about_point=center))
            self.add(regions[_i])
            self.remove(clone)

        self.cut_and_wait()

        self.play(self.camera.frame.animate.shift(3.5 * RIGHT))
        self.play(
            *[FadeOut(regions[_i]) for _i in range(1, 4)],
        )
        r_region = regions[0]
        r_name = MathTex(r"\mathcal{R}", color=BLACK).move_to(center + .7 * UR)
        self.play(Write(r_name))
        self.cut_and_wait()

        formula_area_quadrilatero_curvilineo = MathTex(r"\mathcal{A}_{EFGH} = 4 \mathcal{R}").to_edge(UP).shift(
            7 * RIGHT)
        self.play(Write(formula_area_quadrilatero_curvilineo))
        self.cut_and_wait()

        self.play(
            FadeOut(arco_ca), FadeOut(arco_ac), FadeOut(arco_db),
            FadeOut(oe), FadeOut(of),
            FadeOut(e_point), FadeOut(e_label),
            FadeOut(f_point), FadeOut(f_label),
        )

        ag = Line(start=vertici[2], end=g_point.get_center())
        ao = Line(start=vertici[2], end=o_point.get_center())
        ah = Line(start=vertici[2], end=h_point.get_center())
        self.play(Create(ag), Create(ao), Create(ah))
        self.cut_and_wait()

        formula_area_r = \
            MathTex(
                r"\mathcal{R} = {{ \mathcal{Q} }} - \mathcal{S}_1 - \mathcal{S}_2 {{ - \mathcal{T}_1 - \mathcal{T}_2 }}"). \
                next_to(formula_area_quadrilatero_curvilineo, DOWN)
        self.play(Write(formula_area_r[0]))
        self.cut_and_wait()

        q_region = Intersection(circles[2], quadrato, color=WHITE, fill_color=BLUE, fill_opacity=.5, z_index=-1)
        q_name = MathTex(r"\mathcal{Q}", color=BLACK).move_to(vertici[2] + UR)
        self.play(Create(q_region), Write(q_name))
        self.play(Write(formula_area_r[1]))
        self.cut_and_wait()

        s1_region = Sector(
            outer_radius=LATO, inner_radius=0, arc_center=vertici[2], start_angle=0, angle=PI / 6,
            color=WHITE, fill_color=RED_B, fill_opacity=1, stroke_width=DEFAULT_STROKE_WIDTH
        )
        s2_region = Sector(
            outer_radius=LATO, inner_radius=0, arc_center=vertici[2], start_angle=PI / 3, angle=PI / 6,
            color=WHITE, fill_color=RED_E, fill_opacity=1, stroke_width=DEFAULT_STROKE_WIDTH
        )
        self.play(Create(s1_region), Create(s2_region))
        s1_name = MathTex(r"\mathcal{S}_1", color=BLACK).move_to(vertici[2] + LATO * RIGHT / 2 + LATO * UP / 8)
        s2_name = MathTex(r"\mathcal{S}_2", color=BLACK).move_to(vertici[2] + LATO * UP / 2 + LATO * RIGHT / 8)
        self.play(Write(s1_name), Write(s2_name))
        self.play(Write(formula_area_r[2]))
        self.cut_and_wait()

        t1_region = Polygon(
            vertici[2], g_point.get_center(), o_point.get_center(),
            color=WHITE, fill_color=GREEN_B, fill_opacity=1
        )
        t2_region = Polygon(
            vertici[2], h_point.get_center(), o_point.get_center(),
            color=WHITE, fill_color=GREEN_E, fill_opacity=1
        )
        self.play(Create(t1_region), Create(t2_region))
        t1_name = MathTex(r"\mathcal{T}_1", color=BLACK).move_to(vertici[2] + LATO * RIGHT / 2 + LATO * UP / 2.6)
        t2_name = MathTex(r"\mathcal{T}_2", color=BLACK).move_to(vertici[2] + LATO * UP / 2 + LATO * RIGHT / 2.6)
        self.play(Write(t1_name), Write(t2_name))
        self.play(Write(formula_area_r[3]))
        self.cut_and_wait()

        self.play(
            FadeOut(t1_region), FadeOut(t1_name),
            FadeOut(t2_region), FadeOut(t2_name),
            FadeOut(s1_region), FadeOut(s1_name),
            FadeOut(s2_region), FadeOut(s2_name),
            FadeOut(r_region), FadeOut(r_name),
            FadeOut(ao), FadeOut(ag), FadeOut(ah)
        )

        formula_area_q = \
            MathTex(r"\mathcal{Q} = \dfrac{\pi r^2}{4} {{ = \dfrac{\pi}{4} }}"). \
                next_to(formula_area_r, DOWN)
        self.play(Write(formula_area_q[0]))
        self.cut_and_wait()
        self.play(Write(formula_area_q[1]))
        self.cut_and_wait()

        # Area S1 S2

        self.play(
            FadeOut(q_name),
            FadeIn(s1_region), FadeIn(s1_name),
            FadeIn(s2_region), FadeIn(s2_name),
        )
        self.cut_and_wait()

        clone = s1_region.copy()
        self.play(Rotate(clone, about_point=vertici[2], angle=PI / 3))
        self.cut_and_wait()

        self.play(
            FadeOut(clone),
            FadeOut(s2_region), FadeOut(s2_name),
        )
        self.cut_and_wait()

        agd_triangle = Polygon(
            vertici[2], g_point.get_center(), vertici[1], color=YELLOW
        )
        self.play(Create(agd_triangle))
        self.cut_and_wait()

        clone_ac = arco_ac.copy()
        clone_ac.set_color(YELLOW)
        clone_bd = arco_bd.copy()
        clone_bd.set_color(YELLOW)
        self.play(Create(clone_ac), Create(clone_bd))
        self.cut_and_wait()

        dag_angle = Angle(
            Line(start=vertici[2], end=g_point.get_center()),
            Line(start=vertici[2], end=vertici[1]),
            color=YELLOW
        )
        dag_angle_mes = MathTex(r"60^{\circ}", color=YELLOW).move_to(
            Angle(
                Line(start=vertici[2], end=g_point.get_center()),
                Line(start=vertici[2], end=vertici[1]),
                radius=.8
            ).get_midpoint()
        )
        self.play(Create(dag_angle), Write(dag_angle_mes))
        self.cut_and_wait()

        bag_angle = Angle(
            Line(start=vertici[2], end=vertici[3]),
            Line(start=vertici[2], end=g_point.get_center()),
            radius=.8
        )
        bag_angle_mes = MathTex(r"30^{\circ}").move_to(
            Angle(
                Line(start=vertici[2], end=vertici[3]),
                Line(start=vertici[2], end=g_point.get_center()),
                radius=1.4
            ).get_midpoint()
        )
        self.play(
            Create(bag_angle), Write(bag_angle_mes),
            FadeOut(clone_ac), FadeOut(clone_bd),
            FadeOut(agd_triangle), FadeOut(dag_angle), FadeOut(dag_angle_mes)
        )
        self.cut_and_wait()

        formula_area_s1 = \
            MathTex(r"\mathcal{S}_1 = \dfrac{\pi r^2}{12} = \dfrac{\pi}{12}").next_to(formula_area_q, DOWN)
        self.play(Write(formula_area_s1))
        self.cut_and_wait()

        formula_area_s1_s2 = \
            MathTex(r"\mathcal{S}_1 = \mathcal{S}_2 = \dfrac{\pi}{12}").next_to(formula_area_q, DOWN)
        self.play(
            ReplacementTransform(formula_area_s1, formula_area_s1_s2),
            FadeIn(s2_region), FadeIn(s2_name),
            FadeOut(bag_angle), FadeOut(bag_angle_mes)
        )
        self.cut_and_wait()

        # Area T1 T2

        self.play(
            FadeOut(s1_region), FadeOut(s1_name),
            FadeOut(s2_region), FadeOut(s2_name),
            FadeIn(t1_region), FadeIn(t1_name),
            FadeIn(t2_region), FadeIn(t2_name),
        )
        self.cut_and_wait()

        self.play(
            FadeOut(t2_region), FadeOut(t2_name), o_label.animate.set_z_index(10), o_point.animate.set_z_index(10)
        )
        self.cut_and_wait()

        self.play(Create(agd_triangle))
        i_point = Dot(vertici[2] + LATO * UP / 2, color=YELLOW)
        i_label = MathTex("I", color=YELLOW).next_to(i_point, DL, ABCD_LABEL_BUFF)
        ig = Line(start=g_point.get_center(), end=i_point.get_center(), color=YELLOW)
        self.play(Create(ig), Create(i_point), Write(i_label))
        self.cut_and_wait()

        scale_formule = .8

        formule_gi_oi = VGroup(
            MathTex(r"\overline{GI} = \dfrac{\sqrt{3}}{2}"),
            MathTex(r"\overline{OI} = \dfrac{1}{2}")
        ).scale(scale_formule).arrange(RIGHT, buff=1).next_to(formula_area_s1_s2, DOWN)
        self.play(Write(formule_gi_oi[0]))
        self.cut_and_wait()
        self.play(Write(formule_gi_oi[1]))
        self.cut_and_wait()

        formule_go_ai = VGroup(
            MathTex(r"\overline{GO} = \dfrac{\sqrt{3} - 1}{2}"),
            MathTex(r"\overline{AI} = \dfrac{1}{2}")
        ).scale(scale_formule).arrange(RIGHT, buff=1).next_to(formule_gi_oi, DOWN)
        self.play(Write(formule_go_ai[0]))
        self.cut_and_wait()
        self.play(Write(formule_go_ai[1]))
        self.cut_and_wait()

        formula_area_t1 = \
            MathTex(r"\mathcal{T}_1 = \dfrac{1}{2} \cdot \overline{GO} \cdot \overline{AI} = \dfrac{\sqrt{3} - 1}{8}").next_to(formule_go_ai, DOWN)
        self.play(Write(formula_area_t1))
        self.cut_and_wait()

        formula_area_t1_t2 = \
            MathTex(r"\mathcal{T}_1 = \mathcal{T}_2 = \dfrac{\sqrt{3} - 1}{8}").next_to(formule_go_ai, DOWN)
        self.play(
            ReplacementTransform(formula_area_t1, formula_area_t1_t2),
            FadeIn(t2_region), FadeIn(t2_name),
            FadeOut(agd_triangle), FadeOut(ig), FadeOut(i_point), FadeOut(i_label)
        )
        self.play(
            FadeOut(formule_gi_oi), FadeOut(formule_go_ai),
            formula_area_t1_t2.animate.next_to(formula_area_s1_s2, DOWN)
        )
        self.cut_and_wait()

        # Area di R

        formula_area_r_1 = MathTex(
                r"\mathcal{R} = \dfrac{\pi}{4} - \dfrac{\pi}{12} - \dfrac{\pi}{12} - \dfrac{\sqrt{3} - 1}{8} - \dfrac{\sqrt{3} - 1}{8}"
        ).scale(.8).next_to(formula_area_t1_t2, DOWN)
        self.play(
            FadeIn(r_region), FadeIn(r_name),
            FadeIn(s1_region), FadeIn(s1_name),
            FadeIn(s2_region), FadeIn(s2_name),
        )

        self.play(Write(formula_area_r_1[0][:2]))
        clone1 = formula_area_q[1][1:].copy()
        clone1.target = formula_area_r_1[0][2:5]
        self.play(MoveToTarget(clone1))
        self.play(Write(formula_area_r_1[0][5]))
        clone2 = formula_area_s1_s2[0][6:].copy()
        clone2.target = formula_area_r_1[0][6:10]
        self.play(MoveToTarget(clone2))
        self.play(Write(formula_area_r_1[0][10]))
        clone3 = formula_area_s1_s2[0][6:].copy()
        clone3.target = formula_area_r_1[0][11:15]
        self.play(MoveToTarget(clone3))
        self.play(Write(formula_area_r_1[0][15]))
        clone4 = formula_area_t1_t2[0][6:].copy()
        clone4.target = formula_area_r_1[0][16:23]
        self.play(MoveToTarget(clone4))
        self.play(Write(formula_area_r_1[0][23]))
        clone5 = formula_area_t1_t2[0][6:].copy()
        clone5.target = formula_area_r_1[0][24:]
        self.play(MoveToTarget(clone5))

        self.add(formula_area_r_1)
        self.remove(clone1, clone2, clone3, clone4, clone5)

        formula_area_r_2 = MathTex(
                r"\mathcal{R} = \dfrac{\pi}{12} - \dfrac{\sqrt{3} - 1}{4}"
        ).next_to(formula_area_t1_t2, DOWN)
        self.play(ReplacementTransform(formula_area_r_1, formula_area_r_2))
        self.play(
            FadeOut(formula_area_r),
            VGroup(formula_area_q, formula_area_s1_s2, formula_area_t1_t2, formula_area_r_2).animate.next_to(formula_area_quadrilatero_curvilineo, DOWN)
        )
        self.cut_and_wait()

        self.play(
            FadeOut(t1_region), FadeOut(t1_name),
            FadeOut(t2_region), FadeOut(t2_name),
            FadeOut(s1_region), FadeOut(s1_name),
            FadeOut(s2_region), FadeOut(s2_name),
            FadeOut(q_region),
            FadeIn(arco_ca), FadeIn(arco_ac), FadeIn(arco_db),
            FadeIn(e_point), FadeIn(e_label),
            FadeIn(f_point), FadeIn(f_label),
            *[FadeIn(regions[_i]) for _i in range(1, 4)]
        )

        finale_1 = MathTex(r"\mathcal{A}_{EFGH} = 4 \biggr(\dfrac{\pi}{12} - \dfrac{\sqrt{3} - 1}{4} \biggl)")
        finale_1.next_to(formula_area_r_2, DOWN)

        clone1 = formula_area_quadrilatero_curvilineo[0][:7].copy()
        self.play(clone1.animate.move_to(finale_1[0][:7]))
        self.play(Write(finale_1[0][7]), Write(finale_1[0][20]))
        clone2 = formula_area_r_2[0][2:].copy()
        self.play(clone2.animate.move_to(finale_1[0][8:20]))
        self.add(finale_1)
        self.remove(clone1, clone2)

        finale_2 = MathTex(r"\mathcal{A}_{EFGH} = \dfrac{\pi}{3} - \sqrt{3} +1").next_to(formula_area_r_2, DOWN)
        self.play(ReplacementTransform(finale_1, finale_2))

        self.wait(30)
