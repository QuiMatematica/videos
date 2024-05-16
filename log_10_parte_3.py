from manim import *

DELAY = 30
SCALE = 1.6
BUFF = .7


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        riga_1 = MathTex(r"- \log (4{,}3 \cdot 10^{-5}) {{ < 4{,}57 }}")
        riga_2 = MathTex(r"\log (4{,}3 \cdot 10^{-5}) {{ = }} \log 4{,}3 {{ + \log 10^{-5} }} ")

        VGroup(riga_1, riga_2).scale(SCALE).arrange(DOWN, buff=1)

        self.play(Write(riga_1[0]))
        self.cut_and_wait()
        
        token = riga_1[0][1:].copy()
        self.play(token.animate.move_to(riga_2[0]))
        self.add(riga_2[0])
        self.remove(token)
        self.cut_and_wait()

        self.play(Write(riga_2[1:]))
        self.cut_and_wait()

        riga_2_a = MathTex(r"\log (4{,}3 \cdot 10^{-5}) {{ = }} \log 4{,}3 {{ -5 }} ").scale(SCALE).move_to(riga_2)
        self.play(TransformMatchingTex(riga_2, riga_2_a))
        self.cut_and_wait()

        riga_2_b = MathTex(r"\log (4{,}3 \cdot 10^{-5}) {{ > }} 0{,}43 {{ -5 }} ").scale(SCALE).move_to(riga_2)
        self.play(TransformMatchingTex(riga_2_a, riga_2_b))
        self.cut_and_wait()

        riga_2_c = MathTex(r"\log (4{,}3 \cdot 10^{-5}) {{ > }} -4{,}57 ").scale(SCALE).move_to(riga_2)
        self.play(TransformMatchingTex(riga_2_b, riga_2_c))
        self.cut_and_wait()

        self.play(Write(riga_1[1][0]))

        token = riga_2_c[2][1:].copy()
        self.play(token.animate.move_to(riga_1[1][1:]))

        self.wait(30)
