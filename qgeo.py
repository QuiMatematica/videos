from abc import ABC

from manim import *


class AngleWithArc(Arc, ABC):

    def __init__(
            self,
            radius=.3,
            start_angle=0,
            angle=PI,
            center=ORIGIN,
            arc_color=RED,
            line_color=BLUE,
            **kwargs
    ):
        super().__init__(radius=radius,
                         start_angle=start_angle,
                         angle=angle,
                         arc_center=center,
                         color=arc_color,
                         z_index=-1)
        extra_line = 1.3

        line1 = Line(start=center, end=(self.get_start() - center) * extra_line + center, color=BLUE)
        line2 = Line(start=center, end=(self.get_end() - center) * extra_line + center, color=BLUE)

        self.add(line1)
        self.add(line2)
