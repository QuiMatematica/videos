import math

from manim import *

DELAY = 30

SQRT_3 = math.sqrt(3)
SQRT_3_DIV_2 = SQRT_3 / 2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        _unit = 2.5

        start_c2 = _unit
        start_c1 = -start_c2

        center_y = _unit * (SQRT_3 - 1) / 2

        radius_1 = Line(
                (start_c1, center_y, 0),
                (start_c1 + _unit, center_y, 0))

        radius_2 = Line(
                (start_c2, center_y, 0),
                (start_c2 - _unit, center_y, 0))

        self.add(radius_1, radius_2)

        circle_1 = Circle(radius=_unit, arc_center=(start_c1, center_y, 0), z_index=2)
        circle_2 = Circle(radius=_unit, arc_center=(start_c2, center_y, 0), z_index=2).rotate(PI)

        radius_1_value = Tex("1 cm").next_to(radius_1, UP, buff=.1)
        radius_2_value = Tex("1 cm").next_to(radius_2, UP, buff=.1)
        self.add(radius_1_value, radius_2_value, circle_1, circle_2)

        o1_point = Dot(circle_1.get_center())
        o1_label = MathTex(r"O_1").next_to(o1_point, UL, buff=.1)
        o2_point = Dot(circle_2.get_center())
        o2_label = MathTex(r"O_2").next_to(o2_point, UR, buff=.1)
        self.add(o1_point, o1_label)
        self.add(o2_point, o2_label)

        tangent = DashedLine(
            (0, 2 * _unit, 0),
            (0, -2 * _unit, 0)
        )
        self.add(tangent)

        p_point = Dot((0, -_unit * (SQRT_3 + 1) / 2, 0), z_index=5)
        p_label = MathTex(r"P").next_to(p_point, DR, buff=.1)
        self.add(p_point, p_label)

        p_o1_line = Line(p_point.get_center(), o1_point.get_center())
        p_o2_line = Line(p_point.get_center(), o2_point.get_center())

        self.add(p_o1_line, p_o2_line)

        o1_p_o2_angle = Angle.from_three_points(
                o2_point.get_center(), p_point.get_center(), o1_point.get_center(), radius=0.6, color=YELLOW)

        o1_p_o2_value = Integer(
                o1_p_o2_angle.get_value(degrees=True),
                unit=r"^{\circ}",
                color=YELLOW,
                z_index=5).next_to(o1_p_o2_angle, UP, buff=.1)

        self.add(o1_p_o2_angle, o1_p_o2_value)

        t2_coordinates = (_unit * SQRT_3 * SQRT_3_DIV_2, center_y - _unit * SQRT_3 / 2, 0)
        t1_coordinates = (-_unit * SQRT_3 * SQRT_3_DIV_2, center_y - _unit * SQRT_3 / 2, 0)
        p_a_line = Line(p_point.get_center(), t1_coordinates, color=RED)
        p_c_line = Line(p_point.get_center(), t2_coordinates, color=RED)
        self.add(p_a_line, p_c_line)

        # Quanto vale l’area del cuore ottenuto?
        triangoli = Polygon(
            t1_coordinates,
            o1_point.get_center(),
            o2_point.get_center(),
            t2_coordinates,
            p_point.get_center(), color=DARK_BLUE, fill_opacity=1, z_index=-1)
        cuore = Union(circle_1, circle_2)
        diff = Difference(triangoli, cuore)
        cuore = Union(cuore, diff, color=DARK_BLUE, fill_opacity=1, z_index=-1)
        self.add(cuore)
        self.cut_and_wait()

        # Chiamiamo A, B e C i punti di tangenza delle rette uscenti da P.

        a_point = Dot(t1_coordinates, z_index=5)
        a_label = MathTex("A").next_to(a_point, DL, buff=.1)
        self.play(Create(a_point), Write(a_label))

        b_point = Dot((start_c1 + _unit, center_y, 0), z_index=5)
        b_label = MathTex("B").next_to(b_point, DR, buff=.1)
        self.play(Create(b_point), Write(b_label))

        c_point = Dot(t2_coordinates, z_index=5)
        c_label = MathTex("C").next_to(c_point, DR, buff=.1)
        self.play(Create(c_point), Write(c_label))

        self.cut_and_wait()

        # E congiunqiamo i punti A e C ai centri O1 e O2.

        a_o1_line = Line(a_point.get_center(), o1_point.get_center())
        c_o2_line = Line(c_point.get_center(), o2_point.get_center())
        self.play(Create(a_o1_line))
        self.play(Create(c_o2_line))
        self.cut_and_wait()

        # Vogliamo calcolare l'area del cuore sommando le aree dei due settori circolari e dei quattro triangoli.

        arc1 = Arc(radius=_unit, start_angle=0, angle=PI*4/3, arc_center=o1_point.get_center(), color=WHITE)
        arc2 = Arc(radius=_unit, start_angle=PI, angle=-PI*4/3, arc_center=o2_point.get_center(), color=WHITE)
        p_b_line = Line(p_point.get_center(), b_point.get_center())
        self.play(
            FadeIn(arc1),
            FadeIn(arc2),
            FadeOut(circle_1),
            FadeOut(circle_2),
            p_a_line.animate.set_color(WHITE),
            p_c_line.animate.set_color(WHITE),
            FadeIn(p_b_line),
            FadeOut(tangent),
            FadeOut(o1_p_o2_angle),
            FadeOut(o1_p_o2_value)
        )
        self.cut_and_wait()

        # Partiamo dai triangoli. Ci sono molte simmetrie in questa figura, e i triangoli sembrano essere tutti
        # congruenti. Vediamo se riusciamo a dimostrarlo.

        self.play(
            FadeOut(cuore),
            FadeIn(triangoli)
        )
        self.cut_and_wait()

        # I segmenti che congiungono i punti di tangenza ai centri sono tutti raggi, quindi sono congruenti.

        segments = [a_o1_line, radius_1, radius_2, c_o2_line]
        tics = []
        for _s in segments:
            tic = Text("//", color=YELLOW).scale(.5)
            tic.move_to(_s.get_center())
            tic.rotate(_s.get_angle())
            tics.append(tic)
        self.play(*[Write(_t) for _t in tics])
        self.cut_and_wait()

        # Grazie al teorema delle tangenti possiamo dire che:
        # - i segmenti di tangenza PA, PB e PC sono congruenti

        segments = [p_a_line, p_b_line, p_c_line]
        tildes = []
        for _s in segments:
            tilde = MathTex(r"\sim").stretch_to_fit_width(.2).set_color(GREEN).scale(2)
            tilde.move_to(_s).rotate(_s.get_angle())
            tildes.append(tilde)
        self.play(*[Write(_t) for _t in tildes])
        self.cut_and_wait()

        # - i quattro angoli in P sono congruenti

        points = [a_point.get_center(), o1_point.get_center(), b_point.get_center(), o2_point.get_center(), c_point.get_center()]
        points.reverse()
        dots = []
        for _i in range(len(points) - 1):
            dot = Dot(color=RED)
            angle = Angle.from_three_points(points[_i], p_point.get_center(), points[_i + 1], radius=.8)
            dot.move_to(angle.get_midpoint())
            dots.append(dot)
        self.play(*[Create(_d) for _d in dots])
        self.cut_and_wait()

        # - gli angoli formati dalle tangenti con i raggi sono perpendicolari.

        rights = [
            RightAngle(p_a_line, a_o1_line, length=0.4, color=PURPLE, quadrant=(-1, 1), z_index=-1),
            RightAngle(p_b_line, radius_1, length=0.4, color=PURPLE, quadrant=(-1, 1), z_index=-1),
            RightAngle(p_b_line, radius_2, length=0.4, color=PURPLE, quadrant=(-1, 1), z_index=-1),
            RightAngle(p_c_line, c_o2_line, length=0.4, color=PURPLE, quadrant=(-1, 1), z_index=-1),
            ]
        self.play(*[Create(_a) for _a in rights])
        self.cut_and_wait()

        # Da tutte queste informazioni deduciamo che i quattro triangoli sono tutti congruenti e quindi equivalenti.
        # Ci basta calcolare l'area di uno dei triangoli per conoscerle tutte e quattro.

        triangolo = Polygon(
            p_point.get_center(), b_point.get_center(), o1_point.get_center(),
            color=GREEN, fill_opacity=1, z_index=-2
        )
        self.play(
            FadeOut(triangoli),
            *[FadeOut(_t) for _t in tics],
            *[FadeOut(_t) for _t in tildes],
            *[FadeOut(_d) for _d in dots],
            *[FadeOut(_a) for _a in rights],
            FadeIn(triangolo),
        )
        self.cut_and_wait()

        # Inoltre tali triangoli sono
        # rettangoli, quindi per calcolare l'area ci basta conoscere i cateti.

        self.play(Create(rights[2]))
        self.cut_and_wait()

        # Il triangolo O1PO2 è isoscele, perché PO1 e PO2 sono congruenti, e ha l'angolo al vertice pari a 60°.

        triangolo2 = Polygon(
            p_point.get_center(), b_point.get_center(), o2_point.get_center(),
            color=GREEN_E, fill_opacity=1, z_index=-2
        )
        self.play(Create(triangolo2))
        segments = [p_o1_line, p_o2_line]
        ticss = []
        for _s in segments:
            tic = Text("///", color=YELLOW).scale(.5)
            tic.move_to(_s.get_center())
            tic.rotate(_s.get_angle())
            ticss.append(tic)
        self.play(*[Write(_t) for _t in ticss])
        self.cut_and_wait()
        self.play(Create(o1_p_o2_angle), Write(o1_p_o2_value))
        self.cut_and_wait()

        # Quindi in verità è un triangolo equilatero, e il triangolo BPO1 è metà di un triangolo equilatero.

        self.play(
            FadeOut(triangolo2),
            FadeOut(o1_p_o2_angle), FadeOut(o1_p_o2_value),
            *[FadeOut(_t) for _t in ticss]
        )
        self.cut_and_wait()

        # Il cateto BO1 è un raggio, quindi è lungo 1.
        # L'ipotenusa PO1 è lato del triangolo equilatero, doppia del cateto BO1, quindi è lunga 2,

        p_o2_value = MathTex("2").move_to(p_o1_line.get_center())
        p_o2_value.shift(.2 * rotate_vector(p_o1_line.get_unit_vector(), PI/2))
        self.play(Write(p_o2_value))
        self.cut_and_wait()

        # e il cateto BP è l'altezza del triangolo equilatero di lato 2, quindi è lunga radice di 3.

        p_b_value = MathTex(r"\sqrt{3}").move_to(p_b_line.get_center())
        p_b_value.shift(.4 * rotate_vector(p_b_line.get_unit_vector(), -PI/2))
        self.play(Write(p_b_value))
        self.cut_and_wait()

        # Possiamo quindi calcolare l'area del triangolo moltiplicando la base BO1 per l'altezza BP diviso 2,
        # che fa radice di 3 fratto 2.

        formula_area = MathTex(r"\dfrac{1 \cdot \sqrt{3}}{2}", color=YELLOW).move_to(triangolo.get_center_of_mass())
        base = radius_1_value[0][0].copy()
        base.target = formula_area[0][0]
        altezza = p_b_value.copy()
        altezza.target = formula_area[0][2:5]
        self.play(MoveToTarget(base))
        self.play(Write(formula_area[0][1]))
        self.play(MoveToTarget(altezza))
        self.play(Write(formula_area[0][5:]))
        self.cut_and_wait()
        self.add(formula_area)
        self.remove(base, altezza)

        tri = [
            [p_point.get_center(), a_point.get_center(), o1_point.get_center()],
            [p_point.get_center(), b_point.get_center(), o1_point.get_center()],
            [p_point.get_center(), b_point.get_center(), o2_point.get_center()],
            [p_point.get_center(), c_point.get_center(), o2_point.get_center()],
        ]
        aree = []
        for _i in tri:
            area = MathTex(r"\dfrac{\sqrt{3}}{2}", color=YELLOW)
            area.move_to(Polygon(*tri[1]).get_center_of_mass())
            aree.append(area)
        self.play(ReplacementTransform(formula_area, aree[1]))
        self.cut_and_wait()

        # E gli altri tre triangoli congruenti hanno la stessa area.

        self.play(
            FadeOut(triangolo),
            FadeOut(p_b_value),
            FadeOut(p_o2_value),
            FadeOut(rights[2])
        )
        self.play(
            aree[0].animate.move_to(Polygon(*tri[0]).get_center_of_mass()),
            aree[2].animate.move_to(Polygon(*tri[2]).get_center_of_mass()),
            aree[3].animate.move_to(Polygon(*tri[3]).get_center_of_mass()),
        )
        self.cut_and_wait()

        # Dobbiamo ora calcolare l'area dei due settori circolari.

        settore_1 = Difference(circle_1, triangoli, color=RED, fill_opacity=1, z_index=-5)
        settore_2 = Difference(circle_2, triangoli, color=RED, fill_opacity=1, z_index=-5)
        self.play(Create(settore_1), Create(settore_2))
        self.cut_and_wait()

        # Per simmetria è immediato osservare che sono congruenti, quindi sono anche equivalenti.

        self.play(settore_2.animate.rotate(PI/3).move_to(settore_1))
        self.play(FadeOut(settore_2))
        self.cut_and_wait()

        # Tornando per un attimo al triangolo BPO1, visto che l'angolo in P è di 30°,

        o1_p_b_angle = Angle.from_three_points(
                b_point.get_center(), p_point.get_center(), o1_point.get_center(), radius=0.6, color=BLUE)

        o1_p_b_value = Integer(
                o1_p_b_angle.get_value(degrees=True),
                unit=r"^{\circ}",
                color=BLUE,
                z_index=5).next_to(o1_p_b_angle, UP, buff=.1)

        self.play(Create(o1_p_b_angle), Write(o1_p_b_value))
        self.cut_and_wait()

        # l'angolo al centro è di 60°.

        b_o1_p_angle = Angle.from_three_points(
                p_point.get_center(), o1_point.get_center(), b_point.get_center(), radius=0.6, color=BLUE)

        b_o1_p_value = Integer(
                b_o1_p_angle.get_value(degrees=True),
                unit=r"^{\circ}",
                color=BLUE,
                z_index=5)
        b_o1_p_value.move_to(
            Angle.from_three_points(
                p_point.get_center(), o1_point.get_center(), b_point.get_center(), radius=1).get_midpoint()
        )
        self.play(Create(b_o1_p_angle), Write(b_o1_p_value))
        self.cut_and_wait()

        # Quindi l'angolo AO1B è di 120°, ovvero un terzo di angolo giro.

        b_o1_a_angle = Angle.from_three_points(
            a_point.get_center(), o1_point.get_center(), b_point.get_center(), radius=0.6, color=BLUE)

        b_o1_a_value = Integer(
            b_o1_a_angle.get_value(degrees=True),
            unit=r"^{\circ}",
            color=BLUE,
            z_index=5)
        b_o1_a_value.move_to(
            Angle.from_three_points(
                a_point.get_center(), o1_point.get_center(), b_point.get_center(), radius=1).get_midpoint()
        )
        self.play(
            ReplacementTransform(b_o1_p_angle, b_o1_a_angle),
            ReplacementTransform(b_o1_p_value, b_o1_a_value),
            FadeOut(o1_p_b_angle), FadeOut(o1_p_b_value)
        )
        self.cut_and_wait()

        # Risulta quindi che il settore circolare è 2/3 del cerchio,
        # quindi la sua area è 2/3 pi greco r quadro,

        formula_area = MathTex(r"\dfrac{2}{3} \cdot \pi \cdot r^2", color=YELLOW)
        formula_area.move_to(o1_point.get_center() + 1.5 * UP)
        self.play(Write(formula_area))
        self.cut_and_wait()

        # ma il raggio è 1,

        raggio = radius_1_value[0][0].copy()
        self.play(
            raggio.animate.move_to(formula_area[0][6]).set_color(YELLOW),
            FadeOut(formula_area[0][6])
        )
        self.cut_and_wait()

        # quindi l'area di un settore circolare è 2/3 pi greco.

        area_settore_1 = MathTex(r"\dfrac{2}{3}\pi", color=YELLOW)
        area_settore_1.move_to(o1_point.get_center() + 1.5 * UP)
        self.play(ReplacementTransform(
            VGroup(formula_area, raggio), area_settore_1
        ))
        self.cut_and_wait()

        # E lo stesso vale per l'altro settore.

        area_settore_2 = MathTex(r"\dfrac{2}{3}\pi", color=YELLOW)
        area_settore_2.move_to(o1_point.get_center() + 1.5 * UP)
        self.play(area_settore_2.animate.move_to(o2_point.get_center() + 1.5 * UP))
        self.play(
            FadeOut(settore_1),
            FadeOut(b_o1_a_angle), FadeOut(b_o1_a_value),
            FadeOut(radius_1_value), FadeOut(radius_2_value),
            FadeOut(a_label), FadeOut(b_label), FadeOut(c_label),
            FadeOut(o1_label), FadeOut(o2_label), FadeOut(p_label)
        )
        self.cut_and_wait()

        # Non ci rimane che sommare tutte le aree trovate.

        somma = MathTex(
            r"\dfrac{2}{3}\pi {{+}} \dfrac{2}{3}\pi {{+}} \dfrac{\sqrt{3}}{2} {{+}} \dfrac{\sqrt{3}}{2} {{+}} \dfrac{\sqrt{3}}{2} {{+}} \dfrac{\sqrt{3}}{2}",
            color=YELLOW
        ).move_to(cuore.get_center_of_mass() + DOWN)

        self.play(
            FadeOut(a_point), FadeOut(b_point), FadeOut(c_point),
            FadeOut(o1_point), FadeOut(o2_point), FadeOut(p_point),
            FadeOut(a_o1_line), FadeOut(radius_1), FadeOut(radius_2), FadeOut(c_o2_line),
            FadeOut(p_b_line), FadeOut(p_o1_line), FadeOut(p_o2_line),
            FadeIn(cuore),
        )
        self.play(
            area_settore_1.animate.move_to(somma[0]),
            area_settore_2.animate.move_to(somma[2]),
            aree[0].animate.move_to(somma[4]),
            aree[1].animate.move_to(somma[6]),
            aree[2].animate.move_to(somma[8]),
            aree[3].animate.move_to(somma[10]),
        )
        self.play(
            Write(somma[1]),
            Write(somma[3]),
            Write(somma[5]),
            Write(somma[7]),
            Write(somma[9]),
        )
        self.add(somma)
        self.remove(area_settore_1, area_settore_2, *aree)
        self.cut_and_wait()

        # L'area del cuore è pari a 4/3 pi greco più 2 radice di 3.
        
        totale = MathTex(r"\dfrac{4}{3}\pi + 2\sqrt{3}", color=YELLOW).scale(2).move_to(somma)
        self.play(ReplacementTransform(somma, totale))

        self.wait(30)
