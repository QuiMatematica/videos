from manim import *

from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX
from qui_matematica.piano_cartesiano.segmento import Segmento

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        fuoco = Punto(0, 0, nome="F")
        direttrice = RettaParallelaAsseX(-2, nome="d")

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

        parabola = FunctionGraph(
            lambda t: (t ** 2 - direttrice.get_ordinata() ** 2 - fuoco.get_ascissa() ** 2) / (
                    2 * fuoco.get_ascissa() - 2 * direttrice.get_ordinata()),
            color=YELLOW
        )
        self.play(Create(parabola))
        self.cut_and_wait()

        p = Punto(-10, 10).set_color(ORANGE)
        pf = Segmento(p, fuoco, color=ORANGE)
        vert = direttrice.perpendicolare_per_punto(p)
        h = vert.intersezione(direttrice)
        ph = Segmento(p, h, color=ORANGE)

        self.add(p)
        self.add(pf)
        self.add(ph)

        def update_ph(old):
            _vert = direttrice.perpendicolare_per_punto(p)
            _h = _vert.intersezione(direttrice)
            old.become(Segmento(p, _h, color=ORANGE))

        pf.add_updater(lambda old: old.become(Segmento(p, fuoco, color=ORANGE)))
        ph.add_updater(lambda old: update_ph(old))

        self.play(MoveAlongPath(p, parabola), run_time=5, rate_functions=linear)
        self.remove(p, pf, ph)

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
