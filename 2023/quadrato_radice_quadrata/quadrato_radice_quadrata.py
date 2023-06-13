from manim import *
import math


class Video(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def construct(self):
        delay = 10

        scale = 3

        self.wait(1)

        linea1 = MathTex(r"(\sqrt{5})^2 = {{ \sqrt{25} = }} 5").scale(scale)

        self.play(Write(linea1[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(linea1[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(linea1[2]))
        self.wait(delay)
        self.next_section()

        self.wait(30)