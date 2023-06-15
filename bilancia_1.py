from manim import *

from bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.wait(delay)

        bilancia_sinistra = Bilancia().scale(.5).move_to(LEFT*3.5 + DOWN)
        self.play(Create(bilancia_sinistra))

        bilancia_destra = Bilancia().scale(.5).move_to(RIGHT*3.5 + DOWN)
        self.play(Create(bilancia_destra))

        ananas = ImageMobject('img/frutta/ananas.png').scale(.6)
        mela = ImageMobject('img/frutta/mela.png').scale(.35)
        mela_baseline = 0.5
        pera = ImageMobject('img/frutta/pera.png').scale(.25)
        albicocca = ImageMobject('img/frutta/albicocca.png').scale(.15)

        ananas_1_a = Group(
            ananas.copy().move_to(LEFT*5.8 + UP*1.5),
            ananas.copy().move_to(LEFT*4.6 + UP*1.5)
        )
        for f in ananas_1_a:
            self.play(FadeIn(f, run_time=1/ananas_1_a.dim))

        self.play(FadeIn(mela.copy().move_to(LEFT*6.3 + UP*mela_baseline)))
        self.play(FadeIn(mela.copy().move_to(LEFT*5.4 + UP*mela_baseline)))
        self.play(FadeIn(mela.copy().move_to(LEFT*4.5 + UP*mela_baseline)))
        self.play(FadeIn(pera.copy().move_to(LEFT*5.9 + UP*0.45)))
        self.play(FadeIn(pera.copy().move_to(LEFT*4.9 + UP*0.45)))

        ananas_1_b = Group(
            ananas.copy().move_to(LEFT*2.3 + UP*1.5),
            ananas.copy().move_to(LEFT*1.1 + UP*1.5)
        )
        for f in ananas_1_b:
            self.play(FadeIn(f, run_time=1/ananas_1_b.dim))

        self.play(FadeIn(mela.copy().move_to(LEFT*2.5 + UP*mela_baseline)))
        self.play(FadeIn(mela.copy().move_to(LEFT*1.3 + UP*mela_baseline)))
        first = 2.9
        shift = 0.35
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first + shift*0) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*1) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*2) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*3) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*4) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*5) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*6) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(LEFT*(first - shift*7) + UP*0.16)))

        self.play(FadeIn(ananas.copy().move_to(RIGHT*1.1 + UP*1.5)))
        self.play(FadeIn(ananas.copy().move_to(RIGHT*2.3 + UP*1.5)))
        self.play(FadeIn(mela.copy().move_to(RIGHT*0.8 + UP*mela_baseline)))
        self.play(FadeIn(mela.copy().move_to(RIGHT*2.1 + UP*mela_baseline)))
        self.play(FadeIn(pera.copy().move_to(RIGHT*0.7 + UP*0.45)))
        self.play(FadeIn(pera.copy().move_to(RIGHT*1.65 + UP*0.45)))
        self.play(FadeIn(pera.copy().move_to(RIGHT*2.6 + UP*0.45)))

        self.play(FadeIn(ananas.copy().move_to(RIGHT*4.7 + UP*1.5)))
        self.play(FadeIn(ananas.copy().move_to(RIGHT*5.9 + UP*1.5)))
        self.play(FadeIn(mela.copy().move_to(RIGHT*5.1 + UP*mela_baseline)))
        first = 4.2
        shift = 0.25
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*0) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*1) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*2) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*3) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*4) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*5) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*6) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*7) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*8) + UP*0.16)))
        self.play(FadeIn(albicocca.copy().move_to(RIGHT*(first + shift*9) + UP*0.16)))

        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(f) for f in ananas_1_a], *[FadeOut(f) for f in ananas_1_b])
        self.wait(delay)
        self.next_section()

        self.wait(30)

