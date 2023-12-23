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

        H_SHIFT = 5.5
        BOX_W = 3
        LABEL_V_SHIFT = 1.5

        box_blu = Rectangle(width=BOX_W, height=5, color=BLUE).shift(H_SHIFT * LEFT)
        label_blu = ImageMobject(
            '../../img/omini/ciclista_blu.png').scale(.1).shift(H_SHIFT * LEFT + LABEL_V_SHIFT * UP)

        self.add(box_blu, label_blu)

        self.add(pista)

        self.add(blu)

        SCALE_IN_BOXES = .8

        v1 = Tex("$v_1$ = 45 km/h").scale(SCALE_IN_BOXES).next_to(label_blu, DOWN, buff=1)

        self.play(Write(v1))
        self.play(Circumscribe(v1))
        self.cut_and_wait()

        box_t = MathTex(r"t = \dfrac{3}{50} \text{h}").move_to(H_SHIFT * RIGHT + 2 * UP)
        self.play(Write(box_t))
        self.play(Circumscribe(box_t))
        self.cut_and_wait()

        formula_s_1 = MathTex(r"s = v \cdot t").next_to(box_t, DOWN, buff=1)
        self.play(Write(formula_s_1))
        self.play(Circumscribe(formula_s_1))
        self.cut_and_wait()

        formula_s_2 = MathTex(r"s = 45 \cdot \dfrac{3}{50}").move_to(formula_s_1)
        self.play(Transform(formula_s_1, formula_s_2))
        self.play(Circumscribe(formula_s_1))
        self.cut_and_wait()

        formula_s_3 = MathTex(r"s = 2,7 \text{km}").move_to(formula_s_1)
        self.play(Transform(formula_s_1, formula_s_3))
        self.play(Circumscribe(formula_s_1))
        self.cut_and_wait()

        formula_giri = MathTex(r"\text{giri} = \dfrac{2,7}{0,5}").next_to(formula_s_1, DOWN, buff=1)
        self.play(Write(formula_giri))
        self.play(Circumscribe(formula_giri))
        self.cut_and_wait()

        formula_giri_2 = MathTex(r"\text{giri} = 5,4").move_to(formula_giri)
        self.play(Transform(formula_giri, formula_giri_2))
        self.play(Circumscribe(formula_giri))
        self.cut_and_wait()

        timer = ValueTracker(0)

        def get_s1():
            _s = VEL_BLU_MS * timer.get_value()
            return Tex("$s_1$ = %d m" % _s).scale(SCALE_IN_BOXES).next_to(v1, DOWN)

        s1 = get_s1()

        def get_n1():
            _n = VEL_BLU_MS * timer.get_value() / 500
            return Tex("giri$_1$ = %d" % _n).scale(SCALE_IN_BOXES).next_to(s1, DOWN)

        n1 = get_n1()

        self.play(Write(VGroup(s1, n1)))
        self.cut_and_wait()

        pista.add_updater(
            lambda _p: _p.rotate_to(VEL_ANGOLARE_PISTA * timer.get_value())
        )
        blu.add_updater(
            lambda _p: _p.rotate_to(VEL_ANGOLARE_BLU * timer.get_value())
        )
        s1.add_updater(
            lambda old: old.become(get_s1())
        )
        n1.add_updater(
            lambda old: old.become(get_n1())
        )

        self.play(timer.animate.set_value(216), run_time=5, rate_func=linear)

        pista.clear_updaters()
        blu.clear_updaters()
        s1.clear_updaters()
        n1.clear_updaters()
        self.cut_and_wait()

        self.play(Circumscribe(n1))
        self.cut_and_wait()

        conclusione = Tex("Durante il sesto giro.", color=YELLOW).add_background_rectangle(buff=1)
        self.play(Write(conclusione))

        self.wait(30)
