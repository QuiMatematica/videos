from manim import *

DELAY = 1
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
        self.wait(1)

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

        radice_quadrata[0][2:].set_color(BLACK)

        self.play(FadeIn(radice_quadrata[0][0:2].copy()))
        self.cut_and_wait()

        numero = MathTex("317,3").scale(SCALE).move_to(radice_quadrata[0][2:])
        self.play(Write(numero))
        self.cut_and_wait()

        freccetta = Arrow(start=DOWN, end=UP, color=GOLD).move_to(numero[0][3].get_center() + DOWN)
        self.play(Create(freccetta))
        self.cut_and_wait()

        self.play(freccetta.animate.shift(LEFT))
        self.cut_and_wait()

        solo_il_3 = numero[0][0]
        self.play(solo_il_3.animate.move_to(radice_quadrata[0][2]))
        solo_il_punto = MathTex(r"\cdot").scale(SCALE).move_to(radice_quadrata[0][3])
        self.play(Write(solo_il_punto), FadeOut(freccetta))
        self.play(numero[0][1:].animate.move_to(radice_quadrata[0][4:8]))
        self.cut_and_wait()

        freccetta.move_to(numero[0][3].get_center() + DOWN)
        self.play(Create(freccetta))
        self.cut_and_wait()

        self.play(freccetta.animate.shift(RIGHT))
        self.cut_and_wait()

        solo_lo_0 = MathTex("0").scale(SCALE).move_to(radice_quadrata[0][8])
        self.play(Write(solo_lo_0))
        self.play(FadeOut(freccetta))
        self.cut_and_wait()

        self.play(Create(linea_verticale))
        self.play(Create(linea_orizzontale))
        self.cut_and_wait()

        self.play(solo_il_3.animate.set_color(GREEN))
        self.cut_and_wait()

        domanda = MathTex("?^2 < 3").scale(SCALE)
        box = SurroundingRectangle(domanda, fill_color=BLACK, fill_opacity=1, buff=.5)

        self.play(Create(box))
        self.play(Write(domanda[0][0:3]))
        copia_del_3 = solo_il_3.copy()
        self.play(copia_del_3.animate.move_to(domanda[0][3]))
        self.cut_and_wait()

        risposta_1 = MathTex("1", color=RED).scale(SCALE).move_to(domanda[0][0])
        self.play(ReplacementTransform(domanda[0][0], risposta_1))
        self.cut_and_wait()

        self.play(risposta_1.animate.move_to(risultato[0][0]))
        self.play(FadeOut(domanda[0][1:]), FadeOut(box), FadeOut(copia_del_3))
        self.cut_and_wait()

        copia_per_quadrato = risposta_1.copy()
        quadrato_dell_uno = MathTex("1^2")


        self.wait(30)
