from manim import Dot, RIGHT, UP, MathTex, DL

POINT_DISTANCE_RATIO = .5 * .7


class Punto(Dot):

    def __init__(self, ascissa, ordinata, nome=None, **kwargs):
        self.ordinata = ordinata
        self.nome = nome
        super().__init__(ascissa * RIGHT + ordinata * UP, **kwargs)

    def get_ascissa(self):
        return self.get_center()[0]

    def get_ordinata(self):
        return self.get_center()[1]

    def get_label(self, **kwargs):
        return MathTex(self.nome, color=self.get_color(), **kwargs).next_to(self, POINT_DISTANCE_RATIO * DL)

    def sposta_in(self, ascissa, ordinata):
        self.move_to(ascissa * RIGHT + ordinata * UP)
