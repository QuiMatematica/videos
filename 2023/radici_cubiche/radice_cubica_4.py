from manim import *
from numpy import array


class Scene(ThreeDScene):

    def construct(self):
        delay = 30

        self.move_camera(zoom=1.5)

        ipotesi = MathTex(r"a \in \mathbb{R} \quad b \in \mathbb{R}")
        ipotesi[0][0].set_color(GREEN)
        ipotesi[0][3].set_color(YELLOW)
        definizione = MathTex(r"\sqrt[3]{a} = b \quad\Longleftrightarrow\quad b^3 = a")
        definizione[0][3].set_color(GREEN)
        definizione[0][5].set_color(YELLOW)
        definizione[0][8].set_color(YELLOW)
        definizione[0][11].set_color(GREEN)

        VGroup(ipotesi, definizione).arrange(DOWN, buff=.5).rotate(PI/2, axis=array([1., 0., 0.]))

        self.move_camera(phi=75 * DEGREES, theta=-65 * DEGREES, added_anims=[Write(ipotesi)])
        self.wait(delay)
        self.next_section()

        self.play(Write(definizione))

        self.wait(30)
