from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        equazione = MathTex(r"\left| x - 2 \right| - 3x = 4").move_to(2 * UP)
        self.play(Write(equazione))
        self.cut_and_wait()

        studio = MathTex(r"\left| x - 2 \right| = "
                         r"\begin{cases} "
                         r"x - 2 & \text{ se }\quad x - 2 \ge 0 \\ "
                         r"-(x-2) & \text{ se }\quad x - 2 < 0 "
                         r"\end{cases}").move_to(0 * UP)
        self.play(Write(studio))
        self.cut_and_wait()

        sistemi = MathTex(r"\begin{cases}"
                          r"x - 2 \ge 0 \\"
                          r"x - 2 - 3x = 4"
                          r"\end{cases}"
                          r"\quad\quad\lor\quad\quad"
                          r"\begin{cases}"
                          r"x - 2 < 0 \\"
                          r"-(x - 2) - 3x = 4"
                          r"\end{cases}").move_to(2 * DOWN)
        self.play(Write(sistemi))
        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
