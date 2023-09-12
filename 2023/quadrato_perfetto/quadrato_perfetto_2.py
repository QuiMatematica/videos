from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        scomposto_di_n = MathTex(r"n = p_1^{a_1} \cdot p_2^{a_2} \cdot ... \cdot p_t^{a_t}").scale(1.5)
        scomposto_di_n[0][2].set_color(RED)
        scomposto_di_n[0][3:5].set_color(GREEN)
        scomposto_di_n[0][5].set_color(RED)
        scomposto_di_n[0][7].set_color(ORANGE)
        scomposto_di_n[0][8:10].set_color(GREEN)
        scomposto_di_n[0][10].set_color(ORANGE)
        scomposto_di_n[0][16].set_color(YELLOW)
        scomposto_di_n[0][17:19].set_color(GREEN)
        scomposto_di_n[0][19].set_color(YELLOW)

        scomposto_di_168 = MathTex(r"168 = 2^3 \cdot 3 \cdot 7").scale(2)
        scomposto_di_168[0][4].set_color(RED)
        scomposto_di_168[0][5].set_color(GREEN)
        scomposto_di_168[0][7].set_color(ORANGE)
        scomposto_di_168[0][9].set_color(YELLOW)

        scomposto_del_quadrato_di_n = \
            MathTex(r"{{ n^2 &= (p_1^{a_1} \cdot p_2^{a_2} \cdot ... \cdot p_t^{a_t})^2 = }}"
                    r"\\ &= (p_1^{a_1})^2 \cdot (p_2^{a_2})^2 \cdot ... \cdot (p_t^{a_t})^2 = "
                    r"\\ {{ &= p_1^{2a_1} \cdot p_2^{2a_2} \cdot ... \cdot p_t^{2a_t} }}").scale(1.5)
        scomposto_del_quadrato_di_n[0][1].set_color(GREEN)
        scomposto_del_quadrato_di_n[0][4].set_color(RED)
        scomposto_del_quadrato_di_n[0][5:7].set_color(GREEN)
        scomposto_del_quadrato_di_n[0][7].set_color(RED)
        scomposto_del_quadrato_di_n[0][9].set_color(ORANGE)
        scomposto_del_quadrato_di_n[0][10:12].set_color(GREEN)
        scomposto_del_quadrato_di_n[0][12].set_color(ORANGE)
        scomposto_del_quadrato_di_n[0][18].set_color(YELLOW)
        scomposto_del_quadrato_di_n[0][19:21].set_color(GREEN)
        scomposto_del_quadrato_di_n[0][21].set_color(YELLOW)

        scomposto_del_quadrato_di_n[1][2].set_color(RED)
        scomposto_del_quadrato_di_n[1][3:5].set_color(GREEN)
        scomposto_del_quadrato_di_n[1][5].set_color(RED)
        scomposto_del_quadrato_di_n[1][7].set_color(GREEN)
        scomposto_del_quadrato_di_n[1][10].set_color(ORANGE)
        scomposto_del_quadrato_di_n[1][11:13].set_color(GREEN)
        scomposto_del_quadrato_di_n[1][13].set_color(ORANGE)
        scomposto_del_quadrato_di_n[1][15].set_color(GREEN)
        scomposto_del_quadrato_di_n[1][22].set_color(YELLOW)
        scomposto_del_quadrato_di_n[1][23:25].set_color(GREEN)
        scomposto_del_quadrato_di_n[1][25].set_color(YELLOW)
        scomposto_del_quadrato_di_n[1][27].set_color(GREEN)

        scomposto_del_quadrato_di_n[2][1].set_color(RED)
        scomposto_del_quadrato_di_n[2][2:5].set_color(GREEN)
        scomposto_del_quadrato_di_n[2][5].set_color(RED)
        scomposto_del_quadrato_di_n[2][7].set_color(ORANGE)
        scomposto_del_quadrato_di_n[2][8:11].set_color(GREEN)
        scomposto_del_quadrato_di_n[2][11].set_color(ORANGE)
        scomposto_del_quadrato_di_n[2][17].set_color(YELLOW)
        scomposto_del_quadrato_di_n[2][18:21].set_color(GREEN)
        scomposto_del_quadrato_di_n[2][21].set_color(YELLOW)

        VGroup(scomposto_di_n, scomposto_del_quadrato_di_n).arrange(DOWN, buff=1)

        self.play(Write(scomposto_di_n[0][0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_di_n[0][1:3]),
                  Write(scomposto_di_n[0][5:8]),
                  Write(scomposto_di_n[0][10:17]),
                  Write(scomposto_di_n[0][19]))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_di_n[0][3:5]),
                  Write(scomposto_di_n[0][8:10]),
                  Write(scomposto_di_n[0][17:19]))
        self.wait(delay)
        self.next_section()

        # self.add(index_labels(scomposto_di_n[0]))

        scomposto_di_168.next_to(scomposto_di_n, DOWN)
        self.play(Write(scomposto_di_168))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(scomposto_di_168[0][0:3]), Circumscribe(scomposto_di_n[0][0]))
        self.play(Circumscribe(scomposto_di_168[0][0:3]), Circumscribe(scomposto_di_n[0][0]))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(scomposto_di_168[0][4:6]), Circumscribe(scomposto_di_n[0][2:6]))
        self.play(Circumscribe(scomposto_di_168[0][4:6]), Circumscribe(scomposto_di_n[0][2:6]))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(scomposto_di_168[0][5]), Circumscribe(scomposto_di_n[0][3:5]))
        self.play(Circumscribe(scomposto_di_168[0][5]), Circumscribe(scomposto_di_n[0][3:5]))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(scomposto_di_168[0][7]), Circumscribe(scomposto_di_n[0][7:11]))
        self.play(Circumscribe(scomposto_di_168[0][7]), Circumscribe(scomposto_di_n[0][7:11]))
        self.wait(delay)
        self.next_section()

        self.play(Circumscribe(scomposto_di_168[0][9]), Circumscribe(scomposto_di_n[0][16:20]))
        self.play(Circumscribe(scomposto_di_168[0][9]), Circumscribe(scomposto_di_n[0][16:20]))
        self.wait(delay)
        self.next_section()

        self.play(Unwrite(scomposto_di_168))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_n[0]))
        self.wait(delay)
        self.next_section()

        prop_potenza = MathTex(r"(a \cdot b)^n = a^n \cdot b^n").scale(2).to_edge(DOWN)
        riquadro = SurroundingRectangle(prop_potenza, color=YELLOW, buff=.3, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(prop_potenza))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_n[1]))
        self.play(FadeOut(riquadro), FadeOut(prop_potenza))
        self.wait(delay)
        self.next_section()

        prop_potenza = MathTex(r"(a^m)^n = a^{mn}").scale(2).to_edge(UP)
        riquadro = SurroundingRectangle(prop_potenza, color=YELLOW, buff=.3, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(prop_potenza))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_n[2]))
        self.play(FadeOut(riquadro), FadeOut(prop_potenza))
        self.wait(delay)
        self.next_section()

        risultato = MathTex(r"n^2 = p_1^{2a_1} \cdot p_2^{2a_2} \cdot ... \cdot p_t^{2a_t}").scale(2)
        risultato[0][1].set_color(GREEN)
        risultato[0][3].set_color(RED)
        risultato[0][4:7].set_color(GREEN)
        risultato[0][7].set_color(RED)
        risultato[0][9].set_color(ORANGE)
        risultato[0][10:13].set_color(GREEN)
        risultato[0][13].set_color(ORANGE)
        risultato[0][19].set_color(YELLOW)
        risultato[0][20:23].set_color(GREEN)
        risultato[0][23].set_color(YELLOW)

        riquadro = SurroundingRectangle(risultato, color=YELLOW, buff=.5, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(risultato))

        self.wait(30)

