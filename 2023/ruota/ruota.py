from manim import *


class Ruota(ImageMobject):

    def __init__(self, **kwargs):
        super().__init__('../../img/ruota_1.png', **kwargs)
        self.actual_angle = 0

    def rotate_to(self, angle):
        actual = self.actual_angle
        delta_angle = angle - actual
        self.rotate(angle=delta_angle)
        self.actual_angle = angle

