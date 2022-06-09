from manim import *
from laser.line import LaserLine
from laser.text import LaserTitle


class Video(MovingCameraScene):

    def construct(self):
        delay = 10

        Tex.set_default(font_size=56)
        MathTex.set_default(font_size=56)

        text = VGroup(
            VGroup(
                LaserTitle("PROBABILITÀ", color=RED).scale(1.5),
                Tex("sommare o moltiplicare?", color=RED)
            ).arrange(DOWN),
            LaserLine(4 * LEFT, 4 * RIGHT),
            MathTex(r"p(E_1 \land E_2) = p(E_1) \cdot p(E_2)"),
            VGroup(
                Tex("Eventi dipendenti:"),
                MathTex(r"p(E_1 \land E_2) = p(E_1) \cdot p(E_2 | E_1)")
            ).arrange(DOWN),
            LaserLine(4 * LEFT, 4 * RIGHT),
            MathTex(r"p(E_1 \lor E_2) = p(E_1) + p(E_2)"),
            VGroup(
                Tex("Eventi compatibili:"),
                MathTex(r"p(E_1 \lor E_2) = p(E_1) + p(E_2) - p(E_1 \land E_2)")
            ).arrange(DOWN),
            LaserLine(4 * LEFT, 4 * RIGHT)
        ).arrange(DOWN, buff=1).move_to(4.5 * UP)

        def write_and_wait(t):
            if isinstance(t, Line):
                self.play(FadeIn(t))
            else:
                self.play(Write(t))
            self.wait(delay)
            self.next_section()

        for i in range(len(text)):
            if isinstance(text[i], VGroup):
                for j in range(len(text[i])):
                    write_and_wait(text[i][j])
            else:
                write_and_wait(text[i])

        self.wait(60)


