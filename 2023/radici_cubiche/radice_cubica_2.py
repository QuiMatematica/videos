from manim import *
from numpy import array


class Scene(ThreeDScene):

    def construct(self):
        delay = 30

        self.wait(1)
        self.move_camera(zoom=1.5)

        elevamento = MathTex(r"(-3)^3 = -27")
        radice = MathTex(r"\sqrt[3]{-27} = -3")

        VGroup(elevamento, radice).arrange(DOWN, buff=.5).rotate(PI/2, axis=array([1., 0., 0.]))

        self.move_camera(phi=75 * DEGREES, theta=-65 * DEGREES, added_anims=[Write(elevamento)])
        self.wait(delay)
        self.next_section()

        self.play(Write(radice))

        self.wait(30)
