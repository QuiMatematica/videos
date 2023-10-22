from manim import *

DELAY = 0


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        equazione = MathTex(r"\bigl| \left| x - 2 \right| - 3  \bigr| = 4").scale(3.5)
        equazione[0][0:2].set_color(GREEN)
        equazione[0][9:11].set_color(GREEN)
        equazione[0][2].set_color(RED)
        equazione[0][6].set_color(RED)
        self.play(Write(equazione[0][0:2]), Write(equazione[0][9:11]))
        self.cut_and_wait()

        self.play(Write(equazione[0][2]), Write(equazione[0][6]))
        self.cut_and_wait()

        self.play(Write(equazione[0][3:6]))
        self.cut_and_wait()

        self.play(Write(equazione[0][7:9]))
        self.cut_and_wait()

        self.play(Write(equazione[0][11:]))
        self.cut_and_wait()

        self.play(Wiggle(equazione[0][0:2]), Wiggle(equazione[0][9:11]))
        self.cut_and_wait()

        self.play(Wiggle(equazione[0][2]), Wiggle(equazione[0][6]))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
