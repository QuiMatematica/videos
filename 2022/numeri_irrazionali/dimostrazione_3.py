from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        scala = 1.1

        quadrato_1 = Square().shift(LEFT)
        quadrato_2 = quadrato_1.copy().shift(2 * RIGHT)
        quadrati_1_2 = VGroup(quadrato_1, quadrato_2).shift(4.5*LEFT + .5*UP)
        quadrato_3 = quadrato_1.copy()
        quadrato_4 = quadrato_2.copy()
        quadrati_3_4 = VGroup(quadrato_3, quadrato_4).shift(2*UP)

        quadrato_colorato_interno = Polygon(quadrato_1.get_vertices()[1], quadrato_2.get_vertices()[2],
                                            quadrato_4.get_vertices()[3], quadrato_3.get_vertices()[0],
                                            fill_opacity=1, fill_color=GREEN, color=WHITE, z_index=-1)
        area_interna = MathTex(r"2\text{ m}^2", color=BLACK).scale(scala).move_to(quadrato_colorato_interno)

        self.add(quadrati_1_2, quadrati_3_4)
        self.play(Create(quadrato_colorato_interno))
        self.play(Write(area_interna))
        self.play(FadeOut(quadrati_1_2), FadeOut(quadrati_3_4))

        graffa = Brace(quadrato_colorato_interno, direction=DOWN + RIGHT)
        misura_lato = MathTex(r"l").scale(scala).move_to(graffa).shift(0.5 * DR)
        self.play(Create(graffa))
        self.play(Write(misura_lato))

        self.wait(delay)
        self.next_section()

        tesi = Tex(r"Tesi: $l \not\in \mathbb{Q}$", color=YELLOW).scale(scala).shift(2.5*RIGHT + 3*UP)
        self.play(Write(tesi))

        self.wait(delay)
        self.next_section()

        assurdo = Tex(r"Per assurdo: $l \in \mathbb{Q}$").scale(scala).next_to(tesi, 1.5*DOWN)
        self.play(Write(assurdo))

        self.wait(delay)
        self.next_section()

        lato = MathTex(r"l = \dfrac{a}{b}").scale(scala).next_to(assurdo, DOWN)
        self.play(Write(lato))

        self.wait(delay)
        self.next_section()

        area = MathTex(r"{{ A = l^2 }} = \biggl(\dfrac{a}{b}\biggr)^2 = \dfrac{a^2}{b^2}").scale(scala).next_to(lato, DOWN)
        self.play(Write(area[0]))

        self.wait(delay)
        self.next_section()

        self.play(Write(area[1]))

        self.wait(delay)
        self.next_section()

        area_bis = MathTex(r"\dfrac{a^2}{b^2} = 2").scale(scala).next_to(area, DOWN)
        self.play(Write(area_bis))

        self.wait(delay)
        self.next_section()

        equivalenza = MathTex(r"a^2 = 2 b^2").scale(scala).next_to(area_bis, DOWN)
        self.play(Write(equivalenza))

        self.wait(delay)
        self.next_section()
