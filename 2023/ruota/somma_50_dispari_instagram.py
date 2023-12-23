from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)
        somma = VGroup(
            MathTex(r"1 + 3 + 5 + 7 + 9 +"),
            MathTex(r"+\, 11 + 13 + 15 + 17 + 19 \,+"),
            MathTex(r"+\, 21 + 23 + 25 + 27 + 29 \,+"),
            MathTex(r"+\, 31 + 33 + 35 + 37 + 39 \,+"),
            MathTex(r"+\, 41 + 43 + 45 + 47 + 49 \,+"),
            MathTex(r"+\, 51 + 53 + 55 + 57 + 59 \,+"),
            MathTex(r"+\, 61 + 63 + 65 + 67 + 69 \,+"),
            MathTex(r"+\, 71 + 73 + 75 + 77 + 79 \,+"),
            MathTex(r"+\, 81 + 83 + 85 + 87 + 89 \,+"),
            MathTex(r"+\, 91 + 93 + 95 + 97 + 99 ="),
            MathTex(r"= \,\,?").scale(2)
        ).scale(1.9).arrange(DOWN, buff=.6)
        somma[0].match_width(somma[1])
        self.play(Write(somma, run_time=3))
        self.wait(30)
