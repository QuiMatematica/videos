from manim import *

DELAY = 1
WIDTH = 1.2
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 2.8
CARDS_BUFF = .05


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        segnaposti = VGroup()
        for _i in range(11):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=WHITE
            )
            segnaposti.add(riquadro)
        segnaposti.arrange(RIGHT, buff=CARDS_BUFF)

        lettere = ["C", "O", "C", "C", "O", "D", "R", "I", "L", "L", "O"]

        carte = VGroup()
        for _i in range(11):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=BLACK, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=BLACK).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carta.rotate(np.random.uniform(-2, 2) * DEGREES)
            carte.add(carta)

        self.add(carte)

        self.play(*[carte[_i].animate.move_to(segnaposti[_i]) for _i in range(11)])

        self.wait(30)
