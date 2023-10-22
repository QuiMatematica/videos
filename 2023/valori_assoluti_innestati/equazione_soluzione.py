from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        equazione = MathTex(r"\bigl| \left| x - 2 \right| - 3  \bigr| = 4").move_to(3 * UP)
        equazione[0][0:2].set_color(GREEN)
        equazione[0][9:11].set_color(GREEN)
        equazione[0][2].set_color(RED)
        equazione[0][6].set_color(RED)
        self.play(Write(equazione))
        self.cut_and_wait()

        riga1 = MathTex(r"\left| x - 2 \right| - 3 = 4"
                        r" \quad\quad\lor\quad\quad "
                        r"\left| x - 2 \right| - 3 = -4").move_to(1 * UP)

        freccia1 = Arrow(start=equazione.get_bottom(), end=riga1[0][:9].get_top())
        freccia2 = Arrow(start=equazione.get_bottom(), end=riga1[0][10:].get_top())
        self.play(GrowArrow(freccia1), GrowArrow(freccia2))
        self.cut_and_wait()

        riga1[0][0].set_color(RED)
        riga1[0][4].set_color(RED)
        riga1[0][10].set_color(RED)
        riga1[0][14].set_color(RED)
        self.play(Write(riga1))
        self.cut_and_wait()

        riga2 = MathTex(r"\left| x - 2 \right| = 7"
                        r" \quad\quad\lor\quad\quad "
                        r"\left| x - 2 \right| = -1").move_to(0 * UP)
        riga2[0][0].set_color(RED)
        riga2[0][4].set_color(RED)
        riga2[0][8].set_color(RED)
        riga2[0][12].set_color(RED)
        self.play(Write(riga2))
        self.cut_and_wait()

        impossibile = Tex("impossibile").next_to(riga2[0][8:], DOWN).shift(RIGHT + .2 * UP)
        self.play(Write(impossibile))
        self.cut_and_wait()

        riga3 = MathTex(r"x - 2 = 7"
                        r" \quad\quad\lor\quad\quad "
                        r"x - 2 = -7").move_to(-2 * UP)

        freccia1 = Arrow(start=riga2[0][:7].get_bottom(), end=riga3[0][:5].get_top())
        freccia2 = Arrow(start=riga2[0][:7].get_bottom(), end=riga3[0][6:].get_top())
        self.play(GrowArrow(freccia1), GrowArrow(freccia2))
        self.cut_and_wait()

        self.play(Write(riga3))
        self.cut_and_wait()

        riga4 = MathTex(r"x = 9"
                        r" \quad\quad\lor\quad\quad "
                        r"x = -5").move_to(-3 * UP)
        self.play(Write(riga4))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
