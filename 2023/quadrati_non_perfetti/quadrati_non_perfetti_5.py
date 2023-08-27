from manim import *


DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        delay = DELAY

        scale = 1

        self.wait(1)

        riga_1 = MathTex(r"\sqrt{600} = \,\,?").scale(scale)
        riga_2 = MathTex(r"600 &= 2^3 \cdot 3^1 \cdot 5^2 = \\"
                         r"{{ &= 2^{2+1} \cdot 3^1 \cdot 5^2 = }} \\"
                         r"&= 2^2 \cdot 2^1 \cdot 3^1 \cdot 5^2").scale(scale)
        riga_3 = MathTex(r"\sqrt{600} &= \sqrt{2^2 \cdot 2 \cdot 3 \cdot 5^2} = \\"
                         r"{{ &= \sqrt{2^2 \cdot 5^2} \cdot \sqrt{2 \cdot 3} = }} \\"
                         r"&= 2 \cdot 5 \cdot \sqrt{2 \cdot 3} = \\"
                         r"{{ &= 10\sqrt{6} }}").scale(scale)
        riga_4 = MathTex(r"(10\sqrt{6})^2 = {{ 10^2 \cdot (\sqrt{6})^2 = }} 100 \cdot 6 = {{ 600 }}").scale(scale)
        verticale = Line().rotate(PI/2)
        linea = Line()

        VGroup(
            riga_1,
            VGroup(riga_2, verticale, riga_3).arrange(RIGHT, buff=1),
            linea,
            riga_4).arrange(DOWN, buff=.5)

        self.play(Write(riga_1))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_2[0]))
        self.wait(delay)
        self.next_section()

        self.teorema(MathTex(r"d &= p + 1 \\ 17 &= 16 + 1"))

        self.play(Write(riga_2[1]))
        self.wait(delay)
        self.next_section()

        self.teorema(MathTex(r"a^m \cdot a^n = a^{m + n}"))

        self.play(Write(riga_2[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_3[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_3[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_3[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_3[3]))
        self.wait(delay)
        self.next_section()

        self.play(Create(linea))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_4[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_4[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_4[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(riga_4[3]))

        self.wait(30)

    def teorema(self, teorema):
        cornice = SurroundingRectangle(teorema, fill_opacity=1, fill_color=BLACK, buff=.5)

        self.play(Create(cornice), Write(teorema))

        self.wait(DELAY)
        self.next_section()

        self.play(FadeOut(teorema), FadeOut(cornice))
        self.wait(DELAY)
        self.next_section()
