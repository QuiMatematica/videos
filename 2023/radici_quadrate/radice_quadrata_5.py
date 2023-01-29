from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        condizioni = MathTex(r"a \ge 0 \quad b \ge 0").scale(3)
        condizioni[0][0:3].set_color(GREEN)
        condizioni[0][3:].set_color(YELLOW)

        definizione = MathTex(r"\sqrt{a} = b \Longleftrightarrow b^2 = a").scale(3)
        definizione[0][2].set_color(GREEN)
        definizione[0][4].set_color(YELLOW)
        definizione[0][5:7].set_color(RED)
        definizione[0][7].set_color(YELLOW)
        definizione[0][10].set_color(GREEN)

        gruppo = VGroup(condizioni, definizione).arrange(DOWN, buff=1)

        self.play(Write(definizione[0][0:3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(condizioni[0][0:3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(definizione[0][3:5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(condizioni[0][3:]))
        self.wait(delay)
        self.next_section()

        self.play(Write(definizione[0][5:]))

        self.wait(30)
