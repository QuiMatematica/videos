from manim import *

DELAY = 60

DIAMETRO_COLOR = RED


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        ruota = ImageMobject('../../img/ruota_1.png').scale(.5).shift(3 * LEFT).shift(UP)
        self.play(FadeIn(ruota))
        self.cut_and_wait()

        diametro_frecce = DoubleArrow(start=ruota.get_top(), end=ruota.get_bottom(), buff=0, color=DIAMETRO_COLOR)
        self.play(Create(diametro_frecce))

        diametro_misura = Tex("60 cm", color=DIAMETRO_COLOR).scale(2).next_to(diametro_frecce, RIGHT)
        self.play(Write(diametro_misura))
        self.cut_and_wait()

        diametro = Tex("diametro = 60 cm", color=YELLOW)
        giri = Tex("10 giri al secondo", color=YELLOW)
        domanda = Tex("velocità?", color=RED)
        VGroup(diametro, giri, domanda).arrange(DOWN).shift(3 * RIGHT).shift(UP)

        self.play(Transform(VGroup(diametro_frecce, diametro_misura), diametro))
        self.cut_and_wait()

        self.play(Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.play(Rotate(ruota, angle=-PI), Write(giri), run_time=1, rate_func=linear)
        self.next_section()
        self.play(Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.play(Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.next_section()

        self.play(Write(domanda), Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.next_section()

        risposte = Tex(r"A) 8 km/h \quad B) 38 km/h \quad C) 68 km/h \quad D) 108 km/h", color=GREEN).shift(2.5 * DOWN)
        self.play(Write(risposte), Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.next_section()
        self.play(Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)
        self.play(Rotate(ruota, angle=-PI), run_time=1, rate_func=linear)

        self.wait(30)
