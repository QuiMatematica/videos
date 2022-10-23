from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        scala_testi = 1.5

        titolo = Tex(r"$\mathbb{N}$: numeri naturali", color=YELLOW).scale(scala_testi).to_edge(UP)
        self.play(Write(titolo))
        self.wait(delay)
        self.next_section()

        numeri = VGroup()
        for _i in range(23):
            numeri.add(MathTex(str(_i)).scale(scala_testi))
        numeri.add(Tex("..."))
        numeri.arrange_in_grid(4, 6, buff=MED_LARGE_BUFF, row_alignments="dddd")

        for _i in numeri:
            self.play(Write(_i, run_time=.5))

        self.wait(30)
        self.next_section()
