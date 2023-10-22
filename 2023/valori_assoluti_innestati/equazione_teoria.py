from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        riga1 = MathTex(r"\left| x \right| = a")

        riga2 = MathTex(r"\text{se } a < 0 \quad \Longrightarrow \quad \text{equazione impossibile}")
        esempio2 = MathTex(r"\left| x \right| = -1 \quad \Longrightarrow \quad \text{equazione impossibile}")

        riga3 = MathTex(r"\text{se } a = 0 \quad \Longrightarrow \quad x = 0")
        esempio3 = MathTex(r"\left| x \right| = 0 \quad \Longrightarrow \quad x = 0")

        riga4 = MathTex(r"\text{se } a > 0 \quad \Longrightarrow \quad x = a \,\lor\, x = -a")
        esempio4 = MathTex(r"\left| x \right| = 1 \quad \Longrightarrow \quad x = 1 \,\lor\, x = -1")

        righe = VGroup(
            riga1,
            VGroup(riga2, esempio2).arrange(DOWN),
            VGroup(riga3, esempio3).arrange(DOWN),
            VGroup(riga4, esempio4).arrange(DOWN)
        ).arrange(DOWN, buff=.8)

        self.play(Write(riga1))
        self.cut_and_wait()
        self.play(Write(riga2))
        self.play(Write(esempio2))
        self.cut_and_wait()
        self.play(Write(riga3))
        self.play(Write(esempio3))
        self.cut_and_wait()
        self.play(Write(riga4))
        self.cut_and_wait()
        self.play(Write(esempio4))
        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
