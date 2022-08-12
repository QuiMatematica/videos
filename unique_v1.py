from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        equation = VGroup(
            MathTex(r"(2x + 1)^2 -3(2x - 1)(2x + 1) = -2(2x + 1)(2x - 3)"),
            MathTex(r"4x^2 +4x +1 -3(4x^2 - 1) = -2(4x^2 -6x + 2x - 3)"),
            MathTex(r"4x^2 +4x +1 -12x^2 + 3 = -8x^2 +12x -4x +6"),
            MathTex(r"-8x^2 +4x +4 = -8x^2 +8x +6"),
            MathTex(r"-8x^2 +4x +8x^2 -8x = 6 -4"),
            MathTex(r"-4x = 2"),
            MathTex(r"x = \dfrac{2}{-4}"),
            MathTex(r"x = -\dfrac{1}{2}")
        ).scale(.7).arrange(DOWN, aligned_edge=LEFT).to_edge(UL)

        rules = VGroup(
            Tex("REGOLE"),
            Tex("- prodotti tra polinomi"),
            Tex("- prodotti notevoli"),
            Tex("- somma tra monomi"),
            Tex("- regola del trasporto"),
            Tex("- dividere i membri per numero"),
            Tex("- ridurre ai minimi termini")
        ).set_color(GREEN).scale(.7).arrange(DOWN, aligned_edge=LEFT).shift(4*LEFT)

        strats = VGroup(
            Tex("STRATEGIA"),
            Tex("1) semplificare i membri"),
            Tex("2) trasportare i termini"),
            Tex("3) semplificare i membri"),
            Tex("4) dividere per il coeff. della x"),
            Tex("5) semplificare la frazione")
        ).set_color(RED).scale(.7).arrange(DOWN, aligned_edge=LEFT).shift(4*RIGHT)

        rs = VGroup(rules, strats).arrange(RIGHT, aligned_edge=UP, buff=0.6).to_edge(DR)

        self.play(Write(equation[0]))
        self.wait(delay)
        self.next_section()

        self.play(Create(BackgroundRectangle(rules, color=DARK_GREY, buff=.25)))
        self.play(Write(rules[0]))
        self.wait(delay)
        self.next_section()

        self.play(Create(BackgroundRectangle(strats, color=DARK_GREY, buff=.25)))
        self.play(Write(strats[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(strats[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(rules[1]))
        self.play(Write(rules[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[1]))
        self.play(Write(equation[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(rules[3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(strats[2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(rules[4]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[4]))
        self.wait(delay)
        self.next_section()

        self.play(Write(strats[3]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(strats[4]))
        self.wait(delay)
        self.next_section()

        self.play(Write(rules[5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[6]))
        self.wait(delay)
        self.next_section()

        self.play(Write(strats[5]))
        self.wait(delay)
        self.next_section()

        self.play(Write(rules[6]))
        self.wait(delay)
        self.next_section()

        self.play(Write(equation[7]))
        self.wait(delay)
        self.next_section()

        # self.add(equation)
        # self.add(rules)
        # self.add(strats)

        self.wait(60)
