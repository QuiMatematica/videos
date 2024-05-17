from manim import *


class Scene(MovingCameraScene):

    config.background_color = LIGHTER_GREY

    def construct(self):
        formula = MathTex(r"-\log (4{,}3 \cdot 10^{-5})", color=BLACK).scale(3.5)
        self.add(formula)

        # vero = MathTex(r"\text{valore corretto: } 4{,}37 \qquad \text{errore: } 4{,}6\%").to_edge(DOWN)
        # self.add(vero)

        a_mente = Text("SENZA CALCOLATRICE", font="Noto Sans", color=PURE_RED).scale(2)
        box = SurroundingRectangle(a_mente, corner_radius=0.2, color=PURE_RED, stroke_width=6)
        gruppo = VGroup(a_mente).move_to((0, 2.5, 0))
        self.add(gruppo)
