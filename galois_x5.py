import numpy as np
from manim import *

DELAY = 1
SCALE = .7
COLORS = [PURE_RED, ORANGE, YELLOW, PURE_GREEN, PURE_BLUE]

COORDINATE_PIANI = [
    (-2, 1.1, 0),
    (5, 1.1, 0),
    (-2, -2.1, 0),
    (5, -2.1, 0)
]

class Scene(MovingCameraScene):

    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.zeri = None
        self.piani = None

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.zeri = []
        for _i in range(5):
            arg = _i * 2 * PI / 5
            zero = (np.cos(arg), np.sin(arg))
            self.zeri.append(zero)

        titolo = Title("$x^5-1$", color=RED)
        titolo.underline.set_color(RED)
        self.play(Write(titolo))

        radici = MathTex(
            r"x \in \{ 1, e^{i \frac{2 \pi}{5}}, e^{i \frac{4 \pi}{5}}, e^{i \frac{6 \pi}{5}}, e^{i \frac{8 \pi}{5}} \}"
        ).move_to((-3.5, 2, 0))
        self.play(Write(radici))

        piano = ComplexPlane(
            x_range=(-1.5, 1.5, 1),
            y_range=(-1.5, 1.5, 1),
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": DARK_GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            },
        ).add_coordinates().move_to((3.5, -.5, 0))
        self.play(Create(piano))

        circonferenza = Circle(radius=1, color=GRAY, stroke_width=2).move_to(piano.c2p(0, 0))
        self.play(Create(circonferenza))

        lines = []
        dots = []
        for _i in range(5):
            arg = _i * 2 * PI / 5
            # dot = Dot(piano.c2p(np.cos(arg), np.sin(arg)), color=COLORS[_i], z_index=1)
            dot = LabeledDot(
                Text(str(_i), color=BLACK).scale(.2),
                point=piano.c2p(np.cos(arg), np.sin(arg)),
                radius=DEFAULT_DOT_RADIUS,
                color=COLORS[_i]
            )
            dots.append(dot)
            line = Line(piano.c2p(0, 0), dot.get_center(), color=COLORS[_i], stroke_width=2, z_index=1)
            lines.append(line)

        self.play(*[Create(_i) for _i in lines])
        self.play(*[Create(_i) for _i in dots])

        zeta = MathTex(
            r"\zeta \in \{ e^{i \frac{2 \pi}{5}}, e^{i \frac{4 \pi}{5}}, e^{i \frac{6 \pi}{5}}, e^{i \frac{8 \pi}{5}} \}"
        ).next_to(radici, DOWN)
        self.play(Write(zeta))

        polinomio_minimo = MathTex(r"f_\zeta = \phi_5 = x^4 + x^3 + x^2 + x^1 + 1").next_to(zeta, DOWN)
        self.play(Write(polinomio_minimo))

        campo_spezzamento = MathTex(
            r"\Omega = \mathbb{Q}(\zeta) \qquad [ \Omega : \mathbb{Q} ] = 4"
        ).next_to(polinomio_minimo, DOWN)
        self.play(Write(campo_spezzamento))

        gruppo = MathTex(r"G = \text{Gal}(\Omega / \mathbb{Q}) \qquad | G | = 4").next_to(campo_spezzamento, DOWN)
        self.play(Write(gruppo))

        # Pulizia dello schermo e divisione in 4

        grafo = VGroup(piano, *dots)
        self.piani = [grafo, grafo.copy(), grafo.copy(), grafo.copy()]

        self.play(
            FadeOut(radici), FadeOut(zeta), FadeOut(polinomio_minimo),
            FadeOut(campo_spezzamento), FadeOut(gruppo),
            FadeOut(circonferenza), *[FadeOut(_i) for _i in lines],
            Create(Line((-7, -.5, 0), (7, -.5, 0))),
            Create(Line((0, 2.8, 0), (0, -3.8, 0))),
            *[self.piani[_i].animate.scale(SCALE).move_to(COORDINATE_PIANI[_i]) for _i in range(4)]
        )

        self.zoom_su_sigma_1()
        self.zoom_su_sigma_2()
        self.zoom_su_sigma_3()
        self.zoom_su_sigma_4()

        self.wait(30)

    def zoom_su_sigma_2(self):
        self.piani[1].set_z_index(1)
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro), self.piani[1].animate.scale(1 / SCALE).move_to((2, 0, 0)))

        piano = self.piani[1][0]

        sigma_2 = MathTex(r"\sigma_2 \mapsto [\zeta \mapsto \zeta^2]").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        arrows = [
            Arrow(self.piani[1][1 + 1], self.piani[1][1 + 2], color=COLORS[1], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[1][1 + 2], self.piani[1][1 + 4], color=COLORS[2], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[1][1 + 3], self.piani[1][1 + 1], color=COLORS[3], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[1][1 + 4], self.piani[1][1 + 3], color=COLORS[4], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
        ]

        self.play(
            self.piani[1][1+1].animate.move_to(piano.c2p(self.zeri[2][0], self.zeri[2][1])),
            self.piani[1][1+2].animate.move_to(piano.c2p(self.zeri[4][0], self.zeri[4][1])),
            self.piani[1][1+3].animate.move_to(piano.c2p(self.zeri[1][0], self.zeri[1][1])),
            self.piani[1][1+4].animate.move_to(piano.c2p(self.zeri[3][0], self.zeri[3][1])),
            *[GrowArrow(_a) for _a in arrows],
            run_time=2
        )

        self.piani[1].add(*arrows)

        s4 = MathTex(r"\sigma_2 \mapsto (1243)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.cut_and_wait()

        self.play(
            FadeOut(riquadro),
            self.piani[1].animate.scale(SCALE).move_to(COORDINATE_PIANI[1]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[1] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[1] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_3(self):
        self.piani[2].set_z_index(1)
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro), self.piani[2].animate.scale(1 / SCALE).move_to((2, 0, 0)))

        piano = self.piani[2][0]

        sigma_2 = MathTex(r"\sigma_3 \mapsto [\zeta \mapsto \zeta^3]").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        arrows = [
            Arrow(self.piani[2][1 + 1], self.piani[2][1 + 3], color=COLORS[1], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[2][1 + 2], self.piani[2][1 + 1], color=COLORS[2], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[2][1 + 3], self.piani[2][1 + 4], color=COLORS[3], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
            Arrow(self.piani[2][1 + 4], self.piani[2][1 + 2], color=COLORS[4], buff=SMALL_BUFF, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=3, stroke_width=3),
        ]

        self.play(
            self.piani[2][1+1].animate.move_to(piano.c2p(self.zeri[3][0], self.zeri[3][1])),
            self.piani[2][1+2].animate.move_to(piano.c2p(self.zeri[1][0], self.zeri[1][1])),
            self.piani[2][1+3].animate.move_to(piano.c2p(self.zeri[4][0], self.zeri[4][1])),
            self.piani[2][1+4].animate.move_to(piano.c2p(self.zeri[2][0], self.zeri[2][1])),
            *[GrowArrow(_a) for _a in arrows],
            run_time=2
        )

        self.piani[2].add(*arrows)

        s4 = MathTex(r"\sigma_3 \mapsto (1342)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.cut_and_wait()

        self.play(
            FadeOut(riquadro),
            self.piani[2].animate.scale(SCALE).move_to(COORDINATE_PIANI[2]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[2] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[2] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_4(self):
        self.piani[3].set_z_index(1)
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro), self.piani[3].animate.scale(1 / SCALE).move_to((2, 0, 0)))

        piano = self.piani[3][0]

        sigma_2 = MathTex(r"\sigma_4 \mapsto [\zeta \mapsto \zeta^4]").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        arrows = [
            CurvedArrow(self.piani[3][1 + 1].get_center(), self.piani[3][1 + 4].get_center(), color=COLORS[1], stroke_width=3, angle=PI/4),
            CurvedArrow(self.piani[3][1 + 2].get_center(), self.piani[3][1 + 3].get_center(), color=COLORS[2], stroke_width=3, angle=PI/4),
            CurvedArrow(self.piani[3][1 + 3].get_center(), self.piani[3][1 + 2].get_center(), color=COLORS[3], stroke_width=3, angle=PI/4),
            CurvedArrow(self.piani[3][1 + 4].get_center(), self.piani[3][1 + 1].get_center(), color=COLORS[4], stroke_width=3, angle=PI/4),
        ]

        self.play(
            self.piani[3][1+1].animate.move_to(piano.c2p(self.zeri[4][0], self.zeri[4][1])),
            self.piani[3][1+2].animate.move_to(piano.c2p(self.zeri[3][0], self.zeri[3][1])),
            self.piani[3][1+3].animate.move_to(piano.c2p(self.zeri[2][0], self.zeri[2][1])),
            self.piani[3][1+4].animate.move_to(piano.c2p(self.zeri[1][0], self.zeri[1][1])),
            *[Create(_a) for _a in arrows],
            run_time=2
        )

        self.piani[3].add(*arrows)

        s4 = MathTex(r"\sigma_4 \mapsto (14)(23)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.cut_and_wait()

        self.play(
            FadeOut(riquadro),
            self.piani[3].animate.scale(SCALE).move_to(COORDINATE_PIANI[3]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[3] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[3] + 3 * LEFT + .2 * DOWN),
        )

    def zoom_su_sigma_1(self):
        self.piani[0].set_z_index(1)
        riquadro = Rectangle(height=3.2 / SCALE, width=7 / SCALE, fill_color=BLACK, fill_opacity=1)
        self.play(Create(riquadro), self.piani[0].animate.scale(1 / SCALE).move_to((2, 0, 0)))

        piano = self.piani[0][0]

        sigma_2 = MathTex(r"\sigma_1 \mapsto [\zeta \mapsto \zeta]").move_to((-2, .6, 0))
        self.play(Write(sigma_2))

        RADIUS = .3

        arrows = [
            Arc(arc_center=self.piani[0][1 + 1].get_center() + RADIUS * LEFT, color=COLORS[1], stroke_width=3, start_angle=0, angle=2*PI, radius=.3),
            Arc(arc_center=self.piani[0][1 + 2].get_center() + RADIUS * LEFT, color=COLORS[2], stroke_width=3, start_angle=0, angle=2*PI, radius=.3),
            Arc(arc_center=self.piani[0][1 + 3].get_center() + RADIUS * LEFT, color=COLORS[3], stroke_width=3, start_angle=0, angle=2*PI, radius=.3),
            Arc(arc_center=self.piani[0][1 + 4].get_center() + RADIUS * LEFT, color=COLORS[4], stroke_width=3, start_angle=0, angle=2*PI, radius=.3),
        ]

        # for _a in arrows:
        #     _a.add_tip(tip_shape=ArrowTriangleFilledTip)

        self.play(
            *[Create(_a) for _a in arrows],
            run_time=2
        )

        self.piani[0].add(*arrows)

        s4 = MathTex(r"\sigma_1 \mapsto (1)(2)(3)(4)").move_to((-2, -.6, 0))
        self.play(Write(s4))

        self.cut_and_wait()

        self.play(
            FadeOut(riquadro),
            self.piani[0].animate.scale(SCALE).move_to(COORDINATE_PIANI[0]).set_z_index(0),
            sigma_2.animate.scale(SCALE).move_to(COORDINATE_PIANI[0] + 3 * LEFT + .5 * UP),
            s4.animate.scale(SCALE).move_to(COORDINATE_PIANI[0] + 3 * LEFT + .2 * DOWN),
        )
