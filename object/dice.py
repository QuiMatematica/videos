from typing import Optional

from colour import Color
from manim import *


class Face(Square):

    def __init__(self, vect, number, side_length=2.0, **kwargs):
        self.vect = vect
        super().__init__(side_length, shade_in_3d=True, **kwargs)
        self.round_corners(radius=0.1)
        if number in [1, 3, 5]:
            # puntino centrale
            self.add(Dot(color=BLACK, radius=0.2).move_to(self))
        if number in [2, 3, 5, 6]:
            # due puntini opposti in diagonale
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * UR))
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * DL))
        if number in [4, 5, 6]:
            # due puntini opposti nell'altra diagonale
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * UL))
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * DR))
        if number == 6:
            # due punti opposti in orizzontale
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * UP))
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * DOWN))

    def set_color(self, color, family=True):
        super().set_color(color, False)

    def set_fill(
            self,
            color: Optional[str] = None,
            opacity: Optional[float] = None,
            family: bool = True,
    ):
        if np.array_equal(self.vect, IN):
            color = interpolate_color(Color(color), Color(WHITE), .3).hex
        elif np.array_equal(self.vect, RIGHT):
            color = interpolate_color(Color(color), Color(BLACK), .2).hex
        super().set_fill(color, 1, False)


class Dice(VMobject):

    result_map = [
        [1, 3, 2],
        [2, 3, 6],
        [3, 5, 6],
        [4, 2, 6],
        [5, 6, 3],
        [6, 3, 5]
    ]

    def __init__(
            self,
            result=1,
            side_length=2,
            fill_color=GRAY,
            **kwargs,
    ):
        self.result = result
        self.side_length = side_length
        super().__init__(
            fill_color=fill_color,
            fill_opacity=1,
            stroke_width=0,
            **kwargs,
        )
        self.rotate(.4 * PI, axis=RIGHT).rotate(PI / 6, axis=UP).rotate(.05 * PI, axis=IN)

    def generate_points(self):
        i = 0
        for vect in IN, DOWN, RIGHT:
            face = Face(vect, Dice.result_map[self.result - 1][i])
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
            i += 1

    init_points = generate_points
