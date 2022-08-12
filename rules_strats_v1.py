from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        self.add(ImageMobject("img/paper.jpg").scale(3))

        self.play(Create(Line(4*UP, 4*DOWN, color=BLACK)))

        rules = VGroup(
            Tex("REGOLE"),
            Tex("- prodotti tra polinomi"),
            Tex("- prodotti notevoli"),
            Tex("- somma tra monomi"),
            Tex("- regola del trasporto"),
            Tex("- dividere i membri per numero"),
            Tex("- ridurre ai minimi termini")
        ).set_color(BLACK).scale(.6).arrange(DOWN, buff=0.40).shift(2*LEFT)

        strats = VGroup(
            Tex("STRATEGIA"),
            Tex("1) semplificare i membri"),
            Tex("2) trasportare i termini"),
            Tex("3) semplificare i membri"),
            Tex("4) dividere per il coeff. della x"),
            Tex("5) semplificare la frazione")
        ).set_color(BLACK).scale(.6).arrange(DOWN, buff=0.40).shift(2*RIGHT)

        self.add(rules)
        self.add(strats)

        self.wait(60)
