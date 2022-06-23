from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

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
                  FadeOut(right_arrow), FadeOut(ball2), FadeOut(question2), FadeOut(urna),
                  FadeOut(question))
        self.wait(delay)
        self.next_section()

        self.play(
            white1.animate.move_to(6 * LEFT + 2.5 * UP),
            white2.animate.move_to(6 * LEFT + 1.5 * UP),
            white3.animate.move_to(6 * LEFT + .5 * UP),
            white4.animate.move_to(6 * LEFT + .5 * DOWN),
            black1.animate.move_to(6 * LEFT + 1.5 * DOWN),
            black2.animate.move_to(6 * LEFT + 2.5 * DOWN),
            black3.animate.move_to(6 * LEFT + 3.5 * DOWN))
        self.wait(delay)
        self.next_section()

        wh1 = MathTex("1", color=BLACK).move_to(white1)
        self.play(Write(wh1))
        white1.add(wh1)
        wh2 = MathTex("2", color=BLACK).move_to(white2)
        self.play(Write(wh2))
        white2.add(wh2)
        wh3 = MathTex("3", color=BLACK).move_to(white3)
        self.play(Write(wh3))
        white3.add(wh3)
        wh4 = MathTex("4", color=BLACK).move_to(white4)
        self.play(Write(wh4))
        white4.add(wh4)
        self.wait(delay)
        self.next_section()

        bl1 = MathTex("1", color=BLACK).move_to(black1)
        self.play(Write(bl1))
        black1.add(bl1)
        bl2 = MathTex("2", color=BLACK).move_to(black2)
        self.play(Write(bl2))
        black2.add(bl2)
        bl3 = MathTex("3", color=BLACK).move_to(black3)
        self.play(Write(bl3))
        black3.add(bl3)
        self.wait(delay)
        self.next_section()

        palline_first = [white1, white2, white3, white4, black1, black2, black3]
        palline_second = [white1.copy(), white2.copy(), white3.copy(), white4.copy(), black1.copy(), black2.copy(), black3.copy()]

        self.play(
            palline_second[0].animate.move_to(5 * LEFT + 3.5 * UP),
            palline_second[1].animate.move_to(4 * LEFT + 3.5 * UP),
            palline_second[2].animate.move_to(3 * LEFT + 3.5 * UP),
            palline_second[3].animate.move_to(2 * LEFT + 3.5 * UP),
            palline_second[4].animate.move_to(1 * LEFT + 3.5 * UP),
            palline_second[5].animate.move_to(0 * LEFT + 3.5 * UP),
            palline_second[6].animate.move_to(-1 * LEFT + 3.5 * UP))
        self.wait(delay)
        self.next_section()

        table_first = []
        table_second = []

        for i in range(7):
            table_first.append([])
            table_second.append([])
            for j in range(7):
                table_first[i].append(palline_first[i].copy())
                table_second[i].append(palline_second[j].copy())
                self.play(
                    table_first[i][j].animate.move_to((5.15 - j) * LEFT + (2.65 - i) * UP).scale(.5),
                    table_second[i][j].animate.move_to((4.85 - j) * LEFT + (2.35 - i) * UP).scale(.5))
        self.wait(delay)
        self.next_section()

        risposta = VGroup(
            MathTex(r"p(\text{medesimo colore}) ="),
            MathTex(r"= \dfrac{25}{49}")
        ).arrange(DOWN).move_to(4.5*RIGHT)
        self.play(Write(risposta[0]))
        self.play(Write(risposta[1][0][0]))
        self.play(Write(risposta[1][0][3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(risposta[1][0][4:6]))
        self.wait(delay)
        self.next_section()

        ul_balls = VGroup(table_first[0][0], table_second[3][3])
        ul_rect = SurroundingRectangle(ul_balls)
        self.play(Create(ul_rect))
        dr_balls = VGroup(table_first[4][4], table_second[6][6])
        dr_rect = SurroundingRectangle(dr_balls)
        self.play(Create(dr_rect))
        self.wait(delay)
        self.next_section()

        ul_card = MathTex("16", color=YELLOW).scale(3).move_to(ul_balls)
        self.play(Write(ul_card))
        dr_card = MathTex("9", color=YELLOW).scale(3).move_to(dr_balls)
        self.play(Write(dr_card))
        self.wait(delay)
        self.next_section()

        self.play(Write(risposta[1][0][1:3]))
        self.wait(delay)
        self.next_section()

        self.wait(60)
