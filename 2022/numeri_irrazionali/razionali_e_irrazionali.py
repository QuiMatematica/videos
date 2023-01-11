from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        scala_unita = 1.1

        ellipse_1 = Ellipse(width=6, height=4, color=WHITE)
        rect = Rectangle(width=3, height=4).shift(1.5*LEFT)
        insieme_razionali = Intersection(ellipse_1, rect, color=GREEN, fill_opacity=1).shift(LEFT)
        nome_razionali = MathTex("Razionali", color=BLACK).scale(scala_unita).move_to(insieme_razionali)
        self.play(Create(insieme_razionali), Write(nome_razionali))

        self.wait(30)
        self.next_section()

        ellipse_1 = Ellipse(width=6, height=4, color=WHITE)
        rect = Rectangle(width=3, height=4).shift(1.5*RIGHT)
        insieme_irrazionali = Intersection(ellipse_1, rect, color=RED, fill_opacity=1).shift(RIGHT)
        nome_irrazionali = MathTex("Irrazionali", color=BLACK).scale(scala_unita).move_to(insieme_irrazionali)
        self.play(Create(insieme_irrazionali), Write(nome_irrazionali))

        self.wait(30)
        self.next_section()

        razionali = VGroup(insieme_razionali, nome_razionali)
        irrazionali = VGroup(insieme_irrazionali, nome_irrazionali)
        self.play(razionali.animate.shift(RIGHT), irrazionali.animate.shift(LEFT))

        self.wait(30)
        self.next_section()

        nome_reali = MathTex("Reali", color=BLACK).scale(1.5).move_to(1.5*UP)
        self.play(Write(nome_reali))

        # self.wait(30)
        # self.next_section()
        #
        # r = MathTex(r"\mathbb{R}",color=BLACK).scale(2).move_to(nome_reali)
        # self.play(Transform(nome_reali, r))
        #
        # self.wait(30)

        self.camera.frame.scale(.6)
