import math

from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX

DELAY = 0


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        a = 1
        b = -2
        c = -3

        x_min = -4.9
        x_max = 5
        y_min = -5.9
        y_max = 6

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        colore_fuoco_direttrice = GREEN
        colore_parabola = YELLOW

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).shift(4*RIGHT)
        self.add(riferimento)

        x_min_parabola = (-b - math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)
        x_max_parabola = (-b + math.sqrt(b**2 - 4 * a * (c - y_max))) / (2 * a)

        fuoco = Punto(-4, -2.3, nome="F", color=colore_fuoco_direttrice)
        direttrice = RettaParallelaAsseX(-3)
        parabola = ParabolaDaFuocoEDirettrice(fuoco, direttrice, color=colore_parabola, x_range=[-7, -1])
        direttrice = Line(start=[-7, -3, 0], end=[-1, -3, 0], color=colore_fuoco_direttrice)
        self.add(fuoco)
        self.add(MathTex("F", color=colore_fuoco_direttrice).move_to([-4, -1.7, 0], UP))
        self.add(direttrice)
        self.add(MathTex("d", color=colore_fuoco_direttrice).move_to([-6.7, -3.3, 0]))
        self.add(parabola)

        self.add(MathTex(r"\Longrightarrow", color=RED).scale(2))

        t1 = Tex(r"Dal luogo geometrico \dots").scale(2.4).shift(.5*LEFT + 2*UP)
        t2 = Tex(r"\dots all'equazione.").scale(2.4).shift(2.3*RIGHT + 2*DOWN)
        self.add(BackgroundRectangle(t1, buff=.3), t1)
        self.add(BackgroundRectangle(t2, buff=.3), t2)

        self.wait(30)
