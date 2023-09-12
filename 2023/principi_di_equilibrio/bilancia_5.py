from manim import *

from qui_matematica.bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        self.delay = 60
        scale = .8

        self.wait(self.delay)

        bilancia = Bilancia().scale(scale).move_to(2.7 * DOWN)
        self.play(Create(bilancia))
        self.wait(self.delay)
        self.next_section()

        mela = ImageMobject('../../img/frutta/mela.png').scale(.7 * scale)
        albicocca = ImageMobject('../../img/frutta/albicocca.png').scale(.3 * scale)

        mele = bilancia.place_on_left(mela, 5)
        self.mostra_frutta([mele[1], mele[3]])

        albicocche = bilancia.place_on_right(albicocca, 9)
        self.mostra_frutta([albicocche[0], *albicocche[2:4], *albicocche[5:7], albicocche[8]])

        self.play(FadeOut(mele[1]), FadeOut(mele[3]), FadeIn(mele[2]),
                  *[FadeOut(f) for f in [albicocche[0], *albicocche[2:4], *albicocche[5:7], albicocche[8]]],
                  FadeIn(albicocche[1]), FadeIn(albicocche[4]), FadeIn(albicocche[7]))
        self.wait(self.delay)
        self.next_section()

        self.play(FadeIn(mele[0]), FadeIn(mele[4]),
                  *[FadeIn(f) for f in [albicocche[0], *albicocche[2:4], *albicocche[5:7], albicocche[8]]])

        self.wait(30)

    def mostra_frutta(self, lista):
        for f in lista:
            self.play(FadeIn(f, run_time=1 / len(lista)))
        self.wait(self.delay)
        self.next_section()
