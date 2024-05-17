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
            x_length=10,
            y_length=7,
            tips=True,
            axis_config={"include_numbers": True},
        )

        funzione_logaritmo = MathTex(r"y = \log x", color=PURE_RED)
        funzione_retta = MathTex(r"y = \dfrac{1}{10}x", color=PURE_GREEN)
        funzione_errore = MathTex(r"y = \dfrac{1}{10}x - \log x", color=YELLOW)

        approx_1 = MathTex(r"\log {{ x }} \approx {{ \dfrac{1}{10} }} x")
        approx_1[0].set_color(PURE_RED)
        approx_1[1].set_color(PURE_RED)
        approx_1[3].set_color(PURE_GREEN)
        approx_1[4].set_color(PURE_GREEN)

        VGroup(
            axes,
            VGroup(
                funzione_logaritmo,
                funzione_retta,
                funzione_errore,
                Tex("*"),
                approx_1
            ).arrange(DOWN)
        ).arrange(RIGHT)

        approx_2 = MathTex(r"\log {{ 4{,}3 }} \approx {{ \dfrac{1}{10} }} 4{,}3").move_to(approx_1)
        approx_2[0].set_color(PURE_RED)
        approx_2[1].set_color(PURE_RED)
        approx_2[3].set_color(PURE_GREEN)
        approx_2[4].set_color(PURE_GREEN)

        approx_3 = MathTex(r"\log {{ 4{,}3 }} \approx {{ 0{,}43 }}").move_to(approx_2)
        approx_3[0].set_color(PURE_RED)
        approx_3[1].set_color(PURE_RED)
        approx_3[3].set_color(PURE_GREEN)

        # #######################################

        self.play(Create(axes))

        for _i in range(1, 11):
            self.play(Create(Line(
                axes.c2p(_i, -0.25), axes.c2p(_i, 1.05),
                color=DARK_GRAY, stroke_width=1, stroke_opacity=.5, z_index=-1
            )), run_time=.1)

        for _i in range(-2, 11):
            self.play(Create(Line(
                axes.c2p(-.5, _i / 10), axes.c2p(10.5, _i / 10),
                color=DARK_GRAY, stroke_width=1,stroke_opacity=.5, z_index=-1
            )), run_time=.1)

        logaritmo = axes.plot(lambda x: np.log10(x), x_range=[1, 10], use_smoothing=True, color=PURE_RED)
        self.play(Create(logaritmo))
        self.play(Write(funzione_logaritmo))
        self.cut_and_wait()

        retta = axes.plot(lambda x: x*.1, x_range=[1, 10], use_smoothing=True, color=PURE_GREEN)
        self.play(Create(retta))
        self.play(Write(funzione_retta))
        self.cut_and_wait()

        self.play(Write(approx_1))
        self.cut_and_wait()

        self.play(TransformMatchingTex(approx_1, approx_2))
        self.cut_and_wait()

        self.play(TransformMatchingTex(approx_2, approx_3))
        self.cut_and_wait()

        tracker = ValueTracker(1)

        def get_errore():
            return axes.plot(lambda x: x*.1 - (np.log10(x)), x_range=[1, tracker.get_value()], use_smoothing=True, color=YELLOW)

        errore = get_errore()
        errore.add_updater(lambda old: old.become(get_errore()))

        def get_log_point_position():
            x = tracker.get_value()
            return axes.c2p(x, np.log10(x))

        log_point = Dot(color=PURE_RED).move_to(get_log_point_position())
        log_point.add_updater(lambda dot: dot.move_to(get_log_point_position()))

        def get_iper_point_position():
            x = tracker.get_value()
            return axes.c2p(x, x*.1)

        iper_point = Dot(color=PURE_GREEN).move_to(get_iper_point_position())
        iper_point.add_updater(lambda dot: dot.move_to(get_iper_point_position()))

        def get_diff_line():
            return Line(log_point.get_center(), iper_point.get_center(), color=YELLOW)

        diff_line = get_diff_line()
        diff_line.add_updater(lambda old: old.become(get_diff_line()))

        self.add(errore, log_point, iper_point, diff_line)

        self.play(tracker.animate.set_value(10), run_time=5, rate_func=linear)

        errore.clear_updaters()
        log_point.clear_updaters()
        iper_point.clear_updaters()
        diff_line.clear_updaters()

        self.remove(log_point, iper_point, diff_line)
        self.play(Write(funzione_errore))
        self.cut_and_wait()

        zero = Dot(axes.c2p(1.37, 0), color=YELLOW)
        zero_label = MathTex(r"1{,}37", color=YELLOW).scale(.8).next_to(zero, 3*DOWN)
        zero_arrow = Arrow(zero_label.get_top(), zero.get_bottom(), color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(zero))
        self.play(Create(zero_arrow))
        self.play(Create(zero_label))

        self.wait(30)
