from manim import *
from numpy import array


class Scene(ThreeDScene):

    def construct(self):
        delay = 30

        self.wait(1)
        self.move_camera(zoom=1.5)

        otto = MathTex(r"\sqrt[3]{8} = 2 \quad\Longleftrightarrow\quad 2^3 = 8")
        otto[0][3].set_color(GREEN)
        otto[0][5].set_color(YELLOW)
        otto[0][8].set_color(YELLOW)
        otto[0][11].set_color(GREEN)

        menootto = MathTex(r"\sqrt[3]{-8} = -2 \quad\Longleftrightarrow\quad (-2)^3 = -8")
        menootto[0][3:5].set_color(GREEN)
        menootto[0][6:8].set_color(YELLOW)
        menootto[0][11:13].set_color(YELLOW)
        menootto[0][16:18].set_color(GREEN)

        uno = MathTex(r"\sqrt[3]{1} = 1 \quad\Longleftrightarrow\quad 1^3 = 1")
        uno[0][3].set_color(GREEN)
        uno[0][5].set_color(YELLOW)
        uno[0][8].set_color(YELLOW)
        uno[0][11].set_color(GREEN)

        menouno = MathTex(r"\sqrt[3]{-1} = -1 \quad\Longleftrightarrow\quad (-1)^3 = -1")
        menouno[0][3:5].set_color(GREEN)
        menouno[0][6:8].set_color(YELLOW)
        menouno[0][11:13].set_color(YELLOW)
        menouno[0][16:18].set_color(GREEN)

        zero = MathTex(r"\sqrt[3]{0} = 0 \quad\Longleftrightarrow\quad 0^3 = 0")
        zero[0][3].set_color(GREEN)
        zero[0][5].set_color(YELLOW)
        zero[0][8].set_color(YELLOW)
        zero[0][11].set_color(GREEN)

        due = MathTex(r"\sqrt[3]{2} = \sqrt[3]{2} \quad\Longleftrightarrow\quad (\sqrt[3]{2})^3 = 2")
        due[0][3].set_color(GREEN)
        due[0][5:9].set_color(YELLOW)
        due[0][12:16].set_color(YELLOW)
        due[0][19].set_color(GREEN)

        VGroup(otto, menootto, uno, menouno, zero, due).arrange(DOWN).rotate(PI/2, axis=array([1., 0., 0.]))

        self.move_camera(phi=75 * DEGREES, theta=-65 * DEGREES, added_anims=[Write(otto)])
        self.wait(delay)
        self.next_section()

        self.play(Write(menootto))
        self.wait(delay)
        self.next_section()

        self.play(Write(uno))
        self.wait(delay)
        self.next_section()

        self.play(Write(menouno))
        self.wait(delay)
        self.next_section()

        self.play(Write(zero))
        self.wait(delay)
        self.next_section()

        self.play(Write(due[0][0:5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(due[0][5:]))

        self.wait(30)
