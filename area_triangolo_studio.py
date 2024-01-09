from manim import *

DELAY = 1

STROKE = 8


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        d_coordinates = [0, 0, 0]
        e_coordinates = [3, 0, 0]
        f_coordinates = [1, 1.7, 0]

        EE = [2 * e_coordinates[0] - d_coordinates[0], 2 * e_coordinates[1] - d_coordinates[1], 0]
        FF = [2 * f_coordinates[0] - e_coordinates[0], 2 * f_coordinates[1] - e_coordinates[1], 0]
        DD = [3 * d_coordinates[0] - 2 * f_coordinates[0], 3 * d_coordinates[1] - 2 * f_coordinates[1], 0]
        DDD = [2 * d_coordinates[0] - f_coordinates[0], 2 * d_coordinates[1] - f_coordinates[1], 0]

        dotD = Dot(d_coordinates)
        dotE = Dot(e_coordinates)
        dotF = Dot(f_coordinates)
        dotDD = Dot(DD)
        dotEE = Dot(EE)
        dotFF = Dot(FF)
        dotDDD = Dot(DDD)

        D_E = Line(start=d_coordinates, end=e_coordinates)
        E_F = Line(start=e_coordinates, end=f_coordinates)
        F_D = Line(start=f_coordinates, end=d_coordinates)

        D_EE = Line(start=d_coordinates, end=EE)
        E_FF = Line(start=e_coordinates, end=FF)
        F_DD = Line(start=f_coordinates, end=DD)

        DD_EE = Line(start=DD, end=EE)
        EE_FF = Line(start=EE, end=FF)
        FF_DD = Line(start=FF, end=DD)

        E_EE = Line(start=e_coordinates, end=EE)
        F_FF = Line(start=f_coordinates, end=FF)
        D_DD = Line(start=d_coordinates, end=DD)

        d_label = MathTex("D").next_to(dotD, -D_EE.get_unit_vector() / 5)
        e_label = MathTex("E").next_to(dotE, -E_FF.get_unit_vector() / 5)
        f_label = MathTex("F").next_to(dotF, -F_DD.get_unit_vector() / 5)
        letteraDD = MathTex("D'").next_to(dotDD, F_DD.get_unit_vector() / 5)
        letteraEE = MathTex("E'").next_to(dotEE, D_EE.get_unit_vector() / 5)
        letteraFF = MathTex("F'").next_to(dotFF, E_FF.get_unit_vector() / 5)

        figura = VGroup(D_E, E_F, F_D, D_EE, E_FF, F_DD, DD_EE, EE_FF, FF_DD, E_EE, F_FF, D_DD)
        dots = VGroup(dotD, dotE, dotF, dotDD, dotEE, dotFF, dotDDD)
        lettere = VGroup(d_label, e_label, f_label, letteraDD, letteraEE, letteraFF)
        insieme = VGroup(figura, dots, lettere)
        insieme.move_to(ORIGIN)

        self.play(
            Create(VGroup(dotD, D_E, dotE, E_F, dotF, F_D)),
            Write(d_label),
            Write(e_label),
            Write(f_label)
        )

        triangoloDEF = Polygon(dotD.get_center(), dotE.get_center(), dotF.get_center(), fill_color=DARK_GRAY,
                               fill_opacity=1).set_z_index(-1).set_color(DARK_BLUE)
        area = Tex(r"8 m$^2$", color=WHITE).move_to((dotD.get_center() + dotE.get_center() + dotF.get_center()) / 3)
        self.play(
            Create(triangoloDEF),
            Write(area)
        )

        tic1 = Tex("/").set_color(RED).scale(.7).move_to(D_E)
        tic2 = Tex("/").set_color(RED).scale(.7).move_to(E_EE)
        self.play(
            Create(VGroup(E_EE, dotEE, tic1, tic2)),
            Write(letteraEE)
        )

        tic1 = Tex("//").set_color(GREEN).scale(.7).move_to(E_F).rotate(E_F.get_angle())
        tic2 = Tex("//").set_color(GREEN).scale(.7).move_to(F_FF).rotate(F_FF.get_angle())
        self.play(
            Create(VGroup(F_FF, dotFF, tic1, tic2)),
            Write(letteraFF)
        )

        tic1 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(F_D).rotate(F_D.get_angle())
        tic2 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(
            Line(start=dotD.get_center(), end=dotDDD.get_center())).rotate(D_DD.get_angle())
        tic3 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(
            Line(start=dotDDD.get_center(), end=dotDD.get_center())).rotate(D_DD.get_angle())
        self.play(
            Create(VGroup(D_DD, dotDDD, dotDD, tic1, tic2, tic3)),
            Write(letteraDD)
        )

        self.play(Create(VGroup(DD_EE, EE_FF, FF_DD)))
        self.cut_and_wait()

        E_FF_strong = E_FF.copy().set_color(YELLOW).set_stroke(color=YELLOW, width=STROKE)
        H = D_EE.get_projection(dotF.get_center())
        HH = D_EE.get_projection(dotFF.get_center())
        F_H_strong = DashedLine(start=dotF.get_center(), end=H, dash_length=0.2).set_color(YELLOW).set_stroke(
            color=YELLOW, width=STROKE)
        FF_HH_strong = DashedLine(start=dotFF.get_center(), end=HH, dash_length=0.2).set_color(YELLOW).set_stroke(
            color=YELLOW, width=STROKE)
        E_HH_strong = DashedLine(start=dotE.get_center(), end=HH, dash_length=0.2).set_color(YELLOW).set_stroke(
            color=YELLOW, width=STROKE)

        letteraH = Tex("H", color=YELLOW).next_to(Dot(H), DOWN)
        letteraHH = Tex("H'", color=YELLOW).next_to(Dot(HH), DOWN)

        self.play(Create(F_H_strong), Write(letteraH))
        self.cut_and_wait()

        self.play(Create(FF_HH_strong), Write(letteraHH))
        self.cut_and_wait()

        self.play(Create(E_HH_strong))
        self.cut_and_wait()

        self.play(Create(E_FF_strong))
        self.cut_and_wait()

        b1 = DoubleArrow(start=dotD.get_center(), end=dotE.get_center(), buff=0, color=YELLOW)
        letterab1 = MathTex("b", color=YELLOW).next_to(b1, DOWN, buff=.05)
        b2 = DoubleArrow(start=dotE.get_center(), end=dotEE.get_center(), buff=0, color=YELLOW)
        letterab2 = MathTex("b", color=YELLOW).next_to(b2, DOWN, buff=.05)
        h1 = DoubleArrow(start=dotF.get_center(), end=H, buff=0, color=YELLOW)
        letterah1 = MathTex("h", color=YELLOW).next_to(h1, RIGHT, buff=.05)
        h2 = DoubleArrow(start=dotFF.get_center(), end=HH, buff=0, color=YELLOW)
        letterah2 = MathTex("2h", color=YELLOW).next_to(h2, RIGHT, buff=.05)
        E_EE_FF = Polygon(dotE.get_center(), dotEE.get_center(), dotFF.get_center(), fill_color=GREEN,
                          fill_opacity=1).set_z_index(-1)
        self.play(
            FadeOut(VGroup(E_FF_strong, F_H_strong, FF_HH_strong, E_HH_strong, letteraH, letteraHH)),
            Create(E_EE_FF)
        )
        self.cut_and_wait()
        self.play(Create(b1), Create(b2), Write(letterab1), Write(letterab2))
        self.cut_and_wait()
        self.play(Create(h1), Create(h2), Write(letterah1), Write(letterah2))
        self.cut_and_wait()

        areaE_EE_FF = Tex("16 m$^2$").move_to( (dotE.get_center() + dotEE.get_center() + dotFF.get_center())/3 )
        self.play(Write(areaE_EE_FF))
        self.play(
            FadeOut(E_EE_FF),
            FadeOut(b1),
            FadeOut(b2),
            FadeOut(h1),
            FadeOut(h2),
            FadeOut(letterab1),
            FadeOut(letterab2),
            FadeOut(letterah1),
            FadeOut(letterah2)
            )
        self.cut_and_wait()

        K = F_DD.get_projection(dotE.get_center())
        KK = F_DD.get_projection(dotEE.get_center())

        b1 = DoubleArrow(start=dotF.get_center(), end=dotD.get_center(), buff=0, color=YELLOW)
        letterab1 = MathTex("b", color=YELLOW).move_to(b1.get_center() + .4 * LEFT)
        b2 = DoubleArrow(start=dotD.get_center(), end=dotDD.get_center(), buff=0, color=YELLOW)
        letterab2 = MathTex("2b", color=YELLOW).move_to(b2.get_center() + .4 * LEFT)
        h1 = DoubleArrow(start=dotE.get_center(), end=K, buff=0, color=YELLOW)
        letterah1 = MathTex("h", color=YELLOW).move_to(h1.get_center() + UP / 2)
        h2 = DoubleArrow(start=dotEE.get_center(), end=KK, buff=0.1, color=YELLOW)
        letterah2 = MathTex("2h", color=YELLOW).move_to(h2.get_center() + UP / 2)

        D_DD_EE = Polygon(dotD.get_center(), dotDD.get_center(), dotEE.get_center(), fill_color=GREEN,
                          fill_opacity=1).set_z_index(-1)
        self.play(Create(D_DD_EE))
        self.cut_and_wait()

        self.play(Create(b1), Create(b2), Write(letterab1), Write(letterab2))
        self.cut_and_wait()
        self.play(Create(h1), Create(h2), Write(letterah1), Write(letterah2))
        self.cut_and_wait()

        areaD_DD_EE = Tex("32 m$^2$").move_to( (dotD.get_center() + dotDD.get_center() + dotEE.get_center())/3 )
        self.play(Write(areaD_DD_EE))
        self.play(
            FadeOut(D_DD_EE),
            FadeOut(b1),
            FadeOut(b2),
            FadeOut(h1),
            FadeOut(h2),
            FadeOut(letterab1),
            FadeOut(letterab2),
            FadeOut(letterah1),
            FadeOut(letterah2))
        self.cut_and_wait()

        K = E_FF.get_projection(dotD.get_center())
        KK = E_FF.get_projection(dotDD.get_center())

        b1 = DoubleArrow(start=dotE.get_center(), end=dotF.get_center(), buff=0, color=YELLOW)
        letterab1 = MathTex("b", color=YELLOW).move_to(b1.get_center() + LEFT / 2)
        b2 = DoubleArrow(start=dotF.get_center(), end=dotFF.get_center(), buff=0, color=YELLOW)
        letterab2 = MathTex("b", color=YELLOW).move_to(b2.get_center() + LEFT / 2)
        h1 = DoubleArrow(start=dotD.get_center(), end=K, buff=0, color=YELLOW)
        letterah1 = MathTex("h", color=YELLOW).move_to(h1.get_center() + UP / 2)
        h2 = DoubleArrow(start=dotDD.get_center(), end=KK, buff=0, color=YELLOW)
        letterah2 = MathTex("3h", color=YELLOW).move_to(h2.get_center() + UP / 2)

        F_FF_DD = Polygon(dotF.get_center(), dotFF.get_center(), dotDD.get_center(), fill_color=GREEN,
                          fill_opacity=1).set_z_index(-1)
        self.play(Create(F_FF_DD))
        self.play(Create(b1), Create(b2), Write(letterab1), Write(letterab2))
        self.play(Create(h1), Create(h2), Write(letterah1), Write(letterah2))
        areaF_FF_DD = Tex("24 m$^2$").move_to( (dotF.get_center() + dotFF.get_center() + dotDD.get_center())/3 )
        self.play(Write(areaF_FF_DD))
        self.play(
            FadeOut(F_FF_DD),
            FadeOut(b1),
            FadeOut(b2),
            FadeOut(h1),
            FadeOut(h2),
            FadeOut(letterab1),
            FadeOut(letterab2),
            FadeOut(letterah1),
            FadeOut(letterah2))
        self.cut_and_wait()

        text = Tex("{{8 m$^2$}} + {{16 m$^2$}} + {{32 m$^2$}} + {{24 m$^2$}} = 80 m$^2$").to_edge(DR)
        self.play(
            area.copy().animate.move_to(text[0]),
            areaE_EE_FF.copy().animate.move_to(text[2]),
            areaD_DD_EE.copy().animate.move_to(text[4]),
            areaF_FF_DD.copy().animate.move_to(text[6]),
            Write(text[1]),
            Write(text[3]),
            Write(text[5]))
        self.play(Write(text[7]))

        self.wait(30)
