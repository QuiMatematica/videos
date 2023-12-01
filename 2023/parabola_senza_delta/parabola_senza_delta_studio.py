from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX
from qui_matematica.qmath import EqSystem

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        equazione = MathTex(r"y= ax^2 + bx + c").to_edge(UP)

        self.play(Write(equazione))
        self.cut_and_wait()

        asse = MathTex(r"\text{asse}: x = {{ -\dfrac{b}{2a} }}")
        asse[0][:5].set_color(YELLOW)

        vertice = VGroup(
            MathTex(r"\text{vertice}: "),
            EqSystem(MathTex(r"x_V = -\dfrac{b}{2a}"), MathTex(r"y_V = -\dfrac{\Delta}{4a}"))
        ).arrange(RIGHT)
        vertice[0].set_color(YELLOW)

        fuoco = VGroup(
            MathTex(r"\text{fuoco}:", color=YELLOW),
            EqSystem(MathTex(r"x_F = {{ -\dfrac{b}{2a} }}"), MathTex(r"y_F = {{ \dfrac{1-\Delta}{4a} }}"))
        ).arrange(RIGHT)

        direttrice = VGroup(
            MathTex(r"\text{direttrice}:", color=YELLOW),
            MathTex(r"y = {{ -\dfrac{1+\Delta}{4a} }}")
        ).arrange(RIGHT)

        gruppo = VGroup(
            VGroup(vertice, asse).arrange(DOWN, aligned_edge=LEFT),
            VGroup(fuoco, direttrice).arrange(DOWN, aligned_edge=LEFT)
        ).arrange(RIGHT, buff=2.5).shift(.5 * DOWN)

        self.play(Write(gruppo))
        self.cut_and_wait()

        # FUOCO

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(fuoco[1].eqs[1]).scale(.5))
        self.cut_and_wait()

        ordinata_fuoco_1 = MathTex(r"\dfrac{1}{4a}-\dfrac{\Delta}{4a}").move_to(fuoco[1].eqs[1][1]).shift(.2 * RIGHT)
        self.play(Transform(fuoco[1].eqs[1][1], ordinata_fuoco_1))
        self.cut_and_wait()

        ordinata_fuoco_2 = MathTex(r"\dfrac{1}{4a} + y_V").move_to(fuoco[1].eqs[1][1])
        self.play(Transform(fuoco[1].eqs[1][1], ordinata_fuoco_2))
        self.wait(.5)
        ordinata_fuoco_3 = MathTex(r"y_V + \dfrac{1}{4a}").move_to(fuoco[1].eqs[1][1])
        self.play(Transform(fuoco[1].eqs[1][1], ordinata_fuoco_3))
        self.cut_and_wait()

        self.play(Restore(self.camera.frame))

        # DIRETTRICE

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(direttrice).scale(.5))
        self.wait(.5)

        direttrice_1 = MathTex(r"-\dfrac{1}{4a}-\dfrac{\Delta}{4a}").move_to(direttrice[1][1]).shift(.2 * RIGHT)
        self.play(Transform(direttrice[1][1], direttrice_1))
        self.wait(.5)

        direttrice_2 = MathTex(r"-\dfrac{1}{4a} + y_V").move_to(direttrice[1][1])
        self.play(Transform(direttrice[1][1], direttrice_2))
        self.wait(.5)
        direttrice_3 = MathTex(r"y_V - \dfrac{1}{4a}").move_to(direttrice[1][1])
        self.play(Transform(direttrice[1][1], direttrice_3))
        self.cut_and_wait()

        self.play(Restore(self.camera.frame))

        # VERTICE

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(vertice[1].eqs[1]).scale(.5))
        self.wait(.5)

        oscuramento = Rectangle(height=8, width=16, color=BLACK, fill_color=BLACK, fill_opacity=.9)
        self.play(Create(oscuramento))

        centro = vertice[1].eqs[1].get_center()

        parabola = ParabolaDaFuocoEDirettrice(
            Punto(centro[0], centro[1] + 1),
            RettaParallelaAsseX(centro[1])
        )
        self.play(Create(parabola))

        punto_vertice = Punto(centro[0], centro[1] + .5, color=YELLOW)
        self.play(Create(punto_vertice))

        label_vertice = MathTex(r"V( {{ x_V }}, {{ y_V }} )", color=YELLOW).next_to(punto_vertice, DOWN)
        self.play(Write(label_vertice))

        equazione_finale = MathTex(r"y_V = a x_V ^ 2 + b x_V + c").next_to(label_vertice, DOWN)

        temp = VGroup(
            equazione_finale[0][0],
            equazione_finale[0][2:6],
            equazione_finale[0][7:10],
            equazione_finale[0][11:],
        )
        self.play(Write(temp))

        clone1 = label_vertice[3].copy()
        self.play(FadeOut(equazione_finale[0][0]), clone1.animate.move_to(equazione_finale[0][0:2]))

        clone2 = label_vertice[1].copy()
        self.play(
            FadeOut(equazione_finale[0][4]),
            clone2.animate.move_to(equazione_finale[0][4:7].get_center() + .082 * DOWN)
        )

        clone3 = label_vertice[1].copy()
        self.play(
            FadeOut(equazione_finale[0][9]),
            clone3.animate.move_to(equazione_finale[0][9:11].get_center())
        )
        self.cut_and_wait()

        self.play(
            FadeOut(oscuramento),
            FadeOut(parabola),
            FadeOut(punto_vertice),
            FadeOut(label_vertice),
            FadeOut(temp),
            FadeOut(clone1),
            FadeOut(clone2),
            FadeOut(clone3),
        )

        ordinata_vertice = MathTex(r"y_V = a x_V ^ 2 + b x_V + c").move_to(vertice[1].eqs[1]).shift(1.1 * RIGHT)
        self.play(Transform(vertice[1].eqs[1], ordinata_vertice))
        self.cut_and_wait()

        self.play(Restore(self.camera.frame))
        self.cut_and_wait()

        self.wait(30)
