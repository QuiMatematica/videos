from manim import *

class EuclideMCD(Scene):
    def construct(self):

        # Titolo
        title = Text("MCD: algoritmo di Euclide", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        divisione_1 = MathTex(r"252&:105 = 2 \\ 42&")

        divisione_2 = MathTex(r"105&:42 = 2 \\ 21&")

        divisione_3 = MathTex(r"42&:21 = 2 \\ 0&")

        griglia = VGroup(
            MathTex(r"\text{MCD}(252,\,105)"),
            MathTex(r"="),
            MathTex(r"\text{MCD}(105,\,42)"),
            MathTex(r"="),
            MathTex(r"\text{MCD}(42,\,21)"),
            divisione_1,
            MathTex(r"="),
            divisione_2,
            MathTex(r"="),
            divisione_3
        )
        griglia.arrange_in_grid(2, 5, buff=(.5, 1.2)).next_to(title, DOWN, buff=1.2)
        self.play(Write(griglia))


        # # Dati iniziali
        # start = MathTex(r"\text{MCD}(252,\,105)")
        # start.next_to(title, DOWN, buff=0.8)
        # self.play(Write(start))
        # self.wait(1.5)
        #
        # # Primo passaggio
        # step1 = MathTex(
        #     r"252 = 105 \cdot 2 + 42"
        # ).shift(UP * 0.5)
        #
        # desc1 = MathTex(
        #     r"\Rightarrow \text{MCD}(105,\,42)"
        # ).next_to(step1, DOWN)
        #
        # self.play(Transform(start, step1))
        # self.wait(1)
        # self.play(Write(desc1))
        # self.wait(2)
        #
        # self.play(FadeOut(start), FadeOut(desc1))
        #
        # # Secondo passaggio
        # step2 = MathTex(
        #     r"105 = 42 \cdot 2 + 21"
        # ).shift(UP * 0.5)
        #
        # desc2 = MathTex(
        #     r"\Rightarrow \text{MCD}(42,\,21)"
        # ).next_to(step2, DOWN)
        #
        # self.play(Write(step2))
        # self.wait(1)
        # self.play(Write(desc2))
        # self.wait(2)
        #
        # self.play(FadeOut(step2), FadeOut(desc2))
        #
        # # Terzo passaggio
        # step3 = MathTex(
        #     r"42 = 21 \cdot 2 + 0"
        # ).shift(UP * 0.5)
        #
        # self.play(Write(step3))
        # self.wait(2)
        #
        # Risultato finale
        result = MathTex(
            r"\boxed{\text{MCD}(252,105) = 21}"
        ).next_to(griglia, DOWN, buff=1.2)

        self.play(Write(result))
        self.wait(3)