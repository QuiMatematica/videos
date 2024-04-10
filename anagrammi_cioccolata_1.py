import itertools

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
        colori = [GREEN_E, BLACK, RED_E, BLUE_E, RED_E, GREEN_E, BLACK, RED_E, BLACK, GREEN_E]

        carte = VGroup()
        for _i in range(10):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=WHITE, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=BLACK).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carta.rotate(np.random.uniform(-5, 5) * DEGREES)
            carte.add(carta)

        self.add(carte)

        self.play(*[carte[_i].animate.move_to(segnaposti[_i]) for _i in range(10)])
        self.cut_and_wait()


        def generate_permutations(n):
            elements = list(range(1, n + 1))  # Creo una lista di numeri da 1 a n
            permutations = list(itertools.permutations(elements))  # Genero tutte le permutazioni
            return permutations

        permutations = generate_permutations(4)

        print("Tutte le permutazioni di 4 elementi sono:")
        for perm in permutations[1:]:
            print(perm)

        griglia = VGroup()
        for _i in range(len(permutations)):
            griglia.add(Dot())
        griglia.arrange_in_grid(rows=6, cols=4, buff=(2, .2))

        self.play(carte.animate.scale(.2).move_to(griglia[0]))

        for _i in range(1, 24):
            perm = permutations[_i]
            copia = carte.copy()

            self.play(copia.animate.move_to(griglia[_i]))
            self.play(
                copia[9].animate.move_to(copia[5 + perm[3]]),
                copia[8].animate.move_to(copia[5 + perm[2]]),
                copia[7].animate.move_to(copia[5 + perm[1]]),
                copia[6].animate.move_to(copia[5 + perm[0]])
            )
            self.cut_and_wait()

        self.wait(30)
