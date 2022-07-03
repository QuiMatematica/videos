from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        urna_color = GREEN
        urna = Rectangle(color=urna_color, fill_color=urna_color, fill_opacity=.05, z_index=1).move_to(DOWN)
        self.play(DrawBorderThenFill(urna))

        ball_radius = .4
        white1 = Circle(radius=ball_radius, color=GRAY_A, fill_color=GRAY_A, fill_opacity=1).set_sheen(-1, DR)\
            .move_to(ball_radius * 3.3 * LEFT + (1.95 - ball_radius) * DOWN)
        white2 = white1.copy()\
            .move_to(ball_radius * 1.1 * LEFT + (1.95 - ball_radius) * DOWN)
        white3 = white1.copy()\
            .move_to(ball_radius * 1.1 * RIGHT + (1.95 - ball_radius) * DOWN)
        white4 = white1.copy()\
            .move_to(ball_radius * 3.3 * RIGHT + (1.95 - ball_radius) * DOWN)

        black_color = PURE_RED
        black1 = Circle(radius=ball_radius, color=black_color, fill_color=black_color, fill_opacity=1).set_sheen(-.8, DR)\
            .move_to(ball_radius * 2.2 * LEFT + (2 - 3 * ball_radius) * DOWN)
        black2 = black1.copy()\
            .move_to((2 - 3 * ball_radius) * DOWN)
        black3 = black1.copy()\
            .move_to(ball_radius * 2.2 * RIGHT + (2 - 3 * ball_radius) * DOWN)

        self.play(GrowFromPoint(white1, 4*UL, BLACK))
        self.play(GrowFromPoint(white2, 4*UL, BLACK))
        self.play(GrowFromPoint(white3, 4*UL, BLACK))
        self.play(GrowFromPoint(white4, 4*UL, BLACK))
        self.play(GrowFromPoint(black1, 4*UR, BLACK))
        self.play(GrowFromPoint(black2, 4*UR, BLACK))
        self.play(GrowFromPoint(black3, 4*UR, BLACK))
        self.wait(delay)
        self.next_section()

        self.play(urna.animate.set_opacity(1))
        self.play(Wiggle(urna))
        self.wait(delay)
        self.next_section()

        left_arrow = CurvedArrow(LEFT, 3*LEFT + 2 * UP, color=RED)
        self.play(Create(left_arrow))
        ball1 = Circle(radius=ball_radius, color=WHITE).move_to((3 + ball_radius) * LEFT + 2 * UP)
        question1 = Tex("?").move_to(ball1)
        self.play(Create(ball1), Write(question1))

        return_arrow = CurvedArrow(3*LEFT + 2 * UP, ORIGIN, angle=-PI/2, color=ORANGE, z_index=-1)
        self.play(Create(return_arrow))

        right_arrow = CurvedArrow(RIGHT, 3*RIGHT + 2 * UP, angle=-PI/2, color=RED)
        self.play(Create(right_arrow))
        ball2 = Circle(radius=ball_radius, color=WHITE).move_to((3 + ball_radius) * RIGHT + 2 * UP)
        question2 = Tex("?").move_to(ball2)
        self.play(Create(ball2), Write(question2))
        self.wait(delay)
        self.next_section()

        question = MathTex(r"p(\text{medesimo colore}) =\,\, ?").move_to(3*UP)
        self.play(Write(question))
        self.wait(delay)
        self.next_section()

        # Fine intro

        self.play(FadeOut(left_arrow), FadeOut(ball1), FadeOut(question1), FadeOut(return_arrow),
                  FadeOut(right_arrow), FadeOut(ball2), FadeOut(question2), FadeOut(urna))
        self.wait(delay)
        self.next_section()

        self.play(white1.animate.move_to(6 * LEFT + 3 * UP),
                  white2.animate.move_to((6 - (2/3)) * LEFT + 3 * UP),
                  white3.animate.move_to((6 - (4/3)) * LEFT + 3 * UP),
                  white4.animate.move_to(4 * LEFT + 3 * UP),
                  black1.animate.move_to(4 * RIGHT + 3 * UP),
                  black2.animate.move_to(5 * RIGHT + 3 * UP),
                  black3.animate.move_to(6 * RIGHT + 3 * UP)
                  )

        self.play(FadeOut(question[0][18:19]), question[0][0:18].animate.set_color(PURE_GREEN).move_to(3*UP))
        self.wait(delay)
        self.next_section()

        soluzione = VGroup(
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                black1.copy().scale(.5),
                black1.copy().scale(.5),
                MathTex(r"\lor", color=PURE_GREEN),
                white1.copy().scale(.5),
                white1.copy().scale(.5),
                MathTex(r") =", color=PURE_GREEN)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                black1.copy().scale(.5),
                black1.copy().scale(.5),
                MathTex(r") + p(", color=PURE_GREEN),
                white1.copy().scale(.5),
                white1.copy().scale(.5),
                MathTex(r") =", color=PURE_GREEN)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                Tex("prima", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r"\land", color=PURE_GREEN),
                Tex("seconda", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") + p(", color=PURE_GREEN),
                Tex("prima"),
                white1.copy().scale(.5),
                MathTex(r"\land", color=PURE_GREEN),
                Tex("seconda"),
                white1.copy().scale(.5),
                MathTex(") =", color=PURE_GREEN)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                Tex("prima", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") \cdot p(", color=PURE_GREEN),
                Tex("seconda", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") + p(", color=PURE_GREEN),
                Tex("prima"),
                white1.copy().scale(.5),
                MathTex(r") \cdot p(", color=PURE_GREEN),
                Tex("seconda"),
                white1.copy().scale(.5),
                MathTex(") =", color=PURE_GREEN)
            ).arrange(RIGHT),
            MathTex(r"= \dfrac{3}{7} \cdot \dfrac{3}{7} + \dfrac{4}{7} \cdot \dfrac{4}{7} ="),
            MathTex(r"= \dfrac{9}{49} + \dfrac{16}{49} ="),
            MathTex(r"= \dfrac{25}{49}")
        ).scale(.9).arrange(DOWN).next_to(question, DOWN)

        soluzione[4][0][0:1].set_color(PURE_GREEN)
        soluzione[4][0][1:4].set_color(PURE_RED)
        soluzione[4][0][4:5].set_color(PURE_GREEN)
        soluzione[4][0][5:8].set_color(PURE_RED)
        soluzione[4][0][8:9].set_color(PURE_GREEN)
        soluzione[4][0][12:13].set_color(PURE_GREEN)
        soluzione[4][0][16:].set_color(PURE_GREEN)

        soluzione[5][0][0:1].set_color(PURE_GREEN)
        soluzione[5][0][1:5].set_color(PURE_RED)
        soluzione[5][0][5:6].set_color(PURE_GREEN)
        soluzione[5][0][11:].set_color(PURE_GREEN)

        soluzione[6].set_color(PURE_GREEN)

        for _i in range(len(soluzione)):
            self.play(Write(soluzione[_i]))
            self.wait(delay)
            self.next_section()

        self.play(FadeOut(soluzione), FadeOut(question[0][0:18]))

        soluzione2 = VGroup(
            MathTex(r"p(\text{almeno una rossa}) =", color=PURE_GREEN),
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                Tex("prima", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r"\lor", color=PURE_GREEN),
                Tex("seconda", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") =", color=PURE_GREEN)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"= p(", color=PURE_GREEN),
                Tex("prima", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") + p(", color=PURE_GREEN),
                Tex("seconda", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") - p(", color=PURE_GREEN),
                Tex("prima", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r"\land", color=PURE_GREEN),
                Tex("seconda", color=PURE_RED),
                black1.copy().scale(.5),
                MathTex(r") =", color=PURE_GREEN)
            ).arrange(RIGHT, buff=.2),
            MathTex(r"= \dfrac{3}{7} + \dfrac{3}{7} - \dfrac{3}{7} \cdot \dfrac{3}{7} =", color=PURE_GREEN),
            MathTex(r"= \dfrac{6}{7} - \dfrac{9}{49} =", color=PURE_GREEN),
            MathTex(r"= \dfrac{42}{49} - \dfrac{9}{49} =", color=PURE_GREEN),
            MathTex(r"= \dfrac{33}{49}", color=PURE_GREEN),
        ).arrange(DOWN)

        soluzione2[3][0][1:4].set_color(PURE_RED)
        soluzione2[3][0][5:8].set_color(PURE_RED)
        soluzione2[3][0][9:12].set_color(PURE_RED)
        soluzione2[3][0][13:16].set_color(PURE_RED)

        soluzione2[4][0][1:4].set_color(PURE_RED)
        soluzione2[4][0][5:9].set_color(PURE_RED)

        soluzione2[5][0][1:6].set_color(PURE_RED)
        soluzione2[5][0][7:11].set_color(PURE_RED)

        soluzione2[6][0][1:].set_color(PURE_RED)

        for _i in range(len(soluzione2)):
            self.play(Write(soluzione2[_i]))
            self.wait(delay)
            self.next_section()

        self.wait(60)
