from manim import *

from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX
from qui_matematica.piano_cartesiano.segmento import Segmento, CongruenzaSegmenti

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        fuoco = Punto(0, 0, nome="F")
        direttrice = RettaParallelaAsseX(-2, nome="d")

        asse = direttrice.perpendicolare_per_punto(fuoco, nome="a", color=WHITE)

        punto_d = direttrice.intersezione(asse, nome="D")
        vertice = Segmento(fuoco, punto_d).punto_medio(nome="V", color=YELLOW)

        legenda = VGroup(
            Tex("$F$: fuoco"),
            Tex("$d$: direttrice"),
            Tex("$a$: asse"),
            Tex("$V$: vertice")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DR)

        self.play(Create(fuoco))
        self.play(Write(fuoco.get_label()))

        self.play(Write(legenda[0]))

        self.play(Create(direttrice))
        self.play(Write(direttrice.get_label()))

        self.play(Write(legenda[1]))

        self.cut_and_wait()

        self.play(Create(asse))
        self.play(Write(asse.get_label()))

        self.play(Write(legenda[2]))

        self.cut_and_wait()

        self.play(Create(punto_d))
        self.play(Write(punto_d.get_label()))

        self.cut_and_wait()

        self.play(Create(vertice))
        self.play(Write(vertice.get_label()))

        self.play(Write(legenda[3]))

        self.cut_and_wait()

        congruenza = CongruenzaSegmenti(Segmento(fuoco, vertice), Segmento(vertice, punto_d), "//", color=RED)
        self.play(Write(congruenza))

        self.cut_and_wait()

        self.play(FadeOut(congruenza), FadeOut(legenda))

        self.cut_and_wait()

        h_point = Punto(punto_d.get_ascissa(), punto_d.get_ordinata(), "H", color=RED)
        h_point_label = h_point.get_label()

        self.play(Create(h_point), Write(h_point_label))

        h_point.add_updater(lambda point: point.sposta_in(6 * np.sin(tracker.get_value()), point.get_ordinata()))
        h_point_label.add_updater(lambda label: label.move_to(h_point.get_label().get_center()))

        tracker = ValueTracker()

        self.play(tracker.animate.set_value(9), run_time=5, rate_func=linear)
        self.cut_and_wait()

        h_point.clear_updaters()
        h_point_label.clear_updaters()

        # Costruzione LUNGA START

        fh = Segmento(fuoco, h_point, color=RED, z_index=-1)
        self.play(Create(fh))
        self.cut_and_wait()

        m_point = fh.punto_medio(nome="M", color=RED)
        m_point_label = m_point.get_label()
        self.play(Create(m_point), Write(m_point_label))
        self.cut_and_wait()

        pm = fh.asse(color=RED, z_index=-1)
        self.play(Create(pm))
        self.cut_and_wait()

        ph = direttrice.perpendicolare_per_punto(h_point, color=RED, z_index=-1)
        self.play(Create(ph))
        self.cut_and_wait()

        p_point = ph.intersezione(pm, "P", color=YELLOW, z_index=10)
        p_point_label = p_point.get_label()
        self.play(Create(p_point), Write(p_point_label))

        pf = Segmento(fuoco, p_point, color=RED, z_index=-1)
        self.play(Create(pf))
        self.cut_and_wait()

        # Costruzione LUNGA END

        triangolo_fmp = Polygon(fuoco.get_center(), m_point.get_center(), p_point.get_center(), fill_color=GREEN, fill_opacity=1, z_index=-20)
        triangolo_hmp = Polygon(h_point.get_center(), m_point.get_center(), p_point.get_center(), fill_color=BLUE, fill_opacity=1, z_index=-20)
        self.play(Create(triangolo_fmp), Create(triangolo_hmp))
        self.cut_and_wait()

        angolo_retto_1 = RightAngle(pm, fh, color=RED, length=0.3, quadrant=(1, -1))
        angolo_retto_2 = RightAngle(pm, fh, color=RED, length=0.3, quadrant=(1, 1))
        self.play(Create(angolo_retto_1), Create(angolo_retto_2))
        self.cut_and_wait()

        congruenza_cateti = CongruenzaSegmenti(
            Segmento(fuoco, m_point), Segmento(m_point, h_point), "/", color=RED)
        self.play(Write(congruenza_cateti))
        self.cut_and_wait()

        congruenza = CongruenzaSegmenti(pf, Segmento(p_point, h_point), "//", color=RED)
        self.play(Write(congruenza))
        self.cut_and_wait()

        self.play(FadeOut(congruenza), FadeOut(congruenza_cateti), FadeOut(angolo_retto_1), FadeOut(angolo_retto_2),
                  FadeOut(triangolo_fmp), FadeOut(triangolo_hmp))
        self.cut_and_wait()

        # Mega animazione START

        self.para_min = h_point.get_center()[0]
        self.para_max = h_point.get_center()[0]

        parabola = FunctionGraph(
            lambda t: (t ** 2 - direttrice.get_ordinata() ** 2 - fuoco.get_ascissa() ** 2) / (
                        2 * fuoco.get_ascissa() - 2 * direttrice.get_ordinata()),
            color=YELLOW,
            x_range=[self.para_min, self.para_max]
        )
        self.add(parabola)

        def update_parabola(old):
            x_h = 6 * np.sin(tracker.get_value())
            if x_h < self.para_min:
                self.para_min = x_h
            if x_h > self.para_max:
                self.para_max = x_h
            old.become(FunctionGraph(
                lambda t: (t ** 2 - direttrice.get_ordinata() ** 2 - fuoco.get_ascissa() ** 2) / (
                            2 * fuoco.get_ascissa() - 2 * direttrice.get_ordinata()),
                color=YELLOW,
                x_range=[self.para_min, self.para_max]
            ))

        h_point.add_updater(lambda point: point.sposta_in(6 * np.sin(tracker.get_value()), point.get_ordinata()))
        h_point_label.add_updater(lambda label: label.move_to(h_point.get_label().get_center()))
        fh.add_updater(lambda old: old.become(Segmento(fuoco, h_point, color=RED, z_index=-1)))
        m_point.add_updater(lambda old: old.move_to(fh.punto_medio().get_center()))
        m_point_label.add_updater(lambda label: label.move_to(m_point.get_label().get_center()))
        pm.add_updater(lambda old: old.diventa(fh.asse(color=RED, z_index=-1)))
        ph.add_updater(lambda old: old.diventa(direttrice.perpendicolare_per_punto(h_point, color=RED, z_index=-1)))
        p_point.add_updater(lambda old: old.move_to(ph.intersezione(pm).get_center()))
        p_point_label.add_updater(lambda old: old.move_to(p_point.get_label().get_center()))
        pf.add_updater(lambda old: old.become(Segmento(fuoco, p_point, color=RED, z_index=-1)))

        parabola.add_updater(lambda old: update_parabola(old))

        self.play(tracker.animate.set_value(15.3), run_time=5, rate_func=linear)

        # Mega animazione END

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
