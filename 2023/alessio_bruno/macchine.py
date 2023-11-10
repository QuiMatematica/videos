from manim import *

DELAY = 30


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        vla = ImageMobject('../../img/macchine.PNG')

        self.add(vla)

        v1_start = -.2 * RIGHT + .05 * UP
        v2_start = -.2 * RIGHT + .25 * UP

        v1 = Arrow(v1_start, end=v1_start + 2 * RIGHT + .09 * UP, color=YELLOW, buff=0)
        v1_label = Tex("50 km/h", color=YELLOW).next_to(v1, DOWN)
        self.play(Create(v1), Write(v1_label))

        v2 = Arrow(v2_start, end=v2_start - 4 * RIGHT - .18 * UP, color=YELLOW, buff=0)
        v2_label = Tex("100 km/h", color=YELLOW).next_to(v2, UP)
        self.play(Create(v2), Write(v2_label))
        self.cut_and_wait()

        v_tot = MathTex(r"v_{tot} = v_1 + v_2 = 50 \text{ km/h} + 100 \text{ km/h} = 150 \text{ km/h}", color=BLACK).to_edge(UP)
        self.play(Write(v_tot))

        self.wait(30)
