from manim import *

DELAY = 30
LINE_STROKE = 2
SHIFT_DOWN = .6 * DOWN
SBORDO_LINE = .1 * RIGHT
SCALE = 1.7


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        radice_quadrata = MathTex(r"\sqrt{3{\cdot}17,30\,}").to_edge(UP)
        self.add(radice_quadrata)

        linea_verticale = Line(
            radice_quadrata.get_right() + .3 * UP,
            radice_quadrata.get_right() + 3.8 * DOWN,
            stroke_width=LINE_STROKE
        )

        risultato = MathTex("17,8").move_to(radice_quadrata[0][2:]).shift(1.45 * RIGHT)

        l_sn_1 = MathTex("1").move_to(radice_quadrata[0][2].get_center() + SHIFT_DOWN)
        l_sn_2_a = MathTex("2").move_to(l_sn_1.get_center() + SHIFT_DOWN)
        l_sn_2_b = MathTex("17").move_to((radice_quadrata[0][4:6].get_center()[0], l_sn_2_a.get_center()[1], 0))
        l_sn_3_a = MathTex("1").move_to(l_sn_2_a.get_center() + SHIFT_DOWN)
        l_sn_3_b = MathTex("89").move_to((radice_quadrata[0][4:6].get_center()[0], l_sn_3_a.get_center()[1], 0))
        l_sn_4_a = MathTex("28").move_to(l_sn_3_b.get_center() + SHIFT_DOWN)
        l_sn_4_b = MathTex("30").move_to((radice_quadrata[0][7:9].get_center()[0], l_sn_4_a.get_center()[1], 0))
        l_sn_5_a = MathTex("27").move_to(l_sn_4_a.get_center() + SHIFT_DOWN)
        l_sn_5_b = MathTex("84").move_to((radice_quadrata[0][7:9].get_center()[0], l_sn_5_a.get_center()[1], 0))
        l_sn_6_a = MathTex("0,").move_to(radice_quadrata[0][5:7].get_center() + 6 * SHIFT_DOWN)
        l_sn_6_b = MathTex("46").move_to((radice_quadrata[0][7:9].get_center()[0], l_sn_6_a.get_center()[1], 0) + .04 * UP)

        h_1 = Line(
            (l_sn_1.get_left() + l_sn_2_a.get_left()) / 2 - SBORDO_LINE,
            (l_sn_1.get_right() + l_sn_2_a.get_right()) / 2 + SBORDO_LINE,
            stroke_width=LINE_STROKE
        )
        h_2 = Line(
            (l_sn_3_a.get_left()[0], (l_sn_3_b.get_right() + l_sn_4_a.get_right())[1] / 2, 0) - SBORDO_LINE,
            (l_sn_3_b.get_right() + l_sn_4_a.get_right()) / 2 + SBORDO_LINE,
            stroke_width=LINE_STROKE
        )
        h_3 = Line(
            (l_sn_5_a.get_left()[0], (l_sn_5_b.get_right() + l_sn_6_b.get_right())[1] / 2, 0) - SBORDO_LINE,
            (l_sn_5_b.get_right() + l_sn_6_b.get_right()) / 2 + SBORDO_LINE,
            stroke_width=LINE_STROKE
        )
        l_dx_1 = MathTex(r"29 \cdot 9 = 261").move_to(risultato.get_center() + SHIFT_DOWN + .77 * RIGHT + .02 * UP)
        l_dx_2 = MathTex(r"28 \cdot 8 = 224").move_to(l_dx_1.get_center() + SHIFT_DOWN)
        l_dx_3 = MathTex(r"27 \cdot 7 = 189").move_to(l_dx_2.get_center() + SHIFT_DOWN)
        l_dx_4 = MathTex(r"349 \cdot 9 = 3141").move_to(l_dx_3.get_center() + SHIFT_DOWN + .23 * RIGHT)
        l_dx_5 = MathTex(r"348 \cdot 8 = 2784").move_to(l_dx_4.get_center() + SHIFT_DOWN)

        h_4 = Line(
            (l_dx_3.get_left() + l_dx_4.get_left()) / 2 - SBORDO_LINE,
            (l_dx_4.get_right()[0], (l_dx_3.get_left() + l_dx_4.get_left())[1] / 2, 0) + SBORDO_LINE,
            stroke_width=LINE_STROKE
        )

        s = radice_quadrata.get_right() + .3 * DOWN

        linea_orizzontale = Line(
            s,
            (h_4.get_right()[0], s[1], 0),
            stroke_width=LINE_STROKE
        )

        finale = VGroup(
            radice_quadrata, risultato,
            linea_verticale, linea_orizzontale,
            l_sn_1, l_sn_2_a, l_sn_2_b, l_sn_3_a, l_sn_3_b, l_sn_4_a, l_sn_4_b, l_sn_5_a, l_sn_5_b, l_sn_6_a, l_sn_6_b,
            h_1, h_2, h_3, h_4,
            l_dx_1, l_dx_2, l_dx_3, l_dx_4, l_dx_5
        ).move_to(ORIGIN).scale(SCALE)

        self.add(
            radice_quadrata,
            linea_verticale,
            linea_orizzontale,
            risultato[0][0:2],
            l_sn_1,
            h_1,
            l_sn_2_a, l_sn_2_b,
            l_sn_3_a, l_sn_3_b,
            h_2,
            l_sn_4_a,
            l_dx_1, l_dx_2, l_dx_3
        )

        self.play(Write(risultato[0][2]))
        self.cut_and_wait()

        position = l_sn_4_b.get_center()
        l_sn_4_b.move_to(radice_quadrata[0][7:9].get_center())
        self.play(l_sn_4_b.animate.move_to(position))
        self.play(l_sn_4_a.animate.set_color(GREEN), l_sn_4_b.animate.set_color(GREEN))
        self.cut_and_wait()

        copia_17 = risultato[0][0:2].copy()
        copia_17.target = l_dx_4[0][0:2]
        self.play(Create(h_4))
        self.play(MoveToTarget(copia_17))
        self.cut_and_wait()

        self.play(Write(l_dx_4[0][2:5]))
        self.cut_and_wait()

        self.play(Write(l_dx_4[0][5:]))
        self.cut_and_wait()

        copia_per_9 = l_dx_4[0][:5].copy()
        copia_per_9.target = l_dx_5[0][0:5]
        self.play(MoveToTarget(copia_per_9))
        self.cut_and_wait()

        self.play(Write(l_dx_5[0][5:]))
        self.cut_and_wait()

        self.play(l_dx_5[0][2].animate.set_color(RED), l_dx_5[0][4].animate.set_color(RED))
        self.cut_and_wait()

        copia_1 = l_dx_5[0][2].copy()
        copia_2 = l_dx_5[0][4].copy()
        self.play(copia_1.animate.move_to(risultato[0][3]), copia_2.animate.move_to(risultato[0][3]))
        self.cut_and_wait()

        posizione_27 = l_sn_5_a.get_center()
        posizione_84 = l_sn_5_b.get_center()
        l_sn_5_a.move_to(l_dx_5[0][6:8])
        l_sn_5_b.move_to(l_dx_5[0][8:10])
        self.play(
            l_sn_5_a.animate.move_to(posizione_27),
            l_sn_5_b.animate.move_to(posizione_84)
        )
        self.cut_and_wait()

        self.play(Create(h_3))
        self.play(Write(l_sn_6_b))
        self.cut_and_wait()

        self.play(Write(l_sn_6_a))
        self.cut_and_wait()

        verifica = MathTex("17,8^2 + 0,46 = 317,3").scale(SCALE)
        box = SurroundingRectangle(verifica, fill_color=BLACK, fill_opacity=1, buff=.5)
        self.play(Create(box))
        copia_risultato_per_verifica = risultato.copy()
        self.play(copia_risultato_per_verifica.animate.move_to(verifica[0][0:4]))
        self.play(Write(verifica[0][4]))
        self.play(Write(verifica[0][5]))
        copia_resto_per_verifica = VGroup(l_sn_6_a.copy(), l_sn_6_b.copy())
        copia_resto_per_verifica.target = verifica[0][6:10]
        self.play(MoveToTarget(copia_resto_per_verifica))
        self.play(Write(verifica[0][10]))
        copia_argomento_per_verifica = radice_quadrata[0][2:8].copy()
        copia_argomento_per_verifica.target = verifica[0][11:]
        self.play(MoveToTarget(copia_argomento_per_verifica))
        self.cut_and_wait()

        self.play(
            FadeOut(box),
            FadeOut(copia_risultato_per_verifica),
            FadeOut(copia_resto_per_verifica),
            FadeOut(copia_argomento_per_verifica),
            FadeOut(verifica[0][4:6]),
            FadeOut(verifica[0][10]),
        )
        self.play(l_sn_4_a.animate.set_color(WHITE), l_sn_4_b.animate.set_color(WHITE),
                  copia_1.animate.set_color(WHITE), copia_2.animate.set_color(WHITE),
                  l_dx_5[0][2].animate.set_color(WHITE), l_dx_5[0][4].animate.set_color(WHITE))

        self.wait(30)
