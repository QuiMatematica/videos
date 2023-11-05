from manim import *

DELAY = 1


class Scene(MovingCameraScene):

    def construct(self):
        scale_factor = .8

        x_min = -7
        x_max = 18 + x_min
        y_min = -4
        y_max = 10 + y_min

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 1],
                           y_range=[y_min, y_max, 1],
                           x_length=x_length,
                           y_length=y_length).add_coordinates().set_color(BLUE).set_z_index(-1)
        self.add(riferimento)
        self.cut_and_wait()

        parabola = riferimento.plot(lambda x: x ** 2 - 4*x + 3, color=YELLOW)
        self.play(Create(parabola))

        equazione_parabola = MathTex(r"y=x^2 - 4x + 3", color=YELLOW)\
            .add_background_rectangle().move_to(riferimento.coords_to_point(2, 5))
        self.play(Write(equazione_parabola))
        self.cut_and_wait()

        punto_p = Dot(riferimento.coords_to_point(2, -2), color=GREEN)
        self.play(Create(punto_p))

        coordinate_punto_p = MathTex(r"P(2, -2)", color=GREEN).add_background_rectangle().next_to(punto_p, RIGHT)
        self.play(Write(coordinate_punto_p))
        self.cut_and_wait()

        m_tracker1 = ValueTracker(0)

        def get_retta1():
            return riferimento.plot(lambda x: m_tracker1.get_value() * (x - 2) - 2, color=RED)

        retta1 = get_retta1()
        retta1.add_updater(
            lambda old: old.become(get_retta1())
        )

        m_tracker2 = ValueTracker(0)

        def get_retta2():
            return riferimento.plot(lambda x: m_tracker2.get_value() * (x - 2) - 2, color=RED)

        retta2 = get_retta2()
        self.play(Create(retta2), Create(retta1))

        retta2.add_updater(
            lambda old: old.become(get_retta2())
        )

        self.play(m_tracker1.animate.set_value(2), m_tracker2.animate.set_value(-2))
        retta1.clear_updaters()
        retta2.clear_updaters()
        self.play(Create(Dot(riferimento.coords_to_point(3, 0), color=RED)),
                  Create(Dot(riferimento.coords_to_point(1, 0), color=RED)))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
