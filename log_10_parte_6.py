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
        riga_1 = MathTex(r"- \log (4{,}3 \cdot 10^{-5}) \approx -(-5 + 0{,}43)").scale(SCALE)
        riga_2 = MathTex(r"- \log (4{,}3 \cdot 10^{-5}) \approx {{ -(-5 + 0{,}53) }}").scale(SCALE)

        self.play(Write(riga_1))
        self.cut_and_wait()

        token_4 = riga_1[0][22]
        token_5 = MathTex("5").scale(SCALE).move_to(riga_1[0][22]).shift(6*UP)

        self.play(
            token_4.animate.shift(6*DOWN),
            token_5.animate.move_to(riga_1[0][22])
        )

        self.remove(riga_1, token_5)
        self.add(riga_2)
        self.cut_and_wait()

        riga_3 = MathTex(r"- \log (4{,}3 \cdot 10^{-5}) {{ \approx -(-4{,}47) }}").scale(SCALE)
        self.play(TransformMatchingTex(riga_2, riga_3))

        riga_4 = MathTex(r"- \log (4{,}3 \cdot 10^{-5}) {{ \approx 4{,}47 }}").scale(SCALE)
        self.play(TransformMatchingTex(riga_3, riga_4))
        self.cut_and_wait()

        vero = MathTex(r"\text{valore corretto: } 4{,}37 \qquad \text{errore: } 2{,}3\%").to_edge(DOWN)
        self.play(Write(vero))

        self.wait(30)
