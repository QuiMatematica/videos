from manim import *

DELAY = 1

A = 2 * UP
B = 2 * DOWN


def get_dist_ac(value):
    return DashedLine(start=value * LEFT, end=A, color=GRAY)


def get_dist_ad(value):
    return DashedLine(start=value * RIGHT, end=A, color=GRAY)


def get_dist_bc(value):
    return DashedLine(start=value * LEFT, end=B, color=GRAY)


def get_dist_bd(value):
    return DashedLine(start=value * RIGHT, end=B, color=GRAY)


def get_axes(value):
    return Line(start=value * LEFT, end=value * RIGHT, color=YELLOW)


def get_point_c(value):
    return Dot(value * LEFT, color=YELLOW)


def get_point_d(value):
    return Dot(value * RIGHT, color=YELLOW)


def get_parable(value):
    return FunctionGraph(
            lambda t: value * t * t / 64,
            color=YELLOW,
        )


def get_directive(value):
    return Line(start=value * LEFT + B, end=value * RIGHT + B)


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        point_a = Dot(A)
        point_b = Dot(B)

        self.play(Create(point_a))
        self.play(Create(point_b))
        self.cut_and_wait()

        axes = get_axes(0)
        point_c = get_point_c(0)
        point_d = get_point_d(0)
        dist_ac = get_dist_ac(0)
        dist_bc = get_dist_bc(0)
        dist_ad = get_dist_ad(0)
        dist_bd = get_dist_bd(0)
        self.add(axes, point_c, point_d, dist_ac, dist_ad, dist_bc, dist_bd)
        self.cut_and_wait()

        tracker = ValueTracker(0)

        axes.add_updater(lambda old: old.become(get_axes(tracker.get_value())))
        point_c.add_updater(lambda old: old.become(get_point_c(tracker.get_value())))
        point_d.add_updater(lambda old: old.become(get_point_d(tracker.get_value())))
        dist_ac.add_updater(lambda old: old.become(get_dist_ac(tracker.get_value())))
        dist_ad.add_updater(lambda old: old.become(get_dist_ad(tracker.get_value())))
        dist_bc.add_updater(lambda old: old.become(get_dist_bc(tracker.get_value())))
        dist_bd.add_updater(lambda old: old.become(get_dist_bd(tracker.get_value())))

        self.play(tracker.animate.set_value(8), run_time=5, rate_func=linear)

        self.remove(dist_ac, dist_ad, dist_bc, dist_bd)
        self.cut_and_wait()

        axes.clear_updaters()
        point_c.clear_updaters()
        point_d.clear_updaters()
        dist_ac.clear_updaters()
        dist_ad.clear_updaters()
        dist_bc.clear_updaters()
        dist_bd.clear_updaters()

        tracker = ValueTracker(0)

        axes.add_updater(lambda old: old.become(get_parable(tracker.get_value())))
        point_b.add_updater(lambda old: old.become(get_directive(tracker.get_value())))

        self.play(tracker.animate.set_value(8), run_time=5, rate_func=linear)

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
