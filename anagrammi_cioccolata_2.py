import itertools

from manim import *

DELAY = 1
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3
CARDS_BUFF = .2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        segnaposti = VGroup()
        for _i in range(4):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=WHITE
            )
            segnaposti.add(riquadro)
        segnaposti.arrange(RIGHT, buff=CARDS_BUFF)

        lettere = ["N", "A", "V", "E"]

        carte = VGroup()
        for _i in range(4):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=BLACK, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=BLACK).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carta.rotate(np.random.uniform(-2, 2) * DEGREES)
            carta.move_to(6*UP)
            self.play(carta.animate.move_to(segnaposti[_i]))
            carte.add(carta)
        self.cut_and_wait()

        posizioni = [(-1.5, -1.55, 0), (-.5, -1.3, 0), (.5, -1.3, 0), (1.5, -1.55, 0)]
        rotazioni = [21, 7, -7, -21]

        self.play(
            *[carte[_i].animate.move_to(posizioni[_i]).rotate(rotazioni[_i] * DEGREES) for _i in range(4)]
        )

        segnaposti.shift(1.5 * UP)

        self.play(Create(segnaposti))
        self.cut_and_wait()

        self.play(self.camera.frame.animate.scale(2).shift(2 * DOWN))
        self.cut_and_wait()

        tutto = VGroup(segnaposti, carte)

        livello_1 = [tutto.copy(), tutto.copy(), tutto.copy(), tutto.copy()]
        self.remove(*[carte[_i] for _i in range(4)])

        delta = 7
        self.play(
            *[livello_1[_i].animate.shift((-(delta * 1.5) + _i * delta) * RIGHT + 6 * DOWN) for _i in range(4)],
        )
        self.play(
            *[Create(Line(segnaposti.get_bottom(), livello_1[_i][0].get_top(), color=GRAY, z_index=-1)) for _i in range(4)]
        )
        self.cut_and_wait()

        for _i in range(4):
            self.play(
                livello_1[_i][1][_i].animate.move_to(livello_1[_i][0][0]).rotate(-rotazioni[_i]*DEGREES)
            )
        self.cut_and_wait()

        livello_2 = [
            [livello_1[0].copy(), livello_1[0].copy(), livello_1[0].copy()],
            [livello_1[1].copy(), livello_1[1].copy(), livello_1[1].copy()],
            [livello_1[2].copy(), livello_1[2].copy(), livello_1[2].copy()],
            [livello_1[3].copy(), livello_1[3].copy(), livello_1[3].copy()]
        ]

        for _i in range(4):
            for _j in range(3):
                self.add(livello_2[_i][_j])

        for _i in range(4):
            for _j in range(4):
                if _i != _j:
                    self.remove(livello_1[_i][1][_j])

        self.play(self.camera.frame.animate.scale(3).shift(2*DOWN))
        self.cut_and_wait()

        self.play(
            *[livello_2[_i // 3][_i % 3].animate
              .shift((-(delta * 5.5) + _i * delta) * RIGHT - (-(delta * 1.5) + (_i // 3) * delta) * RIGHT + 6 * DOWN)
              for _i in range(12)],
        )

        self.wait(30)
