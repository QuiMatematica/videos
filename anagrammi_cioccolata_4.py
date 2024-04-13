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

        lettere = ["N", "E", "V", "E"]

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
            carte.add(carta)

        riquadro = RoundedRectangle(
            corner_radius=0.1, height=HEIGHT, width=WIDTH,
            color=BLACK, fill_color=WHITE, fill_opacity=1
        )
        lettera = Tex("A", color=BLACK).scale(LETTER_SCALE)
        carta = VGroup(riquadro, lettera)
        carta.rotate(np.random.uniform(-2, 2) * DEGREES)
        carta.move_to(6 * UP)

        self.play(carte[0].animate.move_to(segnaposti[0]))
        self.play(carta.animate.move_to(segnaposti[1]))
        self.play(carte[2].animate.move_to(segnaposti[2]))
        self.play(carte[3].animate.move_to(segnaposti[3]))
        self.cut_and_wait()

        self.play(carta.animate.move_to(6*DOWN))
        self.play(carte[1].animate.move_to(segnaposti[1]))
        self.cut_and_wait()
        self.remove(carta)

        # ###################################

        posizioni = [(-1.5, -.15, 0) + 3*RIGHT, (-.5, .15, 0) + 3*RIGHT, (.5, .15, 0) + 3*RIGHT, (1.5, -.15, 0) + 3*RIGHT]
        rotazioni = [21, 7, -7, -21]

        self.play(
            *[carte[_i].animate.move_to(posizioni[_i]).rotate(rotazioni[_i] * DEGREES) for _i in range(4)]
        )

        segnaposti.shift(3*LEFT)

        self.play(Create(segnaposti))

        tutto = VGroup(segnaposti, carte)

        delta_v = 7 * DOWN
        delta_h = 12 * RIGHT

        self.play(self.camera.frame.animate.scale(9).shift(2 * delta_h))

        livello_1 = [tutto.copy(), tutto.copy(), tutto.copy(), tutto.copy()]
        self.remove(*[carte[_i] for _i in range(4)])

        self.play(
            *[livello_1[_i].animate.shift(delta_v * (_i - 1.5) + delta_h) for _i in range(4)],
        )
        self.play(
            *[Create(Line(segnaposti.get_right(), livello_1[_i][0].get_left(), color=GRAY)) for _i in range(4)]
        )

        for _i in range(4):
            self.play(
                livello_1[_i][1][_i].animate.move_to(livello_1[_i][0][0]).rotate(-rotazioni[_i]*DEGREES)
            )

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

        delta_v2 = 3 * DOWN
        delta_v2_b = 6 * DOWN

        self.play(
            *[livello_2[_i // 3][_i % 3].animate.shift(delta_v2 * (_i - 5.5) - delta_v2_b * ((_i // 3) - 1.5) + delta_h)
              for _i in range(12)],
        )
        self.play(
            *[Create(Line(livello_1[_i // 3][0].get_right(), livello_2[_i // 3][_i % 3][0].get_left(), color=GRAY))
              for _i in range(12)]
        )

        self.play(
            livello_2[0][0][1][1].animate.move_to(livello_2[0][0][0][1]).rotate(-rotazioni[1]*DEGREES),
            livello_2[0][1][1][2].animate.move_to(livello_2[0][1][0][1]).rotate(-rotazioni[2]*DEGREES),
            livello_2[0][2][1][3].animate.move_to(livello_2[0][2][0][1]).rotate(-rotazioni[3]*DEGREES),
            livello_2[1][0][1][0].animate.move_to(livello_2[1][0][0][1]).rotate(-rotazioni[0]*DEGREES),
            livello_2[1][1][1][2].animate.move_to(livello_2[1][1][0][1]).rotate(-rotazioni[2]*DEGREES),
            livello_2[1][2][1][3].animate.move_to(livello_2[1][2][0][1]).rotate(-rotazioni[3]*DEGREES),
            livello_2[2][0][1][0].animate.move_to(livello_2[2][0][0][1]).rotate(-rotazioni[0]*DEGREES),
            livello_2[2][1][1][1].animate.move_to(livello_2[2][1][0][1]).rotate(-rotazioni[1]*DEGREES),
            livello_2[2][2][1][3].animate.move_to(livello_2[2][2][0][1]).rotate(-rotazioni[3]*DEGREES),
            livello_2[3][0][1][0].animate.move_to(livello_2[3][0][0][1]).rotate(-rotazioni[0]*DEGREES),
            livello_2[3][1][1][1].animate.move_to(livello_2[3][1][0][1]).rotate(-rotazioni[1]*DEGREES),
            livello_2[3][2][1][2].animate.move_to(livello_2[3][2][0][1]).rotate(-rotazioni[2]*DEGREES)
        )

        livello_3 = []
        for _i in range(12):
            livello_3.append([livello_2[_i // 3][_i % 3].copy(), livello_2[_i // 3][_i % 3].copy()])

        for _i in range(12):
            for _j in range(2):
                self.add(livello_3[_i][_j])

        self.remove(livello_2[0][0][1][2])
        self.remove(livello_2[0][0][1][3])
        self.remove(livello_2[0][1][1][1])
        self.remove(livello_2[0][1][1][3])
        self.remove(livello_2[0][2][1][1])
        self.remove(livello_2[0][2][1][2])
        self.remove(livello_2[1][0][1][2])
        self.remove(livello_2[1][0][1][3])
        self.remove(livello_2[1][1][1][0])
        self.remove(livello_2[1][1][1][3])
        self.remove(livello_2[1][2][1][0])
        self.remove(livello_2[1][2][1][2])
        self.remove(livello_2[2][0][1][1])
        self.remove(livello_2[2][0][1][3])
        self.remove(livello_2[2][1][1][0])
        self.remove(livello_2[2][1][1][3])
        self.remove(livello_2[2][2][1][0])
        self.remove(livello_2[2][2][1][1])
        self.remove(livello_2[3][0][1][1])
        self.remove(livello_2[3][0][1][2])
        self.remove(livello_2[3][1][1][0])
        self.remove(livello_2[3][1][1][2])
        self.remove(livello_2[3][2][1][0])
        self.remove(livello_2[3][2][1][1])

        delta_v2 = 3 * DOWN
        delta_v2_b = 3 * DOWN
        delta_v2_c = 1 * DOWN

        self.play(
            *[livello_3[_i // 2][_i % 2].animate.shift(delta_v2 * (_i - 11.5) - delta_v2_b * ((_i // 2) - 5.5) - delta_v2_c * ((_i // 6) - 1.5) + delta_h)
              for _i in range(24)],
        )
        self.play(
            *[Create(Line(livello_2[_i // 6][(_i % 6 // 2)][0].get_right(), livello_3[_i // 2][_i % 2][0].get_left(), color=GRAY))
              for _i in range(24)]
        )

        self.play(
            livello_3[0][0][1][2].animate.move_to(livello_3[0][0][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[0][1][1][3].animate.move_to(livello_3[0][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[1][0][1][1].animate.move_to(livello_3[1][0][0][2]).rotate(-rotazioni[1]*DEGREES),
            livello_3[1][1][1][3].animate.move_to(livello_3[1][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[2][0][1][1].animate.move_to(livello_3[2][0][0][2]).rotate(-rotazioni[1]*DEGREES),
            livello_3[2][1][1][2].animate.move_to(livello_3[2][1][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[3][0][1][2].animate.move_to(livello_3[3][0][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[3][1][1][3].animate.move_to(livello_3[3][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[4][0][1][0].animate.move_to(livello_3[4][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[4][1][1][3].animate.move_to(livello_3[4][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[5][0][1][0].animate.move_to(livello_3[5][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[5][1][1][2].animate.move_to(livello_3[5][1][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[6][0][1][1].animate.move_to(livello_3[6][0][0][2]).rotate(-rotazioni[1]*DEGREES),
            livello_3[6][1][1][3].animate.move_to(livello_3[6][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[7][0][1][0].animate.move_to(livello_3[7][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[7][1][1][3].animate.move_to(livello_3[7][1][0][2]).rotate(-rotazioni[3]*DEGREES),
            livello_3[8][0][1][0].animate.move_to(livello_3[8][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[8][1][1][1].animate.move_to(livello_3[8][1][0][2]).rotate(-rotazioni[1]*DEGREES),
            livello_3[9][0][1][1].animate.move_to(livello_3[9][0][0][2]).rotate(-rotazioni[1]*DEGREES),
            livello_3[9][1][1][2].animate.move_to(livello_3[9][1][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[10][0][1][0].animate.move_to(livello_3[10][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[10][1][1][2].animate.move_to(livello_3[10][1][0][2]).rotate(-rotazioni[2]*DEGREES),
            livello_3[11][0][1][0].animate.move_to(livello_3[11][0][0][2]).rotate(-rotazioni[0]*DEGREES),
            livello_3[11][1][1][1].animate.move_to(livello_3[11][1][0][2]).rotate(-rotazioni[1]*DEGREES)
        )

        livello_4 = []
        for _i in range(24):
            livello_4.append(livello_3[_i // 2][_i % 2].copy())

        self.remove(livello_3[0][0][1][3])
        self.remove(livello_3[0][1][1][2])
        self.remove(livello_3[1][0][1][3])
        self.remove(livello_3[1][1][1][1])
        self.remove(livello_3[2][0][1][2])
        self.remove(livello_3[2][1][1][1])
        self.remove(livello_3[3][0][1][3])
        self.remove(livello_3[3][1][1][2])
        self.remove(livello_3[4][0][1][3])
        self.remove(livello_3[4][1][1][0])
        self.remove(livello_3[5][0][1][2])
        self.remove(livello_3[5][1][1][0])
        self.remove(livello_3[6][0][1][3])
        self.remove(livello_3[6][1][1][1])
        self.remove(livello_3[7][0][1][3])
        self.remove(livello_3[7][1][1][0])
        self.remove(livello_3[8][0][1][1])
        self.remove(livello_3[8][1][1][0])
        self.remove(livello_3[9][0][1][2])
        self.remove(livello_3[9][1][1][1])
        self.remove(livello_3[10][0][1][2])
        self.remove(livello_3[10][1][1][0])
        self.remove(livello_3[11][0][1][1])
        self.remove(livello_3[11][1][1][0])

        self.play(*[livello_4[_i].animate.shift(delta_h) for _i in range(24)])

        self.play(
            *[Create(Line(livello_3[_i // 2][(_i % 2)][0].get_right(), livello_4[_i][0].get_left(), color=GRAY))
              for _i in range(24)]
        )

        self.play(
            livello_4[0][1][3].animate.move_to(livello_4[0][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[1][1][2].animate.move_to(livello_4[1][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[2][1][3].animate.move_to(livello_4[2][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[3][1][1].animate.move_to(livello_4[3][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[4][1][2].animate.move_to(livello_4[4][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[5][1][1].animate.move_to(livello_4[5][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[6][1][3].animate.move_to(livello_4[6][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[7][1][2].animate.move_to(livello_4[7][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[8][1][3].animate.move_to(livello_4[8][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[9][1][0].animate.move_to(livello_4[9][0][3]).rotate(-rotazioni[0]*DEGREES),
            livello_4[10][1][2].animate.move_to(livello_4[10][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[11][1][0].animate.move_to(livello_4[11][0][3]).rotate(-rotazioni[0]*DEGREES),
            livello_4[12][1][3].animate.move_to(livello_4[12][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[13][1][1].animate.move_to(livello_4[13][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[14][1][3].animate.move_to(livello_4[14][0][3]).rotate(-rotazioni[3]*DEGREES),
            livello_4[15][1][0].animate.move_to(livello_4[15][0][3]).rotate(-rotazioni[0]*DEGREES),
            livello_4[16][1][1].animate.move_to(livello_4[16][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[17][1][0].animate.move_to(livello_4[17][0][3]).rotate(-rotazioni[0]*DEGREES),
            livello_4[18][1][2].animate.move_to(livello_4[18][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[19][1][1].animate.move_to(livello_4[19][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[20][1][2].animate.move_to(livello_4[20][0][3]).rotate(-rotazioni[2]*DEGREES),
            livello_4[21][1][0].animate.move_to(livello_4[21][0][3]).rotate(-rotazioni[0]*DEGREES),
            livello_4[22][1][1].animate.move_to(livello_4[22][0][3]).rotate(-rotazioni[1]*DEGREES),
            livello_4[23][1][0].animate.move_to(livello_4[23][0][3]).rotate(-rotazioni[0]*DEGREES)
        )
        self.cut_and_wait()

        self.wait(30)
