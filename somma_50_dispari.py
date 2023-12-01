from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        max_x = 14
        n_colonne = 17
        shift_x = (n_colonne - 1) / 2
        max_y = 8

        riga1 = VGroup(
            Tex("1°"),
            MathTex(""),
            Tex("2°"),
            MathTex(""),
            Tex("3°"),
            MathTex(""),
            Tex("4°"),
            MathTex(""),
            MathTex(r"\dots"),
            MathTex(""),
            Tex("47°"),
            MathTex(""),
            Tex("48°"),
            MathTex(""),
            Tex("49°"),
            MathTex(""),
            Tex("50°"),
        )

        riga2 = VGroup(
            MathTex("1"),
            MathTex("+"),
            MathTex("3"),
            MathTex("+"),
            MathTex("5"),
            MathTex("+"),
            MathTex("7"),
            MathTex("+"),
            MathTex(r"\dots"),
            MathTex("+"),
            MathTex("93"),
            MathTex("+"),
            MathTex("95"),
            MathTex("+"),
            MathTex("97"),
            MathTex("+"),
            MathTex("99"),
        )

        riga3 = VGroup(
            MathTex("+"),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex(""),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex("+"),
            MathTex(""),
            MathTex("+")
        )

        riga4 = VGroup(
            MathTex("99"),
            MathTex(""),
            MathTex("97"),
            MathTex(""),
            MathTex("95"),
            MathTex(""),
            MathTex("93"),
            MathTex(""),
            MathTex(r"\dots"),
            MathTex(""),
            MathTex("7"),
            MathTex(""),
            MathTex("5"),
            MathTex(""),
            MathTex("3"),
            MathTex(""),
            MathTex("1"),
        )

        tabella = VGroup(riga1, riga2, riga3, riga4)

        n_righe = len(tabella)
        shift_y = (n_righe - 1) / 2

        for _riga in range(n_righe):
            for _colonna in range(n_colonne):
                tabella[_riga][_colonna].move_to([(_colonna - shift_x) * max_x / n_colonne, (_riga - shift_y) * max_y / n_righe, 0])


        riga_2_mostrata = VGroup()
        for _i in range(n_colonne):
            if (_i % 2 == 1) | (_i == ((n_colonne - 1)/2)):
                riga_2_mostrata.add(riga2[_i])

        self.play(Write(riga_2_mostrata))
        self.cut_and_wait()

        for _i in range(4):
            posizione = riga1[_i * 2]
            dispari = riga2[_i * 2]
            self.play(Write(posizione))
            self.play(Write(dispari))
            self.cut_and_wait()
            riga_2_mostrata.add(dispari)

        ultime_posizioni = VGroup()
        for _i in range(4):
            ultime_posizioni.add(riga1[_i * 2 + 10])
        self.play(Write(ultime_posizioni))
        self.cut_and_wait()

        doppio_riga1 = VGroup(
            MathTex("2"),
            MathTex(""),
            MathTex("4"),
            MathTex(""),
            MathTex("6"),
            MathTex(""),
            MathTex("8"),
            MathTex(""),
            MathTex(""),
            MathTex(""),
            MathTex("94"),
            MathTex(""),
            MathTex("96"),
            MathTex(""),
            MathTex("98"),
            MathTex(""),
            MathTex("100"),
        )
        for _i in range(n_colonne):
            doppio_riga1[_i].move_to(riga2[_i].get_center())

        shift_amount = riga3.get_center() - riga2.get_center()
        self.play(riga_2_mostrata.animate.shift(shift_amount))
        for _i in range(4):
            riga2[_i * 2 + 10].shift(shift_amount)

        doppi_mostrati = VGroup()
        for _i in range(4):
            doppio = riga1[_i * 2].copy()
            doppio.target = doppio_riga1[_i * 2]
            doppi_mostrati.add(doppio)

        self.play(*[MoveToTarget(_d) for _d in doppi_mostrati])
        self.cut_and_wait()

        doppi_meno_uno_mostrati = VGroup()
        for _i in range(4):
            doppio_meno_uno = doppi_mostrati[_i].copy()
            doppio_meno_uno.target = riga2[_i * 2]
            doppi_meno_uno_mostrati.add(doppio_meno_uno)

        self.play(*[MoveToTarget(_d) for _d in doppi_meno_uno_mostrati])
        self.cut_and_wait()

        doppi_mostrati_2 = VGroup()
        for _i in range(4):
            doppio = riga1[_i * 2 + 10].copy()
            doppio.target = doppio_riga1[_i * 2 + 10]
            doppi_mostrati_2.add(doppio)

        self.play(*[MoveToTarget(_d) for _d in doppi_mostrati_2])
        self.cut_and_wait()

        doppi_meno_uno_mostrati_2 = VGroup()
        for _i in range(4):
            doppio_meno_uno = doppi_mostrati_2[_i].copy()
            doppio_meno_uno.target = riga2[_i * 2 + 10]
            doppi_meno_uno_mostrati_2.add(doppio_meno_uno)

        self.play(*[MoveToTarget(_d) for _d in doppi_meno_uno_mostrati_2])
        for _i in range(4):
            elemento = riga2[_i * 2 + 10]
            self.add(elemento)
            riga_2_mostrata.add(elemento)
        self.cut_and_wait()

        self.remove(*doppi_meno_uno_mostrati, *doppi_meno_uno_mostrati_2)
        self.play(*[FadeOut(_d) for _d in doppi_mostrati], *[FadeOut(_d) for _d in doppi_mostrati_2])
        self.play(riga_2_mostrata.animate.shift(-shift_amount))

        inversioni = []
        for _i in range(4):
            inversione = riga2[_i * 2].copy()
            inversione.target = riga4[16 - _i * 2]
            inversioni.append(inversione)
            inversione = riga2[16 - _i * 2].copy()
            inversione.target = riga4[_i * 2]
            inversioni.append(inversione)

        self.play(*[MoveToTarget(_i) for _i in inversioni])
        self.cut_and_wait()

        spostamenti_piu = []
        for _i in range(4):
            spostamento = riga2[_i * 2 + 1]
            spostamento.target = riga3[_i * 2]
            spostamenti_piu.append(spostamento)
            spostamento = riga2[15 - _i * 2]
            spostamento.target = riga3[16 - _i * 2]
            spostamenti_piu.append(spostamento)

        self.play(*[MoveToTarget(_s) for _s in spostamenti_piu])
        self.cut_and_wait()

        self.wait(30)
