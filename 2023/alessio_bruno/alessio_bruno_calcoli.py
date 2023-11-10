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
        r1 = MathTex(r"s = 600 \text{ m} = 0,600 \text{ km}")
        r2 = MathTex(r"t = \dfrac{s}{v} = \dfrac{0,600 \text{ km}}{10 \text{ km/h}} = 0,06 \text{ h}")
        r3 = MathTex(r"t = 0,06", ore, r" = 0,06 \cdot 60", minuti, "= 3,6", minuti)
        r4 = MathTex(r"t = 3", minuti, "+ 0,6", minuti, "= 3", minuti, r"+ 0,6 \cdot 60", secondi, "= 3", minuti, r"\,\,36", secondi)

        gruppo = VGroup(r1, r2, r3, r4).arrange(DOWN)

        self.play(Write(r1))
        self.cut_and_wait()
        self.play(Write(r2))
        self.cut_and_wait()
        self.play(Write(r3))
        self.cut_and_wait()
        self.play(Write(r4))

        self.wait(30)
