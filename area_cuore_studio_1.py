import math

from manim import *

DELAY = 1

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
        tangent_1 = Line(p_point.get_center(), t1_coordinates, color=RED)
        tangent_2 = Line(p_point.get_center(), t2_coordinates, color=RED)
        self.add(tangent_1, tangent_2)

        # Quanto vale l’area del cuore ottenuto?
        triangoli = Polygon(
            t1_coordinates,
            o1_point.get_center(),
            o2_point.get_center(),
            t2_coordinates,
            p_point.get_center(), color=GREEN, fill_opacity=1, z_index=-1)
        cuore = Union(circle_1, circle_2)
        diff = Difference(triangoli, cuore)
        cuore = Union(cuore, diff, color=BLUE_E, fill_opacity=1, z_index=-1)
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
            tangent_1.animate.set_color(WHITE),
            tangent_2.animate.set_color(WHITE),
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

        #
        # I segmenti che congiungono i punti di tangenza ai centri sono tutti raggi, quindi sono congruenti.
        #
        # Grazie al teorema delle tangenti possiamo dire che:
        # - i segmenti di tangenza PA, PB e PC sono congruenti
        # - i quattro angoli in P sono congruenti
        # - gli angoli formati dalle tangenti con i raggi sono perpendicolari.
        #
        # Da tutte queste informazioni deduciamo che i quattro triangoli sono tutti congruenti e quindi equivalenti. Ci basta calcolare l'area di uno dei triangoli per conoscerle tutte e quattro. Inoltre tali triangoli sono rettangoli, quindi per calcolare l'area ci basta conoscere i cateti.
        #
        # Il triangolo O1PO2 è isoscele, perché PO1 e PO2 sono congruenti, e ha l'angolo al vertice pari a 60°. Quindi in verità è un triangolo equilatero, e il triangolo BPO1 è metà di un triangolo equilatero. Il cateto BO1 è un raggio, quindi è lungo 1, e il cateto BP è l'altezza del triangolo equilatero di lato 2, quindi è lunga radice di 3.
        #
        # Possiamo quindi calcolare l'area del triangolo moltiplicando la base BO1 per l'altezza BP diviso 2, che fa radice di 3 fratto 2. E gli altri tre triangoli congruenti hanno la stessa area.
        #
        # Dobbiamo ora calcolare l'area dei due settori circolari. Per simmetria è immediato osservare che sono congruenti, quindi sono anche equivalenti.
        # Tornando per un attimo al triangolo BPO1, visto che l'angolo in P è di 30°, l'angolo al centro è di 60°. Quindi l'angolo AO1B è di 120°, ovvero un terzo di angolo giro.
        # Risulta quindi che il settore circolare è 2/3 del cerchio, quindi la sua area è 2/3 pi greco r quadro, ma il raggio è 1, quindi l'area di un settore circolare è 2/3 pi greco.
        # E lo stesso vale per l'altro settore.
        #
        # Non ci rimane che sommare tutte le aree trovate. L'area del cuore è pari a 4/3 pi greco più 2 radice di 3.

        self.wait(30)
