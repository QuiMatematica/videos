from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        formula = MathTex(r"-\log (4{,}3 \cdot 10^{-5}) \approx 4{,}57").scale(2.5)
        self.add(formula)

        vero = MathTex(r"\text{valore corretto: } 4{,}37 \qquad \text{errore: } 4{,}6\%").to_edge(DOWN)
        self.add(vero)

        a_mente = Tex("SENZA CALCOLATRICE", color=RED).scale(2)
        box = SurroundingRectangle(a_mente, corner_radius=0.2, color=RED)
        gruppo = VGroup(a_mente, box).move_to((0, 2, 0))
        self.add(gruppo)
