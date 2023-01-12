from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        radice_quadrata_vuota = MathTex(r"\sqrt{\Box}").scale(3)
        self.play(Write(radice_quadrata_vuota))
        self.wait(delay)
        self.next_section()

        self.play(radice_quadrata_vuota.animate.shift(2*UP))
        self.wait(delay)
        self.next_section()

        doppia_freccia_verticale = MathTex(r"\Updownarrow", color=RED).scale(3)
        self.play(Write(doppia_freccia_verticale))
        self.wait(delay)
        self.next_section()

        quadrato_vuoto = MathTex(r"\Box^2").scale(3).shift(2*DOWN)
        self.play(Write(quadrato_vuoto))
        self.wait(delay)
        self.next_section()

        operazione = Tex("operazione", color=RED).next_to(doppia_freccia_verticale, LEFT)
        inversa = Tex("inversa", color=RED).next_to(doppia_freccia_verticale, RIGHT)
        self.play(Write(operazione), Write(inversa))
        self.wait(delay)
        self.next_section()

        sei_al_quadrato = MathTex("6^2").scale(3).move_to(quadrato_vuoto)
        sei_al_quadrato[0][0].set_color(YELLOW)
        self.play(ReplacementTransform(quadrato_vuoto, sei_al_quadrato))
        self.wait(delay)
        self.next_section()

        sei_al_quadrato_uguale_36 = MathTex("6^2 = 36").scale(3).move_to(quadrato_vuoto)
        sei_al_quadrato_uguale_36[0][0].set_color(YELLOW)
        sei_al_quadrato_uguale_36[0][3:].set_color(GREEN)
        self.play(sei_al_quadrato.animate.move_to(sei_al_quadrato_uguale_36[0][0:2]))
        self.wait(delay)
        self.next_section()

        self.play(Write(sei_al_quadrato_uguale_36[0][2:]))
        self.wait(delay)
        self.next_section()

        radice_di_36 = MathTex(r"\sqrt{36}").scale(3).move_to(radice_quadrata_vuota)
        radice_di_36[0][2:].set_color(GREEN)
        self.play(ReplacementTransform(radice_quadrata_vuota, radice_di_36))
        self.wait(delay)
        self.next_section()

        radice_di_36_uguale_6 = MathTex(r"\sqrt{36} = 6").scale(3).move_to(radice_quadrata_vuota)
        radice_di_36_uguale_6[0][2:4].set_color(GREEN)
        radice_di_36_uguale_6[0][5:].set_color(YELLOW)
        self.play(radice_di_36.animate.move_to(radice_di_36_uguale_6[0][0:4]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_di_36_uguale_6[0][4:]))

        self.wait(30)
