from manim import *

from object import Coin, CROSS, HEAD


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1

        coin_shift = 1.3

        faces = [HEAD, HEAD, CROSS, CROSS, CROSS, CROSS]
        points = [
            [-3.7, coin_shift - .15, 0],
            [-1.5, coin_shift + 1.4, 0],
            [1.1, coin_shift + 1.2, 0],
            [3.7, coin_shift + .15, 0],
            [1.5, coin_shift - 1.4, 0],
            [-1.1, coin_shift - 1.2, 0]
        ]
        assert len(faces) == len(points), 'Faces <> points'

        colors = [PURE_RED, "#FF7700", YELLOW, PURE_GREEN, PURE_BLUE, "#FF00FF"]
        assert len(faces) == len(colors), 'Faces <> colors'

        coins = [Coin(face=faces[_i]).scale(.6).move_to(points[_i]) for _i in range(len(points))]

        self.play(*[SpinInFromNothing(x, angle=2 * PI, run_time=1) for x in coins])
        self.wait(delay)
        self.next_section()

        domanda = MathTex(r"{{ p(\text{2 teste}) = }} \,\,?").move_to(2*DOWN)
        domanda[0][2:8].set_color(YELLOW)
        self.play(Write(domanda))
        self.wait(delay)
        self.next_section()

        domanda2 = MathTex(r"{{ p(\text{2 teste}) = }} \dfrac{ \text{\# casi favorevoli} }{ \text{\# casi totali} }").move_to(domanda)
        domanda2[0][2:8].set_color(YELLOW)
        domanda2[1][0:15].set_color(YELLOW)
        domanda2[1][16:].set_color(YELLOW)
        self.play(TransformMatchingTex(domanda, domanda2))
        self.wait(delay)
        self.next_section()

        totali1 = MathTex(r"{{ \text{\# casi totali} = }} \,\,?").next_to(domanda2, 1.5*DOWN)
        totali1[0][0:11].set_color(YELLOW)
        self.play(Write(totali1))
        self.wait(delay)
        self.next_section()

        coins[1].flip_coin(self)
        coins[2].flip_coin(self)
        self.wait(delay)
        self.next_section()

        self.play(*[coins[_i].animate.set_color(colors[_i]) for _i in range(len(colors))])
        self.wait(delay)
        self.next_section()

        coins[1].flip_coin(self)
        coins[2].flip_coin(self)
        self.wait(delay)
        self.next_section()

        totali2 = MathTex(r"{{ \text{\# casi totali} = }} 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = {{ 2^6 = 64 }}").move_to(totali1)
        totali2[0][0:11].set_color(YELLOW)

        self.play(totali1[0].animate.move_to(totali2[0]), FadeOut(totali1[1]))

        twos = []
        for _i in range(len(coins)):
            number_two = MathTex('2', z_index=3, color=BLACK).scale(2).move_to(coins[_i])
            number_two.target = totali2[1][_i * 2]
            self.play(Write(number_two))
            self.play(MoveToTarget(number_two), FadeIn(totali2[1][_i * 2 + 1]))
            twos.append(number_two)
        self.wait(delay)
        self.next_section()

        self.play(Write(totali2[2]))
        self.wait(delay)
        self.next_section()

        totali3 = MathTex(r"{{ \text{\# casi totali} = }} D^{(r)}_{2, 6} = {{ 2^6 = 64 }}").move_to(totali2)
        totali3[0][0:11].set_color(YELLOW)
        self.play(FadeOut(totali2), FadeOut(totali1[0]), *[FadeOut(t) for t in twos])

        self.play(Write(totali3[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(totali3[1]))
        self.wait(delay)
        self.next_section()

        regola = MathTex(r"D^{(r)}_{n, k} = n^k").move_to(1.5*UP)
        rect = SurroundingRectangle(regola, fill_color=BLACK, fill_opacity=1, buff=MED_LARGE_BUFF)
        group = VGroup(rect, regola).set_z_index(5)

        self.play(Write(group))
        self.wait(delay)
        self.next_section()

        self.play(Write(totali3[2]))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(group))
        self.play(totali3[2][3:].copy().animate.move_to(domanda2[1][16:]), FadeOut(domanda2[1][16:]))
        self.play(FadeOut(totali3))
        self.wait(delay)
        self.next_section()

        favorevoli1 = MathTex(r"{{ \text{\# casi favorevoli} = }} \,\,?").next_to(domanda2, 1.5*DOWN)
        favorevoli1[0][0:15].set_color(YELLOW)
        self.play(Write(favorevoli1))
        self.wait(delay)
        self.next_section()

        distanza = 2
        for _i in range(len(coins)):
            coins[_i].target = coins[_i].copy().move_to([distanza*(_i - 2.5), 3, 0])
        self.play(*[MoveToTarget(c) for c in coins])
        self.wait(delay)
        self.next_section()

        coins[1].flip_coin(self)
        coins[2].flip_coin(self)
        self.wait(delay)
        self.next_section()

        coins2 = [Coin(face=faces[_i]).set_color(colors[_i]).scale(.6).move_to(coins[_i].get_center() - 2*DOWN) for _i in range(len(faces))]
        self.play(*[Create(c) for c in coins2])
        self.wait(delay)
        self.next_section()

        self.wait(60)
