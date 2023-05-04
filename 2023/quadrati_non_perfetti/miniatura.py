from manim import *


class Scene(MovingCameraScene):

    def construct(self):

        titolo1 = Tex("Radici perfette di")
        titolo2 = Tex("quadrati non perfetti")

        gruppo = VGroup(titolo1, titolo2).scale(2.5).arrange(DOWN)
        esempio = MathTex(r"\sqrt{600}", color=GREEN).scale(4)

        gruppone = VGroup(gruppo, esempio).arrange(DOWN, buff=1)

        self.add(gruppone)
