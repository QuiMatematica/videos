import math

from manim import *

DELAY = 1

SQRT_3 = math.sqrt(3)
SQRT_3_DIV_2 = SQRT_3 / 2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(1)

        # Alice disegna un cuore sul quaderno di matematica come segue:
        # prima disegna due circonferenze di raggio 1cm

        unit = 2.5

        start_c2 = unit * 1.5
        start_c1 = -start_c2

        center_y = unit * (SQRT_3 - 1) / 2

        tracker = ValueTracker()

        def get_radius_1():
            return Line(
                (start_c1, center_y, 0),
                (start_c1 + unit * math.cos(tracker.get_value()), center_y + unit * math.sin(tracker.get_value()), 0))

        radius_1 = get_radius_1()

        def get_radius_2():
            return Line(
                (start_c2, center_y, 0),
                (start_c2 - unit * math.cos(tracker.get_value()), center_y - unit * math.sin(tracker.get_value()), 0))

        radius_1 = get_radius_1()
        radius_2 = get_radius_2()

        self.play(Create(radius_1), Create(radius_2))

        circle_1 = Circle(radius=unit, arc_center=(start_c1, center_y, 0), z_index=2)
        circle_2 = Circle(radius=unit, arc_center=(start_c2, center_y, 0), z_index=2).rotate(PI)
        radius_1.add_updater(lambda r: r.become(get_radius_1()))
        radius_2.add_updater(lambda r: r.become(get_radius_2()))
        self.play(
            tracker.animate.set_value(TAU), Create(circle_1), Create(circle_2),
        )
        radius_1.clear_updaters()
        radius_2.clear_updaters()

        radius_1_value = Tex("1 cm").next_to(radius_1, UP, buff=.1)
        radius_2_value = Tex("1 cm").next_to(radius_2, UP, buff=.1)
        self.play(Write(radius_1_value), Write(radius_2_value))

        self.cut_and_wait()

        # e centri O1,O2,

        o1_point = Dot(circle_1.get_center())
        o1_label = MathTex(r"O_1").next_to(o1_point, UL, buff=.1)
        o2_point = Dot(circle_2.get_center())
        o2_label = MathTex(r"O_2").next_to(o2_point, UR, buff=.1)
        self.play(Create(o1_point), Write(o1_label))
        self.play(Create(o2_point), Write(o2_label))
        self.cut_and_wait()

        def get_radius_1_bis():
            return Line(o1_point.get_center(), o1_point.get_center() + unit * RIGHT)

        def get_radius_2_bis():
            return Line(o2_point.get_center(), o2_point.get_center() - unit * RIGHT)

        o1_point.add_updater(lambda p: p.move_to(circle_1.get_center()))
        o2_point.add_updater(lambda p: p.move_to(circle_2.get_center()))
        o1_label.add_updater(lambda l: l.next_to(o1_point, UL, buff=.1))
        o2_label.add_updater(lambda l: l.next_to(o2_point, UR, buff=.1))
        radius_1.add_updater(lambda l: l.become(get_radius_1_bis()))
        radius_2.add_updater(lambda l: l.become(get_radius_2_bis()))
        radius_1_value.add_updater(lambda v: v.next_to(radius_1, UP, buff=.1))
        radius_2_value.add_updater(lambda v: v.next_to(radius_2, UP, buff=.1))

        # tangenti  esternamente.
        self.play(
            circle_1.animate.shift((start_c2 - unit) * RIGHT),
            circle_2.animate.shift((start_c2 - unit) * LEFT),
        )

        o1_point.clear_updaters()
        o2_point.clear_updaters()
        o1_label.clear_updaters()
        o2_label.clear_updaters()
        radius_1.clear_updaters()
        radius_2.clear_updaters()
        radius_1_value.clear_updaters()
        radius_2_value.clear_updaters()

        self.cut_and_wait()

        # Chiamata r la tangente comune alle due circonferenze passante per il punto di contatto,

        tangent = DashedLine(
            (0, 2 * unit, 0),
            (0, -2 * unit, 0)
        )
        self.play(Create(tangent))
        self.cut_and_wait()

        # sceglie poi un punto P su r in modo che si abbia O1PO2 = 60°

        p_point = Dot((0, center_y - unit, 0), z_index=5)
        p_label = MathTex(r"P").next_to(p_point, DR, buff=.1)
        self.play(Create(p_point), Write(p_label))

        def get_p_o1_line():
            return Line(p_point.get_center(), o1_point.get_center())

        def get_p_o2_line():
            return Line(p_point.get_center(), o2_point.get_center())

        p_o1_line = get_p_o1_line()
        p_o2_line = get_p_o2_line()

        self.play(Create(p_o1_line), Create(p_o2_line))

        def get_o1_p_o2_angle():
            return Angle.from_three_points(
                o2_point.get_center(), p_point.get_center(), o1_point.get_center(), radius=0.6, color=YELLOW)

        o1_p_o2_angle = get_o1_p_o2_angle()

        def get_o1_p_o2_value():
            return Integer(
                Angle.from_three_points(o2_point.get_center(), p_point.get_center(), o1_point.get_center()
                                        ).get_value(degrees=True),
                unit=r"^{\circ}",
                color=YELLOW).next_to(o1_p_o2_angle, UP, buff=.1)

        o1_p_o2_value = get_o1_p_o2_value()

        self.play(Create(o1_p_o2_angle), Write(o1_p_o2_value))

        p_label.add_updater(lambda l: l.next_to(p_point, DR, buff=.1))
        p_o1_line.add_updater(lambda l: l.become(get_p_o1_line()))
        p_o2_line.add_updater(lambda l: l.become(get_p_o2_line()))
        o1_p_o2_angle.add_updater(lambda a: a.become(get_o1_p_o2_angle()))
        o1_p_o2_value.add_updater(lambda v: v.become(get_o1_p_o2_value()))

        self.play(p_point.animate.move_to((0, -unit * (SQRT_3 + 1)/2, 0)))

        p_label.clear_updaters()
        p_o1_line.clear_updaters()
        p_o2_line.clear_updaters()
        o1_p_o2_angle.clear_updaters()
        self.cut_and_wait()

        # e traccia le tangenti alle due circonferenze passanti per P.
        t2_coordinates = (unit * SQRT_3 * SQRT_3_DIV_2, center_y - unit * SQRT_3 / 2, 0)
        t1_coordinates = (-unit * SQRT_3 * SQRT_3_DIV_2, center_y - unit * SQRT_3 / 2, 0)
        tangent_1 = Line(p_point.get_center(), t1_coordinates, color=RED)
        tangent_2 = Line(p_point.get_center(), t2_coordinates, color=RED)
        self.play(Create(tangent_1), Create(tangent_2))
        self.cut_and_wait()

        # Quanto vale l’area del cuore ottenuto?
        polygon = Polygon(
            t1_coordinates,
            o1_point.get_center(),
            o2_point.get_center(),
            t2_coordinates,
            p_point.get_center())
        cuore = Union(circle_1, circle_2)
        diff = Difference(polygon, cuore)
        cuore = Union(cuore, diff, color=BLUE_E, fill_opacity=1, z_index=-1)
        self.play(Create(cuore))

        self.wait(30)
