from manim import *

from galois_x5_common import PianoX5, COLORS

SCALE = .8


class Scene(MovingCameraScene):

    def construct(self):
        titolo = Title("$x^5-1$", color=RED)
        titolo.underline.set_color(RED)
        self.play(Write(titolo))

        titolo_radici = Tex("Roots:").scale(SCALE).move_to((-3.5, 2.5, 0))
        self.play(Write(titolo_radici))

        radici = MathTex(
            r"1, e^{i \frac{2 \pi}{5}}, e^{i \frac{4 \pi}{5}}, e^{i \frac{6 \pi}{5}}, e^{i \frac{8 \pi}{5}}"
        ).scale(SCALE).next_to(titolo_radici, DOWN)
        self.play(Write(radici))

        self.play(
            radici[0][0].animate.set_color(COLORS[0]),
            radici[0][2:8].animate.set_color(COLORS[1]),
            radici[0][9:15].animate.set_color(COLORS[2]),
            radici[0][16:22].animate.set_color(COLORS[3]),
            radici[0][23:].animate.set_color(COLORS[4]),
        )

        piano = PianoX5().move_to((3.5, -.5, 0))
        self.play(Create(piano.piano))

        self.play(Create(piano.circonferenza))

        self.play(*[Create(_i) for _i in piano.lines])
        self.play(*[Create(_i) for _i in piano.dots])

        self.wait(1)

        titolo_zeta = Tex("Primitive 5$^{th}$ root of 1:").scale(SCALE).next_to(radici, DOWN)
        self.play(Write(titolo_zeta))

        zeta = MathTex(
            r"\zeta = e^{i \frac{2 \pi}{5}}"
        ).scale(SCALE).next_to(titolo_zeta, DOWN)
        zeta[0][2:].set_color(COLORS[1])
        self.play(Write(zeta))

        self.wait(1)

        titolo_polinomio_minimo = Tex(r"Minimal polinomial of $\zeta$:").scale(SCALE).next_to(zeta, DOWN)
        self.play(Write(titolo_polinomio_minimo))

        polinomio_minimo = MathTex(r"f_\zeta = \phi_5 = x^4 + x^3 + x^2 + x + 1").scale(SCALE).next_to(titolo_polinomio_minimo, DOWN)
        self.play(Write(polinomio_minimo))

        self.wait(1)

        titolo_campo_spezzamento = Tex("Splitting field:").scale(SCALE).next_to(polinomio_minimo, DOWN)
        self.play(Write(titolo_campo_spezzamento))

        campo_spezzamento = MathTex(
            r"\Omega = \mathbb{Q}(\zeta) \qquad [ \Omega : \mathbb{Q} ] = 4"
        ).scale(SCALE).next_to(titolo_campo_spezzamento, DOWN)
        self.play(Write(campo_spezzamento))

        self.wait(1)

        titolo_gruppo = Tex("Galois group:").scale(SCALE).next_to(campo_spezzamento, DOWN)
        self.play(Write(titolo_gruppo))

        gruppo = MathTex(r"G = \text{Gal}(\Omega / \mathbb{Q}) \qquad | G | = 4").scale(SCALE).next_to(titolo_gruppo, DOWN)
        self.play(Write(gruppo))

        self.wait(3)
