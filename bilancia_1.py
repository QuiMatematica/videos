from manim import *

from bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.wait(delay)

        bilancia_sinistra = Bilancia().scale(.5).move_to(LEFT*3.5)
        self.play(Create(bilancia_sinistra))

        bilancia_destra = Bilancia().scale(.5).move_to(RIGHT*3.5)
        self.play(Create(bilancia_destra))

        ananas = ImageMobject('img/frutta/ananas.png')
        self.add(ananas)

        self.wait(30)

