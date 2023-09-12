from manim import Line, VGroup, Tex, RED

from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaEsplicita


class Segmento(Line):

    def __init__(self, punto_a: Punto, punto_b: Punto, **kwargs):
        self.punto_a = punto_a
        self.punto_b = punto_b
        super().__init__(start=punto_a.get_center(), end=punto_b.get_center(), **kwargs)

    def punto_medio(self, nome=None, **kwargs):
        punto = (self.punto_a.get_center() + self.punto_b.get_center()) / 2
        return Punto(punto[0], punto[1], nome, **kwargs)

    def asse(self, **kwargs):
        m_asse = (self.punto_a.get_ascissa() - self.punto_b.get_ascissa()) / (self.punto_b.get_ordinata() - self.punto_a.get_ordinata())
        punto_m = self.punto_medio()
        q_asse = - m_asse * punto_m.get_ascissa() + punto_m.get_ordinata()
        return RettaEsplicita(m_asse, q_asse, **kwargs)


class CongruenzaSegmenti(VGroup):

    def __init__(self, segmento_a: Segmento, segmento_b: Segmento, simbolo: str, **kwargs):
        super().__init__()
        segno_a = Tex(simbolo, **kwargs).scale(.5)
        segno_b = segno_a.copy()
        segno_a.rotate(segmento_a.get_angle()).move_to(segmento_a.get_center())
        segno_b.rotate(segmento_b.get_angle()).move_to(segmento_b.get_center())
        self.add(segno_a, segno_b)
