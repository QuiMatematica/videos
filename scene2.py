from manim import *

from qmath import Tartaglia
from object import *
from util import *


class Scene(MovingCameraScene):

    config.max_files_cached = 200

    def construct(self):
        delay = 1

        faces = [HEAD, HEAD, CROSS, CROSS, CROSS, CROSS]
        points = [
            6 * LEFT + 3 * UP,
            4.5 * LEFT + 3 * UP,
            3 * LEFT + 3 * UP,
            3 * RIGHT + 3 * UP,
            4.5 * RIGHT + 3 * UP,
            6 * RIGHT + 3 * UP
        ]
        assert len(faces) == len(points), 'Faces <> points'

        coins = [Coin(face=faces[_i]).scale(.4).move_to(points[_i]) for _i in range(len(points))]

        self.play(*[SpinInFromNothing(x, angle=2 * PI, run_time=1) for x in coins])
        self.wait(delay)
        self.next_section()

        six0 = MathTex(r"(t + c)^6 = 1").move_to(3 * UP)
        set_color(six0, 1, color=RED)
        set_color(six0, 3, color=GREEN)
        self.play(Write(six0))
        self.wait(delay)
        self.next_section()

        tartaglia = Tartaglia(7)

        # Facciamo un velocissimo ripasso di come si costruire il triangolo di Tartaglia.
        # Si parte da un singolo 1, che ne rappresenta il vertice.

        surroundings = [SurroundingRectangle(tartaglia[0][0])]
        self.play(*[Create(s) for s in surroundings])
        self.play(Write(tartaglia[0][0]))
        self.play(*[Uncreate(s) for s in surroundings])
        self.wait(delay)
        self.next_section()

        # Nella riga successiva dobbiamo scrivere due elementi.
        # Lungo i bordi del triangolo gli elementi sono sempre uguali ad 1.

        surroundings = [SurroundingRectangle(t) for t in tartaglia[1]]
        self.play(*[Create(s) for s in surroundings])
        self.play(*[Write(t) for t in tartaglia[1]])
        self.play(*[Uncreate(s) for s in surroundings])
        self.wait(delay)
        self.next_section()

        # Aggiungiamo un'altra riga, questa volta con tre elementi.
        surroundings = [SurroundingRectangle(t) for t in tartaglia[2]]
        self.play(*[Create(s) for s in surroundings])
        # Lungo i bordi mettiamo sempre degli uno.
        self.play(Write(tartaglia[2][0]), Write(tartaglia[2][2]))
        # Mentre al centro dobbiamo scrivere la somma dei due elementi della riga precedente.
        arrows = [Arrow(tartaglia[1][0].get_center(), tartaglia[2][1].get_center(), buff=0.1, color=GRAY),
                  Arrow(tartaglia[1][1].get_center(), tartaglia[2][1].get_center(), buff=0.1, color=GRAY)]
        self.play(*[Create(a) for a in arrows])
        # Quindi ci va un 2.
        self.play(Write(tartaglia[2][1]))
        self.play(*[Uncreate(s) for s in surroundings], *[FadeOut(a) for a in arrows])
        self.wait(delay)
        self.next_section()

        # Altra riga: quattro elementi.
        surroundings = [SurroundingRectangle(t) for t in tartaglia[3]]
        self.play(*[Create(s) for s in surroundings])
        # Lungo i bordi mettiamo sempre degli uno.
        self.play(Write(tartaglia[3][0]), Write(tartaglia[3][3]))
        # Le due caselle interne vanno riempite con la somma dei due elementi della riga precedente.
        arrows = [Arrow(tartaglia[2][0].get_center(), tartaglia[3][1].get_center(), buff=0.1, color=GRAY),
                  Arrow(tartaglia[2][1].get_center(), tartaglia[3][1].get_center(), buff=0.1, color=GRAY)]
        self.play(*[Create(a) for a in arrows])
        self.play(Write(tartaglia[3][1]))
        self.play(*[FadeOut(a) for a in arrows])
        arrows = [Arrow(tartaglia[2][1].get_center(), tartaglia[3][2].get_center(), buff=0.1, color=GRAY),
                  Arrow(tartaglia[2][2].get_center(), tartaglia[3][2].get_center(), buff=0.1, color=GRAY)]
        self.play(*[Create(a) for a in arrows])
        self.play(Write(tartaglia[3][2]))
        self.play(*[FadeOut(a) for a in arrows])
        self.play(*[Uncreate(s) for s in surroundings])
        self.wait(delay)
        self.next_section()

        # E così via. Potremo andare all'infinito, ma a noi basta arrivare fino alla settima riga.

        for _i in range(4, 7):
            self.play(*[Write(t) for t in tartaglia[_i]])
        self.wait(delay)
        self.next_section()

        # Il triangolo di Tartaglia ci offre i coefficienti dello sviluppo di un binomio secondo una qualunque potenza.
        # La prima riga corrisponde alla potenza 0;

        potenza = VGroup(
            MathTex(r"(t + c)^0 ="),
            MathTex(r"= 1")
        ).arrange(DOWN).next_to(tartaglia[0], 2 * DOWN)
        set_color(potenza[0], 1, color=RED)
        set_color(potenza[0], 3, color=GREEN)
        background = SurroundingRectangle(potenza, buff=.3, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background))
        self.play(Write(potenza[0]))
        fftf = FromFormulaToFormula(tartaglia[0][0], potenza[1])
        self.play(fftf.write(0))
        self.play(fftf.copy_and_move(0, 1))
        self.add(potenza[1])
        self.remove(*fftf.get_temp_pieces())
        self.play(Circumscribe(tartaglia[0][0]), Circumscribe(potenza[1][0][1]))
        self.play(Circumscribe(tartaglia[0][0]), Circumscribe(potenza[1][0][1]))
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(background), FadeOut(potenza))

        # la seconda riga alla potenza 1;

        potenza = VGroup(
            MathTex(r"(t + c)^1 ="),
            MathTex(r"= 1t^1 + 1c^1")
        ).arrange(DOWN).next_to(tartaglia[1], 2 * DOWN)
        set_color(potenza[0], 1, color=RED)
        set_color(potenza[0], 3, color=GREEN)
        set_color(potenza[1], 2, color=RED)
        set_color(potenza[1], 6, color=GREEN)
        background = SurroundingRectangle(potenza, buff=.3, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background))
        self.play(Create(potenza[0]))
        fftf = FromFormulaToFormula(potenza[0], potenza[1])
        self.play(fftf.write(0))
        self.play(fftf.move(tartaglia[1][0].copy(), 1))
        self.play(fftf.copy_and_move(1, 2))
        self.play(fftf.copy_and_move(5, 3))
        self.play(fftf.write(4))
        self.play(fftf.move(tartaglia[1][1].copy(), 5))
        self.play(fftf.copy_and_move(3, 6))
        self.play(fftf.copy_and_move(5, 7))
        self.add(potenza[1])
        self.remove(*fftf.get_temp_pieces())
        for _i in range(2):
            self.play(
                Circumscribe(tartaglia[1][0]),
                Circumscribe(tartaglia[1][1]),
                Circumscribe(potenza[1][0][1]),
                Circumscribe(potenza[1][0][5]))
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(background), FadeOut(potenza))

        # la terza riga alla potenza 2.
        # Infatti vedi che i numeri del triangolo corrispondono ai coefficienti del quadrato del binomio.

        potenza = VGroup(
            MathTex(r"(t + c)^2 ="),
            MathTex(r"= 1t^2 + 2t^1c^1 + 1c^2")
        ).arrange(DOWN).next_to(tartaglia[2], 2 * DOWN)
        set_color(potenza[0], 1, color=RED)
        set_color(potenza[0], 3, color=GREEN)
        set_color(potenza[1], 2, 6, color=RED)
        set_color(potenza[1], 8, 12, color=GREEN)
        background = SurroundingRectangle(potenza, buff=.3, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background))
        self.play(Create(potenza[0]))
        fftf = FromFormulaToFormula(potenza[0], potenza[1])
        self.play(fftf.write(0))
        self.play(fftf.move(tartaglia[2][0].copy(), 1))
        self.play(fftf.copy_and_move(1, 2))
        self.play(fftf.copy_and_move(5, 3))
        self.play(fftf.write(4))
        self.play(fftf.move(tartaglia[2][1].copy(), 5))
        self.play(fftf.copy_and_move(1, 6))
        self.play(fftf.move(potenza[1][0][3].copy(), 7))
        self.play(fftf.copy_and_move(3, 8))
        self.play(fftf.write(9))
        self.play(fftf.write(10))
        self.play(fftf.move(tartaglia[2][2].copy(), 11))
        self.play(fftf.copy_and_move(3, 12))
        self.play(fftf.move(potenza[1][0][9].copy(), 13))
        self.add(potenza[1])
        self.remove(*fftf.get_temp_pieces())
        for _i in range(2):
            self.play(
                *[Circumscribe(t) for t in tartaglia[2]],
                Circumscribe(potenza[1][0][1]),
                Circumscribe(potenza[1][0][5]),
                Circumscribe(potenza[1][0][11]),
            )
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(background), FadeOut(potenza))

        # La quarta riga corrisponde alla potenza 3.
        # Infatti anche in questo caso vedi che c'è corrispondenza tra i numeri del triangolo
        # e i coefficienti dello sviluppo.

        potenza = VGroup(
            MathTex(r"(t + c)^3 ="),
            MathTex(r"= 1t^3 + 3t^2c^1 + 3t^1c^2 + 1c^3")
        ).arrange(DOWN).next_to(tartaglia[3], 2 * DOWN)
        set_color(potenza[0], 1, color=RED)
        set_color(potenza[0], 3, color=GREEN)
        set_color(potenza[1], 2, 6, 12, color=RED)
        set_color(potenza[1], 8, 14, 18, color=GREEN)
        background = SurroundingRectangle(potenza, buff=.3, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background))
        self.play(Create(potenza[0]))
        fftf = FromFormulaToFormula(potenza[0], potenza[1])
        self.play(fftf.write(0))
        self.play(fftf.move(tartaglia[3][0].copy(), 1))
        self.play(fftf.copy_and_move(1, 2))
        self.play(fftf.copy_and_move(5, 3))
        self.play(fftf.write(4))
        self.play(fftf.move(tartaglia[3][1].copy(), 5))
        self.play(fftf.copy_and_move(1, 6))
        self.play(fftf.move(potenza[1][0][3].copy(), 7))
        self.play(fftf.copy_and_move(3, 8))
        self.play(fftf.write(9))
        self.play(fftf.write(10))
        self.play(fftf.move(tartaglia[3][2].copy(), 11))
        self.play(fftf.copy_and_move(1, 12))
        self.play(fftf.move(potenza[1][0][7].copy(), 13))
        self.play(fftf.copy_and_move(3, 14))
        self.play(fftf.move(potenza[1][0][9].copy(), 15))
        self.play(fftf.write(16))
        self.play(fftf.move(tartaglia[3][3].copy(), 17))
        self.play(fftf.copy_and_move(3, 18))
        self.play(fftf.move(potenza[1][0][15], 19))
        self.add(potenza[1])
        self.remove(*fftf.get_temp_pieces())
        for _i in range(2):
            self.play(
                *[Circumscribe(t) for t in tartaglia[3]],
                Circumscribe(potenza[1][0][1]),
                Circumscribe(potenza[1][0][5]),
                Circumscribe(potenza[1][0][11]),
                Circumscribe(potenza[1][0][17]))
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(background), FadeOut(potenza))

        # Per trovare i coefficienti della sesta potenza dobbiamo arrivare alla settima riga.
        # Quindi t più c elevato alla sesta è pari a:
        # t alla sesta + 6 per t alla quinta per c + 15 per t alla quarta per c alla seconda
        # + 20 per t alla terza per c alla terza + 15 per t alla seconda per c alla quarta
        # + 6 per t per c alla quinta + c alla sesta.

        potenza = VGroup(
            MathTex(r"(t + c)^6 ="),
            MathTex(r"= 1t^6 + 6t^5c^1 + 15t^4c^2 + 20t^3c^3 + 15t^2c^4 + 6t^1c^5 + 1c^6")
        ).arrange(DOWN).next_to(tartaglia[6], 2 * DOWN)
        set_color(potenza[0], 1, color=RED)
        set_color(potenza[0], 3, color=GREEN)
        set_color(potenza[1], 2, 6, 13, 20, 27, 33, color=RED)
        set_color(potenza[1], 8, 15, 22, 29, 35, 39, color=GREEN)
        background = SurroundingRectangle(potenza, buff=.2, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background))
        # self.play(Create(potenza))
        self.play(Create(potenza[0]))
        fftf = FromFormulaToFormula(potenza[0], potenza[1])
        self.play(fftf.write(0))

        self.play(fftf.move(tartaglia[6][0].copy(), 1))
        self.play(fftf.copy_and_move(1, 2))
        self.play(fftf.copy_and_move(5, 3))
        self.play(fftf.write(4))

        self.play(fftf.move(tartaglia[6][1].copy(), 5))
        self.play(fftf.copy_and_move(1, 6))
        self.play(fftf.move(potenza[1][0][3].copy(), 7))
        self.play(fftf.copy_and_move(3, 8))
        self.play(fftf.write(9))
        self.play(fftf.write(10))

        self.play(fftf.move(tartaglia[6][2].copy(), slice(11, 13)))
        self.play(fftf.copy_and_move(1, 13))
        self.play(fftf.move(potenza[1][0][7].copy(), 14))
        self.play(fftf.copy_and_move(3, 15))
        self.play(fftf.move(potenza[1][0][9].copy(), 16))
        self.play(fftf.write(17))

        self.play(fftf.move(tartaglia[6][3].copy(), slice(18, 20)))
        self.play(fftf.copy_and_move(1, 20))
        self.play(fftf.move(potenza[1][0][14].copy(), 21))
        self.play(fftf.copy_and_move(3, 22))
        self.play(fftf.move(potenza[1][0][16].copy(), 23))
        self.play(fftf.write(24))

        self.play(fftf.move(tartaglia[6][4].copy(), slice(25, 27)))
        self.play(fftf.copy_and_move(1, 27))
        self.play(fftf.move(potenza[1][0][21].copy(), 28))
        self.play(fftf.copy_and_move(3, 29))
        self.play(fftf.move(potenza[1][0][23].copy(), 30))
        self.play(fftf.write(31))

        self.play(fftf.move(tartaglia[6][5].copy(), 32))
        self.play(fftf.copy_and_move(1, 33))
        self.play(fftf.move(potenza[1][0][28].copy(), 34))
        self.play(fftf.copy_and_move(3, 35))
        self.play(fftf.move(potenza[1][0][30].copy(), 36))
        self.play(fftf.write(37))

        self.play(fftf.move(tartaglia[6][6].copy(), 38))
        self.play(fftf.copy_and_move(3, 39))
        self.play(fftf.move(potenza[1][0][36].copy(), 40))

        self.wait(delay)
        self.next_section()

        # Potremo divertirci a calcolare le probabilità di tutti i possibili risultati del lancio di 6 monete,
        # ma a noi interessa solo la probabilità di ottenere due teste (e quindi quattro croci).
        # Qual è il termine che ci dà le informazioni necessarie?
        # Questo qui, quello con t alla seconda per c alla quarta.

        surround = SurroundingRectangle(potenza[1][0][25:31])
        self.play(Create(surround))
        self.wait(delay)
        self.next_section()

        risultato = VGroup(
            MathTex(r"\text{\# casi favorevoli} = 15"),
            MathTex(r"\text{\# casi totali} = 1 + 6 + 15 + 20 + 15 + 6 + 1 = 64"),
            MathTex(r"p(\text{2 teste}) = \dfrac{15}{64}")
        ).arrange(DOWN).next_to(tartaglia[6], 2 * UP)
        set_color(risultato[0], slice(0, 15), color=YELLOW)
        set_color(risultato[1], slice(0, 11), color=YELLOW)
        set_color(risultato[2], slice(2, 8), color=YELLOW)
        background_risultato = SurroundingRectangle(risultato, buff=.2, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background_risultato))


        # Il coefficiente è 15, per cui 15 è il numero di casi favorevoli.
        fftf = FromFormulaToFormula(potenza[1], risultato[0])
        self.play(fftf.write(slice(0, 16)))
        self.play(fftf.copy_and_move(slice(25, 27), slice(16, 18)))
        self.wait(delay)
        self.next_section()

        # E il numero di casi totali?
        # E' dato dalla somma dei coefficienti della riga.
        # 1+6+15+20+15+6+1 = 64.
        fftf = FromFormulaToFormula(potenza[1], risultato[1])
        self.play(fftf.write(slice(0, 12)))
        self.play(fftf.copy_and_move(1, 12))
        self.play(fftf.write(13))
        self.play(fftf.copy_and_move(5, 14))
        self.play(fftf.write(15))
        self.play(fftf.copy_and_move(slice(11, 13), slice(16, 18)))
        self.play(fftf.write(18))
        self.play(fftf.copy_and_move(slice(18, 20), slice(19, 21)))
        self.play(fftf.write(21))
        self.play(fftf.copy_and_move(slice(25, 27), slice(22, 24)))
        self.play(fftf.write(24))
        self.play(fftf.copy_and_move(32, 25))
        self.play(fftf.write(26))
        self.play(fftf.copy_and_move(38, 27))
        self.play(fftf.write(slice(28, 31)))
        self.wait(delay)
        self.next_section()

        # La probabilità quindi è 15/64.
        fftf = FromFormulaToFormula(risultato[0], risultato[2])
        self.play(fftf.write(slice(0, 10)))
        self.play(fftf.copy_and_move(slice(16, 18), slice(10, 12)))
        self.play(fftf.write(12))
        self.play(fftf.move(risultato[1][0][29:31].copy(), slice(13, 15)))

        self.wait(60)
