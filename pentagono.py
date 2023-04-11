from manim import *

from qgeo import AngleWithArc

DELAY = 1
LEFT_CENTER = 3.5 * LEFT
RIGHT_CENTER = 3.5 * RIGHT
PENTAGONO_CENTER = LEFT_CENTER + .5 * UP
PENTAGONO_RADIUS = 2.4
RAGGIO_DOT = .6
PI_QUINTI = PI / 5


class Scene(MovingCameraScene):
    vertici = {}
    lettere_vertici = {}
    misure_angoli = {}

    def construct(self):
        self.wait(1)

        pentagono = RegularPolygon(n=5, fill_opacity=.2, fill_color=BLUE, z_index=-2).scale(PENTAGONO_RADIUS).shift(
            PENTAGONO_CENTER)
        vertici_pentagono = pentagono.get_vertices()
        self.vertici = {"a": vertici_pentagono[2],
                        "b": vertici_pentagono[3],
                        "c": vertici_pentagono[4],
                        "d": vertici_pentagono[0],
                        "e": vertici_pentagono[1]}

        self.misure_angoli["bac"] = Dot().move_to(
            Arc(radius=RAGGIO_DOT, start_angle=0, angle=PI_QUINTI, arc_center=self.vertici["a"]).get_center())
        self.misure_angoli["cad"] = Dot().move_to(
            Arc(radius=RAGGIO_DOT, start_angle=PI_QUINTI, angle=PI_QUINTI, arc_center=self.vertici["a"]).get_center())
        self.misure_angoli["bad"] = VGroup(self.misure_angoli["bac"], self.misure_angoli["cad"])

        self.misure_angoli["abe"] = Dot().move_to(
            Arc(radius=RAGGIO_DOT, start_angle=4 * PI_QUINTI, angle=PI_QUINTI,
                arc_center=self.vertici["b"]).get_center())
        self.misure_angoli["ebd"] = Dot().move_to(
            Arc(radius=RAGGIO_DOT, start_angle=3 * PI_QUINTI, angle=PI_QUINTI,
                arc_center=self.vertici["b"]).get_center())
        self.misure_angoli["abd"] = VGroup(self.misure_angoli["abe"], self.misure_angoli["ebd"])

        self.misure_angoli["adb"] = Dot().move_to(
            Arc(radius=RAGGIO_DOT, start_angle=7 * PI_QUINTI, angle=PI_QUINTI,
                arc_center=self.vertici["d"]).get_center())

        self.lettere_vertici = {"a": Tex('A').next_to(self.vertici["a"], DOWN, buff=.15),
                                "b": Tex('B').next_to(self.vertici["b"], DOWN, buff=.15),
                                "c": Tex('C').next_to(self.vertici["c"], RIGHT, buff=.15),
                                "d": Tex('D').next_to(self.vertici["d"], UP, buff=.15),
                                "e": Tex('E').next_to(self.vertici["e"], LEFT, buff=.15)}

        self.play(Create(pentagono))
        self.play(*[Write(x) for x in self.lettere_vertici.values()])
        self.wait(DELAY)
        self.next_section()

        angolo_piatto = self.disegna_angolo_piatto(center=RIGHT_CENTER)
        pi = MathTex(r"\pi").next_to(angolo_piatto[3], UP)
        self.play(Write(pi))
        self.wait(DELAY)
        self.next_section()

        self.play(FadeOut(angolo_piatto), FadeOut(pi))
        self.wait(DELAY)
        self.next_section()

        self.legenda_angoli()

        # angolo_abc = self.angoli_interni(vertici)
        #
        # self.angoli_esterni(vertici, angolo_abc)
        #
        # self.suddivisione_angolo(vertici, lettere_vertici)

        self.triangolo_abd()

        self.wait(30)

    def legenda_angoli(self):
        legenda = VGroup(
            Dot(),
            MathTex(r"= \dfrac{1}{5}\pi;").scale(.6),
            Dot(),
            Dot(),
            MathTex(r"= \dfrac{2}{5}\pi;").scale(.6),
            Dot(),
            Dot(),
            Dot(),
            MathTex(r"= \dfrac{3}{5}\pi").scale(.6),
        ).arrange(RIGHT).to_edge(DOWN).shift(LEFT_CENTER)
        cornice = SurroundingRectangle(legenda)
        self.play(Create(cornice), Write(legenda))

    def disegna_angolo_piatto(self, center=ORIGIN):
        radius = .3
        ratio = 1 / radius

        dot_color = BLUE
        arc_color = RED
        line_color = BLUE

        angle_tracker = ValueTracker(0)

        def update_arc(old):
            new_arc = Arc(radius=radius,
                          angle=angle_tracker.get_value(),
                          arc_center=center,
                          color=arc_color)
            old.become(new_arc)

        def update_arrow(old):
            new_arrow = Line(start=center, end=(arc.get_end() - center) * ratio + center, color=line_color, buff=0)
            old.become(new_arrow)

        arc = Arc(radius=radius, start_angle=0, angle=0, arc_center=center, color=arc_color)
        arc.add_updater(lambda j: update_arc(j))
        dot = Dot(center, color=dot_color)
        semiretta1 = Line(start=center, end=(arc.get_start() - center) * ratio + center, color=line_color, buff=0)
        semiretta2 = semiretta1.copy()
        semiretta2.add_updater(lambda j: update_arrow(j))
        self.add(arc)
        self.add(semiretta1, semiretta2)
        self.add(dot)
        self.play(angle_tracker.animate.set_value(PI))

        self.remove(semiretta2)
        self.remove(arc)
        arc = Arc(radius=radius, start_angle=0, angle=PI, arc_center=center, color=arc_color)
        semiretta2 = Line(start=center, end=(arc.get_end() - center) * ratio + center, color=line_color, buff=0)
        self.add(arc)
        self.add(semiretta2)

        return VGroup(semiretta1, semiretta2, dot, arc)

    def angoli_interni(self, vertici):
        raggio_misure = 1.0
        to_fade_out = []

        bae_arc = AngleWithArc(radius=.3, start_angle=0, angle=3 * PI / 5, center=vertici["a"])
        bae_misura = MathTex(r"\frac{3}{5}\pi").scale(.7). \
            move_to(Arc(radius=raggio_misure, start_angle=0, angle=3 * PI / 5, arc_center=vertici["a"]).get_center())

        abc_arc = AngleWithArc(radius=.3, start_angle=2 * PI / 5, angle=3 * PI / 5, center=vertici["b"])
        abc_misura = MathTex(r"\frac{3}{5}\pi").scale(.7). \
            move_to(
            Arc(radius=raggio_misure, start_angle=2 * PI / 5, angle=3 * PI / 5, arc_center=vertici["b"]).get_center())

        bcd_arc = AngleWithArc(radius=.3, start_angle=4 * PI / 5, angle=3 * PI / 5, center=vertici["c"])
        bcd_misura = MathTex(r"\frac{3}{5}\pi").scale(.7). \
            move_to(
            Arc(radius=raggio_misure, start_angle=4 * PI / 5, angle=3 * PI / 5, arc_center=vertici["c"]).get_center())

        cde_arc = AngleWithArc(radius=.3, start_angle=6 * PI / 5, angle=3 * PI / 5, center=vertici["d"])
        cde_misura = MathTex(r"\frac{3}{5}\pi").scale(.7). \
            move_to(
            Arc(radius=raggio_misure, start_angle=6 * PI / 5, angle=3 * PI / 5, arc_center=vertici["d"]).get_center())

        aed_arc = AngleWithArc(radius=.3, start_angle=8 * PI / 5, angle=3 * PI / 5, center=vertici["e"])
        aed_misura = MathTex(r"\frac{3}{5}\pi").scale(.7). \
            move_to(
            Arc(radius=raggio_misure, start_angle=8 * PI / 5, angle=3 * PI / 5, arc_center=vertici["e"]).get_center())

        archi_angoli_interni = [bae_arc, abc_arc, bcd_arc, cde_arc, aed_arc]
        misure_angoli_interni = [bae_misura, abc_misura, bcd_misura, cde_misura, aed_misura]

        self.play(*[Create(x) for x in archi_angoli_interni])

        to_fade_out.append(archi_angoli_interni[0])
        to_fade_out.append(archi_angoli_interni[2])
        to_fade_out.append(archi_angoli_interni[3])
        to_fade_out.append(archi_angoli_interni[4])

        teorema = Tex(r"In ogni poligono di $n$ lati, \\ "
                      r"la somma degli angoli interni è pari a \\ "
                      r"$n - 2$ angoli piatti.")

        cornice = SurroundingRectangle(teorema, fill_opacity=1, fill_color=BLACK, buff=.5)

        self.play(Create(cornice), Write(teorema))

        self.wait(DELAY)
        self.next_section()

        self.play(FadeOut(teorema), FadeOut(cornice))
        self.wait(DELAY)
        self.next_section()

        angolo_interno = AngleWithArc(radius=.3, start_angle=0, angle=3 * PI / 5)
        somma_1 = VGroup(
            angolo_interno.copy(),
            MathTex("+"),
            angolo_interno.copy(),
            MathTex("+"),
            angolo_interno.copy(),
            MathTex("+"),
            angolo_interno.copy(),
            MathTex("+"),
            angolo_interno.copy(),
            MathTex(r"= (5-2) \pi")
        ).arrange(RIGHT).move_to(2.8 * RIGHT + 2 * UP)

        archi_target = [somma_1[0], somma_1[2], somma_1[4], somma_1[6], somma_1[8]]
        somme = [somma_1[1], somma_1[3], somma_1[5], somma_1[7]]

        archi_dinamici_1 = []

        for _i in range(5):
            archi_dinamici_1.append(archi_angoli_interni[_i].copy())
            archi_dinamici_1[_i].target = archi_target[_i]

        self.play(*[MoveToTarget(x) for x in archi_dinamici_1], *[Write(x) for x in somme])
        to_fade_out.extend(archi_dinamici_1)
        to_fade_out.extend(somme)
        self.play(Write(somma_1[9]))
        to_fade_out.append(somma_1[9])
        self.wait(DELAY)
        self.next_section()

        somma_2 = VGroup(
            MathTex(r"5 \cdot"),
            angolo_interno.copy(),
            MathTex(r"= 3 \pi")
        ).arrange(RIGHT).next_to(somma_1, 2 * DOWN)

        archi_dinamici_2 = []

        for _i in range(5):
            archi_dinamici_2.append(archi_dinamici_1[_i].copy())
            archi_dinamici_2[_i].target = somma_2[1]
        archi_dinamici_2.append(somma_1[9].copy())
        archi_dinamici_2[5].target = somma_2[2]

        self.play(Write(somma_2[0]), *[MoveToTarget(x) for x in archi_dinamici_2])
        to_fade_out.append(somma_2[0])
        to_fade_out.extend(archi_dinamici_2)
        self.wait(DELAY)
        self.next_section()

        somma_3 = VGroup(
            angolo_interno.copy(),
            MathTex(r"= \dfrac{3}{5} \pi")
        ).arrange(RIGHT).next_to(somma_2, 2 * DOWN)

        archi_dinamici_3 = []
        for x in somma_2:
            archi_dinamici_3.append(x.copy())
        archi_dinamici_3[0].target = somma_3[1]
        archi_dinamici_3[1].target = somma_3[0]
        archi_dinamici_3[2].target = somma_3[1]

        self.play(*[MoveToTarget(x) for x in archi_dinamici_3])
        to_fade_out.extend(archi_dinamici_3)
        self.wait(DELAY)
        self.next_section()

        archi_dinamici_4 = []
        for _i in range(5):
            archi_dinamici_4.append(archi_dinamici_3[0].copy())
            archi_dinamici_4[_i].target = misure_angoli_interni[_i]

        self.play(*[MoveToTarget(x) for x in archi_dinamici_4])
        to_fade_out.append(archi_dinamici_4[0])
        to_fade_out.append(archi_dinamici_4[2])
        to_fade_out.append(archi_dinamici_4[3])
        to_fade_out.append(archi_dinamici_4[4])
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out])
        self.wait(DELAY)
        self.next_section()

        return VGroup(abc_arc, archi_dinamici_4[1])

    def angoli_esterni(self, vertici, angolo_abc):
        to_fade_out = []

        angolo_esterno_b = AngleWithArc(radius=.3, start_angle=0, angle=2 * PI / 5, center=vertici["b"])
        misura_esterno = MathTex(r"\frac{2}{5}\pi").scale(.7). \
            move_to(Arc(radius=1, angle=2 * PI / 5, arc_center=vertici["b"]).get_center())
        self.play(Create(angolo_esterno_b))
        to_fade_out.append(angolo_esterno_b)
        self.wait(DELAY)
        self.next_section()

        formula_1 = VGroup(
            angolo_abc[0].copy(),
            MathTex("+"),
            angolo_esterno_b.copy(),
            MathTex("="),
            AngleWithArc()
        ).arrange(RIGHT).move_to(RIGHT_CENTER + 2 * UP)

        interno = angolo_abc[0].copy()
        interno.target = formula_1[0]
        esterno = angolo_esterno_b.copy()
        esterno.target = formula_1[2]
        piatto = AngleWithArc(center=vertici["b"])
        piatto.target = formula_1[4]
        dinamo = [interno, esterno, piatto]

        self.play(*[MoveToTarget(x) for x in dinamo], Write(formula_1[1]), Write(formula_1[3]))
        to_fade_out.extend(dinamo)
        to_fade_out.append(formula_1[1])
        to_fade_out.append(formula_1[3])
        self.wait(DELAY)
        self.next_section()

        formula_2 = VGroup(
            angolo_esterno_b.copy(),
            MathTex("="),
            AngleWithArc(),
            MathTex("-"),
            angolo_abc[0].copy()
        ).arrange(RIGHT).next_to(formula_1, 2 * DOWN)

        esterno = esterno.copy()
        esterno.target = formula_2[0]
        uguale = formula_1[3].copy()
        uguale.target = formula_2[1]
        piatto = piatto.copy()
        piatto.target = formula_2[2]
        meno = formula_1[1].copy()
        meno.target = formula_2[3]
        interno = interno.copy()
        interno.target = formula_2[4]
        dinamo = [esterno, uguale, piatto, meno, interno]

        self.play(*[MoveToTarget(x) for x in dinamo])
        to_fade_out.extend(dinamo)
        self.wait(DELAY)
        self.next_section()

        formula_3 = VGroup(
            angolo_esterno_b.copy(),
            MathTex("="),
            MathTex(r"\pi"),
            MathTex("-"),
            MathTex(r"\dfrac{3}{5}\pi")
        ).arrange(RIGHT).next_to(formula_2, 2 * DOWN)

        esterno = esterno.copy()
        esterno.target = formula_3[0]
        uguale = formula_2[1].copy()
        uguale.target = formula_3[1]
        piatto = piatto.copy()
        piatto.target = formula_3[2]
        meno = formula_2[3].copy()
        meno.target = formula_3[3]
        interno = angolo_abc[1].copy()
        interno.target = formula_3[4]
        dinamo = [esterno, uguale, piatto, meno, interno]

        self.play(*[MoveToTarget(x) for x in dinamo])
        to_fade_out.extend(dinamo)
        self.wait(DELAY)
        self.next_section()

        formula_4 = VGroup(
            angolo_esterno_b.copy(),
            MathTex("="),
            MathTex(r"\dfrac{2}{5}\pi")
        ).arrange(RIGHT).next_to(formula_3, 2 * DOWN)

        esterno = esterno.copy()
        esterno.target = formula_4[0]
        self.play(MoveToTarget(esterno), Write(formula_4[1]), Write(formula_4[2]))
        to_fade_out.append(esterno)
        to_fade_out.append(formula_4[1])
        to_fade_out.append(formula_4[2])
        self.wait(DELAY)
        self.next_section()

        misura = formula_4[2].copy()
        misura.target = misura_esterno
        self.play(MoveToTarget(misura))
        to_fade_out.append(misura)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out], FadeOut(angolo_abc[0]), FadeOut(angolo_abc[1]))
        self.wait(DELAY)
        self.next_section()

    def suddivisione_angolo(self, vertici, lettere_vertici):
        to_fade_out = []

        cong = MathTex(r"\cong")
        pi = MathTex(r"\pi")

        alpha = MathTex(r"\alpha")
        beta = MathTex(r"\beta")
        gamma = MathTex(r"\gamma")
        delta = MathTex(r"\delta")
        epsilon = MathTex(r"\epsilon")

        lettere_greche = [alpha, beta, gamma, delta, epsilon]

        diagonale_ad = Line(start=vertici["a"], end=vertici["d"], color=BLUE)
        diagonale_bd = Line(start=vertici["b"], end=vertici["d"], color=BLUE)
        retta_start = vertici["d"].copy()
        retta_start[0] = retta_start[0] - 2.5
        retta_end = vertici["d"].copy()
        retta_end[0] = retta_end[0] + 2.5
        retta = Line(start=retta_start, end=retta_end, color=BLUE)

        self.play(Create(diagonale_ad))
        self.play(Create(diagonale_bd))
        to_fade_out.append(diagonale_ad)
        to_fade_out.append(diagonale_bd)
        self.wait(DELAY)
        self.next_section()
        self.play(Create(retta))
        to_fade_out.append(retta)
        self.wait(DELAY)
        self.next_section()

        angoli = []

        lettere = []

        for _i in range(5):
            angolo = AngleWithArc(radius=.3, start_angle=(5 + _i) * PI / 5, angle=PI / 5, center=vertici["d"])
            angoli.append(angolo)
            lettera = lettere_greche[_i].copy().scale(.7).move_to(
                Arc(radius=.6, start_angle=(5 + _i) * PI / 5, angle=PI / 5, arc_center=vertici["d"]).get_center())
            lettere.append(lettera)

        self.play(*[Create(x) for x in angoli])
        self.play(*[Write(x) for x in lettere])
        to_fade_out.extend(angoli)
        self.wait(DELAY)
        self.next_section()

        template_angolo = AngleWithArc(radius=.3, angle=PI / 5)
        formula_1 = VGroup(
            template_angolo.copy(),
            MathTex("+"),
            template_angolo.copy(),
            MathTex("+"),
            template_angolo.copy(),
            MathTex("+"),
            template_angolo.copy(),
            MathTex("+"),
            template_angolo.copy(),
            MathTex("="),
            AngleWithArc(radius=.3, angle=PI),
            alpha.copy(),
            MathTex("+"),
            beta.copy(),
            MathTex("+"),
            gamma.copy(),
            MathTex("+"),
            delta.copy(),
            MathTex("+"),
            epsilon.copy(),
            MathTex("="),
            pi.copy(),
        ).arrange_in_grid(2, 11, buff=(.25, .1)).move_to(3 * RIGHT + 3 * UP)

        statico = []
        for _i in range(5):
            statico.append(formula_1[(_i * 2) + 12])
        statico.append(formula_1[21])

        dinamo = []
        for _i in range(5):
            angolo = angoli[_i].copy()
            angolo.target = formula_1[_i * 2]
            dinamo.append(angolo)
            lettera = lettere[_i].copy()
            lettera.target = formula_1[_i * 2 + 11]
            dinamo.append(lettera)
        retto = AngleWithArc(radius=.3, start_angle=PI, angle=PI, center=vertici["d"])
        retto.target = formula_1[10]
        dinamo.append(retto)

        self.play(*[MoveToTarget(x) for x in dinamo], *[Write(x) for x in statico])
        to_fade_out.extend(dinamo)
        to_fade_out.extend(statico)

        circonferenza = Circle.from_three_points(vertici["a"], vertici["b"], vertici["c"], color=BLUE, z_index=-3)
        self.play(Create(circonferenza))
        to_fade_out.append(circonferenza)
        self.wait(DELAY)
        self.next_section()

        template_corda = Line(start=vertici["a"], end=vertici["b"], color=BLUE)
        equivalenza_corde = VGroup(
            VGroup(MathTex("A").scale(.7), template_corda.copy(), MathTex("B").scale(.7)).arrange(RIGHT, buff=.1),
            MathTex(r"\cong"),
            VGroup(MathTex("B").scale(.7), template_corda.copy(), MathTex("C").scale(.7)).arrange(RIGHT, buff=.1),
            MathTex(r"\cong"),
            VGroup(MathTex("C").scale(.7), template_corda.copy(), MathTex("D").scale(.7)).arrange(RIGHT, buff=.1),
            MathTex(r"\cong"),
            VGroup(MathTex("D").scale(.7), template_corda.copy(), MathTex("E").scale(.7)).arrange(RIGHT, buff=.1),
            MathTex(r"\cong"),
            VGroup(MathTex("E").scale(.7), template_corda.copy(), MathTex("A").scale(.7)).arrange(RIGHT, buff=.1)
        ).arrange(DOWN).next_to(formula_1, 3 * DOWN)

        corde = [
            Line(start=vertici["a"], end=vertici["b"], color=BLUE),
            Line(start=vertici["b"], end=vertici["c"], color=BLUE),
            Line(start=vertici["c"], end=vertici["d"], color=BLUE),
            Line(start=vertici["d"], end=vertici["e"], color=BLUE),
            Line(start=vertici["e"], end=vertici["a"], color=BLUE),
        ]

        congruenze = [
            equivalenza_corde[1],
            equivalenza_corde[3],
            equivalenza_corde[5],
            equivalenza_corde[7]
        ]

        dinamo = []
        lettera = lettere_vertici["a"].copy()
        lettera.target = equivalenza_corde[0][0]
        dinamo.append(lettera)
        lettera = lettere_vertici["b"].copy()
        lettera.target = equivalenza_corde[0][2]
        dinamo.append(lettera)
        lettera = lettere_vertici["b"].copy()
        lettera.target = equivalenza_corde[2][0]
        dinamo.append(lettera)
        lettera = lettere_vertici["c"].copy()
        lettera.target = equivalenza_corde[2][2]
        dinamo.append(lettera)
        lettera = lettere_vertici["c"].copy()
        lettera.target = equivalenza_corde[4][0]
        dinamo.append(lettera)
        lettera = lettere_vertici["d"].copy()
        lettera.target = equivalenza_corde[4][2]
        dinamo.append(lettera)
        lettera = lettere_vertici["d"].copy()
        lettera.target = equivalenza_corde[6][0]
        dinamo.append(lettera)
        lettera = lettere_vertici["e"].copy()
        lettera.target = equivalenza_corde[6][2]
        dinamo.append(lettera)
        lettera = lettere_vertici["e"].copy()
        lettera.target = equivalenza_corde[8][0]
        dinamo.append(lettera)
        lettera = lettere_vertici["a"].copy()
        lettera.target = equivalenza_corde[8][2]
        dinamo.append(lettera)

        self.play(
            corde[0].animate.move_to(equivalenza_corde[0][1]),
            corde[1].animate.move_to(equivalenza_corde[2][1]).rotate(-2 * PI / 5),
            corde[2].animate.move_to(equivalenza_corde[4][1]).rotate(-4 * PI / 5),
            corde[3].animate.move_to(equivalenza_corde[6][1]).rotate(-6 * PI / 5),
            corde[4].animate.move_to(equivalenza_corde[8][1]).rotate(-8 * PI / 5),
            *[MoveToTarget(x) for x in dinamo],
            *[Write(x) for x in congruenze]
        )
        self.wait(DELAY)
        self.next_section()

        self.play(
            *[FadeOut(x) for x in dinamo],
            *[FadeOut(x) for x in corde],
            *[FadeOut(x) for x in congruenze]
        )

        template_archi = ArcBetweenPoints(start=vertici["a"], end=vertici["b"], arc_center=circonferenza.get_center(),
                                          angle=2 * PI / 5, color=BLUE)
        equivalenza_archi = VGroup(
            template_archi.copy(),
            MathTex(r"\cong"),
            template_archi.copy(),
            MathTex(r"\cong"),
            template_archi.copy(),
            MathTex(r"\cong"),
            template_archi.copy(),
            MathTex(r"\cong"),
            template_archi.copy()
        ).arrange(DOWN).next_to(formula_1, 3 * DOWN)

        archi = [
            ArcBetweenPoints(start=vertici["a"], end=vertici["b"], arc_center=circonferenza.get_center(),
                             angle=2 * PI / 5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["b"], end=vertici["c"], arc_center=circonferenza.get_center(),
                             angle=2 * PI / 5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["c"], end=vertici["d"], arc_center=circonferenza.get_center(),
                             angle=2 * PI / 5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["d"], end=vertici["e"], arc_center=circonferenza.get_center(),
                             angle=2 * PI / 5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["e"], end=vertici["a"], arc_center=circonferenza.get_center(),
                             angle=2 * PI / 5,
                             color=BLUE),
        ]

        congruenze = [
            equivalenza_archi[1],
            equivalenza_archi[3],
            equivalenza_archi[5],
            equivalenza_archi[7]
        ]

        dinamo = []
        lettera = lettere_vertici["a"].copy()
        lettera.target = MathTex("A").scale(.7).next_to(equivalenza_archi[0].get_start(), LEFT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["b"].copy()
        lettera.target = MathTex("B").scale(.7).next_to(equivalenza_archi[0].get_end(), RIGHT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["b"].copy()
        lettera.target = MathTex("B").scale(.7).next_to(equivalenza_archi[2].get_start(), LEFT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["c"].copy()
        lettera.target = MathTex("C").scale(.7).next_to(equivalenza_archi[2].get_end(), RIGHT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["c"].copy()
        lettera.target = MathTex("C").scale(.7).next_to(equivalenza_archi[4].get_start(), LEFT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["d"].copy()
        lettera.target = MathTex("D").scale(.7).next_to(equivalenza_archi[4].get_end(), RIGHT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["d"].copy()
        lettera.target = MathTex("D").scale(.7).next_to(equivalenza_archi[6].get_start(), LEFT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["e"].copy()
        lettera.target = MathTex("E").scale(.7).next_to(equivalenza_archi[6].get_end(), RIGHT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["e"].copy()
        lettera.target = MathTex("E").scale(.7).next_to(equivalenza_archi[8].get_start(), LEFT, buff=.1)
        dinamo.append(lettera)
        lettera = lettere_vertici["a"].copy()
        lettera.target = MathTex("A").scale(.7).next_to(equivalenza_archi[8].get_end(), RIGHT, buff=.1)
        dinamo.append(lettera)

        self.play(
            archi[0].animate.move_to(equivalenza_archi[0]),
            archi[1].animate.rotate(-2 * PI / 5).move_to(equivalenza_archi[2]),
            archi[2].animate.rotate(-4 * PI / 5).move_to(equivalenza_archi[4]),
            archi[3].animate.rotate(-6 * PI / 5).move_to(equivalenza_archi[6]),
            archi[4].animate.rotate(-8 * PI / 5).move_to(equivalenza_archi[8]),
            *[MoveToTarget(x) for x in dinamo],
            *[Write(x) for x in congruenze]
        )
        self.wait(DELAY)
        self.next_section()

        self.play(
            *[FadeOut(x) for x in dinamo],
            *[FadeOut(x) for x in archi],
            *[FadeOut(x) for x in congruenze]
        )

        formula_2 = VGroup()
        for _i in range(5):
            formula_2.add(template_angolo.copy())
            if _i < 4:
                formula_2.add(cong.copy())
        for _i in range(5):
            formula_2.add(lettere_greche[_i].copy())
            if _i < 4:
                formula_2.add(cong.copy())
        formula_2.arrange_in_grid(2, 9, buff=(.25, .1)).next_to(formula_1, 2 * DOWN)

        dinamo = []
        for _i in range(5):
            angolo = angoli[_i].copy()
            angolo.target = formula_2[_i * 2]
            dinamo.append(angolo)
            lettera = lettere[_i].copy()
            lettera.target = formula_2[_i * 2 + 9]
            dinamo.append(lettera)

        statico = []
        for _i in range(4):
            statico.append(formula_2[_i * 2 + 10])

        self.play(*[MoveToTarget(x) for x in dinamo])
        to_fade_out.extend(dinamo)
        self.wait(DELAY)
        self.next_section()

        self.play(*[Write(x) for x in statico])
        to_fade_out.extend(statico)
        self.wait(DELAY)
        self.next_section()

        formula_3 = VGroup(
            MathTex(r"5 \cdot"),
            template_angolo.copy(),
            MathTex(r"="),
            pi
        ).arrange(RIGHT).next_to(formula_2, 2 * DOWN)

        dinamo = []
        for _i in range(5):
            angolo = formula_2[_i * 2].copy()
            angolo.target = formula_3[1]
            dinamo.append(angolo)
        pi_greco = formula_1[21].copy()
        pi_greco.target = formula_3[3]
        dinamo.append(pi_greco)

        self.play(*[MoveToTarget(x) for x in dinamo], Write(formula_3[0]), Write(formula_3[2]))
        to_fade_out.extend(dinamo)
        to_fade_out.append(formula_3[0])
        to_fade_out.append(formula_3[2])
        self.wait(DELAY)
        self.next_section()

        formula_4 = VGroup(
            template_angolo.copy(),
            MathTex(r"=\dfrac{\pi}{5}")
        ).arrange(RIGHT).next_to(formula_3, 2 * DOWN)

        dinamo = formula_3[1].copy()
        dinamo.target = formula_4[0]

        self.play(MoveToTarget(dinamo), Write(formula_4[1]))
        to_fade_out.append(dinamo)
        to_fade_out.append(formula_4[1])
        self.wait(DELAY)
        self.next_section()

        dinamo = []
        for _i in range(5):
            misura = MathTex(r"\dfrac{\pi}{5}").move_to(formula_4[1][0][1:])
            misura.target = MathTex(r"\dfrac{\pi}{5}").scale(.7).move_to(lettere[_i])
            dinamo.append(misura)
        self.play(*[MoveToTarget(x) for x in dinamo],
                  *[FadeOut(x) for x in lettere]),
        to_fade_out.extend(dinamo)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out])

    def triangolo_abd(self):
        to_fade_out = []
        to_fade_out_temp = []

        diagonale_ad = Line(start=self.vertici["a"], end=self.vertici["d"], color=BLUE)
        diagonale_bd = Line(start=self.vertici["b"], end=self.vertici["d"], color=BLUE)

        triangolo_abd = Polygon(self.vertici["a"], self.vertici["b"], self.vertici["d"], color=YELLOW,
                                fill_color=YELLOW, fill_opacity=.5)
        self.play(Create(triangolo_abd))
        to_fade_out.append(triangolo_abd)
        self.wait(DELAY)
        self.next_section()

        segno_lato = MathTex("||", color=YELLOW).scale(.5)
        segno_lato_ad = segno_lato.copy().move_to(diagonale_ad).rotate(diagonale_ad.get_angle())
        segno_lato_bd = segno_lato.copy().move_to(diagonale_bd).rotate(diagonale_bd.get_angle())
        self.play(Write(segno_lato_ad), Write(segno_lato_bd))
        to_fade_out_temp.append(segno_lato_ad)
        to_fade_out_temp.append(segno_lato_bd)
        formula_1 = MathTex(r"AD \cong BD").to_edge(UP).shift(3 * RIGHT)
        formula_2 = MathTex("\Rightarrow").rotate(-PI / 2).next_to(formula_1, 2 * DOWN)
        formula_3 = Tex(r"$ABD$ isoscele").next_to(formula_2, 2 * DOWN)
        self.play(Write(formula_1))
        self.play(Write(formula_2))
        self.play(Write(formula_3))
        to_fade_out_temp.append(formula_1)
        to_fade_out_temp.append(formula_2)
        to_fade_out_temp.append(formula_3)
        self.wait(DELAY)
        self.next_section()

        self.play(Create(self.misure_angoli["adb"].set_color(BLACK)))
        to_fade_out.append(self.misure_angoli["adb"])
        self.wait(DELAY)
        self.next_section()

        formula_4 = MathTex("\Rightarrow").rotate(-PI / 2).next_to(formula_3, 2 * DOWN)
        formula_5 = MathTex(r"\widehat{BAD} = \widehat{ABD} = \dfrac{2}{5}\pi").next_to(formula_4, 2 * DOWN)
        self.play(Write(formula_4))
        self.play(Write(formula_5))
        to_fade_out_temp.append(formula_4)
        to_fade_out_temp.append(formula_5)
        self.play(Create(self.misure_angoli["bad"].set_color(BLACK)),
                  Create(self.misure_angoli["abd"].set_color(BLACK)))
        to_fade_out.append(self.misure_angoli["bad"])
        to_fade_out.append(self.misure_angoli["abd"])
        self.wait(DELAY)
        self.next_section()

        diagonale_ac = Line(start=self.vertici["a"], end=self.vertici["c"], color=YELLOW)
        diagonale_be = Line(start=self.vertici["b"], end=self.vertici["e"], color=YELLOW)

        self.play(Create(diagonale_ac), Create(diagonale_be))
        to_fade_out.append(diagonale_ac)
        to_fade_out_temp.append(diagonale_be)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        to_fade_out_temp = []
        f = line_intersection(
            [diagonale_bd.get_start(), diagonale_bd.get_end()],
            [diagonale_ac.get_start(), diagonale_ac.get_end()],
        )
        lettera_f = MathTex("F").next_to(f, RIGHT, buff=.15)
        self.play(Write(lettera_f))
        self.wait(DELAY)
        self.next_section()

        formula_1 = MathTex(r"\widehat{BAF} = \dfrac{1}{5}\pi \quad \widehat{ABF} = \dfrac{2}{5}\pi").to_edge(UP).shift(
            3 * RIGHT)
        self.play(Write(formula_1))
        to_fade_out_temp.append(formula_1)
        self.wait(DELAY)
        self.next_section()

        formula_2 = MathTex("\Rightarrow").rotate(-PI / 2).next_to(formula_1, 2 * DOWN)
        formula_3 = MathTex(r"\widehat{AFB} = \dfrac{2}{5}\pi").next_to(formula_2, 2 * DOWN)
        self.play(Write(formula_2))
        self.play(Write(formula_3))
        to_fade_out_temp.append(formula_2)
        to_fade_out_temp.append(formula_3)
        misura_angolo_afx = Dot(color=BLACK).move_to(
            Arc(radius=RAGGIO_DOT, start_angle=-2 * PI / 5, angle=-PI / 5, arc_center=f).get_center())
        misura_angolo_bfx = Dot(color=BLACK).move_to(
            Arc(radius=RAGGIO_DOT, start_angle=-4 * PI / 5, angle=PI / 5, arc_center=f).get_center())
        misura_angolo_afb = VGroup(misura_angolo_afx, misura_angolo_bfx)
        self.play(Create(misura_angolo_afb))
        to_fade_out.append(misura_angolo_afb)
        self.wait(DELAY)
        self.next_section()

        formula_4 = MathTex("\Rightarrow").rotate(-PI / 2).next_to(formula_3, 2 * DOWN)
        formula_5 = Tex(r"$ABF$ isoscele").next_to(formula_4, 2 * DOWN)
        self.play(Write(formula_4))
        self.play(Write(formula_5))
        to_fade_out_temp.append(formula_4)
        to_fade_out_temp.append(formula_5)
        triplo_segno_lato = MathTex("|||", color=YELLOW).scale(.5)
        af = Line(start=self.vertici["a"], end=f)
        ab = Line(start=self.vertici["a"], end=self.vertici["b"])
        segno_lato_ad = triplo_segno_lato.copy().move_to(af).rotate(af.get_angle())
        segno_lato_bd = triplo_segno_lato.copy().move_to(ab).rotate(ab.get_angle())
        self.play(Write(segno_lato_ad), Write(segno_lato_bd))
        to_fade_out.append(segno_lato_ad)
        to_fade_out.append(segno_lato_bd)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        to_fade_out_temp = []

        formula_1 = MathTex(r"\widehat{DAF} = \dfrac{1}{5}\pi \quad \widehat{ADF} = \dfrac{1}{5}\pi").to_edge(UP).shift(
            3 * RIGHT)
        self.play(Write(formula_1))
        to_fade_out_temp.append(formula_1)
        self.wait(DELAY)
        self.next_section()

        formula_2 = MathTex("\Rightarrow").rotate(-PI / 2).next_to(formula_1, 2 * DOWN)
        formula_3 = Tex(r"$ADF$ isoscele").next_to(formula_2, 2 * DOWN)
        self.play(Write(formula_2))
        self.play(Write(formula_3))
        to_fade_out_temp.append(formula_2)
        to_fade_out_temp.append(formula_3)
        df = Line(start=self.vertici["d"], end=f)
        segno_lato_df = triplo_segno_lato.copy().move_to(df).rotate(df.get_angle())
        self.play(Write(segno_lato_df))
        to_fade_out.append(segno_lato_df)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        to_fade_out_temp = []

        template_triangolo_abd = triangolo_abd.copy()
        template_triangolo_abf = Polygon(self.vertici["a"], self.vertici["b"], f).rotate(-3 * PI / 5)
        template_triangoli = VGroup(template_triangolo_abd, template_triangolo_abf) \
            .arrange(RIGHT, buff=1).to_edge(UP) \
            .shift(3 * RIGHT + .5 * DOWN)

        moving_triangolo_abd = VGroup(
            triangolo_abd.copy(),
            self.misure_angoli["adb"].copy(),
            self.misure_angoli["abd"].copy(),
            self.misure_angoli["bad"].copy()
        )
        moving_a = self.lettere_vertici["a"].copy()
        moving_b = self.lettere_vertici["b"].copy()
        moving_d = self.lettere_vertici["d"].copy()

        moving_triangolo_abf = VGroup(
            Polygon(self.vertici["a"], self.vertici["b"], f, color=YELLOW, fill_color=YELLOW, fill_opacity=.5),
            misura_angolo_afb.copy(),
            self.misure_angoli["abd"].copy(),
            self.misure_angoli["bac"].copy()
        )
        moving_a_bis = self.lettere_vertici["a"].copy()
        moving_b_bis = self.lettere_vertici["b"].copy()
        moving_f_bis = lettera_f.copy()

        self.play(
            moving_triangolo_abd.animate.move_to(template_triangolo_abd),
            moving_a.animate.next_to(template_triangolo_abd.get_vertices()[0], DOWN, buff=.15),
            moving_b.animate.next_to(template_triangolo_abd.get_vertices()[1], DOWN, buff=.15),
            moving_d.animate.next_to(template_triangolo_abd.get_vertices()[2], UP, buff=.15),
            moving_triangolo_abf.animate.rotate(-3*PI/5).move_to(template_triangolo_abf),
            moving_a_bis.animate.next_to(template_triangolo_abf.get_vertices()[0], UP, buff=.15),
            moving_b_bis.animate.next_to(template_triangolo_abf.get_vertices()[1], DOWN, buff=.15),
            moving_f_bis.animate.next_to(template_triangolo_abf.get_vertices()[2], DOWN, buff=.15),
        )
        to_fade_out_temp.append(moving_triangolo_abd)
        to_fade_out_temp.append(moving_triangolo_abf)
        to_fade_out_temp.append(moving_a)
        to_fade_out_temp.append(moving_a_bis)
        to_fade_out_temp.append(moving_b)
        to_fade_out_temp.append(moving_b_bis)
        to_fade_out_temp.append(moving_d)
        to_fade_out_temp.append(moving_f_bis)
        self.wait(DELAY)
        self.next_section()

        formula_1 = MathTex(r"\overline{AD} : \overline{AB} = \overline{AB} : \overline{BF}")
        formula_1.next_to(template_triangoli, 4*DOWN)
        self.play(Write(formula_1))

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        to_fade_out_temp = []
        self.play(formula_1.animate.to_edge(UP))
        to_fade_out_temp.append(formula_1)
        self.wait(DELAY)
        self.next_section()

        formula_2 = MathTex(r"\overline{AD} : \overline{AB} = \overline{AB} : (\overline{BD} - \overline{DF})")
        formula_2.next_to(formula_1, 2*DOWN)
        self.play(Write(formula_2))
        to_fade_out_temp.append(formula_2)
        self.wait(DELAY)
        self.next_section()

        formula_3 = MathTex(r"\overline{AD} : \overline{AB} = \overline{AB} : (\overline{AD} - \overline{DF})")
        formula_3.next_to(formula_2, 2*DOWN)
        self.play(Write(formula_3))
        to_fade_out_temp.append(formula_3)
        self.wait(DELAY)
        self.next_section()

        formula_4 = MathTex(r"\overline{AD} : \overline{AB} = \overline{AB} : (\overline{AD} - \overline{AF})")
        formula_4.next_to(formula_3, 2*DOWN)
        self.play(Write(formula_4))
        to_fade_out_temp.append(formula_4)
        self.wait(DELAY)
        self.next_section()

        formula_5 = MathTex(r"\overline{AD} : \overline{AB} = \overline{AB} : (\overline{AD} - \overline{AB})")
        formula_5.next_to(formula_4, 2*DOWN)
        self.play(Write(formula_5))
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        to_fade_out_temp = []
        self.play(formula_5.animate.to_edge(UP))
        to_fade_out_temp.append(formula_5)
        self.wait(DELAY)
        self.next_section()

        self.play(Circumscribe(formula_5[0][4:7]), Circumscribe(formula_5[0][8:11]))
        self.play(Circumscribe(formula_5[0][4:7]), Circumscribe(formula_5[0][8:11]))
        self.wait(DELAY)
        self.next_section()

        self.play(Circumscribe(formula_5[0][:3]))
        self.play(Circumscribe(formula_5[0][:3]))
        self.wait(DELAY)
        self.next_section()

        self.play(Circumscribe(formula_5[0][12:]))
        self.play(Circumscribe(formula_5[0][12:]))
        self.wait(DELAY)
        self.next_section()

        formula_6 = MathTex(r"d : l = l : (d - l)")
        formula_6.next_to(formula_5, 2*DOWN)
        self.play(Write(formula_6))
        self.wait(DELAY)
        self.next_section()

        formula_7 = MathTex(r"d \cdot (d-l) = l \cdot l")
        formula_7.next_to(formula_6, 2*DOWN)
        self.play(Write(formula_7))
        self.wait(DELAY)
        self.next_section()

        formula_8 = MathTex(r"d^2 - ld = l^2")
        formula_8.next_to(formula_7, 2*DOWN)
        self.play(Write(formula_8))
        self.wait(DELAY)
        self.next_section()

        formula_9 = MathTex(r"d^2 - ld - l^2 = 0")
        formula_9.next_to(formula_8, 2*DOWN)
        self.play(Write(formula_9))
        self.wait(DELAY)
        self.next_section()
