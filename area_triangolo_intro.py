from manim import *

DELAY = 1


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
        self.cut_and_wait()

        # seconda frase

        tic1 = Tex("/").set_color(RED).scale(.7).move_to(D_E)
        tic2 = Tex("/").set_color(RED).scale(.7).move_to(E_EE)
        self.play(
            Create(VGroup(E_EE, dotEE, tic1, tic2)),
            Write(letteraEE)
        )
        self.cut_and_wait()

        # terza frase

        tic1 = Tex("//").set_color(GREEN).scale(.7).move_to(E_F).rotate(E_F.get_angle())
        tic2 = Tex("//").set_color(GREEN).scale(.7).move_to(F_FF).rotate(F_FF.get_angle())
        self.play(
            Create(VGroup(F_FF, dotFF, tic1, tic2)),
            Write(letteraFF)
        )
        self.cut_and_wait()

        # quarta frase

        tic1 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(F_D).rotate(F_D.get_angle())
        tic2 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(
            Line(start=dotD.get_center(), end=dotDDD.get_center())).rotate(D_DD.get_angle())
        tic3 = Tex("$\sim$").stretch_to_fit_width(.2).set_color(BLUE).scale(2).move_to(
            Line(start=dotDDD.get_center(), end=dotDD.get_center())).rotate(D_DD.get_angle())
        self.play(
            Create(VGroup(D_DD, dotDDD, dotDD, tic1, tic2, tic3)),
            Write(letteraDD)
        )
        self.cut_and_wait()

        # quinta frase

        self.play(Create(VGroup(DD_EE, EE_FF, FF_DD)))

        self.wait(30)
