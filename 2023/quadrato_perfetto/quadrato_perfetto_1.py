from manim import *

from qui_matematica import util


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(1)

        numero_168 = MathTex(r"168").scale(4)
        self.play(Write(numero_168))
        self.wait(delay)
        self.next_section()

        quadrato_di_168 = MathTex(r"168^2 = 28224").scale(2)
        quadrato_di_168[0][3].set_color(GREEN)
        quadrato_di_168[0][5:].set_color(BLUE)
        self.play(numero_168.animate.move_to(quadrato_di_168[0][:3]).scale(.5))
        self.play(Write(quadrato_di_168[0][3:]))
        self.wait(delay)
        self.next_section()

        scomposizione_di_168 = MathTable(
            [[168, 2],
             [84, 2],
             [42, 2],
             [21, 3],
             [7, 7],
             [1, 0]])
        helper = util.TableHelper(scomposizione_di_168)
        for r in scomposizione_di_168.get_entries():
            r.scale(2)
        scomposizione_di_168.get_entries((1, 2)).set_color(RED)
        scomposizione_di_168.get_entries((2, 2)).set_color(RED)
        scomposizione_di_168.get_entries((3, 2)).set_color(RED)
        scomposizione_di_168.get_entries((4, 2)).set_color(ORANGE)
        scomposizione_di_168.get_entries((5, 2)).set_color(YELLOW)
        self.play(Unwrite(quadrato_di_168[0][3:]))
        self.wait(delay)
        self.next_section()

        self.play(numero_168.animate.move_to(scomposizione_di_168.get_entries((1, 1))))
        vertical_line = helper.get_vertical_line(1)
        self.play(Create(vertical_line))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposizione_di_168.get_entries((1, 2))))
        self.play(Write(scomposizione_di_168.get_entries((2, 1))))
        self.wait(delay)
        self.next_section()
        self.play(Write(scomposizione_di_168.get_entries((2, 2))))
        self.play(Write(scomposizione_di_168.get_entries((3, 1))))
        self.wait(delay)
        self.next_section()
        self.play(Write(scomposizione_di_168.get_entries((3, 2))))
        self.play(Write(scomposizione_di_168.get_entries((4, 1))))
        self.wait(delay)
        self.next_section()
        self.play(Write(scomposizione_di_168.get_entries((4, 2))))
        self.play(Write(scomposizione_di_168.get_entries((5, 1))))
        self.wait(delay)
        self.next_section()
        self.play(Write(scomposizione_di_168.get_entries((5, 2))))
        self.play(Write(scomposizione_di_168.get_entries((6, 1))))
        self.wait(delay)
        self.next_section()

        scomposto_di_168 = MathTex(r"168 = 2^3 \cdot 3 \cdot 7").scale(2)
        scomposto_di_168[0][4].set_color(RED)
        scomposto_di_168[0][5].set_color(GREEN)
        scomposto_di_168[0][7].set_color(ORANGE)
        scomposto_di_168[0][9].set_color(YELLOW)

        scomposto_del_quadrato_di_168 = \
            MathTex(r"{{ 168^2 &= (2^3 \cdot 3 \cdot 7)^2 = }}"
                    r"\\ &= (2^3)^2 \cdot (3)^2 \cdot (7)^2 = "
                    r"\\ {{ &= 2^6 \cdot 3^2 \cdot 7^2 }}").scale(2)
        scomposto_del_quadrato_di_168[0][3].set_color(GREEN)
        scomposto_del_quadrato_di_168[0][6].set_color(RED)
        scomposto_del_quadrato_di_168[0][7].set_color(GREEN)
        scomposto_del_quadrato_di_168[0][9].set_color(ORANGE)
        scomposto_del_quadrato_di_168[0][11].set_color(YELLOW)
        scomposto_del_quadrato_di_168[0][13].set_color(GREEN)
        scomposto_del_quadrato_di_168[1][2].set_color(RED)
        scomposto_del_quadrato_di_168[1][3].set_color(GREEN)
        scomposto_del_quadrato_di_168[1][5].set_color(GREEN)
        scomposto_del_quadrato_di_168[1][8].set_color(ORANGE)
        scomposto_del_quadrato_di_168[1][10].set_color(GREEN)
        scomposto_del_quadrato_di_168[1][13].set_color(YELLOW)
        scomposto_del_quadrato_di_168[1][15].set_color(GREEN)
        scomposto_del_quadrato_di_168[2][1].set_color(RED)
        scomposto_del_quadrato_di_168[2][2].set_color(GREEN)
        scomposto_del_quadrato_di_168[2][4].set_color(ORANGE)
        scomposto_del_quadrato_di_168[2][5].set_color(GREEN)
        scomposto_del_quadrato_di_168[2][7].set_color(YELLOW)
        scomposto_del_quadrato_di_168[2][8].set_color(GREEN)

        VGroup(scomposto_di_168, scomposto_del_quadrato_di_168).arrange(DOWN, buff=1)

        self.play(numero_168.animate.move_to(scomposto_di_168[0][:3]),
                  scomposizione_di_168.get_entries((1, 2)).animate.move_to(scomposto_di_168[0][4]),
                  scomposizione_di_168.get_entries((2, 2)).animate.move_to(scomposto_di_168[0][4]),
                  scomposizione_di_168.get_entries((3, 2)).animate.move_to(scomposto_di_168[0][4]),
                  scomposizione_di_168.get_entries((4, 2)).animate.move_to(scomposto_di_168[0][7]),
                  scomposizione_di_168.get_entries((5, 2)).animate.move_to(scomposto_di_168[0][9]),
                  Uncreate(vertical_line),
                  FadeOut(scomposizione_di_168.get_entries((2, 1))),
                  FadeOut(scomposizione_di_168.get_entries((3, 1))),
                  FadeOut(scomposizione_di_168.get_entries((4, 1))),
                  FadeOut(scomposizione_di_168.get_entries((5, 1))),
                  FadeOut(scomposizione_di_168.get_entries((6, 1))),
                  FadeIn(scomposto_di_168))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_168[0]))
        self.wait(delay)
        self.next_section()

        prop_potenza = MathTex(r"(a \cdot b)^n = a^n \cdot b^n").scale(2).to_edge(DOWN)
        riquadro = SurroundingRectangle(prop_potenza, color=YELLOW, buff=.3, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(prop_potenza))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_168[1]))
        self.play(FadeOut(riquadro), FadeOut(prop_potenza))
        self.wait(delay)
        self.next_section()

        prop_potenza = MathTex(r"(a^m)^n = a^{mn}").scale(2).to_edge(UP)
        riquadro = SurroundingRectangle(prop_potenza, color=YELLOW, buff=.3, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(prop_potenza))
        self.wait(delay)
        self.next_section()

        self.play(Write(scomposto_del_quadrato_di_168[2]))
        self.play(FadeOut(riquadro), FadeOut(prop_potenza))
        self.wait(delay)
        self.next_section()

        risultato = MathTex(r"168^2 = 2^6 \cdot 3^2 \cdot 7^2").scale(2)
        risultato[0][3].set_color(GREEN)
        risultato[0][5].set_color(RED)
        risultato[0][6].set_color(GREEN)
        risultato[0][8].set_color(ORANGE)
        risultato[0][9].set_color(GREEN)
        risultato[0][11].set_color(YELLOW)
        risultato[0][12].set_color(GREEN)
        riquadro = SurroundingRectangle(risultato, color=YELLOW, buff=.5, fill_opacity=1, fill_color=BLACK)
        self.play(Create(riquadro), Write(risultato))

        self.wait(30)

