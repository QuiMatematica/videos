from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTip

SURROUNDING_BUFF = .2
SURROUNDING_FILL_OPACITY = .3

PROBLEM_NODE = 0
PROBLEM_DATA = 1
PROBLEM_REQUEST = 2
PROBLEM_UNKNOWN = 3


class ProblemGraphNode:

    def __init__(self, node_name: str, node_object: VMobject, node_type: int):
        self.node_name = node_name
        self.node_object = node_object
        self.node_type = node_type
        self.rendered = self._build_rendered()
        self.n_row = -1
        self.n_col = -1

    def get_object(self):
        return self.node_object

    def get_rendered(self):
        return self.rendered

    def _build_rendered(self):
        rendered = VGroup()
        rendered.add(self.node_object)
        if self.node_type == PROBLEM_REQUEST:
            rendered.add(SurroundingRectangle(self.node_object, RED, buff=SURROUNDING_BUFF,
                                              fill_opacity=SURROUNDING_FILL_OPACITY))
        elif self.node_type == PROBLEM_DATA:
            rendered.add(SurroundingRectangle(self.node_object, YELLOW, buff=SURROUNDING_BUFF,
                                              fill_opacity=SURROUNDING_FILL_OPACITY))
        elif self.node_type == PROBLEM_UNKNOWN:
            rendered.add(SurroundingRectangle(self.node_object, color=BLUE,
                                              fill_opacity=SURROUNDING_FILL_OPACITY, buff=SURROUNDING_BUFF,
                                              corner_radius=.4))
        return rendered


class GraphArrow(Line):

    def __init__(
            self,
            *args,
            stroke_width=2,
            **kwargs,
    ):
        tip_shape = kwargs.pop("tip_shape", ArrowTriangleFilledTip)
        super().__init__(*args, buff=0, stroke_width=stroke_width, **kwargs)
        self.add_tip(tip_shape=tip_shape)

    def get_default_tip_length(self) -> float:
        return .2


class ProblemGraph:

    def __init__(self):
        self.nodes = {}
        self.objects = VGroup()
        self.rows = VGroup()

    def add_node(self, node_name: str, node_object: VMobject, node_type=PROBLEM_NODE):
        self.nodes[node_name] = ProblemGraphNode(node_name, node_object, node_type)
        return self

    def get_objects(self):
        return self.objects

    def build_row(self, *node_names, hbuff=1, vbuff=1):
        n_row = len(self.rows)
        n_col = 0
        row_group = VGroup()
        for name in node_names:
            node = self.nodes[name]
            node.n_row = n_row
            node.n_col = n_col
            n_col += 1
            rendered = node.get_rendered()
            row_group.add(rendered)
            self.objects.add(rendered)
        row_group.arrange(RIGHT, buff=hbuff)
        self.rows.add(row_group)
        self.rows.arrange(DOWN, buff=vbuff)

    def _get_shift(self, node):
        start_row = self.rows[node.n_row]
        len_start_row = len(start_row)
        first_index = (1 - len_start_row) / 2
        index = first_index + node.n_col
        return RIGHT * 0.3 * index

    def add_up_arrow(self, start_node, to_node, start_shift=OUT, to_shift=OUT):
        if type(start_node) is str:
            start_node = self.nodes[start_node]
        if type(to_node) is str:
            to_node = self.nodes[to_node]

        if to_shift is OUT:
            to_shift = self._get_shift(start_node)
        if start_shift is OUT:
            start_shift = self._get_shift(to_node)

        print("Up arrow: from", start_node.node_name, "- to", to_node.node_name, "- from shift", start_shift,
              "- to shift", to_shift)

        start_node = start_node.get_object()
        to_node = to_node.get_object()

        arrow = GraphArrow(start=start_node.get_top() + .1 * UP + start_shift,
                           end=to_node.get_bottom() + .1 * DOWN + to_shift)
        self.objects.add(arrow)

    def add_down_arrow(self, start_node, to_node, start_shift=OUT, to_shift=OUT):
        if type(start_node) is str:
            start_node = self.nodes[start_node]
        if type(to_node) is str:
            to_node = self.nodes[to_node]

        if to_shift is OUT:
            to_shift = self._get_shift(start_node)
        if start_shift is OUT:
            start_shift = self._get_shift(to_node)

        print("Down arrow: from", start_node.node_name, "- to", to_node.node_name, "- from shift", start_shift,
              "- to shift", to_shift)

        start_node = start_node.get_object()
        to_node = to_node.get_object()

        arrow = GraphArrow(start=start_node.get_bottom() + .1 * DOWN + start_shift,
                           end=to_node.get_top() + .1 * UP + to_shift)
        self.objects.add(arrow)

    def add_right_arrow(self, start_node, to_node, start_shift=OUT, to_shift=OUT):
        if type(start_node) is str:
            start_node = self.nodes[start_node]
        if type(to_node) is str:
            to_node = self.nodes[to_node]

        if to_shift is OUT:
            to_shift = ORIGIN
        if start_shift is OUT:
            start_shift = ORIGIN

        print("Right arrow: from", start_node.node_name, "- to", to_node.node_name, "- from shift", start_shift,
              "- to shift", to_shift)

        start_node = start_node.get_object()
        to_node = to_node.get_object()

        arrow = GraphArrow(start=start_node.get_right() + .1 * RIGHT + start_shift,
                           end=to_node.get_left() + .1 * LEFT + to_shift)
        self.objects.add(arrow)

    def add_left_arrow(self, start_node, to_node, start_shift=OUT, to_shift=OUT):
        if type(start_node) is str:
            start_node = self.nodes[start_node]
        if type(to_node) is str:
            to_node = self.nodes[to_node]

        if to_shift is OUT:
            to_shift = ORIGIN
        if start_shift is OUT:
            start_shift = ORIGIN

        print("Left arrow: from", start_node.node_name, "- to", to_node.node_name, "- from shift", start_shift,
              "- to shift", to_shift)

        start_node = start_node.get_object()
        to_node = to_node.get_object()

        arrow = GraphArrow(start=start_node.get_left() + .1 * LEFT + start_shift,
                           end=to_node.get_right() + .1 * RIGHT + to_shift)
        self.objects.add(arrow)

    def add_arrow(self, start_node_name, to_node_name, start_shift=OUT, to_shift=OUT):
        start_node = self.nodes[start_node_name]
        to_node = self.nodes[to_node_name]
        start_row = start_node.n_row
        to_row = to_node.n_row
        if start_row > to_row:
            self.add_up_arrow(start_node, to_node, start_shift, to_shift)
        elif start_row < to_row:
            self.add_down_arrow(start_node, to_node, start_shift, to_shift)
        else:
            start_col = start_node.n_col
            to_col = to_node.n_col
            if start_col > to_col:
                self.add_left_arrow(start_node, to_node, start_shift, to_shift)
            else:
                self.add_right_arrow(start_node, to_node, start_shift, to_shift)

    def scale(self, ratio):
        self.rows.scale(ratio)
