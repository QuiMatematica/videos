from manim import *

DELAY = 1


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
        ).scale(.8)

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

        differenze = VGroup(
            MathTex(""),
            MathTex("a_2 - a_1"),
            MathTex("="),
            MathTex("a_3 - a_2"),
            MathTex("="),
            MathTex("\dots"),
            MathTex("="),
            MathTex("\dots"),
            MathTex("="),
            MathTex("a_{n-1} - a_{n-2}"),
            MathTex("="),
            MathTex("a_n - a_{n-1}"),
            MathTex(""),
        ).scale(.7)
        for _i in range(n_colonne):
            differenze[_i].move_to(riga3[_i].get_center())
        self.play(Write(differenze))
        self.cut_and_wait()

        self.play(Create(title))
        self.cut_and_wait()

        self.play(FadeOut(differenze))

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

        alterazioni_riga6 = []
        for _i in range(6):
            alterato = riga6[0].copy()
            alterazioni_riga6.append(alterato.animate.move_to(riga6[_i * 2 + 2]))
            alterazioni_riga6.append(FadeOut(riga6[_i * 2 + 2]))
        self.play(*alterazioni_riga6)

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
