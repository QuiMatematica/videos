from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        colore_coefficienti = BLUE

        equazione = MathTex(r"y= ax^2 + bx + c", color=PURPLE).to_edge(UP)
        equazione[0][2].set_color(colore_coefficienti)
        equazione[0][6].set_color(colore_coefficienti)
        equazione[0][9].set_color(colore_coefficienti)

        equazione_2 = MathTex(r"y= \dfrac{1}{4f}x^2 - \dfrac{2x_V}{4f} x + \dfrac{x_V^2 + 4 f y_V}{4f}", color=PURPLE).\
            next_to(equazione, DOWN)
        equazione_2[0][2:6].set_color(colore_coefficienti)
        equazione_2[0][8:15].set_color(colore_coefficienti)
        equazione_2[0][17:].set_color(colore_coefficienti)

        risultati = MathTex(r"f = \dfrac{1}{4a} \quad\quad "
                            r"{{ x_V = - \dfrac{b}{2a} }} "
                            r"\quad\quad y_V = - \dfrac{\Delta}{4a} ", color=GREEN).to_edge(DOWN)
        # self.add(risultati)

        self.play(Write(equazione))
        self.cut_and_wait()

        self.play(Write(equazione_2))
        self.cut_and_wait()

        a1 = MathTex(r"\dfrac{1}{4f} {{ = }} a")
        clone1 = equazione_2[0][2:6].copy()
        clone1.target = a1[0]
        clone2 = equazione[0][2].copy()
        clone2.target = a1[2]

        self.play(MoveToTarget(clone1))
        self.play(Write(a1[1]))
        self.play(MoveToTarget(clone2))
        self.add(a1)
        self.remove(clone1, clone2)
        self.cut_and_wait()

        a_diverso_0 = MathTex(r"a \ne 0").to_edge(UR)
        clone1 = a1.copy()
        clone1.target = a_diverso_0
        self.play(MoveToTarget(clone1))
        self.add(a_diverso_0)
        self.remove(clone1)
        self.cut_and_wait()

        a1.target = MathTex(r"4f {{ = }} \dfrac{1}{a}")
        self.play(MoveToTarget(a1))
        self.cut_and_wait()

        a1.target = MathTex(r"f {{ = }} \dfrac{1}{4a}")
        self.play(MoveToTarget(a1))
        self.cut_and_wait()

        a1.target = risultati[0]
        self.play(MoveToTarget(a1))
        self.add(risultati[0])
        self.remove(a1)

        #==================================

        b1 = MathTex(r"- \dfrac{2x_V}{4f} {{ = }} b")
        clone1 = equazione_2[0][8:15].copy()
        clone1.target = b1[0]
        clone2 = equazione[0][6].copy()
        clone2.target = b1[2]

        self.play(MoveToTarget(clone1))
        self.play(Write(b1[1]))
        self.play(MoveToTarget(clone2))
        self.add(b1)
        self.remove(clone1, clone2)
        self.cut_and_wait()

        b1.target = MathTex(r"-2x_V \cdot \dfrac{1}{4f} {{ = }} b")
        self.play(MoveToTarget(b1))
        self.cut_and_wait()

        b1.target = MathTex(r"-2x_V \cdot a {{ = }} b")
        self.play(MoveToTarget(b1))
        self.cut_and_wait()

        b1.target = MathTex(r"x_V {{ = }} - \dfrac{b}{2a}")
        self.play(MoveToTarget(b1))
        self.cut_and_wait()

        b1.target = risultati[1]
        self.play(MoveToTarget(b1))
        self.add(risultati[1])
        self.remove(b1)

        #==================================

        c1 = MathTex(r"\dfrac{x_V^2 + 4 f y_V}{4f} {{ = }} c")
        clone1 = equazione_2[0][17:].copy()
        clone1.target = c1[0]
        clone2 = equazione[0][9].copy()
        clone2.target = c1[2]

        self.play(MoveToTarget(clone1))
        self.play(Write(c1[1]))
        self.play(MoveToTarget(clone2))
        self.add(c1)
        self.remove(clone1, clone2)
        self.cut_and_wait()

        c1.target = MathTex(r"\dfrac{x_V^2}{4f} + \dfrac{4 f y_V}{4f} {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"\dfrac{x_V^2}{4f} + y_V {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"x_V^2 \cdot \dfrac{1}{4f} + y_V {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"\biggr(-\dfrac{b}{2a}\biggl)^2 \cdot a + y_V {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"\dfrac{b^2}{4a^2} \cdot a + y_V {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"\dfrac{b^2}{4a} + y_V {{ = }} c")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"y_V {{ = }} c - \dfrac{b^2}{4a}")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"y_V {{ = }} \dfrac{4ac - b^2}{4a}")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"y_V {{ = }} - \dfrac{b^2 - 4ac}{4a}")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = MathTex(r"y_V {{ = }} - \dfrac{\Delta}{4a}")
        self.play(MoveToTarget(c1))
        self.cut_and_wait()

        c1.target = risultati[2]
        self.play(MoveToTarget(c1))
        self.add(risultati[2])
        self.remove(c1)

        #==================================

        self.play(FadeOut(equazione_2), risultati.animate.next_to(equazione, DOWN))
        self.cut_and_wait()

        self.wait(30)
