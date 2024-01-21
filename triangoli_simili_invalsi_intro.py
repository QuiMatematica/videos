from manim import *

DELAY = 1


class Video(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        h_coords = [0, 0, 0]
        a_coords = [0, 4, 0]
        b_coords = [-3, 0, 0]
        c_coords = [3, 0, 0]
        m_coords = [-6/5, 12/5, 0]
        n_coords = [0, 1.5, 0]

        h_dot = Dot(h_coords)
        a_dot = Dot(a_coords)
        b_dot = Dot(b_coords)
        c_dot = Dot(c_coords)
        m_dot = Dot(m_coords)
        n_dot = Dot(n_coords)

        ab_line = Line(a_coords, b_coords)
        bc_line = Line(b_coords, c_coords)
        ca_line = Line(c_coords, a_coords)
        ah_line = DashedLine(a_coords, h_coords)
        mn_line = Line(m_coords, n_coords)

        figura = VGroup(
            a_dot, b_dot, c_dot, h_dot, m_dot, n_dot,
            ab_line, bc_line, ca_line, ah_line, mn_line
        ).move_to(3.5 * LEFT)

        dati = VGroup(
            MathTex(r"AB \cong AC"),
            MathTex(r"BC = 6 \text{ cm}"),
            MathTex(r"AH = 4 \text{ cm}"),
            MathTex(r"AM : MB = 2 : 3")
        ).arrange(DOWN)

        domande = VGroup(
            MathTex(r"AM = \text{ ?}"),
            MathTex(r"AN = \text{ ?}"),
            MathTex(r"MN = \text{ ?}"),
        ).arrange(DOWN)

        testi = VGroup(dati, domande).arrange(DOWN).move_to(3.5 * RIGHT)

        self.play(Create(VGroup(ab_line, bc_line, ca_line)))
        self.play(
            Create(a_dot), Write(MathTex("A").next_to(a_dot, UP)),
            Create(b_dot), Write(MathTex("B").next_to(b_dot, DOWN)),
            Create(c_dot), Write(MathTex("C").next_to(c_dot, DOWN)),
        )
        self.play(Write(dati[0]))
        self.cut_and_wait()

        self.play(Write(dati[1]))
        self.cut_and_wait()

        self.play(
            Create(VGroup(ah_line, h_dot)),
            Write(MathTex("H").next_to(h_dot, DOWN))
        )
        self.play(Write(dati[2]))
        self.cut_and_wait()

        self.play(
            Create(m_dot), Write(MathTex("M").next_to(m_dot, UL, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * .5)),
        )
        self.cut_and_wait()

        self.play(Write(dati[3]))
        self.cut_and_wait()

        self.play(
            Create(VGroup(mn_line, n_dot)),
            Write(MathTex("N").next_to(n_dot, RIGHT)),
            Create(RightAngle(mn_line, ab_line.copy().reverse_direction()))
        )
        self.cut_and_wait()

        self.play(Write(domande))

        self.wait(30)
