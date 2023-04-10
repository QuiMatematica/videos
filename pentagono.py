from manim import *

from qgeo import AngleWithArc

DELAY = 1
RIGHT_CENTER = 3.5 * RIGHT
PENTAGONO_CENTER = 3.5 * LEFT
PENTAGONO_RADIUS = 2.5


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(1)

        pentagono = RegularPolygon(n=5, fill_opacity=.2, fill_color=BLUE, z_index=-2).scale(PENTAGONO_RADIUS).shift(
            PENTAGONO_CENTER)
        vertici_pentagono = pentagono.get_vertices()
        vertici = {"a": vertici_pentagono[2],
                   "b": vertici_pentagono[3],
                   "c": vertici_pentagono[4],
                   "d": vertici_pentagono[0],
                   "e": vertici_pentagono[1]}

        lettere_vertici = {"a": Tex('A').next_to(vertici["a"], DOWN),
                           "b": Tex('B').next_to(vertici["b"], DOWN),
                           "c": Tex('C').next_to(vertici["c"], RIGHT),
                           "d": Tex('D').next_to(vertici["d"], UP),
                           "e": Tex('E').next_to(vertici["e"], LEFT)}

        self.play(Create(pentagono))
        self.play(*[Write(x) for x in lettere_vertici.values()])
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

        angolo_abc = self.angoli_interni(vertici)

        self.angoli_esterni(vertici, angolo_abc)

        self.suddivisione_angolo(vertici, lettere_vertici)

        self.triangolo_abd(vertici)

        self.wait(30)

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
        ).arrange(RIGHT).next_to(somma_1, 2*DOWN)

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
        ).arrange(RIGHT).next_to(somma_2, 2*DOWN)

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
        ).arrange(RIGHT).next_to(formula_1, 2*DOWN)

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
        ).arrange(RIGHT).next_to(formula_2, 2*DOWN)

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
        ).arrange(RIGHT).next_to(formula_3, 2*DOWN)

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
                                          angle=2*PI/5, color=BLUE)
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
            ArcBetweenPoints(start=vertici["a"], end=vertici["b"], arc_center=circonferenza.get_center(), angle=2*PI/5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["b"], end=vertici["c"], arc_center=circonferenza.get_center(), angle=2*PI/5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["c"], end=vertici["d"], arc_center=circonferenza.get_center(), angle=2*PI/5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["d"], end=vertici["e"], arc_center=circonferenza.get_center(), angle=2*PI/5,
                             color=BLUE),
            ArcBetweenPoints(start=vertici["e"], end=vertici["a"], arc_center=circonferenza.get_center(), angle=2*PI/5,
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
        formula_2.arrange_in_grid(2, 9, buff=(.25, .1)).next_to(formula_1, 2*DOWN)

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
        ).arrange(RIGHT).next_to(formula_2, 2*DOWN)

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
        ).arrange(RIGHT).next_to(formula_3, 2*DOWN)

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

    def triangolo_abd(self, vertici):
        scala_misura_angoli = .6
        raggio_misura_angoli = .7

        to_fade_out = []
        to_fade_out_temp = []

        diagonale_ad = Line(start=vertici["a"], end=vertici["d"], color=BLUE)
        diagonale_bd = Line(start=vertici["b"], end=vertici["d"], color=BLUE)

        triangolo_abd = Polygon(vertici["a"], vertici["b"], vertici["d"], color=YELLOW,
                                fill_color=YELLOW, fill_opacity=.7)
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
        self.wait(DELAY)
        self.next_section()

        misura_angolo_adb = MathTex(r"\dfrac{\pi}{5}", color=BLACK, z_index=100).scale(scala_misura_angoli).move_to(
                Arc(radius=raggio_misura_angoli, start_angle=7 * PI / 5, angle=PI / 5, arc_center=vertici["d"]).get_center())
        self.play(Write(misura_angolo_adb))
        to_fade_out_temp.append(misura_angolo_adb)
        self.wait(DELAY)
        self.next_section()

        misura_angolo_dab = MathTex(r"\dfrac{2}{5}\pi", color=BLACK, z_index=100).scale(scala_misura_angoli).move_to(
                Arc(radius=raggio_misura_angoli, start_angle=0, angle=2 * PI / 5, arc_center=vertici["a"]).get_center())
        misura_angolo_dba = MathTex(r"\dfrac{2}{5}\pi", color=BLACK, z_index=100).scale(scala_misura_angoli).move_to(
                Arc(radius=raggio_misura_angoli, start_angle=3 * PI / 5, angle=2 * PI / 5, arc_center=vertici["b"]).get_center())
        self.play(Write(misura_angolo_dab), Write(misura_angolo_dba))
        to_fade_out_temp.append(misura_angolo_dab)
        to_fade_out_temp.append(misura_angolo_dba)
        self.wait(DELAY)
        self.next_section()

        diagonale_ac = Line(start=vertici["a"], end=vertici["c"], color=YELLOW)
        diagonale_be = Line(start=vertici["b"], end=vertici["e"], color=YELLOW)

        self.play(Create(diagonale_ac), Create(diagonale_be))
        to_fade_out.append(diagonale_ac)
        to_fade_out_temp.append(diagonale_be)
        self.wait(DELAY)
        self.next_section()

        self.play(*[FadeOut(x) for x in to_fade_out_temp])
        f = line_intersection(
            [diagonale_bd.get_start(), diagonale_bd.get_end()],
            [diagonale_ac.get_start(), diagonale_ac.get_end()],
        )
        lettera_f = MathTex("F").next_to(f, RIGHT, buff=.15)
        self.play(Write(lettera_f))
        self.wait(DELAY)
        self.next_section()

        to_fade_out_temp = []

        misura_angolo_fab = MathTex(r"\dfrac{\pi}{5}", color=BLACK, z_index=100).scale(scala_misura_angoli).move_to(
                Arc(radius=raggio_misura_angoli, start_angle=0, angle=PI / 5, arc_center=vertici["a"]).get_center())
        self.play(Write(misura_angolo_fab), Write(misura_angolo_dba))
        to_fade_out_temp.append(misura_angolo_fab)
        to_fade_out_temp.append(misura_angolo_dba)
        self.wait(DELAY)
        self.next_section()

        misura_angolo_afb = MathTex(r"\dfrac{2}{5}\pi", color=BLACK, z_index=100).scale(scala_misura_angoli).move_to(
                Arc(radius=raggio_misura_angoli, start_angle=-2*PI/5, angle=-PI / 5, arc_center=f).get_center())
        self.play(Write(misura_angolo_afb))
        to_fade_out_temp.append(misura_angolo_afb)
        self.wait(DELAY)
        self.next_section()
