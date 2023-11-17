import math

from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        colore_coefficienti = BLUE

        equazione = MathTex(r"y= ax^2 + bx + c", color=PURPLE).shift(4*RIGHT)
        equazione[0][2].set_color(colore_coefficienti)
        equazione[0][6].set_color(colore_coefficienti)
        equazione[0][9].set_color(colore_coefficienti)

        coefficienti = MathTex(r"a \quad b \quad c", color=colore_coefficienti)

        valori = MathTex(r"x_V \quad y_V \quad f", color=GREEN)

        oggetti = Tex(r"vertice \,\, fuoco \,\, asse \,\, direttrice", color=YELLOW)
        # oggetti = MathTex(r"V(x_v, y_V) \quad F(x_V, y_V + f) \quad a: x = x_V \quad d: y = y_V - f", color=GREEN)

        VGroup(equazione, coefficienti, valori, oggetti).scale(2).arrange(DOWN, buff=1)

        self.play(Write(equazione))
        self.cut_and_wait()

        a_copy = equazione[0][2].copy()
        b_copy = equazione[0][6].copy()
        c_copy = equazione[0][9].copy()
        a_copy.target = coefficienti[0][0]
        b_copy.target = coefficienti[0][1]
        c_copy.target = coefficienti[0][2]
        self.play(MoveToTarget(a_copy), MoveToTarget(b_copy), MoveToTarget(c_copy))
        self.cut_and_wait()

        clone = coefficienti.copy()
        clone.target = valori
        self.play(MoveToTarget(clone))
        self.cut_and_wait()

        clone = valori.copy()
        clone.target = oggetti
        self.play((MoveToTarget(clone)))

        self.wait(30)
