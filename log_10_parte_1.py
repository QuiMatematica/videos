from manim import *

DELAY = 1
SCALE = 2.5
BUFF = .7


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        riga_1 = MathTex(r"\log (x \cdot 10^n)").scale(SCALE).to_edge(UP)
        riga_2 = MathTex(r"\log x + \log 10^n").scale(SCALE).next_to(riga_1, DOWN, buff=BUFF)
        riga_3 = MathTex(r"\log x + n").scale(SCALE).next_to(riga_2, DOWN, buff=BUFF)
        condizione = MathTex(r"1 \le x < 10").scale(SCALE).to_edge(DOWN)

        self.play(Write(riga_1))
        self.cut_and_wait()

        self.play(Write(condizione))
        self.cut_and_wait()

        self.play(Write(riga_2))
        self.cut_and_wait()

        self.play(Write(riga_3))
        self.cut_and_wait()

        self.play(Circumscribe(riga_3[0][0:4]))
        self.play(Circumscribe(riga_3[0][0:4]))
        self.cut_and_wait()

        self.play(Circumscribe(condizione))
        self.play(Circumscribe(condizione))
        self.wait(30
                  )