from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        vla = ImageMobject('../../img/vla.jpeg')

        self.add(vla)

        self.wait(10)

        _f = Dot(0.77 * LEFT + 1.0 * UP, color=RED)
        # self.add(_f)

        _m = -5

        points = [
            2.7 * LEFT + 0.4 * DOWN,
            2.2 * LEFT + 0.53 * DOWN,
            1.7 * LEFT + 0.65 * DOWN,
            1.2 * LEFT + 0.7 * DOWN,
            0.7 * LEFT + 0.67 * DOWN,
            0.2 * LEFT + 0.57 * DOWN,
            0.3 * RIGHT + 0.43 * DOWN,
            0.8 * RIGHT + 0.16 * DOWN,
            1.3 * RIGHT + 0.2 * UP,
        ]

        lines = []
        for point in points:
            _x = (4 - point[1] + _m * point[0]) / _m
            line1 = Line(start=UP*4 + RIGHT*_x, end=point, color=YELLOW)
            line2 = Line(start=point, end=_f.get_center(), color=YELLOW)
            lines.append(VGroup(line1, line2))
        self.play(*[Create(line) for line in lines], run_time=3, rate_functions=linear)

        self.wait(30)

