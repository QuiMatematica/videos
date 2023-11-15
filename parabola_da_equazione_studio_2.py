from manim import *

from qui_matematica.qmath import EqSystem

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        colore_coefficienti = BLUE

        equazione = MathTex(r"y= ax^2 + bx + c", color=PURPLE).to_edge(UP)
        equazione[0][2].set_color(colore_coefficienti)
        equazione[0][6].set_color(colore_coefficienti)
        equazione[0][9].set_color(colore_coefficienti)

        risultati = MathTex(r"f = \dfrac{1}{4a} \quad\quad "
                            r"{{ x_V = - \dfrac{b}{2a} }} "
                            r"\quad\quad y_V = - \dfrac{\Delta}{4a} ", color=GREEN).next_to(equazione, DOWN)

        self.add(equazione, risultati)

        asse = MathTex(r"\text{asse}: x = {{ -\dfrac{b}{2a} }}")
        asse[0][:5].set_color(YELLOW)

        vertice = VGroup(
            MathTex(r"\text{vertice}: "),
            EqSystem(MathTex(r"x_V = -\dfrac{b}{2a}"), MathTex(r"y_V = -\dfrac{\Delta}{4a}"))
        ).arrange(RIGHT)
        vertice[0].set_color(YELLOW)

        fuoco = VGroup(
            MathTex(r"\text{fuoco}:"),
            EqSystem(MathTex(r"x_F = {{ -\dfrac{b}{2a} }}"), MathTex("y_F = {{ \dfrac{1-\Delta}{4a} }}"))
        ).arrange(RIGHT)
        fuoco[0].set_color(YELLOW)

        direttrice = MathTex(r"\text{direttrice}: y = -\dfrac{1+\Delta}{4a}")
        direttrice[0][:11].set_color(YELLOW)

        gruppo = VGroup(
            VGroup(vertice, asse).arrange(DOWN, aligned_edge=LEFT),
            VGroup(fuoco, direttrice).arrange(DOWN, aligned_edge=LEFT)
        ).arrange(RIGHT, buff=1).shift(DOWN)

        clone1 = risultati[1].copy()
        clone1.target = vertice[1].eqs[0]
        clone2 = risultati[2].copy()
        clone2.target = vertice[1].eqs[1]
        self.play(Write(VGroup(vertice[0], vertice[1].bracket)))
        self.play(MoveToTarget(clone1))
        self.play(MoveToTarget(clone2))
        self.cut_and_wait()

        pre_asse = MathTex(r"\text{asse}: x = {{ x_V }}").move_to(asse)
        pre_asse[0][:5].set_color(YELLOW)
        self.play(Write(pre_asse))
        self.cut_and_wait()
        self.play(TransformMatchingTex(pre_asse, asse))
        self.cut_and_wait()

        pre_x_fuoco = MathTex(r"x_F = {{ x_V }}").move_to(fuoco[1].eqs[0])
        pre_y_fuoco = MathTex(r"y_F = {{ f + y_V }}").move_to(fuoco[1].eqs[1])
        self.play(Write(VGroup(fuoco[0], fuoco[1].bracket, pre_x_fuoco, pre_y_fuoco)))
        self.cut_and_wait()

        pre_x_fuoco.target = fuoco[1].eqs[0]
        self.play(MoveToTarget(pre_x_fuoco))
        mid_y_fuoco = MathTex("y_F = {{ \dfrac{1}{4a} - \dfrac{\Delta}{4a} }}").move_to(fuoco[1].eqs[1])
        pre_y_fuoco.target = mid_y_fuoco
        self.play(MoveToTarget(pre_y_fuoco))
        self.cut_and_wait()

        pre_y_fuoco.target = fuoco[1].eqs[1]
        self.play(MoveToTarget(pre_y_fuoco))
        self.cut_and_wait()

        pre_direttrice = MathTex(r"\text{direttrice}: {{ y = -f + y_V }}").move_to(direttrice)
        pre_direttrice[0][:11].set_color(YELLOW)
        self.play(Write(pre_direttrice))
        self.cut_and_wait()

        mid_direttrice = MathTex(r"\text{direttrice}: {{ y = -\dfrac{1}{4a} - \dfrac{\Delta}{4a} }}").move_to(direttrice)
        mid_direttrice[0][:11].set_color(YELLOW)
        pre_direttrice.target = mid_direttrice
        self.play(MoveToTarget(pre_direttrice))
        self.cut_and_wait()

        pre_direttrice.target = direttrice
        self.play(MoveToTarget(pre_direttrice))

        self.wait(30)
