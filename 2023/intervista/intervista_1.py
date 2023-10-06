from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        initial_font_size = 42

        testo = VGroup(
            Tex("Da un’intervista ad un gruppo di persone è emerso che:", font_size=initial_font_size),
            Tex(r"- il 23\% salta il pranzo;", font_size=initial_font_size),
            Tex(r"- il 40\% mangia lo yogurt a pranzo;", font_size=initial_font_size),
            Tex(r"- il 33\% non mangia lo yogurt.", font_size=initial_font_size),
            Tex("Possiamo dedurre con certezza che:", font_size=initial_font_size),
            Tex("A: esistono persone che saltano il pranzo e non mangiano lo yogurt;", font_size=initial_font_size),
            Tex("B: tutte le persone che mangiano lo yogurt pranzano;", font_size=initial_font_size),
            Tex("C: tutte le persone che pranzano mangiano lo yogurt;", font_size=initial_font_size),
            Tex("D: esistono persone che mangiano lo yogurt, ma non a pranzo;", font_size=initial_font_size),
            Tex(r"E: la percentuale di persone che non salta il pranzo è inferiore al 70\%.", font_size=initial_font_size)
        ).arrange(DOWN, aligned_edge=LEFT)

        for _l in testo:
            self.play(Write(_l))
            self.cut_and_wait()

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
