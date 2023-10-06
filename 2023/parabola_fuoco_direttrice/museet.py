from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        vla = ImageMobject('../../img/museet.jpeg')

        self.add(vla)

        self.cut_and_wait()

        _f1 = Dot(4.37 * LEFT + 3.1 * DOWN, color=RED)
        # self.add(_f1)

        _f2 = Dot(4.16 * RIGHT + 3.2 * DOWN, color=RED)
        # self.add(_f2)

        points = [
            4.6 * LEFT + 2.5 * DOWN,
            4.8 * LEFT + 2.75 * DOWN,
            4.9 * LEFT + 3.1 * DOWN,
            4.82 * LEFT + 3.45 * DOWN,
            4.7 * LEFT + 3.7 * DOWN
        ]

        lines = []
        for point in points:
            line1 = Line(start=_f1.get_center(), end=point, color=YELLOW)
            delta = point - _f1.get_center()
            delta_x = delta[0] - 0.03
            delta_y = delta[1] + 0.05
            secondo_punto = _f2.get_center() - delta_x * RIGHT + delta_y * UP
            line2 = Line(start=point, end=secondo_punto, color=RED)
            line3 = Line(start=secondo_punto, end=_f2.get_center(), color=GREEN)
            lines.append(VGroup(line1, line2, line3))

        self.play(*[Create(line[0]) for line in lines])
        self.cut_and_wait()
        self.play(*[Create(line[1]) for line in lines])
        self.cut_and_wait()
        self.play(*[Create(line[2]) for line in lines])

        self.wait(30)
