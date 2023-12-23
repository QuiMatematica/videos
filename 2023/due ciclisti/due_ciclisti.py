from manim import *

from ciclista import CiclistaBlu, CiclistaGiallo
from pista import Pista

DELAY = 30

LEN_PISTA_METRI = 500
RAGGIO_PISTA_METRI = 500 / (2 * PI)

VEL_PISTA_MS = -20 / 3.6
VEL_ANGOLARE_PISTA = VEL_PISTA_MS / RAGGIO_PISTA_METRI

VEL_BLU_MS = 45 / 3.6
VEL_ANGOLARE_BLU = VEL_BLU_MS / RAGGIO_PISTA_METRI

VEL_GIALLO_MS = 20 / 3.6
VEL_ANGOLARE_GIALLO = VEL_GIALLO_MS / RAGGIO_PISTA_METRI

TEMPO_MAX_SECS = 216


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        pista = Pista()
        self.add(pista)

        blu = CiclistaBlu(pista)
        self.add(blu)

        giallo = CiclistaGiallo(pista)
        self.add(giallo)

        timer = ValueTracker(0)

        def get_orologio():
            seconds = int(timer.get_value())
            minutes = seconds / 60
            seconds = seconds % 60

            seconds_filled = str(seconds).zfill(2)

            return Tex("%d min, %s s" % (minutes, seconds_filled)).shift(3 * OUT)

        orologio = get_orologio()
        self.play(Write(orologio))

        orologio.add_updater(
            lambda old: old.become(get_orologio())
        )
        pista.add_updater(
            lambda _p: _p.rotate_to(VEL_ANGOLARE_PISTA * timer.get_value())
        )
        blu.add_updater(
            lambda _p: _p.rotate_to(VEL_ANGOLARE_BLU * timer.get_value())
        )
        giallo.add_updater(
            lambda _p: _p.rotate_to(VEL_ANGOLARE_GIALLO * timer.get_value())
        )

        self.play(timer.animate.set_value(TEMPO_MAX_SECS), run_time=5, rate_func=linear)

        orologio.clear_updaters()
        pista.clear_updaters()
        blu.clear_updaters()
        giallo.clear_updaters()

        self.wait(30)
