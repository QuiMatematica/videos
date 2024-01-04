import math

from manim import *

DELAY = 30

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

        vertici = quadrato.get_vertices()
        a_label = MathTex("A").next_to(vertici[2], DL, buff=ABCD_LABEL_BUFF)
        b_label = MathTex("B").next_to(vertici[3], DR, buff=ABCD_LABEL_BUFF)
        c_label = MathTex("C").next_to(vertici[0], UR, buff=ABCD_LABEL_BUFF)
        d_label = MathTex("D").next_to(vertici[1], UL, buff=ABCD_LABEL_BUFF)

        abcd_labels = VGroup(a_label, b_label, c_label, d_label)
        self.play(Write(abcd_labels))
        self.cut_and_wait()

        brace_lato = Brace(mobject=Line(start=vertici[2], end=vertici[3]), buff=.6, color=YELLOW)
        self.play(Create(brace_lato))
        misura_lato = Tex(" 1 dm", color=YELLOW).next_to(brace_lato, DOWN, buff=.15)
        self.play(Write(misura_lato))
        self.cut_and_wait()

        arco_bd = Arc(arc_center=vertici[2], radius=LATO, start_angle=0, angle=PI/2)
        self.play(Create(arco_bd))
        arco_ca = Arc(arc_center=vertici[3], radius=LATO, start_angle=PI/2, angle=PI/2)
        self.play(Create(arco_ca))
        arco_db = Arc(arc_center=vertici[0], radius=LATO, start_angle=PI, angle=PI/2)
        self.play(Create(arco_db))
        arco_ac = Arc(arc_center=vertici[1], radius=LATO, start_angle=3 * PI / 2, angle=PI/2)
        self.play(Create(arco_ac))
        self.cut_and_wait()

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

        circles = []
        for _i in range(4):
            circles.append(Circle(arc_center=vertici[_i], radius=LATO, fill_opacity=1))
        quadrilatero = Intersection(*circles, color=WHITE, fill_color=BLUE, fill_opacity=1)
        self.play(Create(quadrilatero))

        domanda = MathTex(r"\mathcal{A} = \,?", color=BLACK).scale(2).move_to(quadrilatero)
        self.play(Write(domanda))

        self.wait(30)
