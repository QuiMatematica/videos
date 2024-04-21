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

        n = MathTex(r"n").set_color(YELLOW).scale(1.5).next_to(graffa_sopra, UP)
        self.play(Write(n))
        self.cut_and_wait()

        self.play(
            carte[3].animate.move_to(segnaposti[1]),
            carte[4].animate.move_to(segnaposti[2]),
            carte[2].animate.move_to(segnaposti[3]),
            carte[5].animate.move_to(segnaposti[4]),
            carte[7].animate.move_to(segnaposti[5]),
            carte[9].animate.move_to(segnaposti[6]),
            carte[1].animate.move_to(segnaposti[7]),
            carte[6].animate.move_to(segnaposti[8]),
            carte[8].animate.move_to(segnaposti[9]),
        )

        gruppo_3_c = VGroup(carte[0], carte[3], carte[4])
        graffa_c = Brace(gruppo_3_c, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_c))

        p_1 = MathTex(r"p_1").set_color(YELLOW).scale(1.5).next_to(graffa_c, DOWN)
        self.play(Write(p_1))
        self.cut_and_wait()

        ## O

        gruppo_o = VGroup(carte[2], carte[5])
        graffa_o = Brace(gruppo_o, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_o))

        p_2 = MathTex(r"p_2").set_color(YELLOW).scale(1.5).next_to(graffa_o, DOWN)
        self.play(Write(p_2))
        self.cut_and_wait()

        ## A

        gruppo_a = VGroup(carte[7], carte[9])
        graffa_a = Brace(gruppo_a, direction=DOWN, color=YELLOW, sharpness=.5)
        self.play(Create(graffa_a))

        p_3 = MathTex(r"\dots").set_color(YELLOW).scale(1.5).next_to(graffa_a, DOWN)
        self.play(Write(p_3))
        self.cut_and_wait()

        formula = MathTex(r"P_n^{(p_1, p_2, \dots)} } = {{ \dfrac{ n! }{ p_1! \cdot p_2! \dots} }}").set_color(YELLOW).scale(1.5).move_to(DOWN * 2.8)
        self.play(Write(formula[1]))
        self.cut_and_wait()

        self.play(Write(formula[0]))

        self.wait(30)
