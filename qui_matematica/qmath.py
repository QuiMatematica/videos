from abc import ABC
from typing import Sequence

from manim import *


class EqSystem(VMobject, ABC):

    def __init__(self, *equation_texs, **kwargs):
        super().__init__(**kwargs)
        self.eqs = VGroup()
        for tex in equation_texs:
            self.eqs.add(tex)
        self.eqs.arrange(DOWN, aligned_edge=LEFT)

        self.bracket = MathTex(r"\{")
        self.bracket.scale(2)
        # self.bracket.stretch_to_fit_height(self.eqs.height + 2 * MED_SMALL_BUFF)
        self.bracket.stretch_to_fit_height(self.eqs.height)
        self.bracket.next_to(self.eqs, LEFT, MED_SMALL_BUFF)
        self.add(self.bracket, self.eqs)
        self.center()


class PascalTriangle(VGroup, ABC):

    def __init__(self, n_rows):
        super().__init__()
        self.lines = []
        for _i in range(n_rows):
            self.add_line()
        self.arrange(DOWN)

    def add_line(self):
        numbers = []
        items = VGroup()
        line_index = len(self.lines)
        # print("line index: ", line_index)
        for _pos in range(line_index + 1):
            # print("pos: ", _pos)
            if _pos == 0:
                items.add(MathTex(r"1"))
                numbers.append(1)
            elif _pos == line_index:
                items.add(MathTex(r"1").set_x(items[-1].get_x() + 1))
                numbers.append(1)
            else:
                prev_line = self.lines[line_index - 1]
                number = prev_line[_pos - 1] + prev_line[_pos]
                numbers.append(number)
                items.add(MathTex(str(number)).set_x(items[-1].get_x() + 1))
        self.lines.append(numbers)
        self.add(items)


class NumericalTriangle(VGroup):

    def __init__(self, n_rows, rect_width=3, rect_height=1.6):
        super().__init__()
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.values = [None] * n_rows
        self.value_objects = [None] * n_rows
        for _i in range(n_rows):
            self.add_line()

    def add_line(self):
        items = VGroup()
        line_index = len(self.submobjects)
        for _pos in range(line_index + 1):
            items.add(self.get_rect())
        items.arrange(RIGHT, buff=0)
        self.add(items)
        self.arrange(DOWN, buff=0)
        self.values[line_index] = [None] * (line_index + 1)
        self.value_objects[line_index] = [None] * (line_index + 1)

    def get_rect(self):
        return Rectangle(width=self.rect_width, height=self.rect_height)

    def get_cell(self, pos: Sequence[int]) -> Rectangle:
        return self[pos[0]][pos[1]]

    def put_value(self, pos: Sequence[int], value, value_color=WHITE, value_scale=2):
        self.values[pos[0]][pos[1]] = value
        value_object = MathTex(str(value), color=value_color).scale(value_scale).move_to(self.get_cell(pos))
        self.value_objects[pos[0]][pos[1]] = value_object
        return value_object

    def get_value(self, pos: Sequence[int]):
        return self.values[pos[0]][pos[1]]

    def get_value_object(self, pos: Sequence[int]):
        return self.value_objects[pos[0]][pos[1]]