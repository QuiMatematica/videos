from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 30

        self.wait(.5)

        lettere = [
            Tex("$M$", " = ", "$M$", "elanzane"),
            Tex("$A$", " = c", "$A$", "rote"),
            Tex("$I$", " = c", "$I$", "polle")
        ]
        lettere[0][0].set_color(YELLOW)
        lettere[0][2].set_color(YELLOW)
        lettere[1][0].set_color(BLUE)
        lettere[1][2].set_color(BLUE)
        lettere[2][0].set_color(RED)
        lettere[2][2].set_color(RED)

        bilancia_sinistra = [
            MathTex(r"5M + 2A + 3I = 4M + 8A + 2I"),
            MathTex(r"1M + 1I = 6A")
        ]
        bilancia_sinistra[0][0][1].set_color(YELLOW)
        bilancia_sinistra[0][0][4].set_color(BLUE)
        bilancia_sinistra[0][0][7].set_color(RED)
        bilancia_sinistra[0][0][10].set_color(YELLOW)
        bilancia_sinistra[0][0][13].set_color(BLUE)
        bilancia_sinistra[0][0][16].set_color(RED)
        bilancia_sinistra[1][0][1].set_color(YELLOW)
        bilancia_sinistra[1][0][4].set_color(RED)
        bilancia_sinistra[1][0][7].set_color(BLUE)

        bilancia_destra = [
            MathTex(r"5M + 6A = 4M + 4A + 3I"),
            MathTex(r"1M + 2A = 3I"),
            MathTex(r"3M + 6A = 9I")
        ]
        bilancia_destra[0][0][1].set_color(YELLOW)
        bilancia_destra[0][0][4].set_color(BLUE)
        bilancia_destra[0][0][7].set_color(YELLOW)
        bilancia_destra[0][0][10].set_color(BLUE)
        bilancia_destra[0][0][13].set_color(RED)
        bilancia_destra[1][0][1].set_color(YELLOW)
        bilancia_destra[1][0][4].set_color(BLUE)
        bilancia_destra[1][0][7].set_color(RED)
        bilancia_destra[2][0][1].set_color(YELLOW)
        bilancia_destra[2][0][4].set_color(BLUE)
        bilancia_destra[2][0][7].set_color(RED)

        riduzione = [
            MathTex(r"3M + (1M + 1I) = 9I"),
            MathTex(r"4M + 1I = 9I"),
            MathTex(r"4M = 8I"),
            MathTex(r"1M = 2I")
        ]
        riduzione[0][0][1].set_color(YELLOW)
        riduzione[0][0][5].set_color(YELLOW)
        riduzione[0][0][8].set_color(RED)
        riduzione[0][0][12].set_color(RED)
        riduzione[1][0][1].set_color(YELLOW)
        riduzione[1][0][4].set_color(RED)
        riduzione[1][0][7].set_color(RED)
        riduzione[2][0][1].set_color(YELLOW)
        riduzione[2][0][4].set_color(RED)
        riduzione[3][0][1].set_color(YELLOW)
        riduzione[3][0][4].set_color(RED)

        VGroup(
            VGroup(*lettere).arrange(DOWN),
            VGroup(
                VGroup(*bilancia_sinistra).scale(.8).arrange(DOWN),
                VGroup(*bilancia_destra).scale(.8).arrange(DOWN)).arrange(RIGHT, buff=1, aligned_edge=UP),
            VGroup(*riduzione).arrange(DOWN)).arrange(DOWN, buff=.8)

        for _l in lettere:
            self.play(Write(_l))
            self.wait(delay)
            self.next_section()

        self.play(Write(bilancia_sinistra[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(bilancia_destra[0]))
        self.wait(delay)
        self.next_section()

        self.play(Write(bilancia_sinistra[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(bilancia_destra[1]))
        self.wait(delay)
        self.next_section()

        self.play(Write(bilancia_destra[2]))
        self.wait(delay)
        self.next_section()

        blocchi = [
            bilancia_destra[2][0][:3].copy(),
            bilancia_destra[2][0][5:].copy(),
            bilancia_sinistra[1][0][:5].copy()
        ]
        blocchi[0].target = riduzione[0][0][:3]
        blocchi[1].target = riduzione[0][0][10:]
        blocchi[2].target = riduzione[0][0][4:9]

        self.play(MoveToTarget(blocchi[0]))
        self.play(MoveToTarget(blocchi[1]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[0][0][3]), Write(riduzione[0][0][9]))
        self.wait(delay)
        self.next_section()
        self.play(MoveToTarget(blocchi[2]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[1]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[2]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[3]))

        self.wait(30)
