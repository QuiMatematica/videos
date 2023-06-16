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

        ananas_1_a = [
            ananas.copy().move_to(LEFT*5.8 + UP*1.5),
            ananas.copy().move_to(LEFT*4.6 + UP*1.5)
        ]
        self.mostra_frutta(ananas_1_a)

        mele_1_a = [
            mela.copy().move_to(LEFT * 6.3 + UP * mela_baseline),
            mela.copy().move_to(LEFT * 5.4 + UP * mela_baseline),
            mela.copy().move_to(LEFT * 4.5 + UP * mela_baseline)
        ]
        self.mostra_frutta(mele_1_a)

        pere_1_a = [
            pera.copy().move_to(LEFT * 5.9 + UP * 0.45),
            pera.copy().move_to(LEFT * 4.9 + UP * 0.45)
        ]
        self.mostra_frutta(pere_1_a)

        ananas_1_b = Group(
            ananas.copy().move_to(LEFT*2.3 + UP*1.5),
            ananas.copy().move_to(LEFT*1.1 + UP*1.5)
        )
        self.mostra_frutta(ananas_1_b)

        mele_1_b = [
            mela.copy().move_to(LEFT*2.5 + UP*mela_baseline),
            mela.copy().move_to(LEFT*1.3 + UP*mela_baseline)
        ]
        self.mostra_frutta(mele_1_b)
        first = 2.9
        shift = 0.35
        albicocche_1_b = []
        for _i in range(8):
            albicocche_1_b.append(albicocca.copy().move_to(LEFT*(first - shift*_i) + UP*0.16))
        self.mostra_frutta(albicocche_1_b)

        ananas_2_a = [ananas.copy().move_to(RIGHT*1.1 + UP*1.5),
                      ananas.copy().move_to(RIGHT*2.3 + UP*1.5)]
        self.mostra_frutta(ananas_2_a)
        mele_2_a = [mela.copy().move_to(RIGHT*0.8 + UP*mela_baseline),
                    mela.copy().move_to(RIGHT*2.1 + UP*mela_baseline)]
        self.mostra_frutta(mele_2_a)
        pere_2_a = [pera.copy().move_to(RIGHT*0.7 + UP*0.45),
                    pera.copy().move_to(RIGHT*1.65 + UP*0.45),
                    pera.copy().move_to(RIGHT*2.6 + UP*0.45)]
        self.mostra_frutta(pere_2_a)

        ananas_2_b = [ananas.copy().move_to(RIGHT*4.7 + UP*1.5),
                      ananas.copy().move_to(RIGHT*5.9 + UP*1.5)]
        self.mostra_frutta(ananas_2_b)
        mele_2_b = [mela.copy().move_to(RIGHT*5.1 + UP*mela_baseline)]
        self.mostra_frutta(mele_2_b)
        first = 4.2
        shift = 0.25
        albicocche_2_b = []
        for _i in range(10):
            albicocche_2_b.append(albicocca.copy().move_to(RIGHT*(first + shift*_i) + UP*0.16))
        self.mostra_frutta(albicocche_2_b)

        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(f) for f in ananas_1_a], *[FadeOut(f) for f in ananas_1_b])
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(mele_1_a[0]), FadeOut(mele_1_a[2]), *[FadeOut(f) for f in mele_1_b])
        self.wait(delay)
        self.next_section()

        self.play(*[FadeOut(f) for f in ananas_2_a], *[FadeOut(f) for f in ananas_2_b])
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(mele_2_a[0]), FadeOut(mele_2_b[0]))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(bilancia_sinistra))
        self.wait(delay)
        self.next_section()

        uguale = MathTex("=").scale(2).move_to(LEFT * 3.85 + UP * 0.2)
        self.play(Write(uguale))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(mele_2_a[1]), FadeOut(pere_2_a[0]), FadeOut(pere_2_a[2]),
                  *[FadeOut(f) for f in albicocche_2_b[:4]],
                  *[FadeOut(f) for f in albicocche_2_b[6:]])
        self.wait(delay)
        self.next_section()

        self.play(self.camera.frame.animate.move_to(bilancia_destra.get_center() + UP).scale(.5))

        self.wait(30)

    def mostra_frutta(self, lista):
        for f in lista:
            self.play(FadeIn(f, run_time=1 / len(lista)))

