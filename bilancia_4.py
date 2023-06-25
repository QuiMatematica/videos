from manim import *

from bilancia import Bilancia


class Scene(MovingCameraScene):

    def construct(self):
        self.delay = 30

        self.wait(self.delay)

        bilancia_sinistra = Bilancia().scale(.5).move_to(LEFT * 3.5 + DOWN)
        self.play(Create(bilancia_sinistra))

        bilancia_destra = Bilancia().scale(.5).move_to(RIGHT * 3.5 + DOWN)
        self.play(Create(bilancia_destra))

        melanzana = ImageMobject('img/verdura/melanzana.png').scale(.6)
        cipolla = ImageMobject('img/verdura/cipolla.png').scale(.35)
        carota = ImageMobject('img/verdura/carota.png').scale(.35)
        melanzana_h_shift = -.2
        carota_h_shift = -.3

        melanzane_1_a = bilancia_sinistra.place_on_left(melanzana, 5, melanzana_h_shift)
        self.mostra_frutta(melanzane_1_a)
        carote_1_a = bilancia_sinistra.place_on_left(carota, 2, carota_h_shift)
        self.mostra_frutta(carote_1_a)
        cipolle_1_a = bilancia_sinistra.place_on_left(cipolla, 3)
        self.mostra_frutta(cipolle_1_a)

        melanzane_1_b = bilancia_sinistra.place_on_right(melanzana, 4, melanzana_h_shift)
        self.mostra_frutta(melanzane_1_b)
        carote_1_b = bilancia_sinistra.place_on_right(carota, 8, carota_h_shift)
        self.mostra_frutta(carote_1_b)
        cipolle_1_b = bilancia_sinistra.place_on_right(cipolla, 2)
        self.mostra_frutta(cipolle_1_b)

        melanzane_2_a = bilancia_destra.place_on_left(melanzana, 5, melanzana_h_shift)
        self.mostra_frutta(melanzane_2_a)
        carote_2_a = bilancia_destra.place_on_left(carota, 6, carota_h_shift)
        self.mostra_frutta(carote_2_a)

        melanzane_2_b = bilancia_destra.place_on_right(melanzana, 4, melanzana_h_shift)
        self.mostra_frutta(melanzane_2_b)
        carote_2_b = bilancia_destra.place_on_right(carota, 4, carota_h_shift)
        self.mostra_frutta(carote_2_b)
        cipolle_2_b = bilancia_destra.place_on_right(cipolla, 3)
        self.mostra_frutta(cipolle_2_b)

        to_fade = [*melanzane_1_a[:2], *melanzane_1_a[3:], *melanzane_1_b]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        to_fade = [*carote_1_a, carote_1_b[0], carote_1_b[7]]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        to_fade = [cipolle_1_a[0], cipolle_1_a[2], *cipolle_1_b]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        to_fade = [*melanzane_2_a[:2], *melanzane_2_a[3:], *melanzane_2_b]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        to_fade = [*carote_2_a[:2], *carote_2_a[4:], *carote_2_b]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        melanzane_3_a = bilancia_destra.place_on_left(melanzana, 4)
        carote_3_a = bilancia_destra.place_on_left(carota, 6, carota_h_shift)
        cipolle_3_b = bilancia_destra.place_on_right(cipolla, 9)

        to_fade = [melanzane_2_a[2], *carote_2_a[2:4], *cipolle_2_b]
        self.play(*[FadeOut(f) for f in to_fade],
                  *[FadeIn(f) for f in melanzane_3_a[:3]],
                  *[FadeIn(f) for f in carote_3_a],
                  *[FadeIn(f) for f in cipolle_3_b])
        self.wait(self.delay)
        self.next_section()

        cipolle_3_a = bilancia_destra.place_on_left(cipolla, 1)
        to_fade = carote_3_a
        self.play(*[FadeOut(f) for f in to_fade],
                  FadeIn(melanzane_3_a[3]),
                  *[FadeIn(f) for f in cipolle_3_a])
        self.wait(self.delay)
        self.next_section()

        to_fade = [*cipolle_3_a, cipolle_3_b[4]]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        to_fade = [*melanzane_3_a[:2], melanzane_3_a[3], *cipolle_3_b[:3], *cipolle_3_b[6:]]
        self.play(*[FadeOut(f) for f in to_fade])
        self.wait(self.delay)
        self.next_section()

        self.play(self.camera.frame.animate.move_to(bilancia_destra.get_center() + UP).scale(.5))

        self.wait(30)

    def mostra_frutta(self, lista):
        for f in lista:
            self.play(FadeIn(f, run_time=1 / len(lista)))
        self.wait(self.delay)
        self.next_section()
