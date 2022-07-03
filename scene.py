from manim import *

from object import Coin


class Scene(MovingCameraScene):

    def construct(self):
        delay = 60

        coin = Coin()
        self.add(coin)
        self.wait(1)
        self.play(coin.animate.set_color(PURE_RED))
        self.wait(1)
        coin.flip_coin(self)
        self.wait(1)
        coin.flip_coin(self)
        self.wait(1)
