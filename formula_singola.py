from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 0

        self.wait(.5)

        self.add(Tex(r"Segnaposto temporaneo").scale(2))
        # self.add(MathTex(r"\int_{0}^{4\pi} (2 - \cos x) dx").scale(3))

        self.wait(30)

