import itertools

from manim import *

DELAY = 30
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

        self.play(*[carte[_i].animate.move_to(segnaposti[_i]) for _i in range(10)])
        self.cut_and_wait()

        def generate_permutations(n):
            elements = list(range(0, n))  # Creo una lista di numeri da 1 a n
            return list(itertools.permutations(elements))  # Genero tutte le permutazioni

        permutations = generate_permutations(4)

        print("Tutte le permutazioni di 4 elementi sono:")
        for perm in permutations[1:]:
            print(perm)

        griglia = VGroup()
        for _i in range(len(permutations)):
            griglia.add(Dot())
        griglia.arrange_in_grid(rows=6, cols=4, buff=(3, .6))

        self.play(carte.animate.scale(.2).move_to(griglia[0]))

        pos = [0, 2, 6, 9]

        for _i in range(1, 24):
            perm = permutations[_i]
            copia = carte.copy()

            self.play(copia.animate.move_to(griglia[_i]))
            self.play(
                copia[pos[0]].animate.move_to(copia[pos[perm[0]]]),
                copia[pos[1]].animate.move_to(copia[pos[perm[1]]]),
                copia[pos[2]].animate.move_to(copia[pos[perm[2]]]),
                copia[pos[3]].animate.move_to(copia[pos[perm[3]]]),
            )

        self.wait(30)
