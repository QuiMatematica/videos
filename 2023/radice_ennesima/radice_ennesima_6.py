from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 2

        self.wait(1)

        radice_prima = MathTex(r"{{ \sqrt[0]{a} }} = b \,\,\Longleftrightarrow\,\, b^0 = a").scale(scale)
        radice_prima[0][:3].set_color(YELLOW)
        radice_prima[0][3].set_color(GREEN)
        radice_prima[1][5].set_color(YELLOW)
        radice_prima[1][7].set_color(GREEN)
        radice_prima[1][1].set_color(RED)
        radice_prima[1][4].set_color(RED)

        radice_ennesima = MathTex(r"{{ \sqrt[n]{a} }}").move_to(radice_prima[0]).scale(scale)
        radice_ennesima[0][:3].set_color(YELLOW)
        radice_ennesima[0][3].set_color(GREEN)

        self.play(Write(radice_ennesima))
        self.wait(delay)
        self.next_section()

        self.play(Transform(radice_ennesima, radice_prima[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_prima[1]))
        self.wait(delay)
        self.next_section()

        uguaglianza = MathTex(r"{{ b^0 = }} a").scale(scale).move_to(radice_prima[1][4:])
        uguaglianza[0][0].set_color(RED)
        uguaglianza[0][1].set_color(YELLOW)
        uguaglianza[1][0].set_color(GREEN)
        self.play(uguaglianza.animate.next_to(radice_prima, DOWN))
        self.wait(delay)
        self.next_section()

        uguaglianza_estesa = MathTex(r"{{ b^0 = }} 1 = {{ a }}").scale(scale).move_to(uguaglianza)
        uguaglianza_estesa[0][0].set_color(RED)
        uguaglianza_estesa[0][1].set_color(YELLOW)
        uguaglianza_estesa[1][0].set_color(RED)
        uguaglianza_estesa[2][0].set_color(GREEN)
        self.play(TransformMatchingTex(uguaglianza, uguaglianza_estesa))
        self.wait(delay)
        self.next_section()

        radice_prima_bis = MathTex(r"{{ \sqrt[0]{1} }} = 1 \,\,\Longleftrightarrow\,\, 1^0 = 1").scale(scale).move_to(radice_prima)
        radice_prima_bis[0][:3].set_color(YELLOW)
        radice_prima_bis[0][3].set_color(GREEN)
        radice_prima_bis[1][5].set_color(YELLOW)
        radice_prima_bis[1][7].set_color(GREEN)
        radice_prima_bis[1][1].set_color(RED)
        radice_prima_bis[1][4].set_color(RED)

        self.play(FadeOut(radice_prima), FadeOut(radice_ennesima))
        self.play(Write(radice_prima_bis))
        self.wait(delay)
        self.next_section()

        condizione = MathTex(r"n \in \mathbb{N}, n \ne 0").scale(scale).move_to(uguaglianza_estesa)
        self.play(FadeOut(uguaglianza_estesa))
        self.play(Write(condizione))

        self.wait(30)
