import numpy as np
from manim import Line, config, MathTex, DR, DL

from qui_matematica.piano_cartesiano.punto import Punto

LINE_DISTANCE_RATIO = .5 * .7


class Retta(Line):
    pass


class RettaParallelaAsseY(Retta):

    def __init__(self, ascissa, nome=None, y_range=None, **kwargs):
        self.ascissa = ascissa
        self.nome = nome
        if y_range is None:
            y_range = np.array([-config["frame_y_radius"], config["frame_y_radius"]])
        super().__init__(start=[ascissa, y_range[1], 0], end=[ascissa, y_range[0], 0], **kwargs)

    def perpendicolare_per_punto(self, punto: Punto, nome=None, **kwargs):
        return RettaParallelaAsseX(punto.get_ordinata(), nome, **kwargs)

    def intersezione(self, retta: Retta, nome=None, **kwargs):
        if isinstance(retta, RettaParallelaAsseX):
            return Punto(self.get_ascissa(), retta.get_ordinata(), nome, **kwargs)
        else:
            return Punto(
                self.get_ascissa(),
                retta.get_coefficiente_angolare() * self.get_ascissa() + retta.get_ordinata_all_origine(),
                nome, **kwargs)

    def get_label(self):
        return MathTex(self.nome).next_to(self.get_start(), LINE_DISTANCE_RATIO * DL)

    def diventa(self, retta: "RettaParallelaAsseY"):
        self.nome = retta.nome
        self.ascissa = retta.ascissa
        self.become(retta)


class RettaEsplicita(Retta):

    def __init__(self, coefficiente_angolare, ordinata_all_origine, nome=None, x_range=None, **kwargs):
        self.nome = nome
        self.coefficiente_angolare = coefficiente_angolare
        self.ordinata_all_origine = ordinata_all_origine
        if x_range is None:
            x_range = np.array([-config["frame_x_radius"], config["frame_x_radius"]])
        start = [x_range[0], coefficiente_angolare * x_range[0] + ordinata_all_origine, 0]
        end = [x_range[1], coefficiente_angolare * x_range[1] + ordinata_all_origine, 0]
        super().__init__(start=start, end=end, **kwargs)

    def diventa(self, retta: "RettaEsplicita"):
        self.nome = retta.nome
        self.coefficiente_angolare = retta.coefficiente_angolare
        self.ordinata_all_origine = retta.ordinata_all_origine
        self.become(retta)


class RettaParallelaAsseX(RettaEsplicita):

    def __init__(self, ordinata, nome=None, x_range=None, **kwargs):
        self.ordinata = ordinata
        super().__init__(0, ordinata, nome=nome, x_range=x_range, **kwargs)

    def perpendicolare_per_punto(self, punto: Punto, nome=None, **kwargs):
        return RettaParallelaAsseY(punto.get_ascissa(), nome, **kwargs)

    def intersezione(self, retta: Retta, nome=None, **kwargs):
        if isinstance(retta, RettaParallelaAsseY):
            return Punto(retta.get_ascissa(), self.get_ordinata(), nome, **kwargs)
        else:
            raise NotImplementedError

    def get_label(self):
        return MathTex(self.nome, color=self.get_color()).next_to(self.get_start(), LINE_DISTANCE_RATIO * DR)


def retta_per_due_punti(punto_a: Punto, punto_b: Punto):
    coefficiente_angolare = (punto_a.get_ordinata() - punto_b.get_ordinata()) / (punto_a.get_ascissa() - punto_b.get_ascissa())
    ordinata_all_origine = punto_a.get_ordinata() - coefficiente_angolare * punto_a.get_ascissa()
    return RettaEsplicita(coefficiente_angolare, ordinata_all_origine)