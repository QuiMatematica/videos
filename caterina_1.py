import math

from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(1)

        centro = Dot()
        self.play(Create(centro))
        cerchio = Circle(radius=2)
        self.play(Create(cerchio))
        linea1 = Line(start=2*UP, end=2*DOWN)
        self.play(Create(linea1))
        linea2 =Line(start=2*LEFT,end=2*RIGHT)
        self.play(Create(linea2))
        self.wait(30)

