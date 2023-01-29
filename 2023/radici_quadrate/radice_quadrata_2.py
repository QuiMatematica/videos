from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        quadrato = Square(fill_color=RED_E, fill_opacity=.7).scale(1.5)
        area = MathTex("A", color=GREEN).scale(1.5)
        lato = MathTex("l", color=YELLOW).scale(1.5)
        calcolo_area = MathTex(r"A = l^2").scale(3)
        calcolo_area[0][0].set_color(GREEN)
        calcolo_area[0][2].set_color(YELLOW)
        calcolo_lato = MathTex(r"l = \sqrt{A}").scale(3)
        calcolo_lato[0][0].set_color(YELLOW)
        calcolo_lato[0][4].set_color(GREEN)

        calcoli = VGroup(calcolo_area, calcolo_lato).arrange(DOWN, buff=1)
        tutto = VGroup(quadrato, calcoli).arrange(RIGHT, buff=1)
        area.move_to(quadrato)
        lato.next_to(quadrato, DOWN)

        self.play(Create(quadrato))
        self.wait(delay)
        self.next_section()

        self.play(Write(lato))
        self.wait(delay)
        self.next_section()

        self.play(Write(area))
        self.wait(delay)
        self.next_section()

        self.play(Write(calcolo_area))
        self.wait(delay)
        self.next_section()

        self.play(Write(calcolo_lato))

        self.wait(30)
