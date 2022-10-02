from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        livelli = VGroup(
            Tex("regole", color=RED),
            Tex("strategie", color=ORANGE),
            Tex("tattiche", color=YELLOW),
            Tex("logica", color=GREEN),
            Tex("linguaggio", color=BLUE)
        ).scale(2).arrange(DOWN, buff=.5)

        [self.play(Write(s)) for s in livelli]

        self.wait(delay)
        self.next_section()

        self.play(Wiggle(livelli[0], run_time=2), Wiggle(livelli[1], run_time=2))

        self.wait(delay)
        self.next_section()

        self.wait(60)
