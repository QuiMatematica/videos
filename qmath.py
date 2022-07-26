from abc import ABC

from manim import *


class EqSystem(VMobject, ABC):

    def __init__(self, *equation_texs, **kwargs):
        super().__init__(**kwargs)
        eqs = VGroup()
        for tex in equation_texs:
            eqs.add(tex)
        eqs.arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\{")
        bracket.scale(2)
        bracket.stretch_to_fit_height(eqs.height + 2 * MED_SMALL_BUFF)
        bracket.next_to(eqs, LEFT, MED_SMALL_BUFF)
        self.add(bracket, eqs)
        self.center()


class Tartaglia(VGroup, ABC):

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
