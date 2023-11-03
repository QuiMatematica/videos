from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        definizione1 = Tex(r"parabola: {{ luogo geometrico dei punti equidistanti }}", z_index=2).shift(3*DOWN)
        definizione2 = Tex(r"dal fuoco {{ e dalla direttrice }}", z_index=2).shift(3.5*DOWN)
        definizione = VGroup(definizione1, definizione2)
        box_definizione = BackgroundRectangle(definizione, buff=.5)
        self.add(box_definizione)
        self.play(Write(definizione1[0]))
        self.cut_and_wait()
        self.play(Write(definizione1[1]))
        self.cut_and_wait()

        colore_fuoco_direttrice = GREEN
        colore_parabola = YELLOW

        fuoco = Punto(0, 1, nome="F", color=colore_fuoco_direttrice)
        label_fuoco = fuoco.get_label()
        direttrice = RettaParallelaAsseX(-0.5, nome="d", color=colore_fuoco_direttrice)
        label_direttrice = direttrice.get_label()
        parabola = ParabolaDaFuocoEDirettrice(fuoco, direttrice, color=colore_parabola)

        self.play(Create(fuoco), Write(label_fuoco))
        self.play(Write(definizione2[0]))
        self.cut_and_wait()

        self.play(Create(direttrice), Write(label_direttrice))
        self.play(Write(definizione2[1]))
        self.cut_and_wait()

        self.play(Create(parabola))
        self.cut_and_wait()

        x_min = -6.9
        x_max = 17
        y_min = -3.9
        y_max = 9

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1)

        self.play(Create(riferimento))
        self.cut_and_wait()

        self.play(FadeOut(parabola), FadeOut(fuoco), FadeOut(label_fuoco),
                  FadeOut(direttrice), FadeOut(label_direttrice),
                  FadeOut(definizione), FadeOut(box_definizione))
        self.cut_and_wait()

        luogo_equazione = Tex(r"luogo geometrico $\Longleftrightarrow$ equazione in $x$ e $y$")
        box_luogo_equazione = BackgroundRectangle(luogo_equazione, buff=.5)
        self.play(Create(box_luogo_equazione), Write(luogo_equazione))
        self.cut_and_wait()

        self.play(FadeOut(luogo_equazione), FadeOut(box_luogo_equazione))

        self.play(FadeIn(parabola), FadeIn(fuoco), FadeIn(label_fuoco),
                  FadeIn(direttrice), FadeIn(label_direttrice))
        self.cut_and_wait()

        quale_equazione = Tex(r"equazione della parabola?").scale(2).shift(3*DOWN)
        box_quale_equazione = BackgroundRectangle(quale_equazione, buff=.5)
        self.play(Create(box_quale_equazione), Write(quale_equazione))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
