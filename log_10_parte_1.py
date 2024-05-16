from manim import *

DELAY = 30
SCALE = 2.5
BUFF = .7


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        riga_1 = MathTex(r"\log (x \cdot 10^n)").scale(SCALE).to_edge(UP)
        riga_1[0][4].set_color(RED)
        riga_1[0][8].set_color(YELLOW)
        riga_2 = MathTex(r"\log x + \log 10^n").scale(SCALE).next_to(riga_1, DOWN, buff=BUFF)
        riga_2[0][3].set_color(RED)
        riga_2[0][10].set_color(YELLOW)
        riga_3 = MathTex(r"\log x + n").scale(SCALE).next_to(riga_2, DOWN, buff=BUFF)
        riga_3[0][3].set_color(RED)
        riga_3[0][5].set_color(YELLOW)
        condizione = MathTex(r"1 \le x < 10").scale(SCALE).to_edge(DOWN)
        condizione[0][2].set_color(RED)

        self.play(Write(riga_1))
        self.cut_and_wait()

        self.play(Write(condizione))
        self.cut_and_wait()

        token_1 = riga_1[0][0:3].copy()
        token_2 = riga_1[0][4].copy()
        token_3 = riga_1[0][0:3].copy()
        token_4 = riga_1[0][6:9].copy()

        # self.play(Write(riga_2))
        self.play(token_1.animate.move_to(riga_2[0][0:3]))
        self.play(token_2.animate.move_to(riga_2[0][3]))
        self.play(Write(riga_2[0][4]))
        self.play(token_3.animate.move_to(riga_2[0][5:8]))
        self.play(token_4.animate.move_to(riga_2[0][9:]))
        self.cut_and_wait()

        token_1 = riga_2[0][0:5].copy()
        token_2 = riga_2[0][10].copy()
        token_2.target = riga_3[0][5].copy()

        # self.play(Write(riga_3))
        self.play(token_1.animate.move_to(riga_3[0][0:5]))
        self.play(MoveToTarget(token_2))
        self.cut_and_wait()

        self.play(Circumscribe(riga_3[0][0:4]))
        self.play(Circumscribe(riga_3[0][0:4]))
        self.cut_and_wait()

        self.play(Circumscribe(condizione))
        self.play(Circumscribe(condizione))

        self.wait(30)
