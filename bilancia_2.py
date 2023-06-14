from manim import *

from bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1
        scale = .8

        self.wait(delay)

        bilancia = Bilancia().scale(scale).move_to(2.7 * DOWN)
        self.play(Create(bilancia))
        self.wait(delay)
        self.next_section()

        ananas = ImageMobject('img/frutta/ananas.png', z_index=-1).scale(1.2 * scale)
        mela = ImageMobject('img/frutta/mela.png').scale(.7 * scale)
        pera = ImageMobject('img/frutta/pera.png').scale(.5 * scale)
        albicocca = ImageMobject('img/frutta/albicocca.png').scale(.3 * scale)

        self.play(FadeIn(mela.copy().move_to(4 * LEFT + -.35 * UP)))
        self.play(FadeIn(mela.copy().move_to(2.3 * LEFT + -.35 * UP)))

        first = 1.15
        shift = .6
        baseline = -0.88
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*0) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*1) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*2) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*3) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*4) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*5) + UP*baseline)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*6) + UP*baseline)))
        self.wait(delay)
        self.next_section()

        self.play(FadeIn(ananas.copy().move_to(2.8 * LEFT + 1.25 * UP)))
        self.play(FadeIn(ananas.copy().move_to(2.8 * RIGHT + 1.25 * UP)))
