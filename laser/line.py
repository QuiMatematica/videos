from manim import Line, Rectangle, YELLOW, YELLOW_A, BLACK


class LaserLine(Line):

    def __init__(self, start, end, **kwargs):
        super().__init__(start, end, color=YELLOW, **kwargs)
        glom_size = .2
        glom = Rectangle(height=glom_size, width=glom_size + self.width, z_index=self.z_index - 1, fill_opacity=.3,
                         fill_color=YELLOW_A, color=BLACK).round_corners(radius=.2)
        self.add(glom)
