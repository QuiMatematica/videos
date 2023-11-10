from manim import *

DELAY = 30


class Scene(ThreeDScene):

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def construct(self):
        self.wait(.5)

        phi = 75 * DEGREES
        self.set_camera_orientation(phi=phi, theta=-90 * DEGREES)

        pavimento = -.65
        pos_alessio = 6 * LEFT
        pos_bruno = 6 * RIGHT

        vel_alessio = 6
        vel_bruno = 4
        vel_scale = .4

        # axes = ThreeDAxes()
        # x_label = axes.get_x_axis_label("x")
        # y_label = axes.get_y_axis_label("y")
        # z_label = axes.get_z_axis_label("z")
        # self.add(axes, x_label, y_label, z_label)

        axes = Axes(x_range=[-1, 13], y_range=[-2, 2], x_length=14, y_length=4).set_color(YELLOW).shift(pavimento * OUT)

        base = Surface(
            lambda u, v: np.array([u, v, pavimento]), u_range=[-8, 8], v_range=[-1, 1],
            resolution=(16, 3)
        )
        self.add(base)

        alza_nome = .9
        scala_omini = .1

        alessio = ImageMobject('../../img/omini/alessio.png').scale(scala_omini).shift(pos_alessio).rotate(-phi, axis=RIGHT)
        bruno = ImageMobject('../../img/omini/bruno.png').scale(scala_omini).shift(pos_bruno).rotate(-phi, axis=RIGHT)

        def get_nome_alessio():
            return Tex("A", color=YELLOW).next_to(alessio, UP).shift(alza_nome * OUT).rotate(phi, axis=RIGHT)

        def get_nome_bruno():
            return Tex("B", color=YELLOW).next_to(bruno, UP).shift(alza_nome * OUT).rotate(phi, axis=RIGHT)

        nome_alessio = get_nome_alessio()
        nome_bruno = get_nome_bruno()

        self.play(FadeIn(alessio), Write(nome_alessio), FadeIn(bruno), Write(nome_bruno))

        self.play(Create(axes))

        cala_distanza = .7

        distanza = DoubleArrow(
            start=pos_alessio + (pavimento - cala_distanza) * OUT,
            end=pos_bruno + (pavimento - cala_distanza) * OUT,
            color=GREEN,
            buff=0)
        lunghezza_distanza = Tex("600 m", color=GREEN).next_to(distanza, DOWN, buff=.5).rotate(phi, axis=RIGHT)
        self.play(Create(distanza), Write(lunghezza_distanza))

        alza_vettori = 0.2

        def get_vettore_alessio():
            return Arrow(
                start=alessio.get_center(),
                end=alessio.get_center() + vel_alessio * vel_scale * RIGHT,
                color=RED,
                buff=0).shift(alza_vettori * OUT).rotate(phi, axis=RIGHT)

        def get_vettore_bruno():
            return Arrow(
                start=bruno.get_center(),
                end=bruno.get_center() + vel_bruno * vel_scale * LEFT,
                color=RED,
                buff=0).shift(alza_vettori * OUT).rotate(phi, axis=RIGHT)

        def get_velocita_alessio():
            return Tex("6 km/h", color=RED).next_to(vettore_alessio, UP, buff=1.1).rotate(phi, axis=RIGHT)

        def get_velocita_bruno():
            return Tex("4 km/h", color=RED).next_to(vettore_bruno, UP, buff=1.1).rotate(phi, axis=RIGHT)

        vettore_alessio = get_vettore_alessio()
        vettore_bruno = get_vettore_bruno()
        velocita_alessio = get_velocita_alessio()
        velocita_bruno = get_velocita_bruno()
        self.play(Create(vettore_alessio), Write(velocita_alessio))
        self.play(Create(vettore_bruno), Write(velocita_bruno))

        timer = ValueTracker(0)

        def get_orologio():
            seconds = timer.get_value()
            minutes = seconds / 60
            seconds = seconds % 60
            return Tex("%d min, %d s" % (minutes, seconds)).shift(3 * OUT).rotate(phi, axis=RIGHT)

        orologio = get_orologio()
        self.play(Write(orologio))
        self.cut_and_wait()

        scala_percorsi = (pos_bruno[0] - pos_alessio[0]) / 600

        orologio.add_updater(
            lambda old: old.become(get_orologio())
        )
        alessio.add_updater(
            lambda old: old.move_to(pos_alessio + vel_alessio / 3.6 * timer.get_value() * scala_percorsi * RIGHT)
        )
        nome_alessio.add_updater(
            lambda old: old.become(get_nome_alessio())
        )
        bruno.add_updater(
            lambda old: old.move_to(pos_bruno + vel_bruno / 3.6 * timer.get_value() * scala_percorsi * LEFT)
        )
        nome_bruno.add_updater(
            lambda old: old.become(get_nome_bruno())
        )
        vettore_alessio.add_updater(
            lambda old: old.become(get_vettore_alessio())
        )
        vettore_bruno.add_updater(
            lambda old: old.become(get_vettore_bruno())
        )
        velocita_alessio.add_updater(
            lambda old: old.become(get_velocita_alessio())
        )
        velocita_bruno.add_updater(
            lambda old: old.become(get_velocita_bruno())
        )

        self.play(timer.animate.set_value(216), run_time=5, rate_func=linear)

        orologio.clear_updaters()
        alessio.clear_updaters()
        bruno.clear_updaters()
        nome_alessio.clear_updaters()
        nome_bruno.clear_updaters()
        vettore_alessio.clear_updaters()
        vettore_bruno.clear_updaters()
        velocita_alessio.clear_updaters()
        velocita_bruno.clear_updaters()

        self.wait(30)
