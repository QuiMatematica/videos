from math import sqrt

from manim import *


def length(a: Dot, b: Dot):
    diff = a.get_center() - b.get_center()
    return sqrt(diff[0] ** 2 + diff[1] ** 2)


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        self.play(Create(Axes(x_range=(-6, 6, 1), y_range=(-6, 6, 1), x_length=6, y_length=6).move_to(4*LEFT)))

        scale = .4
        t_scale = .8

        a = Dot([-3 * scale - 5, -2 * scale - .5, 0])
        b = Dot([-2 * scale - 5, 3 * scale - .5, 0])
        c = Dot([4 * scale - 5, 4 * scale - .5, 0])
        self.play(Create(a), Write(MathTex("A").scale(t_scale).next_to(a, DL * .5)))
        self.play(Create(b), Write(MathTex("B").scale(t_scale).next_to(b, UL * .5)))
        self.play(Create(c), Write(MathTex("C").scale(t_scale).next_to(c, UR * .5)))
        self.wait(1)

        c_color = GREEN
        ab = Line(a, b, color=c_color)
        bc = Line(b, c, color=c_color)
        self.play(Create(ab))
        self.play(Create(bc))

        r1 = VGroup(
            MathTex(r"m_{AB} = \dfrac{y_B - y_A}{x_B - x_A}"),
            MathTex(r"m_{BC} = \dfrac{y_C - y_B}{x_C - x_B}")
        ).scale(t_scale).arrange(RIGHT, buff=1).to_edge(UP).shift(3*RIGHT)
        self.play(Write(r1))

        m = Dot(midpoint(a.get_center(), b.get_center()), color=c_color)
        n = Dot(midpoint(b.get_center(), c.get_center()), color=c_color)
        self.play(Create(m), Write(MathTex("M", color=c_color).scale(t_scale).next_to(m, LEFT*.5)))
        self.play(Create(n), Write(MathTex("N", color=c_color).scale(t_scale).next_to(n, UP*.5)))

        r2 = VGroup(
            MathTex(r"M(\dfrac{x_A + x_B}{2}; \dfrac{y_A + y_B}{2})"),
            MathTex(r"N(\dots; \dots)")
        ).scale(t_scale).arrange(RIGHT, buff=1).next_to(r1, DOWN)
        self.play(Write(r2))

        ab_bisector = perpendicular_bisector([a.get_center(), b.get_center()])
        self.play(Create(Line(ab_bisector[0], ab_bisector[1], color=c_color)))

        r3 = MathTex(r"asse_{AB}:\quad y - y_M = -\dfrac{1}{m_{AB}}(x - x_M)").scale(t_scale).next_to(r2, DOWN)
        self.play(Write(r3))

        bc_bisector = perpendicular_bisector([b.get_center(), c.get_center()])
        self.play(Create(Line(bc_bisector[0], bc_bisector[1], color=c_color)))

        r4 = MathTex(r"asse_{BC}:\quad y - y_N = -\dfrac{1}{m_{BC}}(x - x_N)").scale(t_scale).next_to(r3, DOWN)
        self.play(Write(r4))

        z = Dot(line_intersection(ab_bisector, bc_bisector), color=RED)
        self.play(Create(z), Write(MathTex("Z", color=RED).scale(t_scale).next_to(z, DL * .5)))

        r5 = VGroup(
            MathTex(r"Z:"),
            EqSystem(MathTex(r"asse_{AB}"), MathTex(r"asse_{BC}"))
        ).scale(t_scale).arrange(RIGHT, buff=1).next_to(r4, DOWN)
        self.play(Write(r5))

        self.play(Create(Circle(radius=length(z, a)).move_to(z)))

        r6 = MathTex(r"r = \sqrt{(x_Z - x_A)^2 + (y_Z - y_A)^2}").scale(t_scale).next_to(r5, DOWN)
        self.play(Write(r6))


class EqSystem(VMobject):

    def __init__(self, *equation_texs, **kwargs):
        super().__init__(**kwargs)
        eqs = VGroup()
        for tex in equation_texs:
            eqs.add(tex)
        eqs.arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex("\{")
        bracket.scale(2)
        bracket.stretch_to_fit_height(eqs.height + 2 * MED_SMALL_BUFF)
        bracket.next_to(eqs, LEFT, MED_SMALL_BUFF)
        self.add(bracket, eqs)
        self.center()