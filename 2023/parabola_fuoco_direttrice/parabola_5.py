from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX, retta_per_due_punti
from qui_matematica.piano_cartesiano.segmento import Segmento

DELAY = 30


class PuntoSuParabola:

    def __init__(self, x_punto, y_punto, m_punto):
        self.x_punto = x_punto
        self.y_punto = y_punto
        self.m_punto = m_punto
        self.angolo_punto = np.arctan(m_punto)

    def get_point(self):
        return [self.x_punto, self.y_punto, 0]


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        colore_incidente = YELLOW
        colore_riflesso = RED
        colore_parabola = GREEN
        colore_angolo = BLUE

        y_direttrice = -3

        fuoco = Punto(0, 0, nome="F")
        direttrice = RettaParallelaAsseX(y_direttrice, nome="d")

        legenda = VGroup(
            Tex("$F$: fuoco"),
            Tex("$d$: direttrice"),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DR)

        # self.play(Create(fuoco))
        # self.play(Write(fuoco.get_label()))
        # self.play(Write(legenda[0]))
        # self.cut_and_wait()

        # self.play(Create(direttrice))
        # self.play(Write(direttrice.get_label()))
        # self.play(Write(legenda[1]))
        # self.cut_and_wait()

        x_range = [-2, 2]

        parabola = ParabolaDaFuocoEDirettrice(fuoco, direttrice, color=colore_parabola, x_range=x_range)

        # self.play(Create(parabola))
        # self.cut_and_wait()

        x_punto = 1.05
        y_punto = parabola.get_ordinata_parabola(x_punto)
        m_punto = parabola.get_derivata(x_punto)
        punto = Punto(x_punto, y_punto, nome="P", color=colore_parabola)

        retta = Line(start=[-2, m_punto*(-2 - x_punto) + y_punto, 0],
                     end=[2, m_punto*(2 - x_punto) + y_punto, 0],
                     color=colore_parabola)
        self.play(Create(retta))
        self.cut_and_wait()

        incidente = Segmento(Punto(x_punto, 4), punto, color=colore_incidente)
        m_riflesso = np.tan(2 * np.arctan(m_punto) + PI - incidente.get_angle())
        punto_a_sinistra = Punto(-8, m_riflesso * (-8 - x_punto) + y_punto)
        riflessa = Segmento(punto, punto_a_sinistra, color=colore_riflesso)

        self.play(Create(VGroup(incidente, riflessa)), rate_functions=linear)
        self.cut_and_wait()

        # angolo1 = Arc(radius=.4,
        #               start_angle=retta.get_angle(),
        #               angle=incidente.get_angle() - retta.get_angle() + PI,
        #               arc_center=punto.get_center())
        # angolo2 = Arc(radius=.4,
        #               start_angle=riflessa.get_angle(),
        #               angle=retta.get_angle() - riflessa.get_angle() + PI,
        #               arc_center=punto.get_center())
        angolo1 = AnnularSector(inner_radius=0,
                                outer_radius=.4,
                                start_angle=retta.get_angle(),
                                angle=incidente.get_angle() - retta.get_angle() + PI,
                                arc_center=punto.get_center(),
                                fill_opacity=.6,
                                fill_color=colore_angolo,
                                color=colore_angolo,
                                z_index=-1)
        angolo2 = angolo1.copy()
        self.play(Create(angolo1))
        self.add(angolo2)
        self.play(Rotate(angolo2, angle=- incidente.get_angle() + retta.get_angle(), about_point=punto.get_center()))
        self.cut_and_wait()

        self.play(FadeOut(angolo1), FadeOut(angolo2), FadeOut(incidente), FadeOut(riflessa))

        angolo1 = AnnularSector(inner_radius=0,
                                outer_radius=.4,
                                start_angle=-PI/6,
                                angle=incidente.get_angle() + PI + PI/6,
                                arc_center=punto.get_center(),
                                fill_opacity=.6,
                                fill_color=colore_angolo,
                                color=colore_angolo,
                                z_index=-1)
        question_mark = Tex("?", color=colore_angolo).move_to(angolo1)

        self.play(Transform(retta, parabola), run_time=3, rate_functions=linear)
        self.play(Create(incidente))
        self.play(Create(angolo1))
        self.play(Transform(angolo1, question_mark))
        self.cut_and_wait()

        self.play(FadeOut(angolo1), FadeOut(incidente))

        # Cambio punto P

        x_punto = 1.75
        y_punto = parabola.get_ordinata_parabola(x_punto)
        m_punto = parabola.get_derivata(x_punto)
        punto = Punto(x_punto, y_punto, nome="P", color=colore_parabola)

        incidente = Segmento(Punto(x_punto, 4), punto, color=colore_incidente)

        punto_h = Punto(x_punto, y_direttrice, nome="H")

        self.play(Create(incidente))
        self.cut_and_wait()

        self.play(Create(punto), Write(punto.get_label()))
        self.cut_and_wait()

        segmento_fh = Segmento(fuoco, punto_h)
        asse_fh = segmento_fh.asse(color=colore_angolo)
        punto_m = segmento_fh.punto_medio(nome="M")
        self.play(Create(asse_fh))
        self.cut_and_wait()

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(punto).scale(1/10))
        self.cut_and_wait()

        self.play(Restore(self.camera.frame), FadeOut(asse_fh))
        self.cut_and_wait()

        prolungamento_incidente = DashedLine(start=punto.get_center(),
                                             end=punto_h.get_center(),
                                             color=colore_incidente)

        self.play(Create(fuoco), Write(fuoco.get_label()))
        self.play(Create(direttrice), Write(direttrice.get_label()))
        self.play(Create(prolungamento_incidente))
        self.cut_and_wait()

        self.play(Create(punto_h), Write(punto_h.get_label()))
        self.cut_and_wait()

        self.play(Create(segmento_fh))
        self.play(Create(punto_m), Write(punto_m.get_label()))
        self.play(Create(asse_fh))
        self.play(Create(RightAngle(asse_fh, segmento_fh, length=0.3, quadrant=(-1, -1))))
        self.cut_and_wait()

        retta_fp = retta_per_due_punti(fuoco, punto)
        self.play(Create(retta_fp))
        self.cut_and_wait()

        angolo1 = AnnularSector(inner_radius=0,
                                outer_radius=.4,
                                start_angle=retta_fp.get_angle(),
                                angle=incidente.get_angle() - retta_fp.get_angle() + PI,
                                arc_center=punto.get_center(),
                                fill_opacity=.6,
                                fill_color=colore_angolo,
                                color=colore_angolo,
                                z_index=-1)
        angolo2 = angolo1.copy()
        self.play(Create(angolo1))
        self.add(angolo2)
        self.play(Rotate(angolo2, angle=PI, about_point=punto.get_center()))
        self.cut_and_wait()

        angolo3 = AnnularSector(inner_radius=0,
                                outer_radius=.4,
                                start_angle=asse_fh.get_angle(),
                                angle=incidente.get_angle() - asse_fh.get_angle() + PI,
                                arc_center=punto.get_center(),
                                fill_opacity=.6,
                                fill_color=colore_angolo,
                                color=colore_angolo,
                                z_index=-1)

        angolo4 = AnnularSector(inner_radius=0,
                                outer_radius=.4,
                                start_angle=retta_fp.get_angle() + PI,
                                angle=asse_fh.get_angle() - retta_fp.get_angle(),
                                arc_center=punto.get_center(),
                                fill_opacity=.6,
                                fill_color=colore_angolo,
                                color=colore_angolo,
                                z_index=-1)

        self.play(Transform(angolo1, angolo3), Transform(angolo2, angolo4))

        self.wait(30)
