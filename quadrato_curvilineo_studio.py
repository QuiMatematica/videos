import math

from manim import *

DELAY = 1

LATO = 5

ABCD_LABEL_BUFF = .1
EFGH_LABEL_BUFF = .2

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

        arco_bd = Arc(arc_center=vertici[2], radius=LATO, start_angle=0, angle=PI/2)
        self.play(Create(arco_bd))
        arco_ca = Arc(arc_center=vertici[3], radius=LATO, start_angle=PI/2, angle=PI/2)
        self.play(Create(arco_ca))
        arco_db = Arc(arc_center=vertici[0], radius=LATO, start_angle=PI, angle=PI/2)
        self.play(Create(arco_db))
        arco_ac = Arc(arc_center=vertici[1], radius=LATO, start_angle=3 * PI / 2, angle=PI/2)
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
            self.play(Rotate(clone, angle=PI/2, about_point=center))
            self.add(regions[_i])
            self.remove(clone)

        self.cut_and_wait()

        self.play(self.camera.frame.animate.shift(3.5 * RIGHT))
        self.play(
            *[FadeOut(regions[_i]) for _i in range(1, 4)],
        )
        r_name = MathTex(r"\mathcal{R}", color=BLACK).move_to(center + .7 * UR)
        self.play(Write(r_name))
        self.cut_and_wait()

        formula_area_quadrilatero_curvilineo = MathTex(r"\mathcal{A}_{EFGH} = 4 \mathcal{R}").to_edge(UP).shift(7 * RIGHT)
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
            MathTex(r"\mathcal{R} = {{ \mathcal{Q} }} - \mathcal{S}_1 {{ - \mathcal{S}_2 }} - \mathcal{T}_1 {{ - \mathcal{T}_2 }}").\
                next_to(formula_area_quadrilatero_curvilineo, DOWN)
        self.play(Write(formula_area_r[0]))
        self.cut_and_wait()

        q_region = Intersection(circles[2], quadrato, color=WHITE, fill_color=BLUE, fill_opacity=.5, z_index=-1)
        q_name = MathTex(r"\mathcal{Q}", color=BLACK).move_to(vertici[2] + UR)
        self.play(Create(q_region), Write(q_name))
        self.play(Write(formula_area_r[1]))
        self.cut_and_wait()


        self.wait(30)
