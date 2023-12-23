from manim import *

from ciclista import CiclistaBlu, CiclistaGiallo
from pista import Pista

DELAY = 60

LEN_PISTA_METRI = 500
RAGGIO_PISTA_METRI = 500 / (2 * PI)

VEL_PISTA_MS = -20 / 3.6
VEL_ANGOLARE_PISTA = VEL_PISTA_MS / RAGGIO_PISTA_METRI

VEL_BLU_MS = 25 / 3.6
VEL_ANGOLARE_BLU = VEL_BLU_MS / RAGGIO_PISTA_METRI

VEL_GIALLO_MS = 0 / 3.6
VEL_ANGOLARE_GIALLO = VEL_GIALLO_MS / RAGGIO_PISTA_METRI

TEMPO_MAX_SECS = 216


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        pista = Pista()

        blu = CiclistaBlu(pista)

        giallo = CiclistaGiallo(pista)

        H_SHIFT = 5.5
        BOX_W = 3
        LABEL_V_SHIFT = 1.5

        box_blu = Rectangle(width=BOX_W, height=5, color=BLUE).shift(H_SHIFT * LEFT)
        label_blu = ImageMobject(
            '../../img/omini/ciclista_blu.png').scale(.1).shift(H_SHIFT * LEFT + LABEL_V_SHIFT * UP)
        box_giallo = Rectangle(width=BOX_W, height=5, color=YELLOW).shift(H_SHIFT * RIGHT)
        label_giallo = ImageMobject(
            '../../img/omini/ciclista_giallo.png').scale(.1).shift(H_SHIFT * RIGHT + LABEL_V_SHIFT * UP)

        self.add(box_blu, label_blu)
        self.add(box_giallo, label_giallo)

        self.add(pista)

        self.add(giallo, blu)

        SCALE_IN_BOXES = .8

        v1 = Tex("$v_1$ = ? km/h").scale(SCALE_IN_BOXES).next_to(label_blu, DOWN, buff=1)

        v2 = Tex("$v_2$ = 0 km/h").scale(SCALE_IN_BOXES).next_to(label_giallo, DOWN, buff=1)
        self.play(Write(v2))
        self.cut_and_wait()

        self.play(Write(v1))
        self.cut_and_wait()

        timer = ValueTracker(0)

        def get_orologio():
            seconds = int(timer.get_value())
            minutes = seconds / 60
            seconds = seconds % 60

            seconds_filled = str(seconds).zfill(2)

            return Tex("%d min, %s s" % (minutes, seconds_filled)).shift(3 * OUT)

        orologio = get_orologio()

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
