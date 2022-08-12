from manim import *

from object import *
from util import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        coin_shift = 1.3

        faces = [HEAD, CROSS, HEAD, CROSS, CROSS, CROSS]
        points = [
            [-1.5, coin_shift + 1.4, 0],
            [1.1, coin_shift + 1.2, 0],
            [-3.7, coin_shift - .15, 0],
            [3.7, coin_shift + .15, 0],
            [1.5, coin_shift - 1.4, 0],
            [-1.1, coin_shift - 1.2, 0]
        ]
        assert len(faces) == len(points), 'Faces <> points'

        coins = [Coin(face=faces[_i]).scale(.6).move_to(points[_i]) for _i in range(len(points))]

        self.play(*[SpinInFromNothing(x, angle=2 * PI, run_time=1) for x in coins])
        self.wait(delay)
        self.next_section()

        domanda = MathTex(r"{{ p(\text{2 teste}) = }} \,\,?").move_to(2*DOWN)
        domanda[0][2:8].set_color(YELLOW)
        self.play(Write(domanda))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(domanda))
        self.play(*[FadeOut(x) for x in coins[2:]])
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(coins[1]))
        self.play(coins[0].animate.move_to(2.5*UP))
        self.wait(delay)
        self.next_section()

        uno0 = MathTex(r"\text{testa} \lor \text{croce} = \text{vero}").next_to(coins[0], 2*DOWN)
        uno0[0][0:5].set_color(RED)
        uno0[0][6:11].set_color(GREEN)
        uno0[0][12:16].set_color(YELLOW)
        self.play(Write(uno0))
        self.wait(delay)
        self.next_section()

        uno1 = MathTex(r"p(\text{testa}) + p(\text{croce}) = 1").next_to(uno0, 2*DOWN)
        uno1[0][2:7].set_color(RED)
        uno1[0][11:16].set_color(GREEN)
        uno1[0][18].set_color(YELLOW)
        self.play(Write(uno1))
        self.wait(delay)
        self.next_section()

        uno2 = MathTex(r"t + c = 1").next_to(uno1, 2*DOWN)
        uno2[0][0].set_color(RED)
        uno2[0][2].set_color(GREEN)
        uno2[0][4].set_color(YELLOW)
        self.play(Write(uno2))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(uno0), FadeOut(uno1))
        self.play(coins[0].animate.scale(.3).move_to(3.5*UP + 2.15*LEFT))
        self.play(uno2.animate.move_to(3.5*UP + 1*RIGHT))
        line = Line(3*LEFT, 3*RIGHT).move_to(3*UP)
        self.play(Create(line))
        self.wait(delay)
        self.next_section()

        two_coins = [Coin(face=faces[_i]).scale(.6) for _i in range(2)]
        two_coins[0].move_to(1.5*UP+LEFT)
        two_coins[1].move_to(1.5*UP+RIGHT)
        self.play(*[SpinInFromNothing(x, angle=2 * PI, run_time=1) for x in two_coins])
        self.wait(delay)
        self.next_section()

        two0 = MathTex(r"(t + c)^2 = 1^2")
        two0[0][1].set_color(RED)
        two0[0][3].set_color(GREEN)
        two0[0][7].set_color(YELLOW)
        self.play(Write(two0))
        self.wait(delay)
        self.next_section()

        two1 = MathTex(r"(t + c)(t+c) = 1^2").next_to(two0, DOWN)
        set_color(two1, 1, 6, color=RED)
        set_color(two1, 3, 8, color=GREEN)
        set_color(two1, 11, color=YELLOW)
        fftf = FromFormulaToFormula(two0, two1)
        self.play(fftf.copy_and_move(slice(0, 5), slice(0, 5)))
        self.play(fftf.copy_and_move(slice(0, 5), slice(5, 10)))
        self.play(fftf.copy_and_move(slice(6, 9), slice(10, 13)))
        self.add(two1)
        self.remove(*fftf.get_temp_pieces())
        self.wait(delay)
        self.next_section()

        two2 = MathTex(r"tt + tc + ct + cc = 1").next_to(two1, DOWN)
        set_color(two2, slice(0, 2), 3, 7, color=RED)
        set_color(two2, 4, 6, slice(9, 11), color=GREEN)
        set_color(two2, 12, color=YELLOW)
        fftf = FromFormulaToFormula(two1, two2)
        self.play(fftf.copy_and_move(1, 0))
        self.play(fftf.copy_and_move(6, 1))
        self.play(fftf.write(2))
        self.play(fftf.copy_and_move(1, 3))
        self.play(fftf.copy_and_move(8, 4))
        self.play(fftf.write(5))
        self.play(fftf.copy_and_move(3, 6))
        self.play(fftf.copy_and_move(6, 7))
        self.play(fftf.write(8))
        self.play(fftf.copy_and_move(3, 9))
        self.play(fftf.copy_and_move(8, 10))
        self.play(fftf.copy_and_move(slice(10, 12), slice(11, 13)))
        self.add(two2)
        self.remove(*fftf.get_temp_pieces())
        self.wait(delay)
        self.next_section()

        surr = SurroundingRectangle(two2[0][0:2])
        self.play(Create(surr))
        c0 = Coin(face=HEAD).scale(.2).next_to(surr, DOWN).shift(.3*LEFT)
        c1 = Coin(face=HEAD).scale(.2).next_to(surr, DOWN).shift(.3*RIGHT)
        self.play(SpinInFromNothing(c0), SpinInFromNothing(c1))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(surr), FadeOut(c0), FadeOut(c1))
        surr = SurroundingRectangle(two2[0][3:5])
        self.play(Create(surr))
        c0 = Coin(face=HEAD).scale(.2).next_to(surr, DOWN).shift(.3*LEFT)
        c1 = Coin(face=CROSS).scale(.2).next_to(surr, DOWN).shift(.3*RIGHT)
        self.play(SpinInFromNothing(c0), SpinInFromNothing(c1))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(surr), FadeOut(c0), FadeOut(c1))
        surr = SurroundingRectangle(two2[0][6:8])
        self.play(Create(surr))
        c0 = Coin(face=CROSS).scale(.2).next_to(surr, DOWN).shift(.3*LEFT)
        c1 = Coin(face=HEAD).scale(.2).next_to(surr, DOWN).shift(.3*RIGHT)
        self.play(SpinInFromNothing(c0), SpinInFromNothing(c1))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(surr), FadeOut(c0), FadeOut(c1))
        surr = SurroundingRectangle(two2[0][9:11])
        self.play(Create(surr))
        c0 = Coin(face=CROSS).scale(.2).next_to(surr, DOWN).shift(.3*LEFT)
        c1 = Coin(face=CROSS).scale(.2).next_to(surr, DOWN).shift(.3*RIGHT)
        self.play(SpinInFromNothing(c0), SpinInFromNothing(c1))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(surr), FadeOut(c0), FadeOut(c1))
        brace = Brace(two2[0][0:11])
        self.play(Write(brace))
        under_brace = MathTex(r"\text{casi totali} = 4").next_to(brace, DOWN)
        self.play(Write(under_brace))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(brace), FadeOut(under_brace))
        two3 = MathTex(r"{{ t^2 }} + 2 {{ t }} c {{ + }} c^2 {{ = 1 }}").next_to(two2, DOWN)
        two3[0][0].set_color(RED)
        two3[2].set_color(RED)
        two3[3].set_color(GREEN)
        two3[5][0].set_color(GREEN)
        two3[6][1].set_color(YELLOW)
        self.play(Write(two3))
        self.wait(delay)
        self.next_section()

        two3bis = MathTex(r"1 {{ t^2 }} + 2 {{ t }} ^1 {{ c }} ^1 + 1 {{ c^2 }} = 1").next_to(two2, DOWN)
        two3bis[1][0].set_color(RED)
        two3bis[3].set_color(RED)
        two3bis[5].set_color(GREEN)
        two3bis[7][0].set_color(GREEN)
        two3bis[8][1].set_color(YELLOW)
        self.play(TransformMatchingTex(two3, two3bis))
        self.wait(delay)
        self.next_section()

        two3ter = MathTex(r"1 t^2 + 2 t^1 c^1 + 1 c^2 = 1").move_to(two3bis)

        spiegone = VGroup(
            MathTex(r"\text{evento: } 2 \,\, teste"),
            MathTex(r"\text{\# casi favorevoli: } 1")
        ).arrange(DOWN).next_to(two3ter[0][0:3], 1.5*DOWN)
        spiegone[0][0][:7].set_color(YELLOW)
        spiegone[0][0][8:].set_color(RED)
        spiegone[1][0][:16].set_color(YELLOW)
        surr = SurroundingRectangle(two3ter[0][0:3])
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(surr), Create(back))
        self.play(Write(spiegone[0][0][:7]))
        esponente = two3ter[0][2].copy()
        esponente.target = spiegone[0][0][7]
        self.play(MoveToTarget(esponente))
        lettera = two3ter[0][1].copy()
        lettera.target = spiegone[0][0][8]
        self.play(MoveToTarget(lettera))
        self.play(Write(spiegone[0][0][9:]))
        self.play(Write(spiegone[1][0][:16]))
        coefficiente = two3ter[0][0].copy()
        coefficiente.target = spiegone[1][0][16]
        self.play(MoveToTarget(coefficiente))
        self.wait(delay)
        self.next_section()
        self.add(spiegone)
        self.play(FadeOut(surr), FadeOut(back), FadeOut(spiegone), FadeOut(esponente), FadeOut(lettera),
                  FadeOut(coefficiente))

        spiegone = VGroup(
            MathTex(r"\text{evento: } 1 \,\, testa \,\land\, 1 \,\, croce"),
            MathTex(r"\text{\# casi favorevoli: } 2")
        ).arrange(DOWN).next_to(two3ter[0][4:9], 1.5*DOWN)
        spiegone[0][0][:7].set_color(YELLOW)
        spiegone[0][0][8:13].set_color(RED)
        spiegone[0][0][15:].set_color(GREEN)
        spiegone[1][0][:16].set_color(YELLOW)
        surr = SurroundingRectangle(two3ter[0][4:9])
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(surr), Create(back))
        self.play(Write(spiegone[0][0][:7]))
        esponente_t = two3ter[0][6].copy()
        esponente_t.target = spiegone[0][0][7]
        self.play(MoveToTarget(esponente_t))
        lettera_t = two3ter[0][5].copy()
        lettera_t.target = spiegone[0][0][8]
        self.play(MoveToTarget(lettera_t))
        self.play(Write(spiegone[0][0][9:14]))
        esponente_c = two3ter[0][8].copy()
        esponente_c.target = spiegone[0][0][14]
        self.play(MoveToTarget(esponente_c))
        lettera_c = two3ter[0][7].copy()
        lettera_c.target = spiegone[0][0][15]
        self.play(MoveToTarget(lettera_c))
        self.play(Write(spiegone[0][0][16:]))
        self.play(Write(spiegone[1][0][:16]))
        coefficiente = two3ter[0][4].copy()
        coefficiente.target = spiegone[1][0][16]
        self.play(MoveToTarget(coefficiente))
        self.wait(delay)
        self.next_section()
        self.add(spiegone)
        self.play(FadeOut(surr), FadeOut(back), FadeOut(spiegone), FadeOut(esponente_t), FadeOut(lettera_t),
                  FadeOut(esponente_c), FadeOut(lettera_c), FadeOut(coefficiente))

        spiegone = VGroup(
            MathTex(r"\text{evento: } 2 \,\, croci"),
            MathTex(r"\text{\# casi favorevoli: } 1")
        ).arrange(DOWN).next_to(two3ter[0][10:13], 1.5*DOWN)
        spiegone[0][0][:7].set_color(YELLOW)
        spiegone[0][0][8:].set_color(GREEN)
        spiegone[1][0][:16].set_color(YELLOW)
        surr = SurroundingRectangle(two3ter[0][10:13])
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(surr), Create(back))
        self.play(Write(spiegone[0][0][:7]))
        esponente = two3ter[0][12].copy()
        esponente.target = spiegone[0][0][7]
        self.play(MoveToTarget(esponente))
        lettera = two3ter[0][11].copy()
        lettera.target = spiegone[0][0][8]
        self.play(MoveToTarget(lettera))
        self.play(Write(spiegone[0][0][9:]))
        self.play(Write(spiegone[1][0][:16]))
        coefficiente = two3ter[0][10].copy()
        coefficiente.target = spiegone[1][0][16]
        self.play(MoveToTarget(coefficiente))
        self.wait(delay)
        self.next_section()
        self.add(spiegone)
        self.play(FadeOut(surr), FadeOut(back), FadeOut(spiegone), FadeOut(esponente), FadeOut(lettera),
                  FadeOut(coefficiente))

        spiegone = MathTex(r"\text{\# casi totali: } 1 + 2 + 1 = 4").next_to(two3ter, 1.5*DOWN)
        spiegone[0][:12].set_color(YELLOW)
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(back))
        self.play(Write(spiegone[0][:12]))
        coefficiente_1 = two3ter[0][0].copy()
        coefficiente_1.target = spiegone[0][12]
        self.play(MoveToTarget(coefficiente_1))
        self.play(Write(spiegone[0][13]))
        coefficiente_2 = two3ter[0][4].copy()
        coefficiente_2.target = spiegone[0][14]
        self.play(MoveToTarget(coefficiente_2))
        self.play(Write(spiegone[0][15]))
        coefficiente_3 = two3ter[0][10].copy()
        coefficiente_3.target = spiegone[0][16]
        self.play(MoveToTarget(coefficiente_3))
        self.play(Write(spiegone[0][17:]))
        self.wait(delay)
        self.next_section()
        self.add(spiegone)
        self.play(FadeOut(back), FadeOut(spiegone), FadeOut(coefficiente_1), FadeOut(coefficiente_2),
                  FadeOut(coefficiente_3))

        spiegone = MathTex(r"p(t \land t) = \dfrac{1}{4} \quad p(t \land c) = \dfrac{2}{4} \quad p(c \land c) = "
                           r"\dfrac{1}{4}").next_to(two3ter, 1.5*DOWN)
        spiegone[0][2].set_color(RED)
        spiegone[0][4].set_color(RED)
        spiegone[0][12].set_color(RED)
        spiegone[0][14].set_color(GREEN)
        spiegone[0][22].set_color(GREEN)
        spiegone[0][24].set_color(GREEN)
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(back))
        fftf = FromFormulaToFormula(two3ter, spiegone)

        self.play(fftf.write(slice(0, 2)))
        self.play(fftf.copy_and_move(slice(1, 2), slice(2, 3)),
                  fftf.write(slice(3, 4)),
                  fftf.copy_and_move(slice(1, 2), slice(4, 5)))
        self.play(fftf.write(slice(5, 7)))

        self.play(fftf.copy_and_move(slice(1), slice(7, 8)))
        self.play(fftf.write(slice(8, 10)))

        self.play(fftf.write(slice(10, 12)))
        self.play(fftf.copy_and_move(slice(5, 6), slice(12, 13)),
                  fftf.write(slice(13, 14)),
                  fftf.copy_and_move(slice(7, 8), slice(14, 15)))
        self.play(fftf.write(slice(15, 17)))

        self.play(fftf.copy_and_move(slice(4, 5), slice(17, 18)))
        self.play(fftf.write(slice(18, 20)))

        self.play(fftf.write(slice(20, 22)))
        self.play(fftf.copy_and_move(slice(11, 12), slice(22, 23)),
                  fftf.write(slice(23, 24)),
                  fftf.copy_and_move(slice(11, 12), slice(24, 25)))
        self.play(fftf.write(slice(25, 27)))

        self.play(fftf.copy_and_move(slice(10, 11), slice(27, 28)))
        self.play(fftf.write(slice(28, 30)))
        self.wait(delay)
        self.next_section()
        self.add(spiegone)
        self.remove(*fftf.get_temp_pieces())
        self.play(FadeOut(back), FadeOut(spiegone))

        self.play(FadeOut(two0), FadeOut(two1), FadeOut(two2), FadeOut(two3bis))
        self.play(
            two_coins[0].animate.scale(.3).move_to(2.8 * UP + 2.5 * LEFT),
            two_coins[1].animate.scale(.3).move_to(2.8 * UP + 1.8 * LEFT),
            line.animate.shift(.7 * DOWN)
        )
        two3.move_to(2.8 * UP + RIGHT)
        self.play(Write(two3))

        three_coins = [Coin(face=faces[_i]).scale(.6) for _i in range(3)]
        three_coins[0].move_to(.8 * UP + 2 * LEFT)
        three_coins[1].move_to(.8 * UP)
        three_coins[2].move_to(.8 * UP + 2 * RIGHT)
        self.play(*[SpinInFromNothing(x, angle=2 * PI, run_time=1) for x in three_coins])
        self.wait(delay)
        self.next_section()

        three0 = MathTex(r"(t+c)^3 = 1^3").move_to(.7 * DOWN)
        three0[0][1].set_color(RED)
        three0[0][3].set_color(GREEN)
        three0[0][7].set_color(YELLOW)
        self.play(Write(three0))
        self.wait(delay)
        self.next_section()

        three1 = MathTex(r"1 t^3 + 3 t^2 c^1 + 3 t^1 c^2 + 1 c^3 = 1").next_to(three0, 1.5 * DOWN)
        set_color(three1, 1, 5, 11, color=RED)
        set_color(three1, 7, 13, 17, color=GREEN)
        set_color(three1, 20, color=YELLOW)
        self.play(Write(three1))
        self.wait(delay)
        self.next_section()

        spiegone = MathTex(r"p(t \land t \land t) = \dfrac{1}{8} "
                           r"\quad p(t \land t \land c) = \dfrac{3}{8} "
                           r"\quad p(t \land c \land c) = \dfrac{3}{8} "
                           r"\quad p(c \land c \land c) = \dfrac{1}{8}")\
            .scale(.8).next_to(three1, 1.5 * DOWN)
        spiegone[0][2].set_color(RED)
        spiegone[0][4].set_color(RED)
        spiegone[0][6].set_color(RED)
        spiegone[0][14].set_color(RED)
        spiegone[0][16].set_color(RED)
        spiegone[0][18].set_color(GREEN)
        spiegone[0][26].set_color(RED)
        spiegone[0][28].set_color(GREEN)
        spiegone[0][30].set_color(GREEN)
        spiegone[0][38].set_color(GREEN)
        spiegone[0][40].set_color(GREEN)
        spiegone[0][42].set_color(GREEN)
        back = BackgroundRectangle(spiegone, color=GRAY_E, buff=.15)
        self.play(Create(back))
        fftf = FromFormulaToFormula(three1, spiegone)

        # Il cubo di binomio ci dice allora che abbiamo quattro possibili risultati:
        # tre teste,

        self.play(fftf.write(slice(0, 2)))
        self.play(fftf.copy_and_move(1, 2),
                  fftf.write(3),
                  fftf.copy_and_move(1, 4),
                  fftf.write(5),
                  fftf.copy_and_move(1, 6))
        self.play(fftf.write(slice(7, 9)))
        self.wait(delay)
        self.next_section()

        # due teste e una croce,

        self.play(fftf.write(slice(12, 14)))
        self.play(fftf.copy_and_move(5, 14),
                  fftf.write(15),
                  fftf.copy_and_move(5, 16),
                  fftf.write(17),
                  fftf.copy_and_move(7, 18))
        self.play(fftf.write(slice(19, 21)))
        self.wait(delay)
        self.next_section()

        # una testa e due croci,

        self.play(fftf.write(slice(24, 26)))
        self.play(fftf.copy_and_move(11, 26),
                  fftf.write(27),
                  fftf.copy_and_move(13, 28),
                  fftf.write(29),
                  fftf.copy_and_move(13, 30))
        self.play(fftf.write(slice(31, 33)))
        self.wait(delay)
        self.next_section()

        # e tre croci. Non ci sono altre possibili combinazioni.

        self.play(fftf.write(slice(36, 38)))
        self.play(fftf.copy_and_move(17, 38),
                  fftf.write(39),
                  fftf.copy_and_move(17, 40),
                  fftf.write(41),
                  fftf.copy_and_move(17, 42))
        self.play(fftf.write(slice(43, 45)))
        self.wait(delay)
        self.next_section()

        # Per ciascuno di questi risultati i casi favorevoli sono:
        # uno per le tre teste,

        self.play(fftf.copy_and_move(0, 9),
                  fftf.write(10))
        self.wait(delay)
        self.next_section()

        # 3 per le due teste e una croce,

        self.play(fftf.copy_and_move(4, 21),
                  fftf.write(22))
        self.wait(delay)
        self.next_section()

        # 3 per la testa e le due croci,

        self.play(fftf.copy_and_move(10, 33),
                  fftf.write(34))
        self.wait(delay)
        self.next_section()

        # uno per le tre croci.

        self.play(fftf.copy_and_move(16, 45),
                  fftf.write(46))
        self.wait(delay)
        self.next_section()

        # E i casi totali quanti sono? Sommo i coefficienti e ottengo 8.

        casi = MathTex(r"\text{\# casi totali} = 1 + 3 + 3 + 1 = 8").scale(.8).next_to(spiegone, 1.5 * DOWN)
        set_color(casi, slice(0, 11), color=YELLOW)
        back_casi = BackgroundRectangle(casi, color=GRAY_E, buff=.15)
        fftf2 = FromFormulaToFormula(three1, casi)
        self.play(Create(back_casi))
        self.play(fftf2.write(slice(0, 12)))
        self.wait(delay)
        self.next_section()

        self.play(fftf2.copy_and_move(0, 12),
                  fftf2.write(13),
                  fftf2.copy_and_move(4, 14),
                  fftf2.write(15),
                  fftf2.copy_and_move(10, 16),
                  fftf2.write(17),
                  fftf2.copy_and_move(16, 18))
        self.wait(delay)
        self.next_section()

        self.play(fftf2.write(slice(19, 21)))
        self.wait(delay)
        self.next_section()

        # Quindi quali sono le probabilità?
        fftf3 = FromFormulaToFormula(casi, spiegone)
        # La probabilità di ottenere tre teste è uno su 8.
        self.play(fftf3.copy_and_move(20, 11))
        self.wait(delay)
        self.next_section()
        # La probabilità di ottenere due teste e una croce è 3 su 8.
        self.play(fftf3.copy_and_move(20, 23))
        self.wait(delay)
        self.next_section()
        # La probabilità di ottenere una testa e due croci è 3 su 8.
        self.play(fftf3.copy_and_move(20, 35))
        self.wait(delay)
        self.next_section()
        # La probabilità di ottenere tre croci è 1 su 8.
        self.play(fftf3.copy_and_move(20, 47))
        self.wait(delay)
        self.next_section()

        self.wait(60)
