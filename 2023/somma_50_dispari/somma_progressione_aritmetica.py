from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        title = Title("Somma degli elementi di una progressione aritmetica").set_color(GREEN)

        max_x = 14
        n_colonne = 13
        shift_x = (n_colonne - 1) / 2
        max_y = 4

        riga2 = VGroup(
            MathTex("a_1"),
            MathTex("+"),
            MathTex("a_2"),
            MathTex("+"),
            MathTex("a_3"),
            MathTex("+"),
            MathTex(r"\dots"),
            MathTex("+"),
            MathTex("a_{n-2}"),
            MathTex("+"),
            MathTex("a_{n-1}"),
            MathTex("+"),
            MathTex("a_n"),
        )

        riga3 = VGroup(
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+"),
            MathTex("+")
        )

        riga4 = VGroup(
            MathTex("a_n"),
            MathTex(""),
            MathTex("a_{n-1}"),
            MathTex(""),
            MathTex("a_{n-2}"),
            MathTex(""),
            MathTex(r"\dots"),
            MathTex(""),
            MathTex("a_3"),
            MathTex(""),
            MathTex("a_2"),
            MathTex(""),
            MathTex("a_1"),
        )

        riga5 = VGroup(
            Line(start=ORIGIN, end=RIGHT),
            MathTex(""),
            Line(start=ORIGIN, end=RIGHT),
            MathTex(""),
            Line(start=ORIGIN, end=RIGHT),
            MathTex(""),
            MathTex(""),
            MathTex(""),
            Line(start=ORIGIN, end=RIGHT),
            MathTex(""),
            Line(start=ORIGIN, end=RIGHT),
            MathTex(""),
            Line(start=ORIGIN, end=RIGHT),
        )

        scala_riga_6 = .8
        riga6 = VGroup(
            MathTex("a_1 + a_n"),
            MathTex("+"),
            MathTex("a_2 + a_{n-1}"),
            MathTex("+"),
            MathTex("a_3 + a_{n-2}"),
            MathTex("+"),
            MathTex(r"\dots"),
            MathTex("+"),
            MathTex("a_{n-2} + a_3"),
            MathTex("+"),
            MathTex("a_{n-1} + a_2"),
            MathTex("+"),
            MathTex("a_n + a_1"),
        ).scale(scala_riga_6)

        tabella = VGroup(riga2, riga3, riga4, riga5, riga6)

        n_righe = len(tabella)
        shift_y = (n_righe - 1) / 2

        for _riga in range(n_righe):
            for _colonna in range(n_colonne):
                tabella[_riga][_colonna].move_to(
                    [(_colonna - shift_x) * max_x / n_colonne, (shift_y - _riga) * max_y / n_righe, 0])

        # tabella.shift(UP)

        riga_2_mostrata = VGroup()
        for _i in range(7):
            riga_2_mostrata.add(riga2[_i * 2])

        self.play(Write(riga_2_mostrata))
        self.cut_and_wait()

        buff = .1
        _y = riga2[0].get_top()[1]+buff
        for _i in range(6):
            start = riga2[_i * 2].get_top()+[+buff, 0, 0]
            start[1] = _y
            end = riga2[_i * 2 + 2].get_top()+[-buff, 0, 0]
            end[1] = _y
            arco = CurvedArrow(
                start_point=start,
                end_point=end,
                angle=-TAU / 6,
                color=YELLOW)
            self.play(Create(arco))
            ragione = MathTex("+r", color=YELLOW).next_to(arco, UP, buff=buff)
            self.play(Write(ragione))
        self.cut_and_wait()

        self.play(Create(title))
        self.cut_and_wait()

        segni_piu = VGroup()
        for _i in range(6):
            segni_piu.add(riga2[_i * 2 + 1])
        self.play(Write(segni_piu))
        self.cut_and_wait()

        inversioni = []
        for _i in range(7):
            inversione = riga2[_i * 2].copy()
            inversione.target = riga4[12 - _i * 2]
            inversioni.append(inversione)

        self.play(*[MoveToTarget(_i) for _i in inversioni])
        self.add(riga4)
        self.remove(*inversioni)
        self.cut_and_wait()

        spostamenti_piu = []
        for _i in range(3):
            spostamento = riga2[_i * 2 + 1]
            spostamento.target = riga3[_i * 2]
            spostamenti_piu.append(spostamento)
            spostamento = riga2[11 - _i * 2]
            spostamento.target = riga3[12 - _i * 2]
            spostamenti_piu.append(spostamento)

        self.play(*[MoveToTarget(_s) for _s in spostamenti_piu])
        self.cut_and_wait()

        self.play(Write(riga5))
        self.cut_and_wait()

        riga6_visualizzata = VGroup()
        for _i in range(7):
            riga6_visualizzata.add(riga6[_i * 2])
        self.play(Write(riga6_visualizzata))
        self.cut_and_wait()

        self.play(Flash(riga2[2]))
        self.play(Transform(riga2[2], MathTex(r"a_1 + r").move_to(riga2[2])))
        self.cut_and_wait()

        self.play(Flash(riga4[2]))
        arco = CurvedArrow(
            start_point=riga4[0].get_top() + [+buff, +buff, 0],
            end_point=riga4[2].get_top() + [-buff, +buff, 0],
            angle=-TAU / 6,
            color=YELLOW)
        self.play(Create(arco))
        ragione = MathTex("-r", color=YELLOW).next_to(arco, UP, buff=buff)
        self.play(Write(ragione))
        self.play(Transform(riga4[2], MathTex(r"a_n - r").move_to(riga4[2])))
        self.cut_and_wait()

        self.play(Transform(riga6[2], MathTex(r"a_1 + r + a_n - r").scale(scala_riga_6).move_to(riga6[2])))
        self.play(Transform(riga6[2], MathTex(r"a_1 + a_n").scale(scala_riga_6).move_to(riga6[2])))
        self.cut_and_wait()

        self.play(
            Transform(riga2[4], MathTex(r"a_1 + 2r").move_to(riga2[4])),
            Transform(riga2[8], MathTex(r"a_n -2r").move_to(riga2[8])),
            Transform(riga2[10], MathTex(r"a_n - r").move_to(riga2[10])),
            Transform(riga4[4], MathTex(r"a_n - 2r").move_to(riga4[4])),
            Transform(riga4[8], MathTex(r"a_1 + 2r").move_to(riga4[8])),
            Transform(riga4[10], MathTex(r"a_1 + r").move_to(riga4[10])),
        )

        for _i in range(5):
            if _i != 1:
                self.play(Transform(riga6[_i*2+4], MathTex(r"a_1 + a_n").scale(scala_riga_6).move_to(riga6[_i*2+4])))
        self.cut_and_wait()

        graffona = Brace(riga6, color=YELLOW)
        self.play(Create(graffona))

        moltiplicazione = MathTex(r"(a_1 + a_n) \cdot n").next_to(graffona, DOWN)
        self.play(Write(moltiplicazione))
        self.cut_and_wait()

        self.play(Flash(riga2[0]), Flash(riga4[12]))
        self.play(Flash(riga2[2]), Flash(riga4[10]))
        self.play(Flash(riga2[4]), Flash(riga4[8]))
        self.cut_and_wait()

        finale1 = MathTex(r"a_1 + a_2 + \dots + a_{n-1} + a_n = \dfrac{(a_1 + a_n) \cdot n}{2}", color=YELLOW).next_to(graffona, DOWN)
        self.play(
            FadeOut(moltiplicazione),
            FadeIn(finale1),
        )
        self.cut_and_wait()

        self.play(Flash(finale1[0][19:21]))
        self.cut_and_wait()
        self.play(Flash(finale1[0][22:24]))
        self.cut_and_wait()
        self.play(Flash(finale1[0][26]))
        self.cut_and_wait()
        self.play(Flash(finale1[0][28]))

        self.wait(30)
