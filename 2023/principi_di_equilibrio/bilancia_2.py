from manim import *

from qui_matematica.bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30
        scale = .8

        self.wait(delay)

        bilancia = Bilancia().scale(scale).move_to(2.7 * DOWN)
        self.play(Create(bilancia))
        self.wait(delay)
        self.next_section()

        ananas = ImageMobject('../../img/frutta/ananas.png', z_index=-1).scale(1.2 * scale)
        mela = ImageMobject('../../img/frutta/mela.png').scale(.7 * scale)
        albicocca = ImageMobject('../../img/frutta/albicocca.png').scale(.3 * scale)

        mele = Group(
            mela.copy().move_to(4 * LEFT + -.35 * UP),
            mela.copy().move_to(2.3 * LEFT + -.35 * UP)
        )
        for m in mele:
            self.play(FadeIn(m, run_time=1/mele.dim))

        first = 1.15
        shift = .6
        baseline = -0.88
        albicocche = Group()
        for _i in range(7):
            albicocche.add(albicocca.copy().move_to(RIGHT*(first + shift*_i) + UP*baseline))

        for m in albicocche:
            self.play(FadeIn(m, run_time=1/albicocche.dim))
        self.wait(delay)
        self.next_section()

        self.play(
            FadeIn(ananas.copy().move_to(2.8 * LEFT + 1.25 * UP)),
            FadeIn(ananas.copy().move_to(2.8 * RIGHT + 1.25 * UP)))

        self.wait(30)
