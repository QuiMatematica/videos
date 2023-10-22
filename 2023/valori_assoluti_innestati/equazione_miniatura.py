import math

from manim import *

DELAY = 0


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        equazione = MathTex(r"\bigl| \left| x - 2 \right| - 3  \bigr| = 4").scale(3.5)
        equazione[0][0:2].set_color(GREEN)
        equazione[0][9:11].set_color(GREEN)
        equazione[0][2].set_color(RED)
        equazione[0][6].set_color(RED)
        self.add(equazione)

        self.wait(30)