from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        formula = MathTex(r"-\log (4{,}3 \cdot 10^{-5}) \approx 4{,}57").scale(2.5)

        corretto = MathTex(r"-\log (4{,}3 \cdot 10^{-5}) = 4{,}37").scale(2.5)

        errore = MathTex(r"\text{errore: } 4{,}6\%").scale(2.5)

        formula.next_to(corretto, UP, buff=1)
        errore.next_to(corretto, DOWN, buff=1)

        self.play(Write(formula))
        self.cut_and_wait()

        self.play(Write(corretto))
        self.cut_and_wait()

        self.play(Write(errore))
        self.wait(30)
