from typing import Optional

from colour import Color
from manim import *


class Video2D(MovingCameraScene):

    def construct(self):
        delay = 1

        red_dice = Dice().shift(4*LEFT)
        yellow_dice = Dice()
        blue_dice = Dice().shift(4*RIGHT)
        self.play(
            SpinInFromNothing(red_dice),
            SpinInFromNothing(yellow_dice),
            SpinInFromNothing(blue_dice))
        self.wait(delay)
        self.next_section()

        title = Title("6 su tutti i dadi")
        self.play(Write(title))
        self.wait(delay)
        self.next_section()

        self.play(red_dice.animate.set_color(PURE_RED))
        self.play(yellow_dice.animate.set_color(YELLOW))
        self.play(blue_dice.animate.set_color(PURE_BLUE))
        self.wait(delay)
        self.next_section()

        riga1 = VGroup(
            MathTex(r"p("),
            Dice().scale(.2),
            MathTex(r"=6 \,\,\land "),
            Dice().scale(.2),
            MathTex(r"=6 \,\,\land "),
            Dice().scale(.2),
            MathTex(r"=6\,\,) ="),
        ).arrange(RIGHT).next_to(yellow_dice, 4*DOWN)

        self.play(Write(riga1[0]))
        self.play(red_dice.animate.scale(.2).move_to(riga1[1]))
        self.play(Write(riga1[2]))
        self.play(yellow_dice.animate.scale(.2).move_to(riga1[3]))
        self.play(Write(riga1[4]))
        self.play(blue_dice.animate.scale(.2).move_to(riga1[5]))
        self.play(Write(riga1[6]))

        riga1[1] = red_dice
        riga1[3] = yellow_dice
        riga1[5] = blue_dice

        self.play(riga1.animate.next_to(title, 3*DOWN))
        self.wait(delay)
        self.next_section()

        prob_prodotto = VGroup(
            Tex("Probabilità del prodotto logico:"),
            MathTex(r"\text{eventi indipendenti: }p(E_1 \,\land\, E_2) = p(E_1) \cdot p(E_2)"),
            MathTex(r"\text{eventi dipendenti: }p(E_1 \,\land\, E_2) = p(E_1) \cdot p(E_2 | E_1)")
        ).arrange(DOWN).to_edge(DOWN)
        surr = SurroundingRectangle(prob_prodotto, fill_color=WHITE, fill_opacity=0.15)
        self.play(Create(surr))
        self.play(Write(prob_prodotto))
        self.wait(delay)
        self.next_section()

        self.play(prob_prodotto[1].animate.set_color(YELLOW))
        self.wait(delay)
        self.next_section()

        riga2 = VGroup(
            MathTex(r"= p("),
            red_dice.copy(),
            MathTex(r"=6\,\,) \cdot p("),
            yellow_dice.copy(),
            MathTex(r"=6\,\,) \cdot p("),
            blue_dice.copy(),
            MathTex(r"=6\,\,) ="),
        ).arrange(RIGHT).next_to(riga1, 2 * DOWN)
        self.play(Create(riga2))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(prob_prodotto), FadeOut(surr))
        self.wait(delay)
        self.next_section()

        riga3 = MathTex(r"= \dfrac{1}{6} \cdot \dfrac{1}{6} \cdot \dfrac{1}{6} = ").next_to(riga2, 2 * DOWN)
        riga3[0][1:4].set_color(PURE_RED)
        riga3[0][5:8].set_color(YELLOW)
        riga3[0][9:12].set_color(PURE_BLUE)
        self.play(Write(riga3))
        self.wait(delay)
        self.next_section()
        # self.add(index_labels(riga3[0]))

        riga4 = MathTex(r"= \dfrac{1}{216} = 0,00463 \dots").next_to(riga3, 2 * DOWN)
        self.play(Write(riga4))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(title), FadeOut(riga4), FadeOut(riga3), FadeOut(riga2),
                  FadeOut(riga1[0]), FadeOut(riga1[2]), FadeOut(riga1[4]), FadeOut(riga1[6]),
                  red_dice.animate.scale(5).move_to(4*LEFT + UP),
                  yellow_dice.animate.scale(5).move_to(UP),
                  blue_dice.animate.scale(5).move_to(4*RIGHT + UP))
        self.wait(delay)
        self.next_section()

        title = Title("6 su uno e un solo dado")
        self.play(Write(title))
        self.wait(delay)
        self.next_section()

        caso1 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"=6 \,\,\land "),
            yellow_dice.copy().scale(.2),
            MathTex(r"\ne 6 \,\,\land "),
            blue_dice.copy().scale(.2),
            MathTex(r"\ne 6"),
            MathTex(r")\, +")
        ).arrange(RIGHT)

        caso2 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"\ne 6 \,\,\land "),
            yellow_dice.copy().scale(.2),
            MathTex(r"= 6 \,\,\land "),
            blue_dice.copy().scale(.2),
            MathTex(r"\ne 6"),
            MathTex(r")\, +")
        ).arrange(RIGHT)

        caso3 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"\ne 6 \,\,\land "),
            yellow_dice.copy().scale(.2),
            MathTex(r"\ne 6 \,\,\land "),
            blue_dice.copy().scale(.2),
            MathTex(r"= 6"),
            MathTex(") =")
        ).arrange(RIGHT)

        tre_casi = VGroup(caso1, caso2, caso3).arrange(DOWN).next_to(yellow_dice, 3*DOWN)
        self.play(Create(tre_casi[0][1:7]))
        self.wait(delay)
        self.next_section()

        self.play(Create(tre_casi[1][1:7]))
        self.wait(delay)
        self.next_section()

        self.play(Create(tre_casi[2][1:7]))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(red_dice), FadeOut(yellow_dice), FadeOut(blue_dice), tre_casi.animate.next_to(title, 3*DOWN))
        self.wait(delay)
        self.next_section()

        caso1 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"=6\,\,) \cdot p("),
            yellow_dice.copy().scale(.2),
            MathTex(r"\ne 6\,\,) \cdot p("),
            blue_dice.copy().scale(.2),
            MathTex(r"\ne 6"),
            MathTex(r")\, +")
        ).arrange(RIGHT)

        caso2 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"\ne 6\,\,) \cdot p("),
            yellow_dice.copy().scale(.2),
            MathTex(r"= 6\,\,) \cdot p("),
            blue_dice.copy().scale(.2),
            MathTex(r"\ne 6"),
            MathTex(r")\, +")
        ).arrange(RIGHT)

        caso3 = VGroup(
            MathTex(r"p("),
            red_dice.copy().scale(.2),
            MathTex(r"\ne 6\,\,) \cdot p("),
            yellow_dice.copy().scale(.2),
            MathTex(r"\ne 6\,\,) \cdot p("),
            blue_dice.copy().scale(.2),
            MathTex(r"= 6"),
            MathTex(") =")
        ).arrange(RIGHT)

        tre_casi_2 = VGroup(caso1, caso2, caso3).arrange(DOWN).next_to(tre_casi, 3*DOWN)
        self.play(Create(tre_casi_2))
        self.wait(delay)
        self.next_section()

        self.play(FadeOut(tre_casi), tre_casi_2.animate.move_to(tre_casi))

        tre_casi_3 = MathTex(r"= \dfrac{1}{6} \cdot \dfrac{5}{6} \cdot \dfrac{5}{6} + \dfrac{5}{6} \cdot \dfrac{1}{6} "
                             r"\cdot \dfrac{5}{6} + \dfrac{5}{6} \cdot \dfrac{5}{6} \cdot \dfrac{1}{6} =")\
            .next_to(tre_casi_2, 2*DOWN)
        tre_casi_3[0][1:4].set_color(PURE_RED)
        tre_casi_3[0][5:8].set_color(YELLOW)
        tre_casi_3[0][9:12].set_color(PURE_BLUE)
        tre_casi_3[0][13:16].set_color(PURE_RED)
        tre_casi_3[0][17:20].set_color(YELLOW)
        tre_casi_3[0][21:24].set_color(PURE_BLUE)
        tre_casi_3[0][25:28].set_color(PURE_RED)
        tre_casi_3[0][29:32].set_color(YELLOW)
        tre_casi_3[0][33:36].set_color(PURE_BLUE)
        self.play(Write(tre_casi_3))
        self.wait(delay)
        self.next_section()
        # self.add(index_labels(tre_casi_3[0]))

        tre_casi_4 = MathTex(r"= \dfrac{1}{6} \cdot \dfrac{5}{6} \cdot \dfrac{5}{6} \cdot 3 = \dfrac{75}{216} = 0,"
                             r"3472\dots").next_to(tre_casi_3, 2*DOWN)
        self.play(Write(tre_casi_4[0][0:14]))
        self.wait(delay)
        self.next_section()
        # self.add(index_labels(tre_casi_4[0]))

        self.play(Write(tre_casi_4[0][14:]))
        self.wait(delay)
        self.next_section()

        self.wait(60)


class Face(Square):

    def __init__(self, vect, side_length=2.0, **kwargs):
        self.vect = vect
        super().__init__(side_length, shade_in_3d=True, **kwargs)
        self.round_corners(radius=0.1)
        if not np.array_equal(self.vect, IN):
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * UR))
            self.add(Dot(color=BLACK, radius=0.2).move_to(self.get_center() + .55 * DL))
        if not np.array_equal(self.vect, RIGHT):
            self.add(Dot(color=BLACK, radius=0.2).move_to(self))

    def set_color(self, color, family=True):
        super().set_color(color, False)

    def set_fill(
            self,
            color: Optional[str] = None,
            opacity: Optional[float] = None,
            family: bool = True,
    ):
        if np.array_equal(self.vect, IN):
            color = interpolate_color(Color(color), Color(WHITE), .3).hex
        elif np.array_equal(self.vect, RIGHT):
            color = interpolate_color(Color(color), Color(BLACK), .2).hex
        super().set_fill(color, 1, False)


class Dice(VMobject):

    def __init__(
            self,
            side_length=2,
            fill_color=GRAY,
            **kwargs,
    ):
        self.side_length = side_length
        super().__init__(
            fill_color=fill_color,
            fill_opacity=1,
            stroke_width=0,
            **kwargs,
        )
        self.rotate(.4 * PI, axis=RIGHT).rotate(PI / 6, axis=UP).rotate(.05 * PI, axis=IN)

    def generate_points(self):
        for vect in IN, DOWN, RIGHT:
            face = Face(vect)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

    init_points = generate_points
