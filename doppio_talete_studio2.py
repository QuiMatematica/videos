import math

from manim import *

DELAY = 1


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        a_coord = [-6, -2, 0]
        b_coord = [-1, -1, 0]
        c_coord = [-5, 2, 0]

        a_dot = Dot(a_coord)
        b_dot = Dot(b_coord)
        c_dot = Dot(c_coord)

        a_label = MathTex("A").next_to(a_dot, LEFT)
        b_label = MathTex("B").next_to(b_dot, RIGHT)
        c_label = MathTex("C").next_to(c_dot, UP)

        def get_ab_line():
            return Line(a_dot.get_center(), b_dot.get_center())

        def get_bc_line():
            return Line(b_dot.get_center(), c_dot.get_center())

        ab_line = get_ab_line()
        bc_line = get_bc_line()
        ca_line = Line(c_coord, a_coord)

        abc_dots = VGroup(a_dot, b_dot, c_dot)
        abc_labels = VGroup(a_label, b_label, c_label)
        abc_edges = VGroup(ab_line, bc_line, ca_line)

        self.add(abc_dots, abc_labels, abc_edges)

        def get_p_position():
            return (b_dot.get_center() - a_dot.get_center()) / 3 + a_dot.get_center()

        p_dot = Dot(get_p_position())
        p_label = MathTex("P").next_to(p_dot, DOWN)

        dato0 = MathTex(r"\overline{AP} = \dfrac{1}{3} \cdot \overline{AB}")
        dato1 = MathTex(r"\overline{CO} = \dfrac{1}{3} \cdot \overline{CP}")
        dato2 = MathTex(r"\overline{AC} = 968")
        dato3 = Tex(r"$\overline{CE}$ = ?")

        dati = VGroup(
            dato0, dato1, dato2, dato3
        ).arrange(DOWN).move_to(3.5 * RIGHT)

        self.add(p_dot, p_label, dato0)

        def get_cp_line():
            return Line(c_dot.get_center(), p_dot.get_center())

        cp_line = get_cp_line()
        self.add(cp_line)

        def get_o_position():
            return (p_dot.get_center() - c_dot.get_center()) / 3 + c_dot.get_center()

        o_dot = Dot(get_o_position())
        o_label = MathTex("O").next_to(o_dot, RIGHT)
        self.add(o_dot, o_label, dato1)

        e_coord = line_intersection([a_dot.get_center(), c_dot.get_center()], [b_dot.get_center(), o_dot.get_center()])
        e_dot = Dot(e_coord)
        e_label = MathTex("E").next_to(e_dot, UL)

        def get_be_line():
            return Line(b_dot.get_center(), e_dot.get_center())

        be_line = get_be_line()

        self.add(be_line)
        self.add(e_dot, e_label)

        self.add(dato2)

        self.add(dato3)
        self.wait(1)

        # Seconda osservazione: siamo partiti da un triangolo ABC qualunque, conosciamo solo la misura di un lato e ci
        # viene chiesta la misura di una parte di questo lato. Curioso: sembra quindi che la soluzione del problema sia
        # indipendente dalla scelta del triangolo. E un po' di grafica computerizzata ci conferma che è proprio così.

        # path = Circle(radius=1, arc_center=b_dot.get_center() + RIGHT).rotate(PI)
        path = Ellipse(width=2.0, height=4.0).move_to(b_dot.get_center() + RIGHT).rotate(PI)

        b_label.add_updater(
            lambda l: l.next_to(b_dot, RIGHT)
        )
        ab_line.add_updater(
            lambda l: l.become(get_ab_line())
        )
        bc_line.add_updater(
            lambda l: l.become(get_bc_line())
        )
        p_dot.add_updater(lambda p: p.move_to(get_p_position()))
        o_dot.add_updater(lambda p: p.move_to(get_o_position()))
        p_label.add_updater(lambda p: p.next_to(p_dot, DOWN))
        o_label.add_updater(lambda p: p.next_to(o_dot, RIGHT))
        cp_line.add_updater(lambda l: l.become(get_cp_line()))
        be_line.add_updater(lambda l: l.become(get_be_line()))

        self.play(MoveAlongPath(b_dot, path, run_time=4))
        self.cut_and_wait()

        b_label.clear_updaters()
        ab_line.clear_updaters()
        bc_line.clear_updaters()
        p_dot.clear_updaters()
        o_dot.clear_updaters()
        p_label.clear_updaters()
        o_label.clear_updaters()
        cp_line.clear_updaters()
        be_line.clear_updaters()

        # Ma stiamo divagando... andiamo alla soluzione.
        # Quando abbiamo a che fare con segmenti suddivisi in parti proporzionali, dovrebbe subito venirci in mente la
        # più probabile delle soluzioni: il teorema di Talete.
        # Tuttavia in questa figura non abbiamo rette parallele. Ma quello che non c'è lo si può sempre aggiungere.
        # Tracciamo la retta parallela ad EB passante per il punto P. E chiamiamo K l'intersezione di tale retta con il
        # lato AC. Ora abbiamo due rette parallele: non ci resta che trovare le due trasversali.
        # Ma la scelta è immediata.
        # Consideriamo le rette AC e CP. Il segmento OP risulta essere il doppio del segmento CO. Quindi per il teorema
        # di Talete, il segmento EK è il doppio del segmento CE. Quindi se chiamiamo x la lunghezza del segmento CE, il
        # segmento EK è lungo 2x.
        # Ma non ci basta: dobbiamo ancora legare in qualche modo il segmento AK al segmento CE. E per farlo utilizziamo
        # l'altra proporzionalità che conosciamo.
        # Quindi questa volta consideriamo la retta AB e AC. Il segmento AP è metà del segmento BP, quindi per il
        # teorema di Talete il segmento AK è metà del segmento EK. Quindi se è EK è 2x, AK risulta essere uguale ad x.
        # Sommando le singole parti sappiamo che AK + EK + CE è uguale ad AC. Ovvero x + 2x + x è uguale ad AC, quindi
        # x, che poi CE, è un quarto di AC.
        # Quindi il segmento CE è lungo 968 diviso 4 che fa 242.

        self.wait(30)
