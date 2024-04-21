from manim import *

DELAY = 1
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3
CARDS_BUFF = SMALL_BUFF


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
        segnaposti.arrange(RIGHT, buff=CARDS_BUFF)

        lettere = ["C", "I", "O", "C", "C", "O", "L", "A", "T", "A"]

        carte = VGroup()
        for _i in range(10):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=BLACK, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=BLACK).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carta.rotate(np.random.uniform(-2, 2) * DEGREES)
            carte.add(carta)

        self.add(carte)

        sort = [0, 8, 6, 3, 9, 1, 4, 5, 7, 2]
        self.play(*[carte[sort[_i]].animate.move_to(segnaposti[_i]) for _i in range(10)])

        self.play(*[carte[_i].animate.move_to(ORIGIN) for _i in range(10)])

        sort = [3, 5, 7, 9, 1, 0, 8, 6, 4, 2]
        self.play(*[carte[sort[_i]].animate.move_to(segnaposti[_i]) for _i in range(10)])

        self.play(*[carte[_i].animate.move_to(ORIGIN) for _i in range(10)])

        sort = [2, 6, 8, 0, 4, 1, 9, 5, 7, 3]
        self.play(*[carte[sort[_i]].animate.move_to(segnaposti[_i]) for _i in range(10)])

        self.play(*[carte[_i].animate.move_to(ORIGIN) for _i in range(10)])

        self.play(*[carte[_i].animate.move_to(segnaposti[_i]) for _i in range(10)])

        self.wait(30)
