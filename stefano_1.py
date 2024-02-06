import math

from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(1)

        circonferenza = Circle(radius=2)
        self.play(Create(circonferenza))

        centro = Dot()
        self.play(Create(centro))

        diagonale = Line(start=2*LEFT, end=2*RIGHT)
        self.play(Create(diagonale))

        diagonale2 = Line(start=2*UP, end=2*DOWN)
        self.play(Create(diagonale2))

        punto1 = Dot(2*UP)
        self.play(Create(punto1))

        punto2 = Dot(2*DOWN)
        self.play(Create(punto2))

        punto3 = Dot(2*LEFT)
        self.play(Create(punto3))

        punto4 = Dot(2*RIGHT)
        self.play(Create(punto4))

        lato1 = Line(start=2*UP, end=2*LEFT)
        self.play(Create(lato1))

        lato2 = Line(start=2*UP, end=2*RIGHT)
        self.play(Create(lato2))

        lato3 = Line(start=2*LEFT, end=2*DOWN)
        self.play(Create(lato3))

        lato4 = Line(start=2*DOWN, end=2*RIGHT)
        self.play(Create(lato4))

        self.wait(30)

