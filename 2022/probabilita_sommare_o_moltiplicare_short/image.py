from manim import *


class Video(MovingCameraScene):

    def construct(self):
        Tex.set_default(font_size=60)
        MathTex.set_default(font_size=60)

        logo = ImageMobject("../../Loghi/Logo Qui Matematica 3.png").scale(.15).to_edge(UR).shift(.5 * RIGHT + .5 * UP)
        self.add(logo)

        par = VGroup(
            Tex(r"Probabilità in \#shorts:"),
            Tex("sommare o moltiplicare?")
        ).scale(2).arrange(DOWN, buff=1)

        self.add(par)

        self.wait(5)
