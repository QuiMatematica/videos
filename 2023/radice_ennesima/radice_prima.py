from manim import *


class Scene(MovingCameraScene):

    config.pixel_height = 1920
    config.pixel_width = 1080
    # config.background_color = BLUE_E

    def construct(self):
        delay = 10

        scale = 6

        self.wait(1)

        radice_prima = VGroup(
            MathTex(r"\sqrt[1]{a} = b"),
            MathTex(r"\Leftrightarrow").rotate(PI/2),
            MathTex(r"b^1 = a")).arrange(DOWN).scale(scale)
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

        potenza_senza_esponente = MathTex(r"b = a").scale(scale).move_to(radice_prima[2])
        potenza_senza_esponente[0][0].set_color(RED)
        potenza_senza_esponente[0][2].set_color(GREEN)

        dinamo = []
        a = radice_prima[2][0][0]
        a.target = potenza_senza_esponente[0][0]
        dinamo.append(a)
        a = radice_prima[2][0][3]
        a.target = potenza_senza_esponente[0][2]
        dinamo.append(a)
        a = radice_prima[2][0][2]
        a.target = potenza_senza_esponente[0][1]
        dinamo.append(a)

        self.play(*[MoveToTarget(x) for x in dinamo], FadeOut(radice_prima[2][0][1]))
        self.wait(delay)
        self.next_section()

        self.add(potenza_senza_esponente)
        self.remove(*dinamo)

        radice_prima_bis = MathTex(r"\sqrt[1]{a} = a").scale(scale).move_to(radice_prima[0])
        radice_prima_bis[0][:3].set_color(YELLOW)
        radice_prima_bis[0][3].set_color(GREEN)
        radice_prima_bis[0][5].set_color(GREEN)

        dinamo = []
        a = potenza_senza_esponente[0][2].copy()
        a.target = radice_prima_bis[0][5]
        dinamo.append(a)

        self.play(*[MoveToTarget(x) for x in dinamo], FadeOut(radice_prima[0][0][5]))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(radice_prima[1]), FadeOut(potenza_senza_esponente))

        self.wait(30)
