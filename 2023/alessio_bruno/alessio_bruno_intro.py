from manim import *

DELAY = 15


class Scene(ThreeDScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        phi = 75 * DEGREES
        self.set_camera_orientation(phi=phi, theta=-90 * DEGREES)

        pavimento = -1.8
        pos_alessio = 6*LEFT
        pos_bruno = 6*RIGHT

        vel_alessio = 6
        vel_bruno = 4
        vel_scale = .8

        # axes = ThreeDAxes()
        # x_label = axes.get_x_axis_label("x")
        # y_label = axes.get_y_axis_label("y")
        # z_label = axes.get_z_axis_label("z")
        # self.add(axes, x_label, y_label, z_label)

        base = Surface(
            lambda u, v: np.array([u, v, pavimento]), u_range=[-8, 8], v_range=[-1, 1],
            resolution=(16, 3)
        )
        self.add(base)

        alza_nome = 2.3

        alessio = ImageMobject('../../img/omini/alessio.png').scale(.3).shift(pos_alessio).rotate(-phi, axis=RIGHT)
        nome_alessio = Tex("Alessio", color=YELLOW).next_to(alessio, UP).shift(alza_nome*OUT).rotate(phi, axis=RIGHT)
        bruno = ImageMobject('../../img/omini/bruno.png').scale(.3).shift(pos_bruno).rotate(-phi, axis=RIGHT)
        nome_bruno = Tex("Bruno", color=YELLOW).next_to(bruno, UP).shift(alza_nome*OUT).rotate(phi, axis=RIGHT)

        self.play(FadeIn(alessio), Write(nome_alessio))
        self.play(FadeIn(bruno), Write(nome_bruno))
        self.cut_and_wait()

        cala_distanza = .7

        distanza = DoubleArrow(
            start=pos_alessio + (pavimento - cala_distanza) * OUT,
            end=pos_bruno + (pavimento - cala_distanza) * OUT,
            color=GREEN,
            buff=0)
        lunghezza_distanza = Tex("600 m", color=GREEN).next_to(distanza, DOWN, buff=.5).rotate(phi, axis=RIGHT)
        self.play(Create(distanza))
        self.play(Write(lunghezza_distanza))
        self.cut_and_wait()

        alza_vettori = 0.9

        vettore_alessio = Arrow(
            start=pos_alessio,
            end=pos_alessio + vel_alessio * vel_scale * RIGHT,
            color=RED,
            buff=0).shift(alza_vettori * OUT).rotate(phi, axis=RIGHT)
        vettore_bruno = Arrow(
            start=pos_bruno,
            end=pos_bruno + vel_bruno * vel_scale * LEFT,
            color=RED,
            buff=0).shift(alza_vettori * OUT).rotate(phi, axis=RIGHT)
        velocita_alessio = Tex("6 km/h", color=RED).next_to(vettore_alessio, UP, buff=1.1).rotate(phi, axis=RIGHT)
        velocita_bruno = Tex("4 km/h", color=RED).next_to(vettore_bruno, UP, buff=1.1).rotate(phi, axis=RIGHT)
        self.play(Create(vettore_alessio))
        self.play(Write(velocita_alessio))
        self.play(Create(vettore_bruno))
        self.play(Write(velocita_bruno))

        self.wait(30)
