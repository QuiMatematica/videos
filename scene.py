from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        scala_unita = 1.5

        quadrato_1 = Square()
        self.play(Create(quadrato_1))

        graffa = Brace(quadrato_1)
        misura_lato = MathTex(r"1\text{ m}").scale(scala_unita).next_to(graffa, DOWN)
        self.play(Create(graffa))
        self.play(Write(misura_lato))

        self.wait(delay)
        self.next_section()

        quadrato_colorato = Square(fill_opacity=1, fill_color=RED)
        self.play(Create(quadrato_colorato))
        area = MathTex(r"1\text{ m}^2", color=BLACK).scale(scala_unita).move_to(quadrato_colorato)
        self.play(Write(area))

        self.wait(delay)
        self.next_section()

        self.play(FadeOut(quadrato_colorato), FadeOut(area), FadeOut(graffa), FadeOut(misura_lato))
        self.play(quadrato_1.animate.shift(LEFT))
        quadrato_2 = quadrato_1.copy()
        self.play(quadrato_2.animate.shift(2 * RIGHT))

        quadrati_1_2 = VGroup(quadrato_1, quadrato_2)
        self.play(quadrati_1_2.animate.shift(DOWN))
        quadrato_3 = quadrato_1.copy()
        quadrato_4 = quadrato_2.copy()
        quadrati_3_4 = VGroup(quadrato_3, quadrato_4)
        self.play(quadrati_3_4.animate.shift(2 * UP))

        self.wait(delay)
        self.next_section()

        graffa = Brace(quadrati_1_2)
        misura_lato = MathTex(r"2\text{ m}").scale(scala_unita).next_to(graffa, DOWN)
        self.play(Create(graffa))
        self.play(Write(misura_lato))

        self.wait(delay)
        self.next_section()

        quadrato_colorato = Square(fill_opacity=1, fill_color=RED, side_length=4, z_index=-2)
        self.play(Create(quadrato_colorato))
        area = MathTex(r"4\text{ m}^2", color=BLACK).scale(scala_unita).move_to(quadrato_colorato)
        self.play(Write(area))

        self.wait(delay)
        self.next_section()

        self.play(FadeOut(quadrato_colorato), FadeOut(area), FadeOut(graffa), FadeOut(misura_lato))
        self.play(Create(Line(quadrato_1.get_vertices()[1], quadrato_1.get_vertices()[3])))
        self.play(Create(Line(quadrato_2.get_vertices()[2], quadrato_2.get_vertices()[0])))
        self.play(Create(Line(quadrato_4.get_vertices()[3], quadrato_4.get_vertices()[1])))
        self.play(Create(Line(quadrato_3.get_vertices()[0], quadrato_3.get_vertices()[2])))

        self.wait(delay)
        self.next_section()

        quadrato_colorato_interno = Polygon(quadrato_1.get_vertices()[1], quadrato_2.get_vertices()[2],
                                            quadrato_4.get_vertices()[3], quadrato_3.get_vertices()[0],
                                            fill_opacity=1, fill_color=GREEN, z_index=-1)
        self.play(Create(quadrato_colorato_interno))
        area_interna = MathTex(r"?", color=BLACK).scale(scala_unita).move_to(quadrato_colorato_interno)
        self.play(Write(area_interna))

        self.wait(delay)
        self.next_section()

        self.play(FadeOut(quadrato_colorato_interno), FadeOut(area_interna))
        self.play(FadeIn(quadrato_colorato), FadeIn(area))

        self.wait(delay)
        self.next_section()

        self.play(FadeIn(quadrato_colorato_interno), FadeOut(area))

        self.wait(delay)
        self.next_section()

        area_interna = MathTex(r"2\text{ m}^2", color=BLACK).scale(scala_unita).move_to(quadrato_colorato_interno)
        self.play(Write(area_interna))
        self.play(FadeOut(quadrato_colorato), FadeOut(quadrati_1_2), FadeOut(quadrati_3_4))

        self.wait(delay)
        self.next_section()

        graffa = Brace(quadrato_colorato_interno, direction=DOWN + RIGHT)
        misura_lato = MathTex(r"?").scale(scala_unita).move_to(graffa).shift(0.5*DR)
        self.play(Create(graffa))
        self.play(Write(misura_lato))
