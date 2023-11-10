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

        axes = Axes(x_range=[-1, 13], y_range=[-2, 2], x_length=14, y_length=4).set_color(GREEN).rotate(phi, axis=RIGHT)

        def get_pavimento():
            return Surface(
                lambda u, v: np.array([u, v, pavimento]), u_range=[-8, 8], v_range=[-1, 1],
                resolution=(16, 3)
            )

        base = get_pavimento()
        self.add(base)

        alza_nome = .9
        scala_omini = .1

        alessio = ImageMobject('../../img/omini/alessio.png').scale(scala_omini).shift(pos_alessio).rotate(-phi, axis=RIGHT)
        bruno = ImageMobject('../../img/omini/bruno.png').scale(scala_omini).shift(pos_bruno).rotate(-phi, axis=RIGHT)

        def get_nome_alessio():
            return Tex("A", color=YELLOW).next_to(alessio, UP).shift(alza_nome * OUT).shift(.2 * RIGHT).rotate(phi,
                                                                                                               axis=RIGHT)

        def get_nome_bruno():
            return Tex("B", color=YELLOW).next_to(bruno, UP).shift(alza_nome * OUT).rotate(phi, axis=RIGHT)

        nome_alessio = get_nome_alessio()
        nome_bruno = get_nome_bruno()

        self.play(FadeIn(alessio), Write(nome_alessio), FadeIn(bruno), Write(nome_bruno))

        cala_distanza = .7

        def get_distanza():
            return DoubleArrow(
                start=bruno.get_center() + 12 * LEFT + (pavimento - cala_distanza) * OUT,
                end=bruno.get_center() + (pavimento - cala_distanza) * OUT,
                color=GREEN,
                buff=0)

        distanza = get_distanza()

        def get_lunghezza_distanza():
            return Tex("600 m", color=GREEN).next_to(distanza, DOWN, buff=.5).rotate(phi, axis=RIGHT)

        lunghezza_distanza = get_lunghezza_distanza()
        self.play(Create(distanza), Write(lunghezza_distanza))
        self.cut_and_wait()

        self.play(Create(axes))
        self.cut_and_wait()

        alza_vettori = 0.2

        def get_vettore_pavimento():
            return Arrow(
                start=base.get_center(),
                end=base.get_center() + vel_alessio * vel_scale * LEFT,
                color=YELLOW,
                buff=0).rotate(phi, axis=RIGHT)

        def get_vettore_bruno():
            return Arrow(
                start=bruno.get_center(),
                end=bruno.get_center() + vel_bruno * vel_scale * LEFT,
                color=RED,
                buff=0).shift(alza_vettori * OUT).rotate(phi, axis=RIGHT)

        vettore_pavimento = get_vettore_pavimento()
        vettore_bruno = get_vettore_bruno()

        def get_vettore_bruno_2():
            return Arrow(
                start=vettore_bruno.get_end(),
                end=vettore_bruno.get_end() + vel_alessio * vel_scale * LEFT,
                color=YELLOW,
                buff=0).rotate(phi, axis=RIGHT)

        vettore_bruno_2 = get_vettore_bruno_2()

        def get_velocita_pavimento():
            return Tex("6 km/h", color=YELLOW).next_to(vettore_pavimento, UP, buff=1.1).rotate(phi, axis=RIGHT)

        def get_velocita_bruno():
            return Tex("4 km/h", color=RED).next_to(vettore_bruno, UP, buff=1.1).rotate(phi, axis=RIGHT)

        def get_velocita_bruno_2():
            return Tex("6 km/h", color=YELLOW).next_to(vettore_bruno_2, UP, buff=1.1).rotate(phi, axis=RIGHT)

        velocita_pavimento = get_velocita_pavimento()
        velocita_bruno = get_velocita_bruno()
        velocita_bruno_2 = get_velocita_bruno_2()

        self.play(Create(vettore_pavimento), Write(velocita_pavimento))
        self.cut_and_wait()

        self.play(Create(vettore_bruno), Write(velocita_bruno))
        self.cut_and_wait()

        self.play(Create(vettore_bruno_2), Write(velocita_bruno_2))
        self.cut_and_wait()

        timer = ValueTracker(0)

        def get_orologio():
            seconds = timer.get_value()
            minutes = seconds / 60
            seconds = seconds % 60
            return Tex("%d min, %d s" % (minutes, seconds)).shift(3 * OUT).rotate(phi, axis=RIGHT)

        orologio = get_orologio()
        self.play(Write(orologio))

        scala_percorsi = (pos_bruno[0] - pos_alessio[0]) / 600

        orologio.add_updater(
            lambda old: old.become(get_orologio())
        )
        base.add_updater(
            lambda old: old.become(
                Surface(
                    lambda u, v: np.array([u, v, pavimento]),
                    u_range=[-8 - vel_alessio / 3.6 * timer.get_value() * scala_percorsi,
                             8 - vel_alessio / 3.6 * timer.get_value() * scala_percorsi],
                    v_range=[-1, 1],
                    resolution=(16, 3)
                )
            )
        )
        vettore_pavimento.add_updater(
            lambda old: old.become(get_vettore_pavimento())
        )
        velocita_pavimento.add_updater(
            lambda old: old.become(get_velocita_pavimento())
        )
        bruno.add_updater(
            lambda old: old.move_to(
                pos_bruno + (vel_bruno + vel_alessio) / 3.6 * timer.get_value() * scala_percorsi * LEFT)
        )
        nome_bruno.add_updater(
            lambda old: old.become(get_nome_bruno())
        )
        vettore_bruno.add_updater(
            lambda old: old.become(get_vettore_bruno())
        )
        velocita_bruno.add_updater(
            lambda old: old.become(get_velocita_bruno())
        )
        vettore_bruno_2.add_updater(
            lambda old: old.become(get_vettore_bruno_2())
        )
        velocita_bruno_2.add_updater(
            lambda old: old.become(get_velocita_bruno_2())
        )
        distanza.add_updater(
            lambda old: old.become(get_distanza())
        )
        lunghezza_distanza.add_updater(
            lambda old: old.become(get_lunghezza_distanza())
        )

        self.play(timer.animate.set_value(216), run_time=5, rate_func=linear)

        orologio.clear_updaters()
        base.clear_updaters()
        vettore_pavimento.clear_updaters()
        velocita_pavimento.clear_updaters()
        bruno.clear_updaters()
        nome_bruno.clear_updaters()
        vettore_bruno.clear_updaters()
        velocita_bruno.clear_updaters()
        vettore_bruno_2.clear_updaters()
        velocita_bruno_2.clear_updaters()
        distanza.clear_updaters()
        lunghezza_distanza.clear_updaters()

        self.wait(30)
