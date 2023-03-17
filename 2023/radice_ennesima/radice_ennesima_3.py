from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scale = 2

        self.wait(1)

        argomento_negativo = MathTex(r"\sqrt[4]{-16} = ? \,\,\Longleftrightarrow\,\, ?^4 = -16")
        argomento_negativo[0][:3].set_color(YELLOW)
        argomento_negativo[0][3:6].set_color(GREEN)
        argomento_negativo[0][7].set_color(RED)
        argomento_negativo[0][10].set_color(RED)
        argomento_negativo[0][11].set_color(YELLOW)
        argomento_negativo[0][13:].set_color(GREEN)

        quadrati = MathTex(r"(+2)^4 = 16 \quad (-2)^4 = 16")
        quadrati[0][1:3].set_color(RED)
        quadrati[0][4].set_color(YELLOW)
        quadrati[0][6:8].set_color(GREEN)
        quadrati[0][9:11].set_color(RED)
        quadrati[0][12].set_color(YELLOW)
        quadrati[0][14:].set_color(GREEN)

        risultato_negativo = MathTex(r"{{ \sqrt[4]{16} = }} ?")
        risultato_negativo[0][:3].set_color(YELLOW)
        risultato_negativo[0][3:5].set_color(GREEN)
        risultato_negativo[1].set_color(RED)
        risultato_positivo = MathTex(r"{{ \sqrt[4]{16} = }} +2").scale(scale)
        risultato_positivo[0][:3].set_color(YELLOW)
        risultato_positivo[0][3:5].set_color(GREEN)
        risultato_positivo[1].set_color(RED)

        VGroup(argomento_negativo, MathTex("x"), quadrati, risultato_negativo).scale(scale).arrange(DOWN)

        self.play(Write(argomento_negativo))
        self.wait(delay)
        self.next_section()

        self.play(Write(quadrati))
        self.wait(delay)
        self.next_section()

        self.play(Write(risultato_negativo))
        self.wait(delay)
        self.next_section()

        risultato_positivo.move_to(risultato_negativo)
        self.play(TransformMatchingTex(risultato_negativo, risultato_positivo))

        self.wait(30)
