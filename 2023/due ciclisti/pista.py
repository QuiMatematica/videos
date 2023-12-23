from manim import *

PISTA_RADIUS = 2.8
PISTA_COLOR = WHITE

STONE_LEN = .5
STONE_COLOR = WHITE

FLAG_WIDTH = 1
FLAG_HEIGHT = .5

class Pista(Circle):

    def __init__(self, **kwargs):
        super().__init__(radius=PISTA_RADIUS, color=PISTA_COLOR, **kwargs)

        stones = []
        for _i in range(6):
            line = Line(start=STONE_LEN * RIGHT, end=ORIGIN, color=STONE_COLOR)
            line.shift((PISTA_RADIUS - STONE_LEN) * RIGHT)
            flag = Rectangle(width=FLAG_WIDTH, height=FLAG_HEIGHT, color=STONE_COLOR).\
                rotate(PI/2).\
                shift((PISTA_RADIUS - STONE_LEN - FLAG_HEIGHT / 2) * RIGHT)
            if _i == 0:
                flag.shift((FLAG_WIDTH / 2) * DOWN)
            if _i == 5:
                flag.shift((FLAG_WIDTH / 2) * UP)
            label = Tex(100 * _i, "m").move_to(flag).rotate(PI/2).scale(.6)
            stone = VGroup(line, flag, label)
            stone.rotate(TAU/5 * _i + PI/2, about_point=ORIGIN)
            stones.append(stone)
            self.add(stone)
        self.actual_angle = 0
        self.radius = PISTA_RADIUS

    def rotate_to(self, angle):
        actual = self.actual_angle
        delta_angle = angle - actual
        self.rotate_about_origin(angle=delta_angle)
        self.actual_angle = angle

    def get_start_point(self):
        return self.radius * UP

    def get_radius(self):
        return self.radius