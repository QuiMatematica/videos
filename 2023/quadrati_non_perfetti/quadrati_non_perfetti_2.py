from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 10

        scale = 2

        self.wait(1)

        riga = MathTex(r"\sqrt{2} = 1,414\dots").scale(scale)

        self.play(Write(riga))
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(x) for x in self.mobjects])

        riga = MathTex(r"1,414^2 = 1,999396").scale(scale)

        self.play(Write(riga))
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(x) for x in self.mobjects])

        riga = VGroup(
            MathTex(r"\sqrt{8} \cdot \sqrt{2} ="),
            MathTex(r"= 2,828 \cdot 1,414 ="),
            MathTex(r"= 3,998792")).scale(scale).arrange(DOWN)

        self.play(Write(riga))
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(x) for x in self.mobjects])

        riga = VGroup(
            MathTex(r"\sqrt{8} \cdot \sqrt{2} ="),
            MathTex(r"= \sqrt{8 \cdot 2} ="),
            MathTex(r"= \sqrt{16} ="),
            MathTex(r"= 4")).scale(scale).arrange(DOWN)

        self.play(Write(riga))
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(x) for x in self.mobjects])

        riga = MathTex(r"1,414 = \dfrac{1414}{1000} = \dfrac{707}{500}").scale(scale)

        self.play(Write(riga))
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(x) for x in self.mobjects])

        self.wait(30)