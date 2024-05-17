from manim import *

from galois_x5_common import PianoX5, COLORS

SCALE = .7

COORDINATE_PIANI = [
    (-2, 1.1, 0),
    (5, 1.1, 0),
    (-2, -2.1, 0),
    (5, -2.1, 0)
]

BUFF_DEGREES = 3 * DEGREES


class Scene(MovingCameraScene):

    def construct(self):

        titolo = Title("$x^5-1$: Galois group elements", color=RED)
        titolo.underline.set_color(RED)
        self.play(Write(titolo))

        self.play(
            Create(Line((-7, -.5, 0), (7, -.5, 0))),
            Create(Line((0, 2.6, 0), (0, -3.8, 0))),
        )

        self.zoom_su_sigma_1()
        self.zoom_su_sigma_2()
        self.zoom_su_sigma_3()
        self.zoom_su_sigma_4()

        self.wait(3)

    def zoom_su_sigma_2(self):
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro))

        piano = PianoX5().move_to((2, 0, 0))
        self.play(Create(piano.piano))
        self.play(*[Create(_d) for _d in piano.dots])

        sigma_2 = MathTex(r"\sigma_2(\zeta) = \zeta^2").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        paths = [
            Line(piano.dots[1].get_center(), piano.dots[2].get_center()),
            Line(piano.dots[2].get_center(), piano.dots[4].get_center()),
            Line(piano.dots[3].get_center(), piano.dots[1].get_center()),
            Line(piano.dots[4].get_center(), piano.dots[3].get_center()),
        ]

        def get_arc(n):
            start = paths[n].get_start()
            dot = piano.dots[n + 1].get_center()

            arc = Line(
                start, dot,
                buff=SMALL_BUFF,
                color=COLORS[n+1],
                stroke_width=2
            )

            if arc.get_length() < 2 * SMALL_BUFF:
                arc = VMobject()
            else:
                arc.add_tip(ArrowTriangleFilledTip(
                    length=DEFAULT_ARROW_TIP_LENGTH / 2,
                    width=DEFAULT_ARROW_TIP_LENGTH / 2,
                    color=COLORS[n + 1]
                ))

            return arc

        def init_arc(n):
            arc = get_arc(n)
            arc.add_updater(lambda old: old.become(get_arc(n)))
            self.add(arc)
            return arc

        arcs = [init_arc(_i) for _i in range(4)]

        self.play(
            *[MoveAlongPath(piano.dots[_i + 1], paths[_i]) for _i in range(4)],
            run_time=2
        )

        for _i in range(4):
            arcs[_i].clear_updaters()
        piano.add(*arcs)
        piano.remove(piano.circonferenza)
        piano.remove(*piano.lines)

        s4 = MathTex(r"\sigma_2 \mapsto (1243)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.wait(1)

        self.play(
            FadeOut(riquadro),
            piano.animate.scale(SCALE).move_to(COORDINATE_PIANI[1]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[1] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[1] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_3(self):
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro))

        piano = PianoX5().move_to((2, 0, 0))
        self.play(Create(piano.piano))
        self.play(*[Create(_d) for _d in piano.dots])

        sigma_2 = MathTex(r"\sigma_3(\zeta) = \zeta^3").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        paths = [
            Line(piano.dots[1].get_center(), piano.dots[3].get_center()),
            Line(piano.dots[2].get_center(), piano.dots[1].get_center()),
            Line(piano.dots[3].get_center(), piano.dots[4].get_center()),
            Line(piano.dots[4].get_center(), piano.dots[2].get_center()),
        ]

        def get_arc(n):
            start = paths[n].get_start()
            dot = piano.dots[n + 1].get_center()

            arc = Line(
                start, dot,
                buff=SMALL_BUFF,
                color=COLORS[n+1],
                stroke_width=2
            )

            if arc.get_length() < 2 * SMALL_BUFF:
                arc = VMobject()
            else:
                arc.add_tip(ArrowTriangleFilledTip(
                    length=DEFAULT_ARROW_TIP_LENGTH / 2,
                    width=DEFAULT_ARROW_TIP_LENGTH / 2,
                    color=COLORS[n + 1]
                ))

            return arc

        def init_arc(n):
            arc = get_arc(n)
            arc.add_updater(lambda old: old.become(get_arc(n)))
            self.add(arc)
            return arc

        arcs = [init_arc(_i) for _i in range(4)]

        self.play(
            *[MoveAlongPath(piano.dots[_i + 1], paths[_i]) for _i in range(4)],
            run_time=2
        )

        for _i in range(4):
            arcs[_i].clear_updaters()
        piano.add(*arcs)
        piano.remove(piano.circonferenza)
        piano.remove(*piano.lines)

        s4 = MathTex(r"\sigma_3 \mapsto (1342)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.wait(1)

        self.play(
            FadeOut(riquadro),
            piano.animate.scale(SCALE).move_to(COORDINATE_PIANI[2]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[2] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[2] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_4(self):
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro))

        piano = PianoX5().move_to((2, 0, 0))
        self.play(Create(piano.piano))
        self.play(*[Create(_d) for _d in piano.dots])

        sigma_2 = MathTex(r"\sigma_4 (\zeta) = \zeta^4").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        paths = [
            ArcBetweenPoints(piano.dots[1].get_center(), piano.dots[4].get_center(), angle=PI / 4),
            ArcBetweenPoints(piano.dots[2].get_center(), piano.dots[3].get_center(), angle=PI / 4),
            ArcBetweenPoints(piano.dots[3].get_center(), piano.dots[2].get_center(), angle=PI / 4),
            ArcBetweenPoints(piano.dots[4].get_center(), piano.dots[1].get_center(), angle=PI / 4),
        ]

        def get_arc(n):
            start = paths[n].get_start()
            arc_center = (start[0] + start[1] / np.tan(PI/8), 0, 0)
            dot_center = piano.dots[n + 1].get_center()
            start_angle = np.arctan((start[1] - arc_center[1])/(start[0] - arc_center[0]))
            end_angle = np.arctan((dot_center[1] - arc_center[1])/(dot_center[0] - arc_center[0]))
            if np.sign(start[1]) > 0:
                start_angle += PI
                end_angle += PI
            angle = end_angle - start_angle
            if angle < 2 * BUFF_DEGREES:
                arc = VMobject()
            else:
                arc = Arc(
                    arc_center=arc_center,
                    radius=paths[n].radius,
                    start_angle=start_angle + BUFF_DEGREES,
                    angle=angle - 2 * BUFF_DEGREES,
                    color=COLORS[n+1],
                    stroke_width=2
                )
                arc.add_tip(ArrowTriangleFilledTip(
                    length=DEFAULT_ARROW_TIP_LENGTH/2,
                    width=DEFAULT_ARROW_TIP_LENGTH/2,
                    color=COLORS[n+1]
                ))
            return arc

        def init_arc(n):
            arc = get_arc(n)
            arc.add_updater(lambda old: old.become(get_arc(n)))
            self.add(arc)
            return arc

        arcs = [init_arc(_i) for _i in range(4)]

        self.play(
            *[MoveAlongPath(piano.dots[_i + 1], paths[_i]) for _i in range(4)],
            run_time=2
        )

        for _i in range(4):
            arcs[_i].clear_updaters()
        piano.add(*arcs)
        piano.remove(piano.circonferenza)
        piano.remove(*piano.lines)

        s4 = MathTex(r"\sigma_4 \mapsto (14)(23)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.wait(1)

        self.play(
            FadeOut(riquadro),
            piano.animate.scale(SCALE).move_to(COORDINATE_PIANI[3]),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[3] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[3] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_1(self):
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro))

        piano = PianoX5().move_to((2, 0, 0))
        self.play(Create(piano.piano))
        self.play(*[Create(_d) for _d in piano.dots])

        sigma_2 = MathTex(r"\sigma_1 (\zeta) = \zeta").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        piano.remove(piano.circonferenza)
        piano.remove(*piano.lines)

        s4 = MathTex(r"\sigma_1 \mapsto (1)(2)(3)(4)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.wait(1)

        self.play(
            FadeOut(riquadro),
            piano.animate.scale(SCALE).move_to(COORDINATE_PIANI[0]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[0] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[0] + 3 * LEFT + .2 * DOWN),
        )
