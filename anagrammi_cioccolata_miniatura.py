from manim import *

DELAY = 30
WIDTH = 1.3
HEIGHT = WIDTH * 1.6
LETTER_SCALE = 3

class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        lettere = ["C", "I", "O", "C", "C", "O", "L", "A", "T", "A"]
        colori = [GREEN_E, BLACK, RED_E, BLUE_E, RED_E, GREEN_E, BLACK, RED_E, BLACK, GREEN_E]

        carte = VGroup()
        for _i in range(10):
            riquadro = RoundedRectangle(
                corner_radius=0.1, height=HEIGHT, width=WIDTH,
                color=WHITE, fill_color=WHITE, fill_opacity=1
            )
            lettera = Tex(lettere[_i], color=colori[_i]).scale(LETTER_SCALE)
            carta = VGroup(riquadro, lettera)
            carte.add(carta)

        carte.arrange(RIGHT, buff=SMALL_BUFF)

        for carta in carte:
            carta.rotate(np.random.uniform(-5, 5) * DEGREES)

        self.add(carte)
