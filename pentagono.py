from manim import *
import math


class Video(MovingCameraScene):

    def arco(self, center, radius, start_angle, angle):
        if angle < 0:
            start_angle += .1 / radius
            angle -= .2 / radius
        else:
            start_angle -= .1 / radius
            angle += .2 / radius

        arc = Arc(radius=radius, start_angle=start_angle, angle=angle, arc_center=center, color=GRAY, z_index=-1)
        self.play(Create(arc))
        return arc

    def construct(self):
        Tex.set_default(font_size=60)
        MathTex.set_default(font_size=60)

        delay = 1

        lato = 2
        raggio = .4
        alpha = PI/12

        sqrt3 = math.sqrt(3)
        sqrt3d2 = sqrt3 / 2
        sqrt5 = math.sqrt(5)
        sqrt5d2 = sqrt5 / 2

        self.wait(1)

        a = [-lato/2, -lato/2, 0]
        b = [lato/2, -lato/2, 0]

        lato1 = Line(start=a, end=b)
        self.play(Create(Dot(a)), Write(MathTex('A').next_to(a, DOWN)), run_time=.2)
        self.play(Create(lato1), run_time=.6)
        self.play(Create(Dot(b)), Write(MathTex('B').next_to(b, DOWN)), run_time=.2)

        acos5d7 = math.acos(5/7)
        arco1 = self.arco(radius=.7*lato, start_angle=acos5d7, angle=-2*acos5d7, center=a)
        arco2 = self.arco(radius=.7*lato, start_angle=PI-acos5d7, angle=2*acos5d7, center=b)

        q = [0, 0.2, 0]
        r = [0, -2.2, 0]
        linea2 = Line(start=q, end=r, color=GRAY, z_index=-1)
        self.play(Create(linea2))

        punto_medio = [0, -1, 0]
        self.play(Create(Dot(punto_medio, color=GRAY, z_index=-1)))
        self.play(arco1.animate.set_color(GRAY_E),
                  arco2.animate.set_color(GRAY_E),
                  linea2.animate.set_color(GRAY_E))

        arco3 = self.arco(radius=raggio, start_angle=PI, angle=-2*PI/3, center=b)

        m = [lato/2 - raggio, -lato/2, 0]
        arco4 = self.arco(radius=raggio, start_angle=PI/3, angle=0, center=m)

        n = [lato/2 - raggio/2, -lato/2+sqrt3d2*raggio, 0]
        arco5 = self.arco(radius=raggio, start_angle=PI/3, angle=-PI/3, center=n)

        o = [lato/2 + raggio/2, -lato/2+sqrt3d2*raggio, 0]
        arco6 = self.arco(radius=raggio, start_angle=2*PI/3, angle=PI/3, center=o)

        p = [lato/2, 1.2*lato/2, 0]
        linea1 = Line(start=p, end=b, color=GRAY, z_index=-1)
        self.play(Create(linea1))
        self.play(arco3.animate.set_color(GRAY_E),
                  arco4.animate.set_color(GRAY_E),
                  arco5.animate.set_color(GRAY_E),
                  arco6.animate.set_color(GRAY_E))

        arco7 = self.arco(radius=lato, start_angle=PI, angle=-3*PI/5, center=b)

        arco8 = self.arco(radius=lato*sqrt5d2, start_angle=PI/3, angle=-PI/3, center=punto_medio)

        linea3 = Line(start=b, end=[1.3*lato, -lato/2, 0], color=GRAY, z_index=-1)
        self.play(Create(linea3))

        arco9 = self.arco(radius=lato*(sqrt5d2 + .5), start_angle=0, angle=2*PI/5, center=a)

        arco10 = self.arco(radius=lato*(sqrt5d2 + .5), start_angle=3*PI/5, angle=0, center=b)

        # d = [0, ]

        self.play(linea2.animate.set_color(GRAY_E),
                  linea3.animate.set_color(GRAY_E),
                  arco8.animate.set_color(GRAY_E),
                  arco9.animate.set_color(GRAY_E),
                  arco10.animate.set_color(GRAY_E))

        self.wait(30)
