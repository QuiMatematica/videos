from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        formula = MathTex(r"\text{pH} {{ = -\log [\text{H}^+] }}").scale(2.5)
        self.play(Write(formula[0]))
        self.cut_and_wait()
        self.play(Write(formula[1]))
        self.cut_and_wait()

        a_mente = Tex("SENZA CALCOLATRICE", color=RED).scale(2)
        box = SurroundingRectangle(a_mente, corner_radius=0.2, color=RED)
        gruppo = VGroup(a_mente, box).move_to((0, 2, 0))
        self.play(GrowFromCenter(gruppo))

        self.wait(30)
