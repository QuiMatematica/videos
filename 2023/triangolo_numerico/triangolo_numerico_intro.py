from manim import *

from qui_matematica.qmath import NumericalTriangle

DELAY = 30

SCALE = 2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        triangolo = NumericalTriangle(4)
        self.play(Create(triangolo))
        self.cut_and_wait()

        domanda = Tex("?").scale(SCALE).move_to(triangolo.get_cell((1, 1)))
        self.play(Write(domanda))

        numero_2 = Tex("2").scale(SCALE).move_to(triangolo.get_cell((2, 1)))
        numero_5 = Tex("5").scale(SCALE).move_to(triangolo.get_cell((2, 2)))
        self.play(Write(numero_2), Write(numero_5))

        addizione = Tex("2 + 5", color=YELLOW).scale(SCALE).move_to(triangolo.get_cell((1, 1)))
        n2 = numero_2.copy()
        n5 = numero_5.copy()
        n2.target = addizione[0][0]
        n5.target = addizione[0][2]
        self.play(
            Transform(domanda, addizione[0][1]),
            MoveToTarget(n2),
            MoveToTarget(n5)
        )
        self.add(addizione)
        self.remove(n2, n5, domanda)

        numero_7 = Tex("7", color=YELLOW).scale(SCALE).move_to(triangolo.get_cell((1, 1)))
        self.play(ReplacementTransform(addizione, numero_7))
        self.cut_and_wait()

        self.play(
            FadeOut(numero_2),
            FadeOut(numero_5),
            FadeOut(numero_7),
        )

        self.play(Write(Tex("2").scale(SCALE).move_to(triangolo.get_cell((3, 0)))))
        self.play(Write(Tex("7").scale(SCALE).move_to(triangolo.get_cell((3, 2)))))
        self.play(Write(Tex("3").scale(SCALE).move_to(triangolo.get_cell((3, 3)))))
        self.play(Write(Tex("38").scale(SCALE).move_to(triangolo.get_cell((0, 0)))))

        self.wait(30)

