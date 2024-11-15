import math

from manim import *

DELAY = 30
X_RADIUS = config["frame_x_radius"]
Y_RADIUS = config["frame_y_radius"]
SCALE = 1
BH_COLOR = YELLOW
ANGLE_BORDER = .4
INC_ANGLE_BORDER = ANGLE_BORDER / math.sqrt(2)


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):

        ipotesi_tesi_1 = MathTex(
            r"ABC \text{ isoscele} \Longrightarrow BH \cong \dfrac{1}{2} AC"
        )
        ipotesi_tesi_2 = MathTex(
            r"ABC \text{ isoscele} \Longleftarrow BH \cong \dfrac{1}{2} AC"
        )

        VGroup(ipotesi_tesi_1, ipotesi_tesi_2).arrange(DOWN)
        self.play(Write(ipotesi_tesi_1))
        self.play(Write(ipotesi_tesi_2))

        self.wait(30)
