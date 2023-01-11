from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 20

        title_color = YELLOW
        title_scale = 1.5

        # titolo_teorema = Tex("Teorema fondamentale dell'aritmetica", color=title_color).scale(title_scale).to_edge(UP)
        # testo_teorema = VGroup(
        #     Tex(r"Ogni numero naturale maggiore di 1 o è un \underline{numero primo}"),
        #     Tex(r"o si può esprimere come \underline{prodotto di numeri primi}."),
        #     Tex(r"Tale rappresentazione è \underline{unica}, se si prescinde"),
        #     Tex(r"dall'ordine in cui compaiono i fattori.")).arrange(DOWN).next_to(titolo_teorema, DOWN)
        #
        # self.play(Write(titolo_teorema))
        # self.play(Write(testo_teorema))
        #
        # self.wait(delay)
        # self.next_section()
        #
        # line_1 = Line().next_to(testo_teorema, 2*DOWN)
        # self.play(Create(line_1))

        corollario_1 = VGroup(
            Tex(r"Due numeri sono uguali"),
            Tex(r"se e solo se"),
            Tex(r"sono uguali"),
            Tex(r"le loro scomposizioni"),
            Tex(r"in fattori primi.")).scale(title_scale).arrange(DOWN)

        self.play(Write(corollario_1))

        self.wait(delay)
        self.next_section()

        corollario_2 = VGroup(
            Tex(r"Due numeri sono diversi"),
            Tex(r"se e solo se"),
            Tex(r"sono diverse"),
            Tex(r"le loro scomposizioni"),
            Tex(r"in fattori primi.")).scale(title_scale).arrange(DOWN)
        corollario_2[0][0][13:].set_color(YELLOW)
        corollario_2[2][0][4:11].set_color(YELLOW)
        self.play(TransformMatchingTex(corollario_1, corollario_2))

        self.wait(60)
