import numpy as np
from manim import *

DELAY = 1

AXES_SHIFT = np.array((-1, .8, 0))


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        axes = Axes(
            x_range=[-.9, 11, 1],
            y_range=[-.09, 1.1, .1],
            x_length=10,
            y_length=5,
            tips=True,
            axis_config={"include_numbers": True},
        ).shift(AXES_SHIFT)

        self.play(Create(axes))
        self.cut_and_wait()

        for _i in range(1, 11):
            self.play(Create(Line(
                axes.c2p(_i, 0), axes.c2p(_i, 1), color=DARK_GRAY, stroke_width=2, z_index=-1
            )), run_time=.2)

        for _i in range(1, 11):
            self.play(Create(Line(
                axes.c2p(0, _i / 10), axes.c2p(10, _i / 10), color=DARK_GRAY, stroke_width=2, z_index=-1
            )), run_time=.2)

        logaritmo = axes.plot(lambda x: np.log10(x), x_range=[1, 10], use_smoothing=True, color=PURE_RED)
        self.play(Create(logaritmo))
        funzione_logaritmo = MathTex(
            r"y = \log x", color=PURE_RED
        ).move_to(axes.get_center() + 6 * RIGHT + .5 * UP)
        self.play(Write(funzione_logaritmo))
        self.cut_and_wait()

        retta = axes.plot(lambda x: x / 10, x_range=[1, 10], use_smoothing=True, color=PURE_GREEN)
        self.play(Create(retta))
        funzione_retta = MathTex(
            r"y = \dfrac{1}{10}x", color=PURE_GREEN
        ).move_to(axes.get_center() + 6 * RIGHT + .5 * DOWN)
        self.play(Write(funzione_retta))
        self.cut_and_wait()

        approx_1 = MathTex(r"\log x \approx \dfrac{1}{10}x").to_edge(DOWN)
        approx_1[0][0:4].set_color(PURE_RED)
        approx_1[0][5:].set_color(PURE_GREEN)
        self.play(Write(approx_1))
        self.cut_and_wait()

        approx_2 = MathTex(r"\log 4{,}3 \approx \dfrac{1}{10} 4{,}3").to_edge(DOWN)
        approx_2[0][0:6].set_color(PURE_RED)
        approx_2[0][7:].set_color(PURE_GREEN)
        self.play(ReplacementTransform(approx_1, approx_2))

        self.wait(30)
