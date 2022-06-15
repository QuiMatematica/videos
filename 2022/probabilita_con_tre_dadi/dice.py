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

        self.play(FadeOut(prob_prodotto))
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
