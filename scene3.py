from manim import *

from qmath import PascalTriangle
from util import set_color, FromFormulaToFormula


class Scene(MovingCameraScene):

    config.max_files_cached = 200

    def construct(self):
        delay = 60

        tartaglia = PascalTriangle(9)

        for _i in range(9):
            self.play(*[Write(t) for t in tartaglia[_i]])
        self.wait(delay)
        self.next_section()

        potenze = [
            MathTex(r"t^8"),
            MathTex(r"t^7c^1"),
            MathTex(r"t^6c^2"),
            MathTex(r"t^5c^3"),
            MathTex(r"t^4c^4"),
            MathTex(r"t^3c^5"),
            MathTex(r"t^2c^6"),
            MathTex(r"t^1c^7"),
            MathTex(r"c^8"),
        ]
        set_color(potenze[0], 0, color=RED)
        set_color(potenze[1], 0, color=RED)
        set_color(potenze[2], 0, color=RED)
        set_color(potenze[3], 0, color=RED)
        set_color(potenze[4], 0, color=RED)
        set_color(potenze[5], 0, color=RED)
        set_color(potenze[6], 0, color=RED)
        set_color(potenze[7], 0, color=RED)
        set_color(potenze[1], 2, color=GREEN)
        set_color(potenze[2], 2, color=GREEN)
        set_color(potenze[3], 2, color=GREEN)
        set_color(potenze[4], 2, color=GREEN)
        set_color(potenze[5], 2, color=GREEN)
        set_color(potenze[6], 2, color=GREEN)
        set_color(potenze[7], 2, color=GREEN)
        set_color(potenze[8], 0, color=GREEN)
        for _i in range(9):
            potenze[_i].scale(.8)
            potenze[_i].next_to(tartaglia[8][_i], DOWN)
        self.play(*[Write(p) for p in potenze])
        self.wait(delay)
        self.next_section()

        risultato = VGroup(
            MathTex(r"\text{\# casi favorevoli} = 56"),
            MathTex(r"\text{\# casi totali} = 1 + 8 + 28 + 56 + 70 + 56 + 28 + 8 + 1 = 256"),
            MathTex(r"p(\text{5 teste}) = \dfrac{56}{256}")
        ).arrange(DOWN).next_to(tartaglia[8], 2 * UP)
        set_color(risultato[0], slice(0, 15), color=YELLOW)
        set_color(risultato[1], slice(0, 11), color=YELLOW)
        set_color(risultato[2], slice(2, 8), color=YELLOW)
        background_risultato = SurroundingRectangle(risultato, buff=.2, fill_color=GRAY_E, fill_opacity=1)
        self.play(Create(background_risultato))

        # l triangolo di Tartaglia contiene tutte le informazioni di cui abbiamo bisogno:
        # il singolo elemento ci dice quanti sono i casi favorevoli;
        # La probabilità è 56 su 256.

        surr = SurroundingRectangle(tartaglia[8][3])
        self.play(Create(surr))
        self.play(Write(risultato[0][0][0:16]))
        temp = tartaglia[8][3].copy()
        temp.target = risultato[0][0][16:]
        self.play(MoveToTarget(temp))
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(surr))

        # la somma degli elementi della riga ci dice quanti sono i casi totali.
        surr = SurroundingRectangle(tartaglia[8])
        self.play(Create(surr))
        self.play(Write(risultato[1][0][0:12]))
        temp = [t.copy() for t in tartaglia[8]]
        temp[0].target = risultato[1][0][12]
        temp[1].target = risultato[1][0][14]
        temp[2].target = risultato[1][0][16:18]
        temp[3].target = risultato[1][0][19:21]
        temp[4].target = risultato[1][0][22:24]
        temp[5].target = risultato[1][0][25:27]
        temp[6].target = risultato[1][0][28:30]
        temp[7].target = risultato[1][0][31]
        temp[8].target = risultato[1][0][33]
        self.play(*[MoveToTarget(t) for t in temp],
                  Write(risultato[1][0][13]),
                  Write(risultato[1][0][15]),
                  Write(risultato[1][0][18]),
                  Write(risultato[1][0][21]),
                  Write(risultato[1][0][24]),
                  Write(risultato[1][0][27]),
                  Write(risultato[1][0][30]),
                  Write(risultato[1][0][32]),
                  )
        self.play(Write(risultato[1][0][34:]))
        self.wait(delay)
        self.next_section()
        self.play(FadeOut(surr))

        # La probabilità quindi è 15/64.
        self.play(Write(risultato[2][0][:10]))
        temp = risultato[0][0][16:].copy()
        temp.target = risultato[2][0][10:12]
        self.play(MoveToTarget(temp))
        self.play(Write(risultato[2][0][12]))
        temp = risultato[1][0][35:].copy()
        temp.target = risultato[2][0][13:]
        self.play(MoveToTarget(temp))

        self.wait(60)
