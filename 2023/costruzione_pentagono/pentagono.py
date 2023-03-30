from manim import *
import math


class Video(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def linea(self, start, end):
        freccia = Arrow(start=start, end=end, color=YELLOW, buff=0)
        self.play(GrowArrow(freccia))
        self.remove(freccia)
        line = Line(start=start, end=end, color=GRAY, z_index=-1)
        self.add(line)
        return line

    def arco(self, center, radius, start_angle, angle):
        if angle < 0:
            start_angle += .3 / radius
            angle -= .6 / radius
        else:
            start_angle -= .3 / radius
            angle += .6 / radius

        angle_tracker = ValueTracker(0)

        def update_arc(old):
            new_arc = Arc(radius=radius, start_angle=start_angle, angle=angle_tracker.get_value(), arc_center=center,
                          color=GRAY, z_index=-1)
            old.become(new_arc)

        def update_arrow(old):
            new_arrow = Arrow(start=center, end=arc.get_end(), color=YELLOW, buff=0)
            old.become(new_arrow)

        arc = Arc(radius=radius, start_angle=start_angle, angle=0, arc_center=center, color=GRAY, z_index=-1)
        arc.add_updater(lambda j: update_arc(j))
        dot = Dot(center, color=YELLOW)
        freccia = Arrow(start=center, end=arc.get_start(), color=YELLOW, buff=0)
        freccia.add_updater(lambda j: update_arrow(j))
        self.add(arc)
        self.add(freccia)
        self.add(dot)
        self.play(angle_tracker.animate.set_value(angle))
        self.remove(freccia)
        self.remove(dot)

        self.remove(arc)
        arc = Arc(radius=radius, start_angle=start_angle, angle=angle, arc_center=center, color=GRAY, z_index=-1)
        self.add(arc)

        return arc

    def construct(self):
        Dot.set_default(radius=0.15)
        Tex.set_default(font_size=60)
        MathTex.set_default(font_size=60)

        delay = 10

        lato = 6
        raggio = lato*.2

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
        self.wait(delay)
        self.next_section()

        acos5d7 = math.acos(5/7)
        arco1 = self.arco(radius=.7*lato, start_angle=acos5d7, angle=-2*acos5d7, center=a)
        arco2 = self.arco(radius=.7*lato, start_angle=PI-acos5d7, angle=2*acos5d7, center=b)

        q = [0, 0 + lato*0.05, 0]
        r = [0, -lato - lato*0.05, 0]
        linea2 = self.linea(start=q, end=r)

        punto_medio = [0, -lato/2, 0]
        punto_medio_dot = Dot(punto_medio, color=GRAY, z_index=-1)
        punto_medio_nome = Tex('M').next_to(punto_medio, DOWN)
        self.play(Create(punto_medio_dot), Write(punto_medio_nome))
        self.play(arco1.animate.set_color(GRAY_E),
                  arco2.animate.set_color(GRAY_E),
                  linea2.animate.set_color(GRAY_E))
        self.wait(delay)
        self.next_section()

        arco3 = self.arco(radius=raggio, start_angle=PI, angle=-2*PI/3, center=b)

        m = [lato/2 - raggio, -lato/2, 0]
        arco4 = self.arco(radius=raggio, start_angle=PI/3, angle=0, center=m)

        n = [lato/2 - raggio/2, -lato/2+sqrt3d2*raggio, 0]
        arco5 = self.arco(radius=raggio, start_angle=PI/3, angle=-PI/3, center=n)

        o = [lato/2 + raggio/2, -lato/2+sqrt3d2*raggio, 0]
        arco6 = self.arco(radius=raggio, start_angle=2*PI/3, angle=PI/3, center=o)

        p = [lato/2, 1.2*lato/2, 0]
        linea1 = self.linea(start=p, end=b)
        self.play(arco3.animate.set_color(GRAY_E),
                  arco4.animate.set_color(GRAY_E),
                  arco5.animate.set_color(GRAY_E),
                  arco6.animate.set_color(GRAY_E))
        self.wait(delay)
        self.next_section()

        arco7 = self.arco(radius=lato, start_angle=PI, angle=-3*PI/5, center=b)

        p = [lato/2, lato/2, 0]
        p_dot = Dot(p, color=GRAY, z_index=1)
        p_name = Tex('P').next_to(p, UR)
        self.play(Create(p_dot), Write(p_name))
        self.wait(delay)
        self.next_section()

        arco8 = self.arco(radius=lato*sqrt5d2, start_angle=math.atan(2), angle=-math.atan(2), center=punto_medio)

        linea3 = self.linea(start=b, end=[1.3*lato, -lato/2, 0])

        q = [lato*sqrt5d2, -lato/2, 0]
        q_dot = Dot(q, color=GRAY, z_index=1)
        q_name = Tex('Q').next_to(q, DOWN)
        self.play(Create(q_dot), Write(q_name))
        self.wait(delay)
        self.next_section()

        arco9 = self.arco(radius=lato*(sqrt5d2 + .5), start_angle=0, angle=2*PI/5, center=a)
        self.wait(delay)
        self.next_section()

        arco10 = self.arco(radius=lato*(sqrt5d2 + .5), start_angle=3*PI/5, angle=0, center=b)

        d = [0, lato * math.tan(2*PI/5) / 2 - lato/2, 0]
        self.play(Create(Dot(d)), Write(MathTex('D').next_to(d, UP)))

        self.play(linea1.animate.set_color(GRAY_E),
                  linea2.animate.set_color(GRAY_E),
                  linea3.animate.set_color(GRAY_E),
                  arco8.animate.set_color(GRAY_E),
                  p_dot.animate.set_color(GRAY_E),
                  p_name.animate.set_color(GRAY_E),
                  q_dot.animate.set_color(GRAY_E),
                  q_name.animate.set_color(GRAY_E),
                  arco9.animate.set_color(GRAY_E),
                  arco10.animate.set_color(GRAY_E),
                  punto_medio_dot.animate.set_color(GRAY_E),
                  punto_medio_nome.animate.set_color(GRAY_E))
        self.wait(delay)
        self.next_section()

        arco11 = self.arco(radius=lato, start_angle=6*PI/5, angle=3*PI/5, center=d)
        c = [lato/2 + lato * math.cos(2*PI/5), lato * math.sin(2*PI/5) - lato/2, 0]
        self.play(Create(Dot(c)), Write(MathTex('C').next_to(c, RIGHT)))
        self.wait(delay)
        self.next_section()

        arco12 = self.arco(radius=lato, start_angle=3*PI/5, angle=0, center=a)

        e = [-lato/2 - lato * math.cos(2*PI/5), lato * math.sin(2*PI/5) - lato/2, 0]
        self.play(Create(Dot(e)), Write(MathTex('E').next_to(e, LEFT)))

        self.play(arco7.animate.set_color(GRAY_E),
                  arco11.animate.set_color(GRAY_E),
                  arco12.animate.set_color(GRAY_E))
        self.wait(delay)
        self.next_section()

        self.play(Create(Line(start=b, end=c)))
        self.play(Create(Line(start=c, end=d)))
        self.play(Create(Line(start=d, end=e)))
        self.play(Create(Line(start=e, end=a)))

        self.wait(30)
