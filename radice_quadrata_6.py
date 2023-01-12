from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        radice_4 = MathTex(r"\sqrt{4} = 2", r"\,\Longleftrightarrow\, 2^2 = 4")
        radice_4[0][2].set_color(GREEN)
        radice_4[0][4].set_color(YELLOW)
        radice_4[1][0:2].set_color(RED)
        radice_4[1][2].set_color(YELLOW)
        radice_4[1][5].set_color(GREEN)
        radice_9 = MathTex(r"\sqrt{9} = 3", r"\,\Longleftrightarrow\, 3^2 = 9")
        radice_9[0][2].set_color(GREEN)
        radice_9[0][4].set_color(YELLOW)
        radice_9[1][0:2].set_color(RED)
        radice_9[1][2].set_color(YELLOW)
        radice_9[1][5].set_color(GREEN)
        radice_1 = MathTex(r"\sqrt{1} = 1", r"\,\Longleftrightarrow\, 1^2 = 1")
        radice_1[0][2].set_color(GREEN)
        radice_1[0][4].set_color(YELLOW)
        radice_1[1][0:2].set_color(RED)
        radice_1[1][2].set_color(YELLOW)
        radice_1[1][5].set_color(GREEN)
        radice_0 = MathTex(r"\sqrt{0} = 0", r"\,\Longleftrightarrow\, 0^2 = 0")
        radice_0[0][2].set_color(GREEN)
        radice_0[0][4].set_color(YELLOW)
        radice_0[1][0:2].set_color(RED)
        radice_0[1][2].set_color(YELLOW)
        radice_0[1][5].set_color(GREEN)
        radice_2 = MathTex(r"\sqrt{2} = ", r"\sqrt{2}", r"\,\Longleftrightarrow\, (\sqrt{2})^2 = 2")
        radice_2[0][2].set_color(GREEN)
        radice_2[1].set_color(YELLOW)
        radice_2[2][0:2].set_color(RED)
        radice_2[2][3:6].set_color(YELLOW)
        radice_2[2][9].set_color(GREEN)

        VGroup(radice_4, radice_9, radice_1, radice_0, radice_2).scale(2).arrange(DOWN)

        self.play(Write(radice_4[0]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_4[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_9[0]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_9[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_1[0]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_1[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_0[0]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_0[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_2[0]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_2[1]))
        self.wait(delay)
        self.next_section()
        self.play(Write(radice_2[2]))

        self.wait(30)
