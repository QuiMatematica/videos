from manim import *

from util import TableHelper


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        table = MathTable(
            [[180, 2],
             [90, 2],
             [45, 3],
             [15, 3],
             [5, 5],
             [1, 0]], v_buff=0.2, h_buff=0.6
        )
        table.get_entries().scale(1.6)

        soluzione = MathTex(r"180 = 2^2 \cdot 3^2 \cdot 5").scale(1.6)

        VGroup(table, soluzione).arrange(DOWN, buff=.5).move_to(ORIGIN)

        helper = TableHelper(table)

        self.play(Write(table.get_entries((1, 1))))
        self.play(Create(helper.get_vertical_line(1, start=0, end=6)))

        for _i in range(5):
            self.play(Write(table.get_entries((_i + 1, 2))))
            self.play(Write(table.get_entries((_i + 2, 1))))
            self.wait(1)

        self.play(Write(soluzione))

        self.wait(30)
