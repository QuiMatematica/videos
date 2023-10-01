from manim import FunctionGraph

from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX, RettaParallelaAsseY


class Parabola(FunctionGraph):

    def __init__(self, par_a, par_b, par_c, **kwargs):
        self.par_a = par_a
        self.par_b = par_b
        self.par_c = par_c
        super().__init__(lambda x: self.get_ordinata_parabola(x), **kwargs)

    def get_ordinata_parabola(self, _x):
        return self.par_a * (_x ** 2) + self.par_b * _x + self.par_c

    def get_derivata(self, _x):
        return 2 * self.par_a * _x + self.par_b


class ParabolaDaFuocoEDirettrice(Parabola):

    def __init__(self, fuoco: Punto, direttrice: RettaParallelaAsseX, **kwargs):
        denominatore = 2 * fuoco.get_ordinata() - 2 * direttrice.get_ordinata()
        par_a = 1 / denominatore
        par_b = -2 * fuoco.get_ascissa() / denominatore
        par_c = (fuoco.get_ascissa() ** 2 + fuoco.get_ordinata() ** 2 - direttrice.get_ordinata() ** 2) / denominatore
        super().__init__(par_a, par_b, par_c, **kwargs)
