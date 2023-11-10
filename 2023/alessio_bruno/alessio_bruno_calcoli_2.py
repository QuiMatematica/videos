from manim import *

DELAY = 30


class Scene(ThreeDScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        ore = r"\text{ h}"
        minuti = r"\text{ min}"
        secondi = r"\text{ s}"
        metri = r"\text{ m}"
        r1 = MathTex(r"3,6", minuti, ": 600", metri, "= 3", minuti, ": x")
        r2 = MathTex(r"x = \dfrac{3 \text{ min} \cdot 600 \text{ m} }{3,6 \text{ min} } = 500", metri)

        gruppo = VGroup(r1, r2).arrange(DOWN)

        self.play(Write(r1))
        self.cut_and_wait()
        self.play(Write(r2))

        self.wait(30)
