from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        quadrato = MathTex(r"99225", color=YELLOW).scale(6)
        domanda = Tex("è un quadrato perfetto?").scale(2)

        VGroup(quadrato, domanda).arrange(DOWN, buff=.5)

        self.add(quadrato, domanda)

        self.wait(30)
