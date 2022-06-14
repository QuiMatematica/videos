from typing import Optional

from colour import Color
from manim import *


class Video2D(MovingCameraScene):

    def construct(self):
        delay = 1

        title = Title("6 su tutti i dadi")
        self.play(Write(title))
        self.wait(delay)
        self.next_section()

        red_dice = Dice().shift(2*LEFT)
        yellow_dice = Dice()
        blue_dice = Dice().shift(2*RIGHT)
        self.play(SpinInFromNothing(red_dice))
        self.play(SpinInFromNothing(yellow_dice))
        self.play(SpinInFromNothing(blue_dice))
        self.wait(1)
        self.play(red_dice.animate.set_color(PURE_RED))
        self.play(yellow_dice.animate.set_color(YELLOW))
        self.play(blue_dice.animate.set_color(PURE_BLUE))
        self.wait(60)


class Face(Square):

    def __init__(self, vect, side_length=2.0, **kwargs):
        self.vect = vect
        super().__init__(side_length, shade_in_3d=True, **kwargs)
        self.round_corners(radius=0.1)
        if not np.array_equal(self.vect, IN):
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * UR))
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * DL))
        if not np.array_equal(self.vect, RIGHT):
            self.add(Dot(color=BLACK, radius=0.2).move_to(self))

    def set_color(self, color, family=True):
        super().set_color(color, False)

    def set_fill(
            self,
            color: Optional[str] = None,
            opacity: Optional[float] = None,
            family: bool = True,
    ):
        if np.array_equal(self.vect, IN):
            color = interpolate_color(Color(color), Color(WHITE), .5).hex
        elif np.array_equal(self.vect, RIGHT):
            color = interpolate_color(Color(color), Color(BLACK), .2).hex
        super().set_fill(color, 1, False)


class Dice(VMobject):

    def __init__(
            self,
            side_length=2,
            fill_color=GRAY,
            **kwargs,
    ):
        self.side_length = side_length
        super().__init__(
            fill_color=fill_color,
            fill_opacity=1,
            stroke_width=0,
            **kwargs,
        )
        self.rotate(.4 * PI, axis=RIGHT).rotate(PI / 6, axis=UP).rotate(.05 * PI, axis=IN)

    def generate_points(self):
        for vect in IN, DOWN, RIGHT:
            face = Face(vect)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

    init_points = generate_points
