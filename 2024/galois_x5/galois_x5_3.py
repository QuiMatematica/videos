from manim import *

from galois_x5_common import PianoX5, COLORS, ZERI


class Scene(MovingCameraScene):

    def construct(self):
        titolo = Title("$x^5-1$: The Galois group is cyclic", color=RED)
        titolo.underline.set_color(RED)
        self.play(Write(titolo))

        piano = PianoX5().move_to((3.5, -.5, 0))
        self.play(Create(piano.piano))
        self.play(*[Create(_d) for _d in piano.dots])

        testo = VGroup(
            MathTex(r"G =\,{<}\sigma_2{>}"),
            Line(),
            MathTex(r"\sigma_2 \mapsto (1243)"),
            MathTex(r"\sigma_2^2 = \sigma_4 \mapsto (14)(23)"),
            MathTex(r"\sigma_2^3 = \sigma_3 \mapsto (1342)"),
            MathTex(r"\sigma_2^4 = \sigma_1 \mapsto (1)(2)(3)(4)"),
        ).arrange(DOWN).move_to((-3.5, -.5, 0))

        # TITOLO

        self.play(Write(testo[0]))
        self.play(Create(testo[1]))

        # FASE 1

        self.play(Write(testo[2]))

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
                color=PURPLE,
                stroke_width=2
            )

            if arc.get_length() < 2 * SMALL_BUFF:
                arc = VMobject()
            else:
                arc.add_tip(ArrowTriangleFilledTip(
                    length=DEFAULT_ARROW_TIP_LENGTH / 2,
                    width=DEFAULT_ARROW_TIP_LENGTH / 2,
                    color=PURPLE
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

        # FASE 2

        self.play(Write(testo[3]))

        self.play(
            piano.dots[1].animate.move_to(piano.piano.c2p(ZERI[4][0], ZERI[4][1])),
            piano.dots[2].animate.move_to(piano.piano.c2p(ZERI[3][0], ZERI[3][1])),
            piano.dots[3].animate.move_to(piano.piano.c2p(ZERI[2][0], ZERI[2][1])),
            piano.dots[4].animate.move_to(piano.piano.c2p(ZERI[1][0], ZERI[1][1])),
            run_time=2
        )

        # FASE 3

        self.play(Write(testo[4]))

        self.play(
            piano.dots[1].animate.move_to(piano.piano.c2p(ZERI[3][0], ZERI[3][1])),
            piano.dots[2].animate.move_to(piano.piano.c2p(ZERI[1][0], ZERI[1][1])),
            piano.dots[3].animate.move_to(piano.piano.c2p(ZERI[4][0], ZERI[4][1])),
            piano.dots[4].animate.move_to(piano.piano.c2p(ZERI[2][0], ZERI[2][1])),
            run_time=2
        )

        # FASE 4

        self.play(Write(testo[5]))

        self.play(
            piano.dots[1].animate.move_to(piano.piano.c2p(ZERI[1][0], ZERI[1][1])),
            piano.dots[2].animate.move_to(piano.piano.c2p(ZERI[2][0], ZERI[2][1])),
            piano.dots[3].animate.move_to(piano.piano.c2p(ZERI[3][0], ZERI[3][1])),
            piano.dots[4].animate.move_to(piano.piano.c2p(ZERI[4][0], ZERI[4][1])),
            run_time=2
        )

        self.wait(3)
