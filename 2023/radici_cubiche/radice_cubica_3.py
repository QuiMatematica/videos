from manim import *
from numpy import array


class Scene(ThreeDScene):

    def construct(self):
        delay = 30

        self.move_camera(zoom=1.5)

        positivo = MathTex(r"a > 0 \quad\Longrightarrow\quad \sqrt[3]{a} > 0")
        zero = MathTex(r"a = 0 \quad\Longrightarrow\quad \sqrt[3]{a} = 0")
        negativo = MathTex(r"a < 0 \quad\Longrightarrow\quad \sqrt[3]{a} < 0")

        VGroup(positivo, zero, negativo).arrange(DOWN, buff=.5).rotate(PI/2, axis=array([1., 0., 0.]))

        self.move_camera(phi=75 * DEGREES, theta=-65 * DEGREES, added_anims=[Write(positivo)])
        self.wait(delay)
        self.next_section()

        self.play(Write(zero))
        self.wait(delay)
        self.next_section()

        self.play(Write(negativo))

        self.wait(30)
