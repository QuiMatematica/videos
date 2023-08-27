from manim import *


class Scene(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def construct(self):
        delay = 10

        scale = 4

        buff = .1

        self.wait(1)

        radice_prima = VGroup(
            MathTex(r"\sqrt[0]{a} = b"),
            MathTex(r"\Leftrightarrow").rotate(PI/2),
            MathTex(r"b^0 = a")).arrange(DOWN, buff=buff).scale(scale)
        radice_prima[0][0][:3].set_color(YELLOW)
        radice_prima[0][0][3].set_color(GREEN)
        radice_prima[0][0][5].set_color(RED)
        radice_prima[2][0][3].set_color(GREEN)
        radice_prima[2][0][0].set_color(RED)
        radice_prima[2][0][1].set_color(YELLOW)

        self.play(Write(radice_prima[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(radice_prima[1]))
        self.wait(delay)
        self.next_section()

        dinamo = []
        a = radice_prima[0][0][0].copy()
        a.target = radice_prima[2][0][1]
        dinamo.append(a)
        a = radice_prima[0][0][3].copy()
        a.target = radice_prima[2][0][3]
        dinamo.append(a)
        a = radice_prima[0][0][5].copy()
        a.target = radice_prima[2][0][0]
        dinamo.append(a)
        a = radice_prima[0][0][4].copy()
        a.target = radice_prima[2][0][2]
        dinamo.append(a)

        self.play(*[MoveToTarget(x) for x in dinamo])
        self.wait(delay)
        self.next_section()

        self.add(radice_prima[2])
        self.remove(*dinamo)

        potenza_senza_esponente = MathTex(r"b^0 = 1").scale(scale).move_to(radice_prima[2])
        potenza_senza_esponente[0][0].set_color(RED)
        potenza_senza_esponente[0][1].set_color(YELLOW)
        potenza_senza_esponente[0][3].set_color(GREEN)

        dinamo = []
        a = radice_prima[2][0][0]
        a.target = potenza_senza_esponente[0][0]
        dinamo.append(a)
        a = radice_prima[2][0][1]
        a.target = potenza_senza_esponente[0][1]
        dinamo.append(a)
        a = radice_prima[2][0][2]
        a.target = potenza_senza_esponente[0][2]
        dinamo.append(a)
        a = radice_prima[2][0][3]
        a.target = potenza_senza_esponente[0][3]
        dinamo.append(a)

        self.play(*[MoveToTarget(x) for x in dinamo])
        self.wait(delay)
        self.next_section()

        self.add(potenza_senza_esponente)
        self.remove(*dinamo)

        radice_prima_bis = VGroup(
            MathTex(r"\sqrt[0]{1} = 1"),
            MathTex(r"\Leftrightarrow").rotate(PI/2),
            MathTex(r"1^0 = 1")).arrange(DOWN, buff=buff).scale(scale)
        radice_prima_bis[0][0][:3].set_color(YELLOW)
        radice_prima_bis[0][0][3].set_color(GREEN)
        radice_prima_bis[0][0][5].set_color(RED)
        radice_prima_bis[2][0][3].set_color(GREEN)
        radice_prima_bis[2][0][0].set_color(RED)
        radice_prima_bis[2][0][1].set_color(YELLOW)

        self.play(FadeOut(radice_prima), FadeOut(potenza_senza_esponente), FadeIn(radice_prima_bis))

        self.wait(30)
