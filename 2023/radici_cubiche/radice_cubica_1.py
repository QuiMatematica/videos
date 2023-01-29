from manim import *
from numpy import array


class Scene(ThreeDScene):

    def construct(self):
        delay = 30

        self.wait(1)
        self.move_camera(zoom=1.5)

        line = Line(LEFT + DOWN + IN, RIGHT + DOWN + IN, color=BLUE)

        misura = MathTex(r"3").next_to(line, DOWN)

        self.play(Create(line))
        self.play(Write(misura))
        self.wait(delay)
        self.next_section()

        square = Square(fill_color=BLUE, fill_opacity=.7, color=BLUE).shift(IN).rotate(PI)

        self.play(Create(square))
        self.wait(delay)
        self.next_section()

        self.move_camera(phi=75 * DEGREES, theta=-35 * DEGREES)

        cube = Cube()

        self.play(Create(cube), FadeOut(square), FadeOut(line))
        self.wait(delay)
        self.next_section()

        volume = MathTex(r"V = l^3 = 3^3 = 27")
        lato = MathTex(r"l = \sqrt[3]{V} = \sqrt[3]{27} = 3")
        VGroup(volume, lato).arrange(DOWN).next_to(cube, RIGHT, buff=.5).rotate(PI/2, axis=array([1., 0., 0.]))

        self.move_camera(phi=75 * DEGREES, theta=-75 * DEGREES, frame_center=array([2, 0, 0]),
                         added_anims=[Write(volume)])
        self.wait(delay)
        self.next_section()

        self.play(Write(lato))
        self.wait(delay)
        self.next_section()

        self.play(Indicate(lato[0][2], scale_factor=2), Indicate(lato[0][7], scale_factor=2))

        self.wait(30)



