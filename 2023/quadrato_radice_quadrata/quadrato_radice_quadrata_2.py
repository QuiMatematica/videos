from manim import *
import math


class Video(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def construct(self):
        delay = 40

        scale = 4

        self.wait(1)

        linea1 = MathTex(r"(\sqrt{5})^2 {{ = }} 5").scale(scale)

        linea0 = MathTex(r"\sqrt{5}").scale(scale).move_to(linea1[0])

        self.play(Write(linea0))
        self.wait(delay)
        self.next_section()

        self.play(Transform(linea0, linea1[0:2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(linea1[2]))

        self.wait(30)

