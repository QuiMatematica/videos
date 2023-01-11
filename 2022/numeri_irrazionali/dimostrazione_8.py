from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        scala = 1.1

        quadrato_1 = Square().shift(LEFT)
        quadrato_2 = quadrato_1.copy().shift(2 * RIGHT)
        quadrati_1_2 = VGroup(quadrato_1, quadrato_2).shift(3.5*LEFT + DOWN)
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

        tesi = Tex(r"$l \in \mathbb{Q} \Longrightarrow$ assurdo").scale(scala).shift(2.5*RIGHT + .5*UP)
        self.play(Write(tesi))

        self.wait(delay)
        self.next_section()

        assurdo = Tex(r"$\Longrightarrow l \not\in \mathbb{Q}$", color=YELLOW).scale(scala).next_to(tesi, 3*DOWN)
        self.play(Write(assurdo))

        self.wait(delay)
        self.next_section()
