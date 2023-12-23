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
        self.add(v2)

        self.add(v1)
        self.cut_and_wait()

        calcolo_velocita_relativa = Tex("$v_1$ = 45 - 20 = 25 km/h").add_background_rectangle(opacity=.9, buff=.5)
        self.play(Write(calcolo_velocita_relativa))
        self.play(Circumscribe(calcolo_velocita_relativa))
        self.cut_and_wait()

        v1_corretto = Tex("$v_2$ = 25 km/h").scale(SCALE_IN_BOXES).next_to(label_blu, DOWN, buff=1)
        self.play(Transform(v1, v1_corretto), FadeOut(calcolo_velocita_relativa))
        self.cut_and_wait()

        timer = ValueTracker(0)

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

        # def get_orologio():
        #     seconds = int(timer.get_value())
        #     minutes = seconds / 60
        #     seconds = seconds % 60
        #
        #     seconds_filled = str(seconds).zfill(2)
        #
        #     return Tex("%d min, %s s" % (minutes, seconds_filled)).shift(3 * OUT)
        #
        # orologio = get_orologio()
        #
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

        self.play(timer.animate.set_value(72), run_time=3, rate_func=linear)

        # orologio.clear_updaters()
        pista.clear_updaters()
        blu.clear_updaters()
        giallo.clear_updaters()
        s1.clear_updaters()
        s2.clear_updaters()
        n1.clear_updaters()
        n2.clear_updaters()
        self.cut_and_wait()

        self.play(Circumscribe(s1))
        self.cut_and_wait()

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

        self.play(timer.animate.set_value(216), run_time=6, rate_func=linear)

        # orologio.clear_updaters()
        pista.clear_updaters()
        blu.clear_updaters()
        giallo.clear_updaters()
        s1.clear_updaters()
        s2.clear_updaters()
        n1.clear_updaters()
        n2.clear_updaters()
        self.cut_and_wait()

        self.play(Circumscribe(s1))
        self.cut_and_wait()

        formula_s = MathTex(r"s = v \cdot t").add_background_rectangle(buff=.5)
        self.play(Write(formula_s))
        self.play(Circumscribe(formula_s))
        self.cut_and_wait()

        formula_t = MathTex(r"t = \dfrac{s}{v}").add_background_rectangle(buff=.5)
        self.play(Transform(formula_s, formula_t))
        self.play(Circumscribe(formula_s))
        self.cut_and_wait()

        formula_t_2 = MathTex(r"t = \dfrac{1,5}{25}").add_background_rectangle(buff=.5)
        self.play(Transform(formula_s, formula_t_2))
        self.play(Circumscribe(formula_s))
        self.cut_and_wait()

        formula_t_3 = MathTex(r"t = \dfrac{3}{50}").add_background_rectangle(buff=.5)
        self.play(Transform(formula_s, formula_t_3))
        self.play(Circumscribe(formula_s))
        self.cut_and_wait()

        formula_t_4 = MathTex(r"t = \dfrac{3}{50} \text{h}").add_background_rectangle(buff=.5)
        self.play(Transform(formula_s, formula_t_4))
        self.play(Circumscribe(formula_s))
        self.cut_and_wait()

        self.wait(30)
