import math

from manim import *


class Ciclista(ImageMobject):

    def __init__(self, file, pista, **kwargs):
        super().__init__(file, **kwargs)
        self.scale(.1)
        start_point = pista.get_start_point()
        self.move_to(start_point + self.get_top() + self.get_right())
        alpha = math.asin(self.width / pista.get_radius() / 2)
        self.rotate(-alpha, about_point=start_point)
        self.actual_angle = 0

    def rotate_to(self, angle):
        actual = self.actual_angle
        delta_angle = angle - actual
        self.rotate_about_origin(angle=delta_angle)
        self.actual_angle = angle

class CiclistaBlu(Ciclista):

    def __init__(self, pista, **kwargs):
        super().__init__('../../img/omini/ciclista_blu.png', pista, **kwargs)
        self.shift(.1*DOWN)

class CiclistaGiallo(Ciclista):

    def __init__(self, pista, **kwargs):
        super().__init__('../../img/omini/ciclista_giallo.png', pista, **kwargs)
        self.shift(.1*UP)
