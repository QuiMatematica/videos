from manim import Write, MoveToTarget, Table, DL, DR, UR, Line


def set_color(text, *slices, color):
    for _slice in slices:
        text[0][_slice].set_color(color)


class FromFormulaToFormula:

    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.temp_pieces = []

    def write(self, _slice):
        return Write(self.target[0][_slice])

    def copy_and_move(self, source_slice, target_slice):
        tex = self.source[0][source_slice].copy()
        return self.move(tex, target_slice)

    def get_temp_pieces(self):
        return self.temp_pieces

    def move(self, tex, target_slice):
        tex.target = self.target[0][target_slice]
        self.temp_pieces.append(tex)
        return MoveToTarget(tex)


class TableHelper():

    def __init__(self,
                 table: Table):
        self.table = table

    def get_horizontal_line(self,
                            row,
                            start=None,
                            end=None):
        if start is None and end is None:
            return self.table.get_horizontal_lines()[row - 1]
        else:
            start_point = self.table.get_cell((row, start + 1)).get_corner(DL)
            end_point = self.table.get_cell((row, end)).get_corner(DR)
            return Line(start=start_point, end=end_point)

    def get_vertical_line(self,
                          col,
                          start=None,
                          end=None):
        if start is None and end is None:
            return self.table.get_vertical_lines()[col - 1]
        else:
            start_point = self.table.get_cell((start + 1, col)).get_corner(UR)
            end_point = self.table.get_cell((end, col)).get_corner(DR)
            return Line(start=start_point, end=end_point)
