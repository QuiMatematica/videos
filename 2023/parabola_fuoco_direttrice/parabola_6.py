from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX

DELAY = 0


class PuntoSuParabola:

    def __init__(self, x_punto, y_punto, m_punto):
        self.x_punto = x_punto
        self.y_punto = y_punto
        self.m_punto = m_punto
        self.angolo_punto = np.arctan(m_punto)

    def get_point(self):
        return [self.x_punto, self.y_punto, 0]


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        colore_incidente = YELLOW
        colore_riflesso = RED
        colore_parabola = GREEN

        fuoco = Punto(0, 0, nome="F")
        direttrice = RettaParallelaAsseX(-3, nome="d")

        legenda = VGroup(
            Tex("$F$: fuoco"),
            Tex("$d$: direttrice"),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DR)

        self.play(Create(fuoco))
        self.play(Write(fuoco.get_label()))
        self.play(Write(legenda[0]))

        self.cut_and_wait()

        self.play(Create(direttrice))
        self.play(Write(direttrice.get_label()))
        self.play(Write(legenda[1]))

        self.cut_and_wait()

        parabola = ParabolaDaFuocoEDirettrice(fuoco, direttrice, color=colore_parabola, x_range=[-2, 2])

        self.play(Create(parabola))
        self.cut_and_wait()

        def get_punto_su_parabola(_x_punto):
            _y_punto = parabola.get_ordinata_parabola(_x_punto)
            _m_punto = parabola.get_derivata(_x_punto)
            return PuntoSuParabola(_x_punto, _y_punto, _m_punto)

        punti = []
        for _i in range(6):
            x_punto = _i*.7 - 1.75
            punti.append(get_punto_su_parabola(x_punto))

        reciproco_di_m = 0

        def ascissa_in_alto(_punto, _reciproco_di_m):
            return _punto.x_punto + _reciproco_di_m * (4 - _punto.y_punto)

        def get_linea(_punto):
            punto_in_alto1 = Punto(ascissa_in_alto(_punto, reciproco_di_m), 4)
            linea1 = Line(start=punto_in_alto1.get_center(), end=_punto.get_point(), color=colore_incidente)
            m_riflesso = np.tan(2 * _punto.angolo_punto + PI - linea1.get_angle())
            punto_in_alto2 = Punto(ascissa_in_alto(_punto, 1 / m_riflesso), 4)
            linea2 = Line(start=_punto.get_point(), end=punto_in_alto2.get_center(), color=colore_riflesso)
            return VGroup(linea1, linea2)

        linee = []
        for _i in range(6):
            _punto = punti[_i]
            linee.append(get_linea(_punto))

        self.play(*[Create(line) for line in linee], run_time=3, rate_functions=linear)
        self.cut_and_wait()

        for _i in range(6):
            coppia = linee[_i]
            coppia.add_updater(lambda old: old.become(get_linea(get_punto_su_parabola(old[0].get_end()[0]))))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
