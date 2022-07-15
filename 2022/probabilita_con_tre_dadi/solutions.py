from manim import *


class Scene(MovingCameraScene):

    config.background_color = WHITE
    MathTex.color = BLACK

    def construct(self):

        delay = 60

        f1 = MathTex(r"p(\text{6 su tre dadi}) = {{ \dfrac{1}{216} }}", color=BLACK).to_edge(DOWN)
        f1[0][2:12].set_color(PURPLE)

        for _f in f1:
            self.play(Write(_f))
            self.wait(delay)
            self.next_section()

        self.play(FadeOut(f1))

        f2 = MathTex(r"p(\text{6 su un dado}) = {{ \dfrac{75}{216} }}", color=BLACK).to_edge(DOWN)
        f2[0][2:11].set_color(BLUE)

        for _f in f2:
            self.play(Write(_f))
            self.wait(delay)
            self.next_section()

        self.play(FadeOut(f2))

        f3 = MathTex(r"p(\text{6 su almeno un dado}) = {{ \dfrac{91}{216} }}", color=BLACK).to_edge(DOWN)
        f3[0][2:17].set_color(RED)

        for _f in f3:
            self.play(Write(_f))
            self.wait(delay)
            self.next_section()

        self.play(FadeOut(f3))

        r0 = VGroup(
            VGroup(f1, f2).arrange(RIGHT, buff=2),
            f3).arrange(DOWN).to_edge(UP)
        self.play(Write(r0))
        surr = SurroundingRectangle(r0, buff=.3, color=PURE_RED)
        self.play(Create(surr))
        self.wait(delay)
        self.next_section()

        r1 = VGroup(
            MathTex(r"p( {{ \text{6 su almeno un dado} }} ) ="),
            MathTex(r"p( {{ \text{6 su un dado} }} \lor {{ \text{6 su due dadi} }} \lor {{ \text{6 su tre dadi} }} )")
        ).arrange(DOWN).set_color(BLACK).next_to(r0, 5*DOWN)
        r1[0][1].set_color(RED)
        r1[1][1].set_color(BLUE)
        r1[1][3].set_color(GREEN)
        r1[1][5].set_color(PURPLE)
        self.play(Write(r1))
        self.wait(delay)
        self.next_section()

        r2 = VGroup(
            MathTex(r"p( {{ \text{6 su almeno un dado} }} ) ="),
            MathTex(r"p( {{ \text{6 su un dado} }} ) + p( {{ \text{6 su due dadi} }} ) + p( {{ \text{6 su tre dadi} }} )")
        ).arrange(DOWN).set_color(BLACK).move_to(r1)
        r2[0][1].set_color(RED)
        r2[1][1].set_color(BLUE)
        r2[1][3].set_color(GREEN)
        r2[1][5].set_color(PURPLE)
        self.play(TransformMatchingTex(r1, r2))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(r2[1][3], color=PURE_RED))
        self.play(Circumscribe(r2[1][3], color=PURE_RED))
        self.wait(delay)
        self.next_section()

        r3 = MathTex(r"{{ \dfrac{91}{216} }} = {{ \dfrac{75}{216} }} + {{ p(\text{6 su due dadi}) }} + {{ \dfrac{1}{216} }}")\
            .set_color(BLACK).next_to(r2, 2*DOWN)
        r3[4][2:12].set_color(GREEN)

        r3a = f3[1].copy()
        r3b = f2[1].copy()
        r3c = f1[1].copy()
        self.play(r3a.animate.move_to(r3[0]))
        self.play(Write(r3[1]))
        self.play(r3b.animate.move_to(r3[2]))
        self.play(Write(r3[3]))
        self.play(Write(r3[4]))
        self.play(Write(r3[5]))
        self.play(r3c.animate.move_to(r3[6]))

        self.wait(delay)
        self.next_section()

        self.add(r3)
        self.remove(r3a, r3b, r3c)

        r4 = MathTex(r"{{ p(\text{6 su due dadi}) }} = {{ \dfrac{91}{216} }} - {{ \dfrac{75}{216} }} - {{ \dfrac{1}{216} }}")\
            .set_color(BLACK).move_to(r3)
        r4[0][2:12].set_color(GREEN)
        self.play(TransformMatchingTex(r3, r4))
        self.wait(delay)
        self.next_section()

        r5 = MathTex(r"{{ p(\text{6 su due dadi}) }} = \dfrac{15}{216}")\
            .set_color(BLACK).move_to(r4)
        r5[0][2:12].set_color(GREEN)
        self.play(TransformMatchingTex(r4, r5))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(r5), FadeOut(surr), FadeOut(r0), FadeOut(r2))
        self.wait(delay)
        self.next_section()

        r0 = MathTex(r"p(\text{6 su almeno due dadi}) =", color=BLACK).to_edge(UP)
        r0[0][2:18].set_color(PURE_BLUE)
        self.play(Write(r0))
        self.wait(delay)
        self.next_section()

        r1 = MathTex(r"= p(\text{6 su due dadi} \lor \text{6 su tre dadi}) =", color=BLACK).next_to(r0, DOWN)
        r1[0][3:13].set_color(GREEN)
        r1[0][14:24].set_color(PURPLE)
        self.play(Write(r1))
        self.wait(delay)
        self.next_section()

        r2 = MathTex(r"= p(\text{6 su due dadi}) + p(\text{6 su tre dadi}) =", color=BLACK).next_to(r1, DOWN)
        r2[0][3:13].set_color(GREEN)
        r2[0][17:27].set_color(PURPLE)
        self.play(Write(r2))
        self.wait(delay)
        self.next_section()

        copie = VGroup(
            MathTex(r"p(\text{6 su due dadi}) = {{ \dfrac{15}{216} }}", color=BLACK),
            f1
        ).arrange(RIGHT, buff=2).to_edge(DOWN)
        copie[0][0][2:12].set_color(GREEN)
        surr = SurroundingRectangle(copie, buff=.3, color=PURE_RED)
        self.play(Write(copie))
        self.play(Create(surr))
        self.wait(delay)
        self.next_section()

        r3 = MathTex(r"= {{ \dfrac{15}{216} }} + {{ \dfrac{1}{216} }} =", color=BLACK).next_to(r2, DOWN)
        self.play(Write(r3[0]))
        self.play(copie[0][1].copy().animate.move_to(r3[1]))
        self.play(Write(r3[2]))
        self.play(copie[1][1].copy().animate.move_to(r3[3]))
        self.play(Write(r3[4]))
        self.wait(delay)
        self.next_section()

        r4 = MathTex(r" = \dfrac{16}{216}", color=BLACK).next_to(r3, DOWN)
        self.play(Write(r4))
        self.wait(delay)
        self.next_section()

        self.wait(60)
