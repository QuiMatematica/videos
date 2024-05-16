import numpy as np
from manim import *

DELAY = 60


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        axes = Axes(
            x_range=[-.9, 11, 1],
            y_range=[-.29, 1.1, .2],
            x_length=9,
            y_length=7,
            tips=True,
            axis_config={"include_numbers": True},
        )

        funzione_logaritmo = MathTex(r"y = \log x", color=PURE_RED)
        funzione_retta = MathTex(r"y = \dfrac{1}{10}x", color=PURE_GREEN)
        funzione_errore = MathTex(r"y = \dfrac{1}{10}x - \log x", color=YELLOW)
        funzione_abs_errore = MathTex(r"y = \biggl| \dfrac{1}{10}x - \log x \biggr|", color=YELLOW).move_to(funzione_errore)

        VGroup(
            axes,
            VGroup(
                funzione_logaritmo,
                funzione_retta,
                funzione_abs_errore
            ).arrange(DOWN)
        ).arrange(RIGHT)

        funzione_errore.move_to(funzione_abs_errore)

        # #######################################

        self.add(axes)

        for _i in range(1, 11):
            self.add(Line(
                axes.c2p(_i, -0.25), axes.c2p(_i, 1.05),
                color=DARK_GRAY, stroke_width=1, stroke_opacity=.5, z_index=-1
            ))

        for _i in range(-2, 11):
            self.add(Line(
                axes.c2p(-.5, _i / 10), axes.c2p(10.5, _i / 10),
                color=DARK_GRAY, stroke_width=1,stroke_opacity=.5, z_index=-1
            ))

        logaritmo = axes.plot(lambda x: np.log10(x), x_range=[1, 10], use_smoothing=True, color=PURE_RED)
        self.add(logaritmo)
        self.add(funzione_logaritmo)

        retta = axes.plot(lambda x: x*.1, x_range=[1, 10], use_smoothing=True, color=PURE_GREEN)
        self.add(retta)
        self.add(funzione_retta)

        tracker = ValueTracker(1)

        def get_errore():
            return axes.plot(lambda x: x*.1 - (np.log10(x)), x_range=[tracker.get_value(), 10], use_smoothing=False, color=YELLOW)

        errore = get_errore()

        self.add(errore)
        self.add(funzione_errore)

        zero = Dot(axes.c2p(1.37, 0), color=YELLOW)
        zero_label = MathTex(r"1{,}37", color=YELLOW).scale(.8).next_to(zero, 3*DOWN)
        zero_arrow = Arrow(zero_label.get_top(), zero.get_bottom(), color=YELLOW, buff=SMALL_BUFF)
        self.add(zero)
        self.add(zero_arrow)
        self.add(zero_label)

        self.cut_and_wait()

        def get_error_point_position():
            x = tracker.get_value()
            return axes.c2p(x, x*.1 - np.log10(x))

        error_point = Dot(color=YELLOW).move_to(get_error_point_position())
        error_point.add_updater(lambda dot: dot.move_to(get_error_point_position()))

        def get_abs_point_position():
            x = tracker.get_value()
            return axes.c2p(x, np.abs(x*.1 - np.log10(x)))

        abs_point = Dot(color=YELLOW).move_to(get_abs_point_position())
        abs_point.add_updater(lambda dot: dot.move_to(get_abs_point_position()))

        def get_diff_line():
            return Line(get_error_point_position(), get_abs_point_position(), color=YELLOW)

        diff_line = get_diff_line()
        diff_line.add_updater(lambda old: old.become(get_diff_line()))

        def get_abs_errore():
            return axes.plot(lambda x: np.abs(x*.1 - (np.log10(x))), x_range=[1, tracker.get_value()], use_smoothing=True, color=YELLOW)

        abs_errore = get_abs_errore()
        abs_errore.add_updater(lambda old: old.become(get_abs_errore()))

        errore.add_updater(lambda old: old.become(get_errore()))

        self.add(error_point, abs_point, diff_line, abs_errore)

        self.play(tracker.animate.set_value(10), run_time=5, rate_func=linear)

        error_point.clear_updaters()
        abs_point.clear_updaters()
        diff_line.clear_updaters()
        abs_errore.clear_updaters()
        errore.clear_updaters()

        self.remove(error_point, abs_point, diff_line, errore)

        self.play(ReplacementTransform(funzione_errore, funzione_abs_errore))
        self.cut_and_wait()

        max = Dot(axes.c2p(4.34, np.abs(4.34*.1 - (np.log10(4.34)))), color=YELLOW)
        max_x = Dot(axes.c2p(4.34, 0), color=YELLOW)
        max_line = DashedLine(max.get_center(), max_x.get_center(), color=YELLOW)
        max_label = MathTex(r"4{,}34", color=YELLOW).scale(.8).next_to(max_x, 3*DOWN)
        max_arrow = Arrow(max_label.get_top(), max_x.get_bottom(), color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(max))
        self.play(Create(max_line))
        self.play(Create(max_x))
        self.play(Create(max_arrow))
        self.play(Write(max_label))

        max_value = MathTex(r"0{,}20", color=YELLOW).scale(.8).next_to(max, 0.1*UP)
        self.play(Write(max_value))
        self.cut_and_wait()

        media = DashedLine(axes.c2p(1, 0.12), axes.c2p(10, 0.12), color=YELLOW)
        self.play(Create(media))
        media_value = MathTex(r"0{,}12", color=YELLOW).scale(.8).next_to(media, 0.1*UP).shift(3*RIGHT)
        self.play(Write(media_value))

        self.wait(30)
