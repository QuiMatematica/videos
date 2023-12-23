from manim import *

from ciclista import CiclistaBlu, CiclistaGiallo
from pista import Pista

DELAY = 60

LEN_PISTA_METRI = 500
RAGGIO_PISTA_METRI = 500 / (2 * PI)

VEL_PISTA_MS = 0 / 3.6
VEL_ANGOLARE_PISTA = VEL_PISTA_MS / RAGGIO_PISTA_METRI

VEL_BLU_MS = 45 / 3.6
VEL_ANGOLARE_BLU = VEL_BLU_MS / RAGGIO_PISTA_METRI

VEL_GIALLO_MS = 20 / 3.6
VEL_ANGOLARE_GIALLO = VEL_GIALLO_MS / RAGGIO_PISTA_METRI

TEMPO_MAX_SECS = 5000 / VEL_BLU_MS


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

        self.play(Create(box_blu), FadeIn(label_blu))
        self.play(Create(box_giallo), FadeIn(label_giallo))
        self.cut_and_wait()

        self.play(Create(pista))
        self.cut_and_wait()

        self.play(FadeIn(giallo), FadeIn(blu))
        self.cut_and_wait()

        timer = ValueTracker(0)

        def get_orologio():
            seconds = int(timer.get_value())
            minutes = seconds / 60
            seconds = seconds % 60

            seconds_filled = str(seconds).zfill(2)

            return Tex("%d min, %s s" % (minutes, seconds_filled)).shift(3 * OUT)

        orologio = get_orologio()

        SCALE_IN_BOXES = .8

        v1 = Tex("$v_1$ = 45 km/h").scale(SCALE_IN_BOXES).next_to(label_blu, DOWN, buff=1)
        self.play(Write(v1))
        self.cut_and_wait()

        v2 = Tex("$v_2$ = 20 km/h").scale(SCALE_IN_BOXES).next_to(label_giallo, DOWN, buff=1)
        self.play(Write(v2))
        self.cut_and_wait()

        def get_s1():
            _s = VEL_BLU_MS * timer.get_value()
            return Tex("$s_1$ = %d m" % _s).scale(SCALE_IN_BOXES).next_to(v1, DOWN)

        def get_s2():
            _s = VEL_GIALLO_MS * timer.get_value()
            return Tex("$s_2$ = %d m" % _s).scale(SCALE_IN_BOXES).next_to(v2, DOWN)

        s1 = get_s1()
        s2 = get_s2()

        def get_n1():
            _n = VEL_BLU_MS * timer.get_value() / 500
            return Tex("giri$_1$ = %d" % _n).scale(SCALE_IN_BOXES).next_to(s1, DOWN)

        def get_n2():
            _n = VEL_GIALLO_MS * timer.get_value() / 500
            return Tex("giri$_2$ = %d" % _n).scale(SCALE_IN_BOXES).next_to(s2, DOWN)

        n1 = get_n1()
        n2 = get_n2()

        self.play(Write(VGroup(s1, n1, s2, n2)))
        self.cut_and_wait()

        self.play(Create(orologio))

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
        s1.add_updater(
            lambda old: old.become(get_s1())
        )
        s2.add_updater(
            lambda old: old.become(get_s2())
        )
        n1.add_updater(
            lambda old: old.become(get_n1())
        )
        n2.add_updater(
            lambda old: old.become(get_n2())
        )

        self.play(timer.animate.set_value(TEMPO_MAX_SECS), run_time=10, rate_func=linear)

        orologio.clear_updaters()
        pista.clear_updaters()
        blu.clear_updaters()
        giallo.clear_updaters()

        self.wait(30)
