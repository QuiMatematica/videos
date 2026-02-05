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

        self.play(Write(griglia[0]))
        self.wait(1)
        self.next_section()

        self.play(Write(divisione_1[0][:7]))
        self.wait(1)
        self.next_section()

        self.play(Write(divisione_1[0][7:]))
        self.wait(1)
        self.next_section()

        self.play(Write(griglia[1]))
        self.play(Write(griglia[2][0][:4]))
        self.play(divisione_1[0][4:7].copy().animate.move_to(griglia[2][0][4:7]))
        self.play(Write(griglia[2][0][7]))
        self.play(divisione_1[0][9:12].copy().animate.move_to(griglia[2][0][8:10]))
        self.play(Write(griglia[2][0][10]))
        self.wait(1)
        self.next_section()

        self.play(Write(divisione_2[0][:6]))
        self.wait(1)
        self.next_section()

        self.play(Write(divisione_2[0][6:]))
        self.wait(1)
        self.next_section()

        self.play(Write(griglia[3]))
        self.play(Write(griglia[4][0][:4]))
        self.play(divisione_2[0][4:6].copy().animate.move_to(griglia[4][0][4:6]))
        self.play(Write(griglia[4][0][6]))
        self.play(divisione_2[0][8:11].copy().animate.move_to(griglia[4][0][7:9]))
        self.play(Write(griglia[4][0][9]))
        self.wait(1)
        self.next_section()





        result = MathTex(
            r"\boxed{\text{MCD}(252,105) = 21}"
        ).next_to(griglia, DOWN, buff=1.2)

        self.play(Write(result))
        self.wait(3)