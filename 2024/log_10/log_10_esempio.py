from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        concentrazione = MathTex(r"[\text{H}^+] = {{ 4{,}3 \cdot 10^{-5} }} \text{ mol/L}").to_edge(UP)
        self.play(Write(concentrazione))
        self.cut_and_wait()

        domanda = MathTex(r"\text{pH} = \text{?}").next_to(concentrazione, DOWN)
        self.play(Write(domanda))
        self.cut_and_wait()

        linea = Line().next_to(domanda, DOWN, buff=1)
        self.play(Create(linea))
        self.cut_and_wait()

        formula = MathTex(
            r"\text{pH} &= -\log [\text{H}^+] = \\",
            r"&= - \log (4{,}3 \cdot 10^{-5}) \approx \\",
            r"&\approx - (-5 + 0{,}43) = \\",
            r"&= - (-4{,}57) = \\",
            r"&= 4{,}57",
        ).next_to(linea, DOWN, buff=1)

        # Il ph si ottiene come meno logaritmo in base 10 della concentrazione,
        self.play(Write(formula[0]))
        self.cut_and_wait()
        # quindi meno logaritmo in base 10 di 4,3 * 10^-5.
        self.play(Write(formula[1][:6]))
        clone = concentrazione[1].copy()
        self.play(clone.animate.move_to(formula[1][6:14]))
        self.play(Write(formula[1][14:]))
        self.cut_and_wait()
        # Come faccio senza calcolatrice?
        #
        # Parto subito dal trucchetto.
        # La concentrazione normalmente è data in notazione scientifica. Se non lo fosse, convertila.
        # Ti ricordo che la parte davanti alla potenza di 10 si chiama coefficiente.

        self.play(formula[1][6:9].animate.set_color(RED))
        self.play(formula[1][12:14].animate.set_color(YELLOW))

        # Per approssimare il risultato del logaritmo a mente puoi procedere così:

        self.play(Write(formula[2][:3]))
        self.cut_and_wait()

        # scrivi l'esponente della potenza di 10,
        formula[2][3:5].set_color(YELLOW)
        clone = formula[1][12:14].copy()
        clone.target = formula[2][3:5]
        self.play(MoveToTarget(clone))
        self.cut_and_wait()

        # più,

        self.play(Write(formula[2][5]))
        self.cut_and_wait()

        # zero virgola,

        self.play(Write(formula[2][6:8]))

        # e ricopi il coefficiente ma senza la virgola.
        clone1 = formula[1][6].copy()
        clone2 = formula[1][8].copy()
        self.play(
            clone1.animate.move_to(formula[2][8]),
            clone2.animate.move_to(formula[2][9])
        )
        self.play(Write(formula[2][10:]))
        self.cut_and_wait()

        # Quindi nel nostro esercizio ottieni che il ph è meno, meno 5 più 0,43.
        # Facciamo la somma
        self.play(Write(formula[3]))
        self.cut_and_wait()

        # e il cambio di segno e otteniamo un ph pari a 4,57.
        self.play(Write(formula[4]))

        self.wait(30)
