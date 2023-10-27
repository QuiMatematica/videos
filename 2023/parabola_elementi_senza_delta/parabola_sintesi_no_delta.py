from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        titolo = Title("Parabola con asse parallelo all'asse $y$").set_color(RED)
        self.play(Write(titolo))

        equazione = MathTex(r"y = ax^2 + bx + c \qquad {{ (a \ne 0) }}", color=GREEN).next_to(titolo, DOWN)
        self.play(Write(equazione[0]))
        self.cut_and_wait()
        self.play(Write(equazione[1]))
        self.cut_and_wait()

        asse = MathTex(r"\text{asse}: x = -\dfrac{b}{2a}")
        asse[0][:5].set_color(YELLOW)

        vertice = MathTex(r"\text{vertice}: \begin{cases} x_V = -\dfrac{b}{2a} \\[2ex] "
                          r"y_V = ax_V^2 + bx_V + c \end{cases}")
        vertice[0][:8].set_color(YELLOW)

        fuoco = MathTex(r"\text{fuoco}: \begin{cases} x_F = -\dfrac{b}{2a} \\[2ex] "
                        r"y_F = y_V + \dfrac{1}{4a} \end{cases}")
        fuoco[0][:6].set_color(YELLOW)

        direttrice = MathTex(r"\text{direttrice}: y = y_V -\dfrac{1}{4a}")
        direttrice[0][:11].set_color(YELLOW)

        asse_x = MathTex(r"\cap x: \begin{cases} y = ax^2 + bx + c \\ y = 0 \end{cases}")
        asse_x[0][:3].set_color(YELLOW)

        asse_y = MathTex(r"\cap y: \begin{cases} y = ax^2 + bx + c \\ x = 0 \end{cases}")
        asse_y[0][:3].set_color(YELLOW)

        VGroup(
            VGroup(asse, vertice, asse_x).arrange(DOWN, aligned_edge=LEFT),
            VGroup(direttrice, fuoco, asse_y).arrange(DOWN, aligned_edge=LEFT)
        ).arrange(RIGHT, buff=1).shift(DOWN)

        self.play(Write(asse))
        self.cut_and_wait()
        self.play(Write(vertice))
        self.cut_and_wait()
        self.play(Write(fuoco))
        self.cut_and_wait()
        self.play(Write(direttrice))
        self.cut_and_wait()
        self.play(Write(asse_x))
        self.cut_and_wait()
        self.play(Write(asse_y))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
