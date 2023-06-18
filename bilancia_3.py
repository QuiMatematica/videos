from manim import *


class Scene(MovingCameraScene):

    def construct(self):
        delay = 1
        move_camera = False

        self.wait(delay)

        lettere = [
            Tex("$M$", " = ", "M", "ele"),
            Tex("$P$", " = ", "P", "ere"),
            Tex("$A$", " = ", "A", "lbicocche"),
            Tex("$S$", " = anana", "S")
        ]
        lettere[0][0].set_color(YELLOW)
        lettere[0][2].set_color(YELLOW)
        lettere[1][0].set_color(RED)
        lettere[1][2].set_color(RED)
        lettere[2][0].set_color(GREEN)
        lettere[2][2].set_color(GREEN)
        lettere[3][0].set_color(BLUE)
        lettere[3][2].set_color(BLUE)

        bilancia_sinistra = [
            MathTex(r"2S + 3M + 2P = 2S + 2M + 8A"),
            MathTex(r"1M + 2P = 8A")
        ]
        bilancia_sinistra[0][0][1].set_color(BLUE)
        bilancia_sinistra[0][0][4].set_color(YELLOW)
        bilancia_sinistra[0][0][7].set_color(RED)
        bilancia_sinistra[0][0][10].set_color(BLUE)
        bilancia_sinistra[0][0][13].set_color(YELLOW)
        bilancia_sinistra[0][0][16].set_color(GREEN)
        bilancia_sinistra[1][0][1].set_color(YELLOW)
        bilancia_sinistra[1][0][4].set_color(RED)
        bilancia_sinistra[1][0][7].set_color(GREEN)

        bilancia_destra = [
            MathTex(r"2S + 2M + 3P = 2S + 1M + 10A"),
            MathTex(r"1M + 3P = 10A")
        ]
        bilancia_destra[0][0][1].set_color(BLUE)
        bilancia_destra[0][0][4].set_color(YELLOW)
        bilancia_destra[0][0][7].set_color(RED)
        bilancia_destra[0][0][10].set_color(BLUE)
        bilancia_destra[0][0][13].set_color(YELLOW)
        bilancia_destra[0][0][17].set_color(GREEN)
        bilancia_destra[1][0][1].set_color(YELLOW)
        bilancia_destra[1][0][4].set_color(RED)
        bilancia_destra[1][0][8].set_color(GREEN)

        riduzione = [
            MathTex(r"1M + 3P - (1M + 2P) = 10A - (8A)"),
            MathTex(r"1P = 2A")
        ]
        riduzione[0][0][1].set_color(YELLOW)
        riduzione[0][0][4].set_color(RED)
        riduzione[0][0][8].set_color(YELLOW)
        riduzione[0][0][11].set_color(RED)
        riduzione[0][0][16].set_color(GREEN)
        riduzione[0][0][20].set_color(GREEN)
        riduzione[1][0][1].set_color(RED)
        riduzione[1][0][4].set_color(GREEN)

        VGroup(
            VGroup(*lettere).arrange(DOWN),
            VGroup(
                VGroup(*bilancia_sinistra).scale(.8).arrange(DOWN),
                VGroup(*bilancia_destra).scale(.8).arrange(DOWN)).arrange(RIGHT, buff=1),
            VGroup(*riduzione).arrange(DOWN)).arrange(DOWN, buff=1)

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

        # if move_camera:
        #     self.play(self.camera.frame.animate.scale(.5))
        # for _i in range(3):
        #     if move_camera:
        #         self.play(self.camera.frame.animate.move_to(bilancia_sinistra[_i]))
        #     self.play(Write(bilancia_sinistra[_i]))
        #     self.wait(delay)
        #     self.next_section()
        #     if move_camera:
        #         self.play(self.camera.frame.animate.move_to(bilancia_destra[_i]))
        #     self.play(Write(bilancia_destra[_i]))
        #     self.wait(delay)
        #     self.next_section()
        # if move_camera:
        #     self.play(self.camera.frame.animate.move_to(ORIGIN).scale(2))
        # self.wait(delay)
        # self.next_section()

        blocchi = [
            bilancia_destra[1][0][:5].copy(),
            bilancia_destra[1][0][6:].copy(),
            bilancia_sinistra[1][0][:5].copy(),
            bilancia_sinistra[1][0][6:].copy()
        ]
        blocchi[0].target = riduzione[0][0][:5]
        blocchi[1].target = riduzione[0][0][14:17]
        blocchi[2].target = riduzione[0][0][7:12]
        blocchi[3].target = riduzione[0][0][19:21]

        self.play(MoveToTarget(blocchi[0]))
        self.play(Write(riduzione[0][0][13]))
        self.play(MoveToTarget(blocchi[1]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[0][0][5:7]), Write(riduzione[0][0][12]))
        self.play(Write(riduzione[0][0][17:19]), Write(riduzione[0][0][21]))
        self.wait(delay)
        self.next_section()
        self.play(MoveToTarget(blocchi[2]))
        self.play(MoveToTarget(blocchi[3]))
        self.wait(delay)
        self.next_section()
        self.play(Write(riduzione[1]))

        self.wait(30)
