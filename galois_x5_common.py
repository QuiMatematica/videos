from manim import *

DELAY = 1
COLORS = [PURE_RED, ORANGE, YELLOW, PURE_GREEN, PURE_BLUE]

ZERI = [
    (np.cos(_i * 2 * PI / 5), np.sin(_i * 2 * PI / 5), 0) for _i in range(5)
]


class PianoX5(VGroup):

    def __init__(self):
        super().__init__()
        self.piano = ComplexPlane(
            x_range=(-1.5, 1.5, 1),
            y_range=(-1.5, 1.5, 1),
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": DARK_GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            },
        ).add_coordinates()

        self.circonferenza = Circle(
            radius=self.piano.c2p(1, 0)[0],
            color=GRAY,
            stroke_width=2
        ).move_to(self.piano.c2p(0, 0))

        self.lines = []
        self.dots = []
        for _i in range(5):
            dot = LabeledDot(
                MathTex(str(_i), color=BLACK).scale(.4),
                radius=DEFAULT_DOT_RADIUS*1.1,
                color=COLORS[_i],
            )
            dot.move_to(self.piano.c2p(ZERI[_i][0], ZERI[_i][1]))

            self.dots.append(dot)
            line = Line(self.piano.c2p(0, 0), dot.get_center(), color=COLORS[_i], stroke_width=2)
            self.lines.append(line)

        self.add(
            self.piano,
            self.circonferenza,
            *self.lines,
            *self.dots
        )
