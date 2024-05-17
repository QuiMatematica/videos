from manim import *

DELAY = 1
X_RADIUS = config["frame_x_radius"]
Y_RADIUS = config["frame_y_radius"]
POS = [
    -3 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    -1 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    +1 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    +3 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    -3 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    -1 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    +1 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    +3 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
]
SCALE = .6


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        equazione_iniziale = MathTex(r"-2 {{ x^2 }} + 5 {{ x }} - 3 {{ = 0 }}")
        self.play(Write(equazione_iniziale))
        self.cut_and_wait()

        equazione_divisa = MathTex(r"\dfrac{-2}{-2} {{ x^2 }} + \dfrac{5}{-2} {{ x }} - \dfrac{3}{-2} {{ = 0 }}")
        self.play(TransformMatchingTex(equazione_iniziale, equazione_divisa))
        self.cut_and_wait()
        # self.remove(equazione_iniziale)
        # self.remove(equazione_divisa)
        # self.add(equazione_divisa)

        equazione_semplificata = MathTex(r"{{ x^2 }} - \dfrac{5}{2} {{ x }} + \dfrac{3}{2} {{ = 0 }}")
        self.play(TransformMatchingTex(equazione_divisa, equazione_semplificata))
        self.cut_and_wait()

        equazione = MathTex(r"x^2 - \dfrac{5}{2}x + \dfrac{3}{2} = 0").scale(SCALE).move_to(POS[0])
        coeff_b = MathTex(r"b = -\dfrac{5}{2} \in \mathbb{Q}").scale(SCALE).move_to(POS[1])
        coeff_c = MathTex(r"c = \dfrac{3}{2} \in \mathbb{Q}").scale(SCALE).move_to(POS[2])
        media = MathTex(r"m = -\dfrac{b}{2} = \dfrac{5}{4} \in \mathbb{Q}").scale(SCALE).move_to(POS[3])
        delta = MathTex(r"\Delta = b^2 - 4c = \dfrac{1}{4} \in \mathbb{Q}").scale(SCALE).move_to(POS[4])
        radice = MathTex(r"\sqrt{\Delta} = \dfrac{1}{2} \in \mathbb{Q}").scale(SCALE).move_to(POS[5])
        x1 = MathTex(r"x_1 = m - \dfrac{\sqrt{\Delta}}{2} = 1 \in \mathbb{Q}").scale(SCALE).move_to(POS[6])
        x2 = MathTex(r"x_2 = m + \dfrac{\sqrt{\Delta}}{2} = \dfrac{3}{2} \in \mathbb{Q}").scale(SCALE).move_to(POS[7])

        # self.add(equazione, coeff_b, coeff_c, media, delta, radice, x1, x2)

        self.wait(30)
