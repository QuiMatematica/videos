from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.wait(1)

        radice_4 = MathTex(r"\sqrt{4} = 2", r"\Longleftrightarrow 2^2 = 4")
        radice_9 = MathTex(r"\sqrt{9} = 3 { \Longleftrightarrow 3^2 = 9 }")
        radice_1 = MathTex(r"\sqrt{1} = 1 { \Longleftrightarrow 1^2 = 1 }")
        radice_0 = MathTex(r"\sqrt{0} = 0 { \Longleftrightarrow 0^2 = 0 }")
        radice_2 = MathTex(r"\sqrt{2} = { \sqrt{2} } \Longleftrightarrow (\sqrt{2})^2 = 2")

        VGroup(radice_4, radice_9, radice_1, radice_0, radice_2).arrange(DOWN)

        self.play(Write(radice_4[0]))
        self.play(Write(radice_4[1]))

        self.play(Write(radice_9[0]))
        self.play(Write(radice_9[1]))

        self.play(Write(radice_1[0]))
        self.play(Write(radice_1[1]))

        self.play(Write(radice_0[0]))
        self.play(Write(radice_0[1]))

        self.play(Write(radice_2[0]))
        self.play(Write(radice_2[1]))
        self.play(Write(radice_2[2]))

        self.wait(30)