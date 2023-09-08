from manim import *

DELAY = 1

LINE_DISTANCE_RATIO = .5
POINT_DISTANCE_RATIO = LINE_DISTANCE_RATIO * .7

COORD_FUOCO = ORIGIN
Y_DIRETTRICE = 2 * DOWN

FUOCO = Dot(COORD_FUOCO)
DIRETTRICE = Line(start=8 * LEFT + Y_DIRETTRICE, end=8 * RIGHT + Y_DIRETTRICE)

ASSE = Line(start=4 * UP, end=4 * DOWN, color=WHITE)
VERTICE = Dot(Y_DIRETTRICE / 2, color=YELLOW)
D = Dot(Y_DIRETTRICE)


def get_p_point(h_point, m_point):
    h_coord = h_point.get_center()
    m_coord = m_point.get_center()

    x_h = h_coord[0]
    y_h = h_coord[1]

    x_m = m_coord[0]
    y_m = m_coord[1]

    x_p = x_h
    y_p = (x_h - x_m) * (x_h - x_m) / (y_m - y_h) + y_m
    p_coord = [x_p, y_p, 0]

    return Dot(p_coord, color=YELLOW, z_index=10)



class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        self.play(Create(FUOCO))
        self.play(Write(MathTex("F").next_to(FUOCO, POINT_DISTANCE_RATIO * DL)))

        self.play(Create(DIRETTRICE))
        self.play(Write(MathTex("d").next_to(DIRETTRICE, LINE_DISTANCE_RATIO * DOWN).shift(6.8 * LEFT)))

        self.cut_and_wait()

        self.play(Create(ASSE))
        self.play(Write(MathTex("a").next_to(ASSE, LINE_DISTANCE_RATIO * LEFT).shift(3.8 * UP)))

        self.cut_and_wait()

        self.play(Create(D))
        self.play(Write(MathTex("D").next_to(D, POINT_DISTANCE_RATIO * DL)))

        self.cut_and_wait()

        self.play(Create(VERTICE))
        self.play(Write(MathTex("V", color=YELLOW).next_to(VERTICE, POINT_DISTANCE_RATIO * DL)))

        self.cut_and_wait()

        segnetti_1 = Tex("//", color=RED).scale(.5).rotate(PI / 2).move_to((FUOCO.get_center() + VERTICE.get_center()) / 2)
        segnetti_2 = segnetti_1.copy().move_to((D.get_center() + VERTICE.get_center()) / 2)

        self.play(Write(segnetti_1), Write(segnetti_2))

        self.cut_and_wait()

        self.play(FadeOut(segnetti_1), FadeOut(segnetti_2))

        self.cut_and_wait()

        h_point = D.copy().set_color(RED)
        h_point_label = MathTex("H", color=RED).next_to(h_point, POINT_DISTANCE_RATIO * DL)

        self.play(Create(h_point), Write(h_point_label))

        h_point.add_updater(lambda point: point.move_to(Y_DIRETTRICE + 6 * np.sin(tracker.get_value()) * RIGHT))
        h_point_label.add_updater(lambda label: label.next_to(h_point, POINT_DISTANCE_RATIO * DL))

        tracker = ValueTracker()

        self.play(tracker.animate.set_value(9), run_time=5, rate_func=linear)
        self.cut_and_wait()

        h_point.clear_updaters()
        h_point_label.clear_updaters()

        # Costruzione LUNGA START

        fh = Line(start=FUOCO.get_center(), end=h_point.get_center(), color=RED, z_index=-1)
        self.play(Create(fh))
        self.cut_and_wait()

        m_point = Dot((FUOCO.get_center() + h_point.get_center()) / 2, color=RED)
        m_point_label = MathTex("M", color=RED).next_to(m_point, POINT_DISTANCE_RATIO * DL)
        self.play(Create(m_point), Write(m_point_label))
        self.cut_and_wait()

        perp = perpendicular_bisector([FUOCO.get_center(), h_point.get_center()])
        pm = Line(start=perp[0], end=perp[1], color=RED, z_index=-1).scale(2)
        self.play(Create(pm))
        self.cut_and_wait()

        ph = Line(start=h_point.get_center() + 7 * UP, end=h_point.get_center() + 2 * DOWN, color=RED, z_index=-1)
        self.play(Create(ph))
        self.cut_and_wait()

        p_point = get_p_point(h_point, m_point)
        p_point_label = MathTex("P", color=YELLOW, z_index=10).next_to(p_point, POINT_DISTANCE_RATIO * DL)
        self.play(Create(p_point), Write(p_point_label))

        pf = Line(start=p_point.get_center(), end=FUOCO.get_center(), color=RED, z_index=-1)
        self.play(Create(pf))
        self.cut_and_wait()

        # Costruzione LUNGA END

        segnetti_1 = Tex("//", color=RED).scale(.5)
        segnetti_2 = segnetti_1.copy()
        segnetti_1.rotate(pf.get_angle()).move_to(pf.get_center())
        segnetti_2.rotate(ph.get_angle()).move_to((h_point.get_center() + p_point.get_center()) / 2)

        self.play(Write(segnetti_1), Write(segnetti_2))
        self.cut_and_wait()

        self.play(FadeOut(segnetti_1), FadeOut(segnetti_2))
        self.cut_and_wait()

        # Mega animazione START

        self.para_min = h_point.get_center()[0]
        self.para_max = h_point.get_center()[0]

        # self.para_min = h_point.get_center()[0] - 0.1
        # self.para_max = h_point.get_center()[0] + 0.1

        parabola = FunctionGraph(
            lambda t: (t**2 - Y_DIRETTRICE[1]**2 - COORD_FUOCO[1]**2) / (2 * COORD_FUOCO[1] - 2 * Y_DIRETTRICE[1]),
            color=YELLOW,
            x_range=[self.para_min, self.para_max]
        )
        self.add(parabola)

        def update_perpendicula(old):
            perp = perpendicular_bisector([FUOCO.get_center(), h_point.get_center()])
            old.become(Line(start=perp[0], end=perp[1], color=RED, z_index=-1).scale(2))

        def update_parabola(old):
            x_h = 6 * np.sin(tracker.get_value())
            if x_h < self.para_min:
                self.para_min = x_h
            if x_h > self.para_max:
                self.para_max = x_h
            old.become(FunctionGraph(
                lambda t: (t**2 - Y_DIRETTRICE[1]**2 - COORD_FUOCO[1]**2) / (2 * COORD_FUOCO[1] - 2 * Y_DIRETTRICE[1]),
                color=YELLOW,
                x_range=[self.para_min, self.para_max]
            ))

        h_point.add_updater(lambda point: point.move_to(Y_DIRETTRICE + 6 * np.sin(tracker.get_value()) * RIGHT))
        h_point_label.add_updater(lambda label: label.next_to(h_point, POINT_DISTANCE_RATIO * DL))
        fh.add_updater(lambda old: old.become(Line(start=FUOCO.get_center(), end=h_point.get_center(), color=RED, z_index=-1)))
        m_point.add_updater(lambda old: old.move_to((FUOCO.get_center() + h_point.get_center()) / 2))
        m_point_label.add_updater(lambda label: label.next_to(m_point, POINT_DISTANCE_RATIO * DL))
        pm.add_updater(lambda old: update_perpendicula(old))
        ph.add_updater(lambda old: old.become(Line(start=h_point.get_center() + 7 * UP, end=h_point.get_center() + 2 * DOWN, color=RED, z_index=-1)))
        p_point.add_updater(lambda old: old.move_to(get_p_point(h_point, m_point)))
        p_point_label.add_updater(lambda old: old.next_to(p_point, POINT_DISTANCE_RATIO * DL))
        pf.add_updater(lambda old: old.become(Line(start=p_point.get_center(), end=FUOCO.get_center(), color=RED, z_index=-1)))

        parabola.add_updater(lambda old: update_parabola(old))

        self.play(tracker.animate.set_value(15.3), run_time=5, rate_func=linear)
        self.cut_and_wait()

        h_point.clear_updaters()
        h_point_label.clear_updaters()
        fh.clear_updaters()
        m_point.clear_updaters()
        m_point_label.clear_updaters()
        pm.clear_updaters()
        ph.clear_updaters()
        p_point.clear_updaters()
        p_point_label.clear_updaters()
        pf.clear_updaters()

        parabola.clear_updaters()

        # Mega animazione END

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

