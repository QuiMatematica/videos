from manim import *

from qproblem import *

REQUEST = '2P'
DATA_1 = 'BC=AC+7'
DATA_2 = 'AB=AC+BC-14'

class Scene(MovingCameraScene):

    def construct(self):
        delay = 0

        self.wait(.5)

        graph = ProblemGraph()
        graph.add_node(REQUEST, MathTex(r"2P"), PROBLEM_REQUEST)
        graph.add_node(DATA_1, MathTex(r"\overline{BC} = \overline{AC} + 7"), PROBLEM_DATA)
        graph.add_node(DATA_2, MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14"), PROBLEM_DATA)
        graph.add_node('AC', MathTex(r"\overline{AC}"), PROBLEM_UNKNOWN)
        graph.add_node('BC', MathTex(r"\overline{BC}"), PROBLEM_UNKNOWN)
        graph.add_node('AB', MathTex(r"\overline{AB}"))

        graph.build_row(DATA_1, DATA_2)
        graph.build_row('AC', 'BC', hbuff=4)
        graph.build_row('AB')
        graph.build_row(REQUEST)

        graph.add_arrow('AC', REQUEST, to_shift=.3*LEFT)
        graph.add_arrow('AB', REQUEST)
        graph.add_arrow('BC', REQUEST, to_shift=.3*RIGHT)
        graph.add_arrow('AC', DATA_1)
        graph.add_arrow('AC', DATA_2, to_shift=.3*LEFT)
        graph.add_arrow('BC', DATA_1)
        graph.add_arrow('BC', DATA_2, to_shift=.3*RIGHT)
        graph.add_arrow('AB', DATA_2, start_shift=ORIGIN)
        graph.add_arrow('AC', 'AB', start_shift=.3*RIGHT, to_shift=.3*LEFT)
        graph.add_arrow('BC', 'AB', start_shift=.3*LEFT, to_shift=.3*RIGHT)

        self.add(graph.get_objects())

