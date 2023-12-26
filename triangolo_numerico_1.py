from manim import *

from qui_matematica.qmath import NumericalTriangle

DELAY = 1

SUM_SCALE = 1.3
SCALE = 2

TARTA_COLOR=BLUE


class Scene(MovingCameraScene):

    def write_and_add_to_group(self, value_object, gruppo):
        self.play(Write(value_object))
        gruppo.add(value_object)

    def parcheggia(self, gruppo, edge=UL):
        self.play(gruppo.animate.scale(.25).to_edge(edge))

    def ripristina(self, gruppo):
        self.play(gruppo.animate.scale(4).move_to(ORIGIN))

    def togli_evidenzia(self, backs):
        self.play(*[FadeOut(_b) for _b in backs])
        self.cut_and_wait()

    def evidenzia(self, triangolo, *caselle):
        backs = []
        for _c in caselle:
            rect = triangolo.get_cell(_c)
            back = BackgroundRectangle(rect, color=RED, fill_opacity=.3)
            backs.append(back)
        self.play(*[FadeIn(_b) for _b in backs])
        self.cut_and_wait()
        return backs

    def sum(self, triangolo, pos):
        pos_1 = (pos[0] + 1, pos[1])
        pos_2 = (pos[0] + 1, pos[1] + 1)

        p1_value = triangolo.get_value(pos_1)
        p2_value = triangolo.get_value(pos_2)
        sum_value = p1_value + p2_value

        c1 = triangolo.get_value_object(pos_1).copy()
        c2 = triangolo.get_value_object(pos_2).copy()

        temp = triangolo.put_value(pos, str(p1_value) + "+" + str(p2_value), value_color=YELLOW)
        plus = temp[0][1]
        if p1_value < 10:
            c1.target = temp[0][0]
            if p2_value < 10:
                c2.target = temp[0][2]
            else:
                c2.target = temp[0][2:3]
        else:
            plus = temp[0][2]
            c1.target = temp[0][0:1]
            if p2_value < 10:
                c2.target = temp[0][3]
            else:
                c2.target = temp[0][3:4]
        self.play(
            Write(plus),
            MoveToTarget(c1),
            MoveToTarget(c2)
        )
        self.add(temp)
        self.remove(c1, c2)

        sum_object = triangolo.put_value(pos, sum_value, value_color=YELLOW)
        self.play(ReplacementTransform(temp, sum_object))
        self.cut_and_wait()

    def subtract(self, triangolo, pos):
        pos_1 = (pos[0] + 1, pos[1])
        pos_2 = (pos[0] + 1, pos[1] + 1)

        sum_value = triangolo.get_value(pos)
        p2_value = triangolo.get_value(pos_2)
        p1_value = sum_value - p2_value

        sum_object = triangolo.get_value_object(pos).copy()
        c2 = triangolo.get_value_object(pos_2).copy()

        temp = triangolo.put_value(pos_1, str(sum_value) + "-" + str(p2_value), value_color=YELLOW)
        sum_object.target = temp[0][0]
        c2.target = temp[0][2]
        self.play(
            Write(temp[0][1]),
            MoveToTarget(sum_object),
            MoveToTarget(c2)
        )
        self.add(temp)
        self.remove(sum_object, c2)

        c1_object = triangolo.put_value(pos_1, p1_value, value_color=YELLOW)
        self.play(ReplacementTransform(temp, c1_object))
        self.cut_and_wait()

    def somma_tartaglia(self, triangolo, pos):
        pos_1 = (pos[0] - 1, pos[1] - 1)
        pos_2 = (pos[0] - 1, pos[1])

        p1_value = triangolo.get_value(pos_1)
        p2_value = triangolo.get_value(pos_2)
        sum_value = p1_value + p2_value

        c1 = triangolo.get_value_object(pos_1).copy()
        c2 = triangolo.get_value_object(pos_2).copy()

        temp = triangolo.put_value(pos, str(p1_value) + "+" + str(p2_value), value_scale=SUM_SCALE, value_color=TARTA_COLOR)
        c1.target = temp[0][0]
        c2.target = temp[0][2]
        self.play(
            Write(temp[0][1]),
            MoveToTarget(c1),
            MoveToTarget(c2)
        )
        self.add(temp)
        self.remove(c1, c2)

        sum_object = triangolo.put_value(pos, sum_value, value_color=TARTA_COLOR)
        self.play(ReplacementTransform(temp, sum_object))
        self.cut_and_wait()

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        triangolo = NumericalTriangle(4)
        self.play(Create(triangolo))
        self.cut_and_wait()

        gruppo = VGroup(triangolo)

        self.write_and_add_to_group(triangolo.put_value((3, 0), 2), gruppo)
        self.write_and_add_to_group(triangolo.put_value((3, 2), 7), gruppo)
        self.write_and_add_to_group(triangolo.put_value((3, 3), 3), gruppo)
        self.write_and_add_to_group(triangolo.put_value((0, 0), 38), gruppo)
        self.cut_and_wait()

        backs = self.evidenzia(triangolo, (2, 2), (3, 2), (3, 3))

        self.sum(triangolo, (2, 2))
        gruppo.add(triangolo.get_value_object((2, 2)))

        self.togli_evidenzia(backs)

        self.parcheggia(gruppo)

        triangolo_2 = NumericalTriangle(2)
        self.play(Create(triangolo_2))
        self.play(Write(triangolo_2.put_value((1, 0), "a")))
        self.play(Write(triangolo_2.put_value((1, 1), "b")))
        self.play(Write(triangolo_2.put_value((0, 0), "a+b")))
        self.cut_and_wait()

        self.play(
            ReplacementTransform(triangolo_2.get_value_object((1, 0)), triangolo_2.put_value((1, 0), 2)),
            ReplacementTransform(triangolo_2.get_value_object((1, 1)), triangolo_2.put_value((1, 1), 5)),
            FadeOut(triangolo_2.get_value_object((0, 0)))
        )
        self.cut_and_wait()

        self.sum(triangolo_2, (0, 0))

        self.play(
            FadeOut(triangolo_2.get_value_object((1, 0))),
            ReplacementTransform(triangolo_2.get_value_object((1, 1)), triangolo_2.put_value((1, 1), 6)),
            ReplacementTransform(triangolo_2.get_value_object((0, 0)), triangolo_2.put_value((0, 0), 9))
        )
        self.cut_and_wait()

        self.subtract(triangolo_2, (0, 0))

        self.play(
            FadeOut(triangolo_2),
            FadeOut(triangolo_2.get_value_object((0, 0))),
            FadeOut(triangolo_2.get_value_object((1, 0))),
            FadeOut(triangolo_2.get_value_object((1, 1))),
        )

        self.ripristina(gruppo)
        self.cut_and_wait()

        self.parcheggia(gruppo)

        triangolo_3 = NumericalTriangle(3, rect_width=3)
        self.play(Create(triangolo_3))
        self.cut_and_wait()

        self.play(Write(triangolo_3.put_value((2, 0), "a")))
        self.play(Write(triangolo_3.put_value((2, 1), "b")))
        self.play(Write(triangolo_3.put_value((2, 2), "c")))
        self.cut_and_wait()

        self.play(Write(triangolo_3.put_value((1, 0), "a+b")))
        self.play(Write(triangolo_3.put_value((1, 1), "b+c")))
        self.cut_and_wait()

        self.play(Write(triangolo_3.put_value((0, 0), "(a+b)+(b+c)", value_scale=.8)))
        self.cut_and_wait()

        self.play(ReplacementTransform(triangolo_3.get_value_object((0, 0)), triangolo_3.put_value((0, 0), "a + 2b + c", value_scale=1.2)))
        self.cut_and_wait()

        self.play(
            FadeOut(triangolo_3),
            FadeOut(triangolo_3.get_value_object((0, 0))),
            FadeOut(triangolo_3.get_value_object((1, 0))),
            FadeOut(triangolo_3.get_value_object((1, 1))),
            FadeOut(triangolo_3.get_value_object((2, 0))),
            FadeOut(triangolo_3.get_value_object((2, 1))),
            FadeOut(triangolo_3.get_value_object((2, 2))),
        )

        triangolo_4 = NumericalTriangle(4, rect_width=3)
        self.play(Create(triangolo_4))
        self.cut_and_wait()

        gruppo_4 = VGroup()
        gruppo_4.add(triangolo_4)

        self.write_and_add_to_group(triangolo_4.put_value((3, 0), "a"), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((3, 1), "b"), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((3, 2), "c"), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((3, 3), "d"), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((2, 0), "a+b", value_scale=SUM_SCALE), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((2, 1), "b+c", value_scale=SUM_SCALE), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((2, 2), "c+d", value_scale=SUM_SCALE), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((1, 0), "a+2b+c", value_scale=1.2), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((1, 1), "b+2c+d", value_scale=1.2), gruppo_4)
        self.write_and_add_to_group(triangolo_4.put_value((0, 0), "a+3b+3c+d", value_scale=.8), gruppo_4)
        self.cut_and_wait()

        self.parcheggia(gruppo_4, UR)

        tartaglia_4 = NumericalTriangle(4)
        self.play(Create(tartaglia_4))
        self.cut_and_wait()

        gruppo_tartaglia_4 = VGroup()
        gruppo_tartaglia_4.add(tartaglia_4)

        for _i in range(4):
            self.write_and_add_to_group(tartaglia_4.put_value((_i, 0), 1, value_color=TARTA_COLOR), gruppo_tartaglia_4)
        for _i in range(1, 4):
            self.write_and_add_to_group(tartaglia_4.put_value((_i, _i), 1, value_color=TARTA_COLOR), gruppo_tartaglia_4)

        self.somma_tartaglia(tartaglia_4, (2, 1))
        self.somma_tartaglia(tartaglia_4, (3, 1))
        self.somma_tartaglia(tartaglia_4, (3, 2))
        gruppo_tartaglia_4.add(tartaglia_4.get_value_object((2, 1)))
        gruppo_tartaglia_4.add(tartaglia_4.get_value_object((3, 1)))
        gruppo_tartaglia_4.add(tartaglia_4.get_value_object((3, 2)))
        self.cut_and_wait()

        self.play(gruppo_tartaglia_4.animate.scale(.5).move_to(3.5 * LEFT + .5 * DOWN))
        self.play(gruppo_4.animate.scale(2).move_to(3.5 * RIGHT + .5 * DOWN))
        self.cut_and_wait()

        backs_tartaglia = self.evidenzia(tartaglia_4, (3, 0), (3, 1), (3, 2), (3, 3))
        backs_triangolo_4 = self.evidenzia(triangolo_4, (3, 0), (3, 1), (3, 2), (3, 3))

        prodotto = MathTex(r"1a + 3b + 3c + 1d").scale(2).move_to(3.2 * DOWN)
        prodotto[0][0].set_color(TARTA_COLOR)
        prodotto[0][3].set_color(TARTA_COLOR)
        prodotto[0][6].set_color(TARTA_COLOR)
        prodotto[0][9].set_color(TARTA_COLOR)

        c1 = tartaglia_4.get_value_object((3, 0)).copy()
        c2 = tartaglia_4.get_value_object((3, 1)).copy()
        c3 = tartaglia_4.get_value_object((3, 2)).copy()
        c4 = tartaglia_4.get_value_object((3, 3)).copy()
        c1.target = prodotto[0][0]
        c2.target = prodotto[0][3]
        c3.target = prodotto[0][6]
        c4.target = prodotto[0][9]

        v1 = triangolo_4.get_value_object((3, 0)).copy()
        v2 = triangolo_4.get_value_object((3, 1)).copy()
        v3 = triangolo_4.get_value_object((3, 2)).copy()
        v4 = triangolo_4.get_value_object((3, 3)).copy()
        v1.target = prodotto[0][1]
        v2.target = prodotto[0][4]
        v3.target = prodotto[0][7]
        v4.target = prodotto[0][10]

        p1 = prodotto[0][2]
        p2 = prodotto[0][5]
        p3 = prodotto[0][8]

        self.play(MoveToTarget(c1))
        self.play(MoveToTarget(v1))
        self.play(MoveToTarget(c2))
        self.play(MoveToTarget(v2))
        self.play(MoveToTarget(c3))
        self.play(MoveToTarget(v3))
        self.play(MoveToTarget(c4))
        self.play(MoveToTarget(v4))
        self.cut_and_wait()

        self.play(Write(p1))
        self.play(Write(p2))
        self.play(Write(p3))
        self.remove(c1, c2, c3, c4, v1, v2, v3, v4, p1, p2, p3)
        self.add(prodotto)
        self.cut_and_wait()

        backs_cima = self.evidenzia(triangolo_4, (0, 0))

        copia = prodotto.copy()
        copia.target = triangolo_4.get_value_object((0, 0))
        self.play(MoveToTarget(copia))
        self.remove(copia)
        self.cut_and_wait()

        self.play(
            FadeOut(gruppo_4),
            FadeOut(prodotto),
            *[FadeOut(_b) for _b in backs_tartaglia],
            *[FadeOut(_b) for _b in backs_triangolo_4],
            *[FadeOut(_b) for _b in backs_cima]
        )

        self.play(gruppo.animate.scale(2).move_to(3.5 * RIGHT + .5 * DOWN))
        self.cut_and_wait()

        incognita = triangolo.put_value((3, 1), "x", value_color=YELLOW, value_scale=1)
        self.play(Write(incognita))
        self.cut_and_wait()

        backs_tartaglia = self.evidenzia(tartaglia_4, (3, 0), (3, 1), (3, 2), (3, 3))
        backs_triangolo = self.evidenzia(triangolo, (3, 0), (3, 1), (3, 2), (3, 3))

        prodotto = MathTex(r"1 \cdot 2 + 3 \cdot x + 3 \cdot 7 + 1 \cdot 3 = 38").scale(2).move_to(3.2 * DOWN)
        prodotto[0][0].set_color(TARTA_COLOR)
        prodotto[0][4].set_color(TARTA_COLOR)
        prodotto[0][6].set_color(YELLOW)
        prodotto[0][8].set_color(TARTA_COLOR)
        prodotto[0][12].set_color(TARTA_COLOR)

        c1 = tartaglia_4.get_value_object((3, 0)).copy()
        c2 = tartaglia_4.get_value_object((3, 1)).copy()
        c3 = tartaglia_4.get_value_object((3, 2)).copy()
        c4 = tartaglia_4.get_value_object((3, 3)).copy()
        c1.target = prodotto[0][0]
        c2.target = prodotto[0][4]
        c3.target = prodotto[0][8]
        c4.target = prodotto[0][12]

        v1 = triangolo.get_value_object((3, 0)).copy()
        v2 = triangolo.get_value_object((3, 1)).copy()
        v3 = triangolo.get_value_object((3, 2)).copy()
        v4 = triangolo.get_value_object((3, 3)).copy()
        v1.target = prodotto[0][2]
        v2.target = prodotto[0][6]
        v3.target = prodotto[0][10]
        v4.target = prodotto[0][14]

        m1 = prodotto[0][1]
        m2 = prodotto[0][5]
        m3 = prodotto[0][9]
        m4 = prodotto[0][13]

        p1 = prodotto[0][3]
        p2 = prodotto[0][7]
        p3 = prodotto[0][11]

        self.play(MoveToTarget(c1))
        self.play(Write(m1))
        self.play(MoveToTarget(v1))
        self.play(MoveToTarget(c2))
        self.play(Write(m2))
        self.play(MoveToTarget(v2))
        self.play(MoveToTarget(c3))
        self.play(Write(m3))
        self.play(MoveToTarget(v3))
        self.play(MoveToTarget(c4))
        self.play(Write(m4))
        self.play(MoveToTarget(v4))
        self.cut_and_wait()

        self.play(Write(p1))
        self.play(Write(p2))
        self.play(Write(p3))
        self.cut_and_wait()

        backs_cima = self.evidenzia(triangolo, (0, 0))

        ug = prodotto[0][15]
        to = triangolo.get_value_object((0, 0)).copy()
        to.target = prodotto[0][16:]
        self.play(Write(ug))
        self.play(MoveToTarget(to))
        self.cut_and_wait()

        self.remove(c1, c2, c3, c4, v1, v2, v3, v4, m1, m2, m3, m4, p1, p2, p3, ug, to)
        self.add(prodotto)
        self.cut_and_wait()

        prodotto_2 = MathTex(r"2 + 3x + 21 + 3 = 38").scale(2).move_to(3.2 * DOWN)
        prodotto_2[0][3].set_color(YELLOW)
        self.play(Transform(prodotto, prodotto_2))
        prodotto_3 = MathTex(r"3x + 26 = 38").scale(2).move_to(3.2 * DOWN)
        prodotto_3[0][1].set_color(YELLOW)
        self.play(Transform(prodotto, prodotto_3))
        prodotto_4 = MathTex(r"3x = 38 - 26").scale(2).move_to(3.2 * DOWN)
        prodotto_4[0][1].set_color(YELLOW)
        self.play(Transform(prodotto, prodotto_4))
        prodotto_5 = MathTex(r"3x = 12").scale(2).move_to(3.2 * DOWN)
        prodotto_5[0][1].set_color(YELLOW)
        self.play(Transform(prodotto, prodotto_5))
        prodotto_6 = MathTex(r"x = 4").scale(2).move_to(3.2 * DOWN)
        prodotto_6[0][0].set_color(YELLOW)
        self.play(ReplacementTransform(prodotto, prodotto_6))
        self.cut_and_wait()

        copia = prodotto_6[0][2].copy()
        valore = triangolo.put_value((3, 1), 4, value_color=YELLOW, value_scale=1)
        copia.target = valore

        self.play(FadeOut(incognita), MoveToTarget(copia))
        self.remove(copia)
        self.add(valore)
        gruppo.add(valore)
        self.cut_and_wait()

        self.play(
            FadeOut(gruppo_tartaglia_4),
            FadeOut(prodotto_6),
            *[FadeOut(_b) for _b in backs_tartaglia],
            *[FadeOut(_b) for _b in backs_triangolo],
            FadeOut(backs_cima[0])
        )

        self.play(gruppo.animate.scale(2).move_to(ORIGIN))
        self.cut_and_wait()

        self.sum(triangolo, (2, 0))
        self.sum(triangolo, (2, 1))
        self.sum(triangolo, (1, 0))
        self.sum(triangolo, (1, 1))

        self.wait(30)

