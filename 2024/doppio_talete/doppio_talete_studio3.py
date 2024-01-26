import math

from manim import *

DELAY = 30


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

        a_label = MathTex("A").next_to(a_dot, LEFT, buff=.1)
        b_label = MathTex("B").next_to(b_dot, RIGHT, buff=.1)
        c_label = MathTex("C").next_to(c_dot, UP, buff=.1)

        def get_ab_line():
            return Line(a_dot.get_center(), b_dot.get_center(), z_index=-1)

        def get_bc_line():
            return Line(b_dot.get_center(), c_dot.get_center(), z_index=-1)

        ab_line = get_ab_line()
        bc_line = get_bc_line()
        ca_line = Line(c_coord, a_coord, z_index=-1)

        abc_dots = VGroup(a_dot, b_dot, c_dot)
        abc_labels = VGroup(a_label, b_label, c_label)
        abc_edges = VGroup(ab_line, bc_line, ca_line)

        self.add(abc_dots, abc_labels, abc_edges)

        def get_p_position():
            return (b_dot.get_center() - a_dot.get_center()) / 3 + a_dot.get_center()

        p_dot = Dot(get_p_position())
        p_label = MathTex("P").next_to(p_dot, DOWN, buff=.1)

        dato0 = MathTex(r"\overline{AP} = \dfrac{1}{3} \cdot \overline{AB}")
        dato1 = MathTex(r"\overline{CO} = \dfrac{1}{3} \cdot \overline{CP}")
        dato2 = MathTex(r"\overline{AC} = {{ 968 }}")
        dato3 = Tex(r"$\overline{CE}$ = ?")

        dati = VGroup(
            dato0, dato1, dato2, dato3
        ).arrange(DOWN).move_to(3.5 * RIGHT)

        self.add(p_dot, p_label, dato0)

        def get_cp_line():
            return Line(c_dot.get_center(), p_dot.get_center(), z_index=-1)

        cp_line = get_cp_line()
        self.add(cp_line)

        def get_o_position():
            return (p_dot.get_center() - c_dot.get_center()) / 3 + c_dot.get_center()

        o_dot = Dot(get_o_position())
        o_label = MathTex("O").next_to(o_dot, RIGHT, buff=.1).shift(.15*UP)
        self.add(o_dot, o_label, dato1)

        e_coord = line_intersection([a_dot.get_center(), c_dot.get_center()], [b_dot.get_center(), o_dot.get_center()])
        e_dot = Dot(e_coord)
        e_label = MathTex("E").next_to(e_dot, LEFT, buff=.1)

        def get_be_line():
            return Line(b_dot.get_center(), e_dot.get_center(), z_index=-1)

        be_line = get_be_line()

        self.add(be_line)
        self.add(e_dot, e_label)

        self.add(dato2)

        self.add(dato3)
        self.wait(1)

        # Ma stiamo divagando... andiamo alla soluzione.
        # Quando abbiamo a che fare con segmenti suddivisi in parti proporzionali, dovrebbe subito venirci in mente la
        # più probabile delle soluzioni: il teorema di Talete.
        # Tuttavia in questa figura non abbiamo rette parallele. Ma quello che non c'è lo si può sempre aggiungere.
        # Tracciamo la retta parallela ad EB passante per il punto P. E chiamiamo K l'intersezione di tale retta con il
        # lato AC.

        f_coord = (c_dot.get_center() - a_dot.get_center()) / 4 + a_dot.get_center()
        f_dot = Dot(f_coord)
        f_label = MathTex("F").next_to(f_dot, LEFT, buff=.1)
        pf_line = Line(p_dot.get_center(), f_dot.get_center(), z_index=-1)

        self.play(Create(pf_line))
        self.play(Create(f_dot), Write(f_label))
        self.cut_and_wait()

        # Ora abbiamo due rette parallele: non ci resta che trovare le due trasversali.

        self.play(pf_line.animate.set_color(RED), be_line.animate.set_color(RED))
        self.cut_and_wait()

        # Ma la scelta è immediata.
        # Consideriamo le rette AC e CP.

        self.play(
            ca_line.animate.set_color(YELLOW), cp_line.animate.set_color(YELLOW),
            ab_line.animate.set_color(DARK_GRAY), bc_line.animate.set_color(DARK_GRAY)
        )

        # Il segmento OP risulta essere il doppio del segmento CO. Quindi per il teorema
        # di Talete, il segmento EK è il doppio del segmento CE. Quindi se chiamiamo x la lunghezza del segmento CE, il
        # segmento EK è lungo 2x.

        self.play(Circumscribe(dato0))
        self.play(Circumscribe(dato0))
        self.cut_and_wait()

        pezzo = Line(c_dot.get_center(), o_dot.get_center(), color=YELLOW, z_index=-2)
        self.add(pezzo)
        self.play(Rotate(pezzo, angle=-PI, about_point=o_dot.get_center()))
        self.play(Rotate(pezzo, angle=-PI, about_point=pezzo.get_start()))
        self.cut_and_wait()

        pezzo = Line(c_dot.get_center(), e_dot.get_center(), color=YELLOW, z_index=-2)
        self.add(pezzo)
        self.play(Rotate(pezzo, angle=-PI, about_point=e_dot.get_center()))
        self.play(Rotate(pezzo, angle=-PI, about_point=pezzo.get_start()))
        self.cut_and_wait()

        x_ce = MathTex("x", color=BLUE).next_to(Line(c_dot.get_center(), e_dot.get_center()).get_center(), LEFT, buff=.1)
        x_ef = MathTex("2x", color=BLUE).next_to(Line(e_dot.get_center(), f_dot.get_center()).get_center(), LEFT, buff=.1)
        self.play(Write(x_ce))
        self.play(Write(x_ef))
        self.cut_and_wait()

        # Ma non ci basta: dobbiamo ancora legare in qualche modo il segmento AK al segmento CE. E per farlo utilizziamo
        # l'altra proporzionalità che conosciamo.
        # Quindi questa volta consideriamo la retta AB e AC.

        self.play(
            cp_line.animate.set_color(DARK_GRAY),
            ab_line.animate.set_color(YELLOW)
        )
        self.cut_and_wait()

        self.play(Circumscribe(dato1))
        self.play(Circumscribe(dato1))
        self.cut_and_wait()

        pezzo = Line(a_dot.get_center(), p_dot.get_center(), color=YELLOW, z_index=-2)
        self.add(pezzo)
        self.play(Rotate(pezzo, angle=-PI, about_point=p_dot.get_center()))
        self.play(Rotate(pezzo, angle=-PI, about_point=pezzo.get_start()))
        self.cut_and_wait()

        # Il segmento AP è metà del segmento BP, quindi per il
        # teorema di Talete il segmento AK è metà del segmento EK. Quindi se è EK è 2x, AK risulta essere uguale ad x.

        pezzo = Line(a_dot.get_center(), f_dot.get_center(), color=YELLOW, z_index=-2)
        self.add(pezzo)
        self.play(Rotate(pezzo, angle=-PI, about_point=f_dot.get_center()))
        self.play(Rotate(pezzo, angle=-PI, about_point=pezzo.get_start()))
        self.cut_and_wait()


        x_af = MathTex("x", color=BLUE).next_to(Line(a_dot.get_center(), f_dot.get_center()).get_center(), LEFT, buff=.1)
        self.play(Write(x_af))
        self.cut_and_wait()

        # Sommando le singole parti sappiamo che AK + EK + CE è uguale ad AC.

        self.play(
            ab_line.animate.set_color(DARK_GRAY),
            pf_line.animate.set_color(DARK_GRAY),
            be_line.animate.set_color(DARK_GRAY),
        )
        somma1 = MathTex(r"\overline{AF} {{ + }} \overline{EF} {{ + }} \overline{CE} {{ = }} \overline{AC}", color=YELLOW).to_edge(UP)
        self.play(Write(somma1))

        # Ovvero x + 2x + x è uguale ad 968,
        x1 = x_af.copy()
        x2 = x_ef.copy()
        x3 = x_ce.copy()
        sum = dato2[1].copy()
        self.play(x1.animate.move_to(somma1[0]), FadeOut(somma1[0]))
        self.play(x2.animate.move_to(somma1[2]), FadeOut(somma1[2]))
        self.play(x3.animate.move_to(somma1[4]), FadeOut(somma1[4]))
        self.play(sum.animate.move_to(somma1[6]), FadeOut(somma1[6]))
        self.cut_and_wait()

        # quindi x è uguale a 242.

        somma2 = MathTex("4x {{ = }} 968").move_to(somma1)
        somma2[0].set_color(BLUE)
        somma2[1].set_color(YELLOW)
        somma2[2].set_color(WHITE)
        self.play(
            ReplacementTransform(VGroup(x1, x2, x3, somma1[1], somma1[3], somma1[5]), somma2[0]),
            somma1[5].animate.move_to(somma2[1]),
            sum.animate.move_to(somma2[2])
        )
        self.add(somma2)
        self.remove(somma1[5], sum)
        somma3 = MathTex("x {{ = }} 242").move_to(somma2)
        somma3[0].set_color(BLUE)
        somma3[1].set_color(YELLOW)
        somma3[2].set_color(WHITE)
        self.play(ReplacementTransform(somma2, somma3))

        # E x è la misura di CE che stavamo cercando.
        somma4 = MathTex(r"\overline{CE} {{ = }} 242").move_to(somma3)
        somma4[0].set_color(BLUE)
        somma4[1].set_color(YELLOW)
        somma4[2].set_color(WHITE)
        self.play(TransformMatchingTex(somma3, somma4))

        self.wait(30)
