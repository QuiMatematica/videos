from manim import *

DELAY = 1
X_RADIUS = config["frame_x_radius"]
Y_RADIUS = config["frame_y_radius"]
POS = [
    -3 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    -1 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    +1 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    +3 * X_RADIUS / 4 * RIGHT + 5 * Y_RADIUS / 6 * UP,
    -3 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    -1 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    +1 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
    +3 * X_RADIUS / 4 * RIGHT + 7 * Y_RADIUS / 12 * UP,
]
SCALE = 1


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        equazione = MathTex(r"ax^2 + bx + c = 0").scale(SCALE).to_edge(UP, buff=LARGE_BUFF)
        formula = MathTex(r"x = \dfrac{-b \pm \sqrt{ b^2 - 4ac } }{2a}").scale(SCALE).next_to(equazione, DOWN, buff=MED_LARGE_BUFF)
        delta = MathTex(r"\Delta = {{ b^2 - 4ac }}").scale(SCALE).next_to(formula, DOWN, buff=MED_LARGE_BUFF)
        casi = VGroup(
            MathTex(r"\Delta < 0"),
            MathTex(r"\Delta = 0"),
            MathTex(r"\Delta > 0"),
            Tex(r"nessuna \\ radice"),
            Tex(r"due radici \\ coincidenti"),
            Tex(r"due radici \\ distinte"),
        ).arrange_in_grid(rows=2, cols=3, buff=(LARGE_BUFF, MED_SMALL_BUFF)).to_edge(DOWN, buff=LARGE_BUFF)

        self.play(Write(equazione))
        self.cut_and_wait()

        self.play(Write(formula))
        self.cut_and_wait()

        self.play(Write(delta[0]))
        copia = formula[0][7:13].copy()
        self.play(copia.animate.move_to(delta[1]))
        self.cut_and_wait()

        self.play(GrowArrow(Arrow(delta.get_bottom(), casi[0].get_top())))
        self.play(Write(casi[0]))
        self.play(Write(casi[3]))
        self.cut_and_wait()

        self.play(GrowArrow(Arrow(delta.get_bottom(), casi[1].get_top())))
        self.play(Write(casi[1]))
        self.play(Write(casi[4]))
        self.cut_and_wait()

        self.play(GrowArrow(Arrow(delta.get_bottom(), casi[2].get_top())))
        self.play(Write(casi[2]))
        self.play(Write(casi[5]))
        self.cut_and_wait()

        self.wait(30)
