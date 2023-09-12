from qui_matematica.qproblem import *

REQUEST = '2P'
DATA_1 = 'BC=AC+7'
DATA_2 = 'AB=AC+BC-14'
PITAGORA = 'Pitagora'

class Scene(MovingCameraScene):

    def construct(self):
        delay = 0

        self.wait(.5)

        graph = ProblemGraph()
        graph.add_node(REQUEST, MathTex(r"2P"), PROBLEM_REQUEST)
        graph.add_node(DATA_1, MathTex(r"\overline{BC} = \overline{AC} + 7"), PROBLEM_DATA)
        graph.add_node(DATA_2, MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14"), PROBLEM_DATA)
        graph.add_node(PITAGORA, MathTex(r"\overline{AB}^2 = \overline{AC}^2 + \overline{BC}^2"), PROBLEM_DATA)
        graph.add_node('AC', MathTex(r"\overline{AC}"), PROBLEM_UNKNOWN)
        graph.add_node('BC', MathTex(r"\overline{BC}"))
        graph.add_node('AB', MathTex(r"\overline{AB}"))

        graph.build_row(DATA_1, PITAGORA, DATA_2)
        graph.build_row('AC')
        graph.build_row('BC', 'AB', hbuff=4)
        graph.build_row(REQUEST)

        graph.scale(.8)

        graph.add_arrow('AC', REQUEST)
        graph.add_arrow('AB', REQUEST, start_shift=.3*LEFT, to_shift=.3*RIGHT)
        graph.add_arrow('BC', REQUEST, start_shift=.3*RIGHT, to_shift=.3*LEFT)
        graph.add_arrow('AC', 'BC', start_shift=.3*LEFT, to_shift=.3*RIGHT)
        graph.add_arrow('AC', 'AB', start_shift=.3*RIGHT, to_shift=.3*LEFT)
        graph.add_arrow(DATA_1, 'BC')
        graph.add_arrow(DATA_2, 'AB')
        graph.add_arrow('AC', PITAGORA)
        graph.add_arrow('BC', PITAGORA, to_shift=.3*LEFT)
        graph.add_arrow('AB', PITAGORA, to_shift=.3*RIGHT)
        graph.add_arrow('BC', 'AB')

        self.add(graph.get_objects())

