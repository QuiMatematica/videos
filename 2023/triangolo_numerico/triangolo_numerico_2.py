from manim import *

from qui_matematica.qmath import NumericalTriangle, EqSystem

DELAY = 30


class Scene(MovingCameraScene):

    def somma_tartaglia(self, triangolo, pos, gruppo):
        pos_1 = (pos[0] - 1, pos[1] - 1)
        pos_2 = (pos[0] - 1, pos[1])

        p1_value = triangolo.get_value(pos_1)
        p2_value = triangolo.get_value(pos_2)
        sum_value = p1_value + p2_value

        c1 = triangolo.get_value_object(pos_1).copy()
        c2 = triangolo.get_value_object(pos_2).copy()

        temp = triangolo.put_value(pos, str(p1_value) + "+" + str(p2_value), value_scale=1, value_color=BLUE)
        c1.target = temp[0][0]
        c2.target = temp[0][2]
        self.play(
            Write(temp[0][1]),
            MoveToTarget(c1),
            MoveToTarget(c2)
        )
        self.add(temp)
        self.remove(c1, c2)

        sum_object = triangolo.put_value(pos, sum_value, value_scale=1, value_color=BLUE)
        self.play(ReplacementTransform(temp, sum_object))
        gruppo.add(sum_object)
        self.cut_and_wait()

    def togli_evidenzia(self, backs):
        self.play(*[FadeOut(_b) for _b in backs])

    def evidenzia(self, triangolo, *caselle):
        backs = []
        for _c in caselle:
            rect = triangolo.get_cell(_c)
            back = BackgroundRectangle(rect, color=RED, fill_opacity=.3)
            backs.append(back)
        self.play(*[FadeIn(_b) for _b in backs])
        return backs

    def write_and_add_to_group(self, value_object, gruppo):
        self.play(Write(value_object))
        gruppo.add(value_object)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def sum(self, triangolo, pos):
        pos_1 = (pos[0] + 1, pos[1])
        pos_2 = (pos[0] + 1, pos[1] + 1)

        p1_value = triangolo.get_value(pos_1)
        p2_value = triangolo.get_value(pos_2)
        sum_value = p1_value + p2_value

        c1 = triangolo.get_value_object(pos_1).copy()
        c2 = triangolo.get_value_object(pos_2).copy()

        temp = triangolo.put_value(pos, str(p1_value) + "+" + str(p2_value), value_scale=1, value_color=YELLOW)
        plus = temp[0][1]
        if p1_value < 10:
            c1.target = temp[0][0]
            if p2_value < 10:
                c2.target = temp[0][2]
            else:
                c2.target = temp[0][2:4]
        else:
            plus = temp[0][2]
            c1.target = temp[0][0:2]
            if p2_value < 10:
                c2.target = temp[0][3]
            else:
                c2.target = temp[0][3:5]
        self.play(
            Write(plus),
            MoveToTarget(c1),
            MoveToTarget(c2)
        )
        self.add(temp)
        self.remove(c1, c2)

        sum_object = triangolo.put_value(pos, sum_value, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(temp, sum_object))
        self.cut_and_wait()

    def construct(self):
        self.wait(.5)

        triangolo = NumericalTriangle(6).scale(.75)
        self.play(Create(triangolo))
        self.cut_and_wait()

        gruppo = VGroup(triangolo)

        self.write_and_add_to_group(triangolo.put_value((5, 0), 2), gruppo)
        self.write_and_add_to_group(triangolo.put_value((4, 1), 6), gruppo)
        self.write_and_add_to_group(triangolo.put_value((4, 4), 4), gruppo)
        self.write_and_add_to_group(triangolo.put_value((3, 2), 17), gruppo)
        self.write_and_add_to_group(triangolo.put_value((2, 0), 25), gruppo)
        self.write_and_add_to_group(triangolo.put_value((0, 0), 118), gruppo)
        self.cut_and_wait()

        self.write_and_add_to_group(triangolo.put_value((5, 1), 'a', value_color=YELLOW), gruppo)
        self.write_and_add_to_group(triangolo.put_value((5, 2), 'b', value_color=YELLOW), gruppo)
        self.write_and_add_to_group(triangolo.put_value((5, 3), 'c', value_color=YELLOW), gruppo)
        self.write_and_add_to_group(triangolo.put_value((5, 4), 'd', value_color=YELLOW), gruppo)
        self.write_and_add_to_group(triangolo.put_value((5, 5), 'e', value_color=YELLOW), gruppo)
        self.cut_and_wait()

        self.play(gruppo.animate.scale(.5).move_to(3.5 * RIGHT + 2 * UP))
        self.cut_and_wait()

        tartaglia = NumericalTriangle(6).scale(.75).scale(.5).move_to(3.5 * LEFT + 2 * UP)
        self.play(Create(tartaglia))
        self.cut_and_wait()

        gruppo_tartaglia = VGroup()
        gruppo_tartaglia.add(tartaglia)

        for _i in range(6):
            self.write_and_add_to_group(tartaglia.put_value((_i, 0), 1, value_scale=1, value_color=BLUE), gruppo_tartaglia)
        for _i in range(1, 6):
            self.write_and_add_to_group(tartaglia.put_value((_i, _i), 1, value_scale=1, value_color=BLUE), gruppo_tartaglia)

        for _i in range(2, 6):
            for _j in range(1, _i):
                self.somma_tartaglia(tartaglia, (_i, _j), gruppo_tartaglia)
        self.cut_and_wait()

        eq1 = MathTex(r"a + b = 6")
        eq1[0][0].set_color(YELLOW)
        eq1[0][2].set_color(YELLOW)
        eq2 = MathTex(r"d + e = 4")
        eq2[0][0].set_color(YELLOW)
        eq2[0][2].set_color(YELLOW)
        eq3 = MathTex(r"b + 2c + d = 17")
        eq3[0][0].set_color(YELLOW)
        eq3[0][3].set_color(YELLOW)
        eq3[0][5].set_color(YELLOW)
        eq3[0][2].set_color(BLUE)
        eq4 = MathTex(r"2 + 3a + 3b + c = 25")
        eq4[0][3].set_color(YELLOW)
        eq4[0][6].set_color(YELLOW)
        eq4[0][8].set_color(YELLOW)
        eq4[0][2].set_color(BLUE)
        eq4[0][5].set_color(BLUE)
        eq5 = MathTex(r"2 + 5a + 10b + 10c + 5d + e = 118")
        eq5[0][3].set_color(YELLOW)
        eq5[0][7].set_color(YELLOW)
        eq5[0][11].set_color(YELLOW)
        eq5[0][14].set_color(YELLOW)
        eq5[0][16].set_color(YELLOW)
        eq5[0][2].set_color(BLUE)
        eq5[0][5:7].set_color(BLUE)
        eq5[0][9:11].set_color(BLUE)
        eq5[0][13].set_color(BLUE)

        sistema = EqSystem(eq1, eq2, eq3, eq4, eq5).move_to(2 * DOWN)
        # self.add(sistema)

        #################

        back_triangolo = self.evidenzia(triangolo, (4, 1), (5, 1), (5, 2))
        backs_tartaglia = self.evidenzia(tartaglia, (0, 0), (1, 0), (1, 1))
        self.cut_and_wait()

        gruppetto_tartaglia = VGroup(
            tartaglia.get_value_object((1, 0)).copy(),
            tartaglia.get_value_object((1, 1)).copy()
        )
        gruppetto_tartaglia.target = eq1[0][:3]

        gruppetto_triangolo = VGroup(
            triangolo.get_value_object((5, 1)).copy(),
            triangolo.get_value_object((5, 2)).copy()
        )
        gruppetto_triangolo.target = eq1[0][:3]

        self.play(
            MoveToTarget(gruppetto_triangolo),
            MoveToTarget(gruppetto_tartaglia)
        )
        self.play(Write(eq1[0][3]))

        totale = triangolo.get_value_object((4, 1)).copy()
        totale.target = eq1[0][4]
        self.play(MoveToTarget(totale))
        self.cut_and_wait()

        self.togli_evidenzia(backs_tartaglia)
        self.togli_evidenzia(back_triangolo)
        self.cut_and_wait()

        #################

        back_triangolo = self.evidenzia(triangolo, (4, 4), (5, 4), (5, 5))
        backs_tartaglia = self.evidenzia(tartaglia, (0, 0), (1, 0), (1, 1))
        self.cut_and_wait()

        gruppetto_tartaglia = VGroup(
            tartaglia.get_value_object((1, 0)).copy(),
            tartaglia.get_value_object((1, 1)).copy()
        )
        gruppetto_tartaglia.target = eq2[0][:3]

        gruppetto_triangolo = VGroup(
            triangolo.get_value_object((5, 4)).copy(),
            triangolo.get_value_object((5, 5)).copy()
        )
        gruppetto_triangolo.target = eq2[0][:3]

        self.play(
            MoveToTarget(gruppetto_triangolo),
            MoveToTarget(gruppetto_tartaglia)
        )
        self.play(Write(eq2[0][3]))

        totale = triangolo.get_value_object((4, 4)).copy()
        totale.target = eq2[0][4]
        self.play(MoveToTarget(totale))
        self.cut_and_wait()

        self.togli_evidenzia(backs_tartaglia)
        self.togli_evidenzia(back_triangolo)
        self.cut_and_wait()

        #################

        back_triangolo = self.evidenzia(triangolo, (3, 2), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4))
        backs_tartaglia = self.evidenzia(tartaglia, (0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))
        self.cut_and_wait()

        gruppetto_tartaglia = VGroup(
            tartaglia.get_value_object((2, 0)).copy(),
            tartaglia.get_value_object((2, 1)).copy(),
            tartaglia.get_value_object((2, 2)).copy()
        )
        gruppetto_tartaglia.target = eq3[0][:6]

        gruppetto_triangolo = VGroup(
            triangolo.get_value_object((5, 2)).copy(),
            triangolo.get_value_object((5, 3)).copy(),
            triangolo.get_value_object((5, 4)).copy()
        )
        gruppetto_triangolo.target = eq3[0][:6]

        self.play(
            MoveToTarget(gruppetto_triangolo),
            MoveToTarget(gruppetto_tartaglia)
        )
        self.play(Write(eq3[0][6]))

        totale = triangolo.get_value_object((3, 2)).copy()
        totale.target = eq3[0][7:]
        self.play(MoveToTarget(totale))
        self.cut_and_wait()

        self.togli_evidenzia(backs_tartaglia)
        self.togli_evidenzia(back_triangolo)
        self.cut_and_wait()

        #################

        back_triangolo = self.evidenzia(triangolo, (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (5, 3))
        backs_tartaglia = self.evidenzia(tartaglia, (0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3))
        self.cut_and_wait()

        gruppetto_tartaglia = VGroup(
            tartaglia.get_value_object((3, 0)).copy(),
            tartaglia.get_value_object((3, 1)).copy(),
            tartaglia.get_value_object((3, 2)).copy(),
            tartaglia.get_value_object((3, 3)).copy()
        )
        gruppetto_tartaglia.target = eq4[0][:9]

        gruppetto_triangolo = VGroup(
            triangolo.get_value_object((5, 0)).copy(),
            triangolo.get_value_object((5, 1)).copy(),
            triangolo.get_value_object((5, 2)).copy(),
            triangolo.get_value_object((5, 3)).copy(),
        )
        gruppetto_triangolo.target = eq4[0][:9]

        self.play(
            MoveToTarget(gruppetto_triangolo),
            MoveToTarget(gruppetto_tartaglia)
        )
        self.play(Write(eq4[0][9]))

        totale = triangolo.get_value_object((2, 0)).copy()
        totale.target = eq4[0][10:]
        self.play(MoveToTarget(totale))
        self.cut_and_wait()

        self.togli_evidenzia(backs_tartaglia)
        self.togli_evidenzia(back_triangolo)
        self.cut_and_wait()

        #################

        back_triangolo = self.evidenzia(triangolo,
                                        (0, 0),
                                        (1, 0), (1, 1),
                                        (2, 0), (2, 1), (2, 2),
                                        (3, 0), (3, 1), (3, 2), (3, 3),
                                        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
                                        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5))
        backs_tartaglia = self.evidenzia(tartaglia,
                                         (0, 0),
                                         (1, 0), (1, 1),
                                         (2, 0), (2, 1), (2, 2),
                                         (3, 0), (3, 1), (3, 2), (3, 3),
                                         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
                                         (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5))
        self.cut_and_wait()

        gruppetto_tartaglia = VGroup(
            tartaglia.get_value_object((5, 0)).copy(),
            tartaglia.get_value_object((5, 1)).copy(),
            tartaglia.get_value_object((5, 2)).copy(),
            tartaglia.get_value_object((5, 3)).copy(),
            tartaglia.get_value_object((5, 4)).copy(),
            tartaglia.get_value_object((5, 5)).copy(),
        )
        gruppetto_tartaglia.target = eq5[0][:17]

        gruppetto_triangolo = VGroup(
            triangolo.get_value_object((5, 0)).copy(),
            triangolo.get_value_object((5, 1)).copy(),
            triangolo.get_value_object((5, 2)).copy(),
            triangolo.get_value_object((5, 3)).copy(),
            triangolo.get_value_object((5, 4)).copy(),
            triangolo.get_value_object((5, 5)).copy(),
        )
        gruppetto_triangolo.target = eq5[0][:17]

        self.play(
            MoveToTarget(gruppetto_triangolo),
            MoveToTarget(gruppetto_tartaglia)
        )
        self.play(Write(eq5[0][17]))

        totale = triangolo.get_value_object((0, 0)).copy()
        totale.target = eq5[0][18:]
        self.play(MoveToTarget(totale))
        self.cut_and_wait()

        self.togli_evidenzia(backs_tartaglia)
        self.togli_evidenzia(back_triangolo)
        self.cut_and_wait()

        self.play(Write(sistema.bracket))
        self.cut_and_wait()

        self.play(self.camera.frame.animate.move_to(triangolo).scale(.5))

        o1 = triangolo.get_value_object((5, 1))
        n1 = triangolo.put_value((5, 1), 2, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(o1, n1))
        o1 = triangolo.get_value_object((5, 2))
        n1 = triangolo.put_value((5, 2), 4, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(o1, n1))
        o1 = triangolo.get_value_object((5, 3))
        n1 = triangolo.put_value((5, 3), 5, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(o1, n1))
        o1 = triangolo.get_value_object((5, 4))
        n1 = triangolo.put_value((5, 4), 3, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(o1, n1))
        o1 = triangolo.get_value_object((5, 5))
        n1 = triangolo.put_value((5, 5), 1, value_scale=1, value_color=YELLOW)
        self.play(ReplacementTransform(o1, n1))

        self.sum(triangolo, (4, 0))
        self.sum(triangolo, (4, 2))
        self.sum(triangolo, (4, 3))
        self.sum(triangolo, (3, 0))
        self.sum(triangolo, (3, 1))
        self.sum(triangolo, (3, 3))
        self.sum(triangolo, (2, 1))
        self.sum(triangolo, (2, 2))
        self.sum(triangolo, (1, 0))
        self.sum(triangolo, (1, 1))

        self.wait(30)
