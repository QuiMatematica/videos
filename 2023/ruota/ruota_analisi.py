import math

from manim import *

from ruota import Ruota

DELAY = 30

DIAMETRO_COLOR = RED


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        raggio = 4 / PI
        diametro = raggio * 2

        delta_tempo = 10
        delta_spazio = 8
        start_spazio = - delta_spazio / 2

        timer = ValueTracker(0)

        def get_posizione():
            return ((delta_spazio / delta_tempo) * timer.get_value() + start_spazio) * RIGHT + 2 * UP

        start = get_posizione()

        ruota = Ruota().scale_to_fit_width(diametro).move_to(start)

        self.play(FadeIn(ruota))
        self.cut_and_wait()

        def get_spazio():
            return Arrow(start=start, end=get_posizione(), buff=0, color=YELLOW)

        def get_rotazione():
            return (delta_spazio / delta_tempo) * timer.get_value() / raggio

        def get_raggio():
            return Line(
                start=ruota.get_center(),
                end=raggio * math.sin(get_rotazione()) * LEFT + raggio * math.cos(
                    get_rotazione()) * DOWN + ruota.get_center(),
                color=RED
            )

        def get_circonferenza_svolta():
            return Line(
                start=start + raggio * DOWN,
                end=get_posizione() + raggio * DOWN,
                color=RED
            )

        def get_circonferenza_da_svolgere():
            return Arc(
                arc_center=get_posizione(),
                radius=raggio,
                start_angle=- get_rotazione() - PI / 2,
                angle=- 2 * PI + get_rotazione(),
                color=RED
            )

        raggio_linea = get_raggio()
        self.play(Create(raggio_linea))

        spazio = get_spazio()
        self.add(spazio)

        circonferenza_svolta = get_circonferenza_svolta()
        self.add(circonferenza_svolta)

        circonferenza_da_svolgere = get_circonferenza_da_svolgere()
        self.play(Create(circonferenza_da_svolgere))

        ruota.add_updater(
            lambda _r: _r.move_to(get_posizione()).rotate_to(- get_rotazione())
        )
        spazio.add_updater(
            lambda _s: _s.become(get_spazio())
        )
        raggio_linea.add_updater(
            lambda _r: _r.become(get_raggio())
        )
        circonferenza_svolta.add_updater(
            lambda _r: _r.become(get_circonferenza_svolta())
        )
        circonferenza_da_svolgere.add_updater(
            lambda old: old.become(get_circonferenza_da_svolgere())
        )

        self.play(timer.animate.set_value(delta_tempo), run_time=5, rate_func=linear)
        self.cut_and_wait()

        ruota.clear_updaters()
        spazio.clear_updaters()
        raggio_linea.clear_updaters()
        circonferenza_svolta.clear_updaters()
        circonferenza_da_svolgere.clear_updaters()

        spazio_label = MathTex("s", color=YELLOW).next_to(spazio, UP)
        self.play(Write(spazio_label))
        self.cut_and_wait()

        circonferenza_label = MathTex(r"2 {{ \pi }} r", color=RED).next_to(circonferenza_svolta, UP)
        self.play(Write(circonferenza_label))
        self.cut_and_wait()

        circonferenza_label_2 = MathTex(r"{{ \pi }} d", color=RED).next_to(circonferenza_svolta, UP)
        self.play(TransformMatchingTex(circonferenza_label, circonferenza_label_2))
        self.cut_and_wait()

        dato_1 = Tex("10 giri in un secondo")
        dato_2 = MathTex(r"t = 0,1 \text{ s}")
        dato_3 = MathTex(r"d = 60 \text{ cm}")
        VGroup(dato_1, dato_2, dato_3).arrange(DOWN).shift(4 * LEFT + 1 * DOWN)

        formula_1 = MathTex(r"{{ s }}  = {{ \pi d }}")
        formula_2 = MathTex(r"v = \dfrac{s}{t}")
        VGroup(formula_1, formula_2).arrange(DOWN).shift(4 * RIGHT + 1 * DOWN)

        spazio_label.target = formula_1[0]
        circonferenza_label_2.target = formula_1[2]
        self.play(MoveToTarget(spazio_label), MoveToTarget(circonferenza_label_2), FadeIn(formula_1[1]))
        self.cut_and_wait()

        self.play(Write(dato_1))
        self.cut_and_wait()

        self.play(Write(dato_2))
        self.cut_and_wait()

        self.play(Write(formula_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = \dfrac{\pi d}{t}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        self.play(Write(dato_3))
        self.cut_and_wait()

        dato_3_2 = MathTex(r"d = 0,60 \text{ m}").move_to(dato_3)
        self.play(Transform(dato_3, dato_3_2))
        formula_2_2 = MathTex(r"v = \dfrac{\pi \cdot 0,60 \text{ m}}{t}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = \dfrac{\pi \cdot 0,60 \text{ m}}{0,1 \text{ s}}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = \dfrac{3,14 \cdot 0,60 \text{ m}}{0,1 \text{ s}}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = \dfrac{3,14 \cdot 0,60}{0,1} \text{ m/s}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = \dfrac{3,14 \cdot 0,60}{0,1} \cdot 3,6 \text{ km/h}").move_to(formula_2)
        self.play(Transform(formula_2, formula_2_2))
        self.cut_and_wait()

        formula_2_2 = MathTex(r"v = {{ 3,14 }} \cdot {{ 0,60 }} \cdot {{ 10 }} \cdot {{ 3,6 }} \text{ km/h}").move_to(
            formula_2)
        self.play(ReplacementTransform(formula_2, formula_2_2))
        self.cut_and_wait()
        formula_2 = formula_2_2

        formula_2_2 = MathTex(r"v = {{ 3,14 }} \cdot {{ 0,60 }} \cdot {{ 36 }} \text{ km/h}").move_to(formula_2)
        self.play(TransformMatchingTex(formula_2, formula_2_2))
        self.cut_and_wait()
        formula_2 = formula_2_2

        formula_2_2 = MathTex(r"v = {{ 3,14 }} \cdot {{ 21,6 }} \text{ km/h}").move_to(formula_2)
        self.play(TransformMatchingTex(formula_2, formula_2_2))
        self.cut_and_wait()
        formula_2 = formula_2_2

        formula_2_2 = MathTex(r"v = {{ 3 }} \cdot {{ 22 }} \text{ km/h}").move_to(formula_2)
        self.play(TransformMatchingTex(formula_2, formula_2_2))
        self.cut_and_wait()
        formula_2 = formula_2_2

        formula_2_2 = MathTex(r"v = {{ 66 }} \text{ km/h}").move_to(formula_2)
        self.play(TransformMatchingTex(formula_2, formula_2_2))
        self.cut_and_wait()

        risposte = Tex(r"A) 8 km/h \quad B) 38 km/h \quad {{ C) 68 km/h }} \quad D) 108 km/h", color=GREEN).shift(
            3 * DOWN)
        self.play(Write(risposte))
        self.cut_and_wait()

        self.play(Create(SurroundingRectangle(risposte[1])))

        self.wait(30)
