from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        a = 1
        b = -2
        c = -3

        x_min = -3
        x_max = 5
        y_min = -5
        y_max = 5

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        colore_fuoco_direttrice = GREEN
        colore_parabola = YELLOW

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().shift(3*RIGHT).shift(.5 * DOWN)
        self.add(riferimento)

        fuoco = Dot(riferimento.coords_to_point(1, -15/4), color=colore_fuoco_direttrice)
        direttrice = Line(start=riferimento.coords_to_point(x_min, -17/4),
                          end=riferimento.coords_to_point(x_max, -17/4),
                          color=colore_fuoco_direttrice)
        asse = DashedLine(start=riferimento.coords_to_point(1, y_max),
                          end=riferimento.coords_to_point(1, y_min), color=colore_parabola)

        vertice = Dot(riferimento.coords_to_point(1, -4), color=colore_parabola)
        intersezione_asse_x_1 = Dot(riferimento.coords_to_point(-1, 0), color=colore_parabola)
        intersezione_asse_x_2 = Dot(riferimento.coords_to_point(3, 0), color=colore_parabola)
        intersezione_asse_y = Dot(riferimento.coords_to_point(0, -3), color=colore_parabola)

        equazione = MathTex(r"y = x^2 - 2x - 3", color=colore_parabola).shift(3*RIGHT).shift(3.2*UP)
        self.add(equazione)
        self.add(asse)

        testo = VGroup(
            Tex("VERTICE:"),
            MathTex(r"x_V = {{ -\dfrac{b}{2a} }} = 1"),
            MathTex(r"y_V &= ax_V^2 + bx_V + c = \\ {{ &= 1^2 -2 \cdot 1 -3 = }} \\ &= -4"),
            MathTex(r"V (1, -4)"),
            ).arrange(DOWN, buff=.5).shift(3 * LEFT)

        self.play(Write(testo[0]))
        self.cut_and_wait()
        self.play(Write(testo[1][0]))
        self.cut_and_wait()
        self.play(Write(testo[1][1]))
        self.cut_and_wait()
        self.play(Write(testo[1][2]))
        self.cut_and_wait()
        self.play(Write(testo[2][0]))
        self.cut_and_wait()
        self.play(Write(testo[2][1]))
        self.cut_and_wait()
        self.play(Write(testo[2][2]))
        self.cut_and_wait()
        self.play(Write(testo[3]), Create(vertice))
        self.play(Flash(vertice))
        self.play(Flash(vertice))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
