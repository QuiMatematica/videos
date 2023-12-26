from manim import *

DELAY = 30

SCALE = 2


class Scene(MovingCameraScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def togli_radice(self, source, destination):
        destination[0][1].set_color(RED)
        self.play(
            FadeOut(source[0][:4]),
            source[0][4].animate.move_to(destination[0][0]),
            source[0][5].animate.move_to(destination[0][1]),
        )
        self.add(destination)
        self.remove(source[0][4])
        self.remove(source[0][5])
        self.cut_and_wait()

    def moltiplica_indice(self, source, destination):
        cp = source
        tg = destination
        tg[0][0:2].set_color(RED)
        tg[0][5].set_color(RED)
        self.play(
            ReplacementTransform(cp[0][0:3], tg[0][0:2]),
            FadeOut(cp[0][6:8]),
            ReplacementTransform(cp[0][3:5], tg[0][2:4]),
            cp[0][5].animate.move_to(tg[0][4]),
            cp[0][8].animate.move_to(tg[0][5]),
        )
        self.add(tg)
        self.remove(cp[0][5])
        self.remove(cp[0][8])
        self.cut_and_wait()

    def applica_invariantiva(self, source, destination):
        cp = source.copy()
        self.play(cp.animate.move_to(destination))
        tg = destination
        self.play(
            cp[0][0].animate.move_to(tg[0][0]),
            ReplacementTransform(cp[0][1:3], tg[0][3:5]),
            cp[0][3].animate.move_to(tg[0][5]),
            cp[0][4].animate.move_to(tg[0][6]),
        )
        self.play(
            Write(tg[0][1:3]),
            Write(tg[0][7:])
        )
        self.add(tg)
        self.remove(cp[0][0])
        self.remove(cp[0][3])
        self.remove(cp[0][4])
        self.cut_and_wait()

    def applica_invariantiva_n(self, source, destination):
        cp = source.copy()
        self.play(cp.animate.move_to(destination))
        tg = destination
        self.play(
            cp[0][0].animate.move_to(tg[0][0]),
            ReplacementTransform(cp[0][1:3], tg[0][3:5]),
            cp[0][3].animate.move_to(tg[0][5]),
            Write(tg[0][6]),
        )
        self.cut_and_wait()

        tg[0][1:3].set_color(RED)
        self.play(Write(tg[0][1:3]))
        self.cut_and_wait()

        tg[0][7:].set_color(RED)
        self.play(Write(tg[0][7:]))
        self.add(tg)
        self.remove(cp[0][0])
        self.remove(cp[0][3])
        self.cut_and_wait()

    def applica_invariantiva_2(self, source, destination):
        cp = source.copy()
        self.play(cp.animate.move_to(destination))
        tg = destination
        self.play(
            Write(tg[0][0]),
            ReplacementTransform(cp[0][0:2], tg[0][3:5]),
            cp[0][2].animate.move_to(tg[0][5]),
            Write(tg[0][6]),
        )
        self.cut_and_wait()

        tg[0][1:3].set_color(RED)
        self.play(Write(tg[0][1:3]))
        self.cut_and_wait()

        tg[0][7:].set_color(RED)
        self.play(Write(tg[0][7:]))
        self.add(tg)
        self.remove(cp[0][2])
        self.cut_and_wait()

    def construct(self):
        self.wait(.5)

        radicali = VGroup(
            MathTex(r"\sqrt{2}").scale(SCALE),
            MathTex(r"\sqrt[4]{3}").scale(SCALE),
            MathTex(r"\sqrt[3]{4}").scale(SCALE)
        ).arrange(RIGHT, buff=3).to_edge(UP)

        self.play(Write(radicali))

        proprieta_invariantiva = VGroup(
            Tex("Proprietà invariantiva:", color=GREEN),
            MathTex(r"\forall a \ge 0; \forall m, n, p \in \mathbb{N} - \{0\}"),
            VGroup(
                MathTex(r"\sqrt[n]{a^m}"),
                MathTex(r"="),
                MathTex(r"\sqrt[n \cdot p]{a^{m \cdot p}}")
            ).arrange(RIGHT)
        ).scale(SCALE).arrange(DOWN).shift(DOWN)
        proprieta_invariantiva[1][0][10].set_color(RED)
        proprieta_invariantiva[2][2][0][1:3].set_color(RED)
        proprieta_invariantiva[2][2][0][7:9].set_color(RED)

        self.play(Write(proprieta_invariantiva[0]))
        self.play(Write(proprieta_invariantiva[1]))
        self.play(Write(proprieta_invariantiva[2][0:2]))

        self.applica_invariantiva(proprieta_invariantiva[2][0], proprieta_invariantiva[2][2])

        self.play(FadeOut(proprieta_invariantiva))
        minimo_comune_multiplo = Tex("minimo comune multiplo").scale(SCALE)
        self.play(Write(minimo_comune_multiplo[0][12:]))
        self.cut_and_wait()
        self.play(Write(minimo_comune_multiplo[0][6:12]))
        self.cut_and_wait()
        self.play(Write(minimo_comune_multiplo[0][:6]))
        self.cut_and_wait()

        mcm = Tex("mcm").scale(SCALE).move_to(minimo_comune_multiplo)
        self.play(Unwrite(minimo_comune_multiplo[0][13:]))
        self.play(Unwrite(minimo_comune_multiplo[0][7:12]))
        self.play(Unwrite(minimo_comune_multiplo[0][1:6]))
        self.play(
            minimo_comune_multiplo[0][0].animate.move_to(mcm[0][0]),
            minimo_comune_multiplo[0][6].animate.move_to(mcm[0][1]),
            minimo_comune_multiplo[0][12].animate.move_to(mcm[0][2])
        )
        self.add(mcm)
        self.remove(
            minimo_comune_multiplo[0][0],
            minimo_comune_multiplo[0][6],
            minimo_comune_multiplo[0][12],
        )
        self.cut_and_wait()

        mcm_calcolo = Tex("mcm(2, 4, 3) = 12").scale(SCALE).move_to(mcm)
        self.play(mcm.animate.move_to(mcm_calcolo[0][:3]))
        self.play(
            Write(mcm_calcolo[0][3]),
            Write(mcm_calcolo[0][5]),
            Write(mcm_calcolo[0][7]),
            Write(mcm_calcolo[0][9]),
        )
        c1 = radicali[0][0][0].copy()
        c1.target = mcm_calcolo[0][4]
        c2 = radicali[1][0][0].copy()
        c2.target = mcm_calcolo[0][6]
        c3 = radicali[2][0][0].copy()
        c3.target = mcm_calcolo[0][8]
        self.play(
            MoveToTarget(c1),
            MoveToTarget(c2),
            MoveToTarget(c3),
        )
        self.play(Write(mcm_calcolo[0][10:]))
        self.add(mcm_calcolo)
        self.remove(mcm, c1, c2, c3)
        self.cut_and_wait()

        self.play(mcm_calcolo.animate.to_edge(DOWN))
        self.cut_and_wait()

        radicali_2 = VGroup(
            MathTex(r"\sqrt[2 \cdot 6]{2^{1 \cdot 6}}").scale(SCALE),
            MathTex(r"\sqrt[4 \cdot 3]{3^{1 \cdot 3}}").scale(SCALE),
            MathTex(r"\sqrt[3 \cdot 4]{4^{1 \cdot 4}}").scale(SCALE)
        )
        for _i in range(3):
            radicali_2[_i].shift(radicali[_i].get_center()[0] * RIGHT)

        radicali_3 = VGroup(
            MathTex(r"\sqrt[12]{2^6}").scale(SCALE),
            MathTex(r"\sqrt[12]{3^3}").scale(SCALE),
            MathTex(r"\sqrt[12]{4^4}").scale(SCALE)
        )
        for _i in range(3):
            radicali_3[_i].move_to(radicali_2[_i])

        self.applica_invariantiva_2(radicali[0], radicali_2[0])
        self.moltiplica_indice(radicali_2[0], radicali_3[0])
        self.applica_invariantiva_n(radicali[1], radicali_2[1])
        self.moltiplica_indice(radicali_2[1], radicali_3[1])
        self.applica_invariantiva_n(radicali[2], radicali_2[2])
        self.moltiplica_indice(radicali_2[2], radicali_3[2])

        self.play(FadeOut(mcm_calcolo))
        confronto = MathTex(r"\sqrt[n]{a} < \sqrt[n]{b} \quad\Longleftrightarrow\quad a < b").scale(SCALE).to_edge(DOWN)
        self.play(Write(confronto))
        self.cut_and_wait()

        radicali_4 = VGroup(
            MathTex(r"2^6").scale(SCALE),
            MathTex(r"3^3").scale(SCALE),
            MathTex(r"4^4").scale(SCALE)
        )
        for _i in range(3):
            radicali_4[_i].move_to(radicali_3[_i])
            self.togli_radice(radicali_3[_i], radicali_4[_i])

        radicali_5 = VGroup(
            MathTex(r"64").scale(SCALE),
            MathTex(r"27").scale(SCALE),
            MathTex(r"256").scale(SCALE)
        )
        for _i in range(3):
            radicali_5[_i].move_to(radicali_4[_i])
            self.play(ReplacementTransform(radicali_4[_i], radicali_5[_i]))
            self.cut_and_wait()

        self.play(
            MoveAlongPath(radicali[0], ArcBetweenPoints(start=radicali[0].get_center(), end=radicali[1].get_center())),
            MoveAlongPath(radicali_5[0], ArcBetweenPoints(start=radicali_5[0].get_center(), end=radicali_5[1].get_center())),
            MoveAlongPath(radicali[1], ArcBetweenPoints(start=radicali[1].get_center(), end=radicali[0].get_center())),
            MoveAlongPath(radicali_5[1], ArcBetweenPoints(start=radicali_5[1].get_center(), end=radicali_5[0].get_center())),
            Write(MathTex("<").scale(SCALE).move_to((radicali[0].get_center() + radicali[1].get_center())/2)),
            Write(MathTex("<").scale(SCALE).move_to((radicali_5[0].get_center() + radicali_5[1].get_center())/2)),
        )
        self.cut_and_wait()

        self.play(
            Write(MathTex("<").scale(SCALE).move_to((radicali[0].get_center() + radicali[2].get_center()) / 2)),
            Write(MathTex("<").scale(SCALE).move_to((radicali_5[0].get_center() + radicali_5[2].get_center()) / 2)),
        )
        self.cut_and_wait()

        self.play(Create(SurroundingRectangle(radicali, buff=.4)))

        self.wait(30)

