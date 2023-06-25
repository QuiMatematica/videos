from abc import ABC

from manim import *


def place_on(plate, obj, quantity, h_shift):
    x_a = plate.get_left()[0]
    x_b = plate.get_right()[0]
    width = x_b - x_a
    width_per_obj = width / quantity
    first_center = x_a + width_per_obj / 2
    objs = []
    for _i in range(quantity):
        cloned = obj.copy()
        cloned.set_y((plate.get_top() + obj.get_center() - obj.get_bottom())[1])
        cloned.set_x(first_center + h_shift + _i * width_per_obj)
        objs.append(cloned)
    return objs


class Bilancia(VGroup, ABC):

    def __init__(
            self,
            color=WHITE
    ):
        super().__init__()

        base_triangolo_supporto = 2
        altezza_triangolo_supporto = 2.5
        vertici_triangolo_supporto = [
            [0, 0, 0],
            [-base_triangolo_supporto/2, -altezza_triangolo_supporto, 0],
            [base_triangolo_supporto/2, -altezza_triangolo_supporto, 0]
        ]
        triangolo_supporto = Polygon(*vertici_triangolo_supporto, color=color, fill_opacity=1, fill_color=color)
        self.add(triangolo_supporto)

        raggio_dot = .25
        dot = Dot(radius=raggio_dot)
        self.add(dot)

        lunghezza_barra = 7
        altezza_barra = .1
        barra = Rectangle(width=lunghezza_barra, height=altezza_barra, color=color, fill_color=color, fill_opacity=1)
        self.add(barra)

        self.add(Dot(radius=raggio_dot).move_to(LEFT*lunghezza_barra/2))
        self.add(Dot(radius=raggio_dot).move_to(RIGHT*lunghezza_barra/2))

        rettangolo = Rectangle(width=lunghezza_barra*2, height=1.5)
        raggio_piatto = 7
        piatto_a = Circle(radius=raggio_piatto).move_to(LEFT*lunghezza_barra/2 + UP*(raggio_piatto + raggio_dot))
        self.left = Intersection(rettangolo, piatto_a, color=color, fill_color=color, fill_opacity=1)
        self.add(self.left)

        piatto_b = Circle(radius=raggio_piatto).move_to(RIGHT*lunghezza_barra/2 + UP*(raggio_piatto + raggio_dot))
        self.right = Intersection(rettangolo, piatto_b, color=color, fill_color=color, fill_opacity=1)
        self.add(self.right)

    def place_on_left(self, obj, quantity=1, h_shift=0):
        return place_on(self.left, obj, quantity, h_shift)

    def place_on_right(self, obj, quantity=1, h_shift=0):
        return place_on(self.right, obj, quantity, h_shift)
