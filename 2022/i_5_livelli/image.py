from manim import *

from object import Coin, CROSS, HEAD


class Scene(MovingCameraScene):

    def construct(self):

        coin_shift = .7

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

        coins = [Coin(face=faces[_i]).set_color(colors[_i]).scale(.6).move_to(points[_i]) for _i in range(len(points))]

        self.add(*coins)

        domanda = MathTex(r"{{ p(\text{2 teste}) = }} \dfrac{15}{64}").move_to(2.7*DOWN)
        domanda[0][2:8].set_color(YELLOW)
        self.add(domanda)

        self.wait(60)
