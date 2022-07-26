from manim import Write, MoveToTarget


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
