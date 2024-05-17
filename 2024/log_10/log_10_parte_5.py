from manim import *

DELAY = 30


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

        tracker = ValueTracker(0)

        self.add(axes.plot(lambda x: x*.1, x_range=[1, 1.5], use_smoothing=True, color=PURE_GREEN))
        self.add(axes.plot(lambda x: x*.1, x_range=[9, 10], use_smoothing=True, color=PURE_GREEN))

        def get_retta():
            return axes.plot(lambda x: x*.1 + tracker.get_value(), x_range=[1.5, 9], use_smoothing=True, color=PURE_GREEN)

        retta = get_retta()
        self.add(retta)

        self.add(axes.plot(lambda x: x*.1 - (np.log10(x)), x_range=[1, 1.5], use_smoothing=False, color=YELLOW))
        self.add(axes.plot(lambda x: x*.1 - (np.log10(x)), x_range=[9, 10], use_smoothing=True, color=YELLOW))

        def get_errore():
            return axes.plot(lambda x: x*.1 + tracker.get_value() - (np.log10(x)), x_range=[1.5, 9], use_smoothing=False, color=YELLOW)

        errore = get_errore()
        self.add(errore)
        self.cut_and_wait()

        limite_inf = Line(axes.c2p(1.5, 1.05), axes.c2p(1.5, -.25), color=PURE_BLUE, stroke_width=3)
        limite_sup = Line(axes.c2p(9, 1.05), axes.c2p(9, -.25), color=PURE_BLUE, stroke_width=3)

        self.play(Create(limite_inf))
        self.play(Create(limite_sup))
        self.cut_and_wait()

        retta.add_updater(lambda old: old.become(get_retta()))
        errore.add_updater(lambda old: old.become(get_errore()))

        self.play(tracker.animate.set_value(.1), run_time=2, rate_func=linear)

        retta.clear_updaters()
        errore.clear_updaters()
        self.cut_and_wait()

        max = Dot(axes.c2p(4.34, 4.34*.1 + .1 - (np.log10(4.34))), color=YELLOW)
        max_x = Dot(axes.c2p(4.34, 0), color=YELLOW)
        max_line = DashedLine(max.get_center(), max_x.get_center(), color=YELLOW)
        max_label = MathTex(r"4{,}34", color=YELLOW).scale(.8).next_to(max_x, 3*UP)
        max_arrow = Arrow(max_label.get_bottom(), max_x.get_top(), color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(max))
        self.play(Create(max_line))
        self.play(Create(max_x))
        self.play(Create(max_arrow))
        self.play(Write(max_label))

        max_value = MathTex(r"0{,}10", color=YELLOW).scale(.8).next_to(max, 0.1*DOWN)
        self.play(Write(max_value))
        self.cut_and_wait()

        self.wait(30)
