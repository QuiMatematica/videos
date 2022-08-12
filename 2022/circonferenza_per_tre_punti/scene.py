from qmath import sqrt

from manim import *


def length(a: Dot, b: Dot):
    diff = a.get_center() - b.get_center()
    return sqrt(diff[0] ** 2 + diff[1] ** 2)


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)
        scale = .7
        a = Dot([-3 * scale, -2 * scale, 0])
        b = Dot([-2 * scale, 3 * scale, 0])
        c = Dot([4 * scale, 4 * scale, 0])
        self.play(Create(a), Write(MathTex("A").next_to(a, DL)))
        self.play(Create(b), Write(MathTex("B").next_to(b, UL)))
        self.play(Create(c), Write(MathTex("C").next_to(c, UR)))
        self.wait(1)
        c_color = GREEN
        ab = Line(a, b, color=c_color)
        bc = Line(b, c, color=c_color)
        self.play(Create(ab))
        self.play(Create(bc))

        ab_mid = midpoint(a.get_center(), b.get_center())
        ab_bisector = perpendicular_bisector([a.get_center(), b.get_center()])

        p = Dot(ab_mid + 1.2 * normalize(ab_bisector[0] - ab_mid))
        q = Dot(ab_mid + 1.2 * normalize(ab_bisector[1] - ab_mid))

        a_arc = Arc(arc_center=a.get_center(),
                    radius=length(a, q),
                    start_angle=Line(a, q).get_angle() - PI / 12,
                    angle=Line(a, p).get_angle() - Line(a, q).get_angle() + PI / 6,
                    color=c_color)
        self.play(Create(a_arc))
        b_arc = Arc(arc_center=b.get_center(),
                    radius=length(b, p),
                    start_angle=Line(b, p).get_angle() - PI / 12,
                    angle=Line(b, q).get_angle() - Line(b, p).get_angle() + PI / 6,
                    color=c_color)
        self.play(Create(b_arc))

        bc_mid = midpoint(b.get_center(), c.get_center())
        bc_bisector = perpendicular_bisector([b.get_center(), c.get_center()])

        r = Dot(bc_mid + 1.3 * normalize(bc_bisector[0] - bc_mid))
        s = Dot(bc_mid + 1.3 * normalize(bc_bisector[1] - bc_mid))

        bb_arc = Arc(arc_center=b.get_center(),
                     radius=length(b, s),
                     start_angle=Line(b, s).get_angle() - PI / 12,
                     angle=Line(b, r).get_angle() - Line(b, s).get_angle() + PI / 6,
                     color=c_color)
        self.play(Create(bb_arc))
        c_arc = Arc(arc_center=c.get_center(),
                    radius=length(c, r),
                    start_angle=Line(c, r).get_angle() - PI / 12,
                    angle=2 * PI + Line(c, s).get_angle() - Line(c, r).get_angle() + PI / 6,
                    color=c_color)
        self.play(Create(c_arc))

        self.play(Create(Line(ab_bisector[0], ab_bisector[1], color=c_color)))
        self.play(Create(Line(bc_bisector[0], bc_bisector[1], color=c_color)))

        z = Dot(line_intersection(ab_bisector, bc_bisector), color=RED)
        self.play(Create(z), Write(MathTex("Z", color=RED).next_to(z, DR)))

        self.play(Create(Circle(radius=length(z, a)).move_to(z)))

        self.wait(10)
