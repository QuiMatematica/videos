from manim import *

DELAY = 30
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3
CARDS_BUFF = .1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        segnaposti = VGroup()
        for _i in range(10):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=WHITE
            )
            segnaposti.add(riquadro)
        segnaposti.arrange(RIGHT, buff=CARDS_BUFF).shift(1.2 * UP)

        lettere = ["C", "I", "O", "C", "C", "O", "L", "A", "T", "A"]
        colori = [RED_E, BLACK, RED_E, GREEN_E, BLUE_E, GREEN_E, BLACK, RED_E, BLACK, GREEN_E]

        carte = VGroup()
        for _i in range(10):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=BLACK, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=colori[_i]).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carta.rotate(np.random.uniform(-2, 2) * DEGREES)
            carta.move_to(6*UP)
            self.play(carta.animate.move_to(segnaposti[_i]))
            carte.add(carta)
        self.cut_and_wait()

        graffa_sopra = Brace(carte, direction=UP, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_sopra))

        p_10 = [
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 6 \cdot }} 5 \cdot {{ 4 \cdot }} 3 \cdot {{ 2 \cdot 1 }}"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 6 \cdot }} 5 \cdot {{ 4 \cdot }} 3 \cdot {{ 2 }}"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 6 \cdot }} 5 \cdot {{ 4 \cdot }} 6"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 6 \cdot }} 5 \cdot {{ 24 }}"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 6 \cdot }} 120"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 7 \cdot {{ 720 }}"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 8 \cdot }} 5040"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 9 \cdot {{ 40320 }}"),
            MathTex(r"P_{10} = {{ 10 \cdot }} 362880"),
            MathTex(r"P_{10} = {{ 3628800 }}")
        ]

        for _i in range(len(p_10)):
            p_10[_i].set_color(YELLOW).scale(1.5).next_to(graffa_sopra, UP)
        self.play(Write(p_10[0]))
        self.cut_and_wait()

        prev = p_10[0]
        for _i in range(1, len(p_10)):
            self.play(TransformMatchingTex(prev, p_10[_i]))
            prev = p_10[_i]
        self.cut_and_wait()

        self.play(
            carte[3].animate.move_to(segnaposti[1]),
            carte[4].animate.move_to(segnaposti[2]),
            carte[1].animate.move_to(segnaposti[3]),
            carte[2].animate.move_to(segnaposti[4]),
        )

        gruppo_3_c = VGroup(carte[0], carte[3], carte[4])
        graffa_c = Brace(gruppo_3_c, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_c))

        p_3_c = [
            MathTex(r"P_{3} = 3 \cdot {{ 2 \cdot 1 }}"),
            MathTex(r"P_{3} = 3 \cdot {{ 2 }}"),
            MathTex(r"P_{3} = 6")
        ]
        for _i in range(len(p_3_c)):
            p_3_c[_i].set_color(YELLOW).scale(1.5).next_to(graffa_c, DOWN)
        self.play(Write(p_3_c[0]))
        prev = p_3_c[0]
        for _i in range(1, len(p_3_c)):
            self.play(TransformMatchingTex(prev, p_3_c[_i]))
            prev = p_3_c[_i]
        self.cut_and_wait()

        formula = [
            MathTex(r"\dfrac{P_{10}}{P_3} = \dfrac{3628800}{6} = 604800"),
            MathTex(r"\dfrac{P_{10}}{P_3 \cdot P_2} = \dfrac{3628800}{6 \cdot 2} = 302400"),
            MathTex(r"\dfrac{P_{10}}{P_3 \cdot P_2 \cdot P_2} = \dfrac{3628800}{6 \cdot 2 \cdot 2} = 151200"),
        ]
        for _i in range(len(formula)):
            formula[_i].set_color(YELLOW).scale(1.5).move_to(DOWN * 2.8)
        self.play(Write(formula[0]))
        self.cut_and_wait()

        ## O

        self.play(
            carte[2].animate.move_to(segnaposti[3]),
            carte[5].animate.move_to(segnaposti[4]),
            carte[1].animate.move_to(segnaposti[5]),
        )
        self.cut_and_wait()

        gruppo_o = VGroup(carte[2], carte[5])
        graffa_o = Brace(gruppo_o, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_o))

        p_2_o = MathTex(r"P_{2} = 2").set_color(YELLOW).scale(1.5).next_to(graffa_o, DOWN)
        self.play(Write(p_2_o))
        self.cut_and_wait()

        self.play(ReplacementTransform(formula[0], formula[1]))
        self.cut_and_wait()

        ## A

        self.play(
            carte[7].animate.move_to(segnaposti[5]),
            carte[9].animate.move_to(segnaposti[6]),
            carte[1].animate.move_to(segnaposti[7]),
            carte[6].animate.move_to(segnaposti[8]),
            carte[8].animate.move_to(segnaposti[9]),
        )
        self.cut_and_wait()

        gruppo_a = VGroup(carte[7], carte[9])
        graffa_a = Brace(gruppo_a, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_a))

        p_2_a = MathTex(r"P_{2} = 2").set_color(YELLOW).scale(1.5).next_to(graffa_a, DOWN)
        self.play(Write(p_2_a))
        self.cut_and_wait()

        self.play(ReplacementTransform(formula[1], formula[2]))

        self.wait(30)
