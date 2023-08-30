from manim import *

LABEL_FONT_SIZE = 30
PERCENTAGE_FONT_SIZE = 30
RECTANGLE_WIDTH = 8
RECTANGLE_HEIGHT = .5
RECTANGLE_COLOR = BLUE


class Percentage(VGroup):

    def __init__(self, values, **kwargs):
        super(Percentage, self).__init__()
        # implementazione provvisoria con solo 2 valori
        self.values = values
        self.rectangle = Rectangle(width=RECTANGLE_WIDTH, height=RECTANGLE_HEIGHT, color=RECTANGLE_COLOR)
        self.add(self.rectangle)
        self.labels = []
        self.percentages = []
        for v in values:
            label = Tex(v[0], font_size=LABEL_FONT_SIZE).shift(.45 * DOWN)
            self.labels.append(label)
            self.add(label)

        label_0 = self.labels[0]
        label_0.shift((self.rectangle.width - label_0.width)/2 * LEFT)

        label_1 = self.labels[1]
        label_1.shift((self.rectangle.width - label_1.width)/2 * RIGHT)

    def show_side_percentages(self, scene: Scene, side, value, fill_color=RECTANGLE_COLOR, fill_opacity=.5):
        rect_0 = Rectangle(width=0, height=RECTANGLE_HEIGHT, color=RECTANGLE_COLOR,
                           fill_color=fill_color, fill_opacity=fill_opacity)
        rect_0.move_to(self.rectangle)
        rect_0.shift((self.rectangle.width - rect_0.width)/2 * side)
        val_0 = MathTex(r"0\%", font_size=PERCENTAGE_FONT_SIZE).move_to(rect_0)
        trk_0 = ValueTracker(0)

        scene.add(rect_0)
        scene.add(val_0)

        def update_rect_0(old_rect):
            new_width = trk_0.get_value() / 100 * RECTANGLE_WIDTH
            new_rect = Rectangle(width=new_width, height=RECTANGLE_HEIGHT, color=RECTANGLE_COLOR,
                           fill_color=fill_color, fill_opacity=fill_opacity)
            new_rect.move_to(self.rectangle).shift((self.rectangle.width - new_width) / 2 * side)
            old_rect.become(new_rect)

        def update_val_0(old_val):
            val = int(trk_0.get_value())
            new_val = MathTex(str(val) + r"\%", font_size=PERCENTAGE_FONT_SIZE).move_to(rect_0)
            old_val.become(new_val)

        rect_0.add_updater(lambda r: update_rect_0(r))
        val_0.add_updater(lambda v: update_val_0(v))

        scene.play(trk_0.animate.set_value(value))

        rect_0.clear_updaters()
        val_0.clear_updaters()

        self.add(rect_0, val_0)
        self.percentages.append(val_0)

    def show_percentages(self, scene: Scene):
        scene.play(Create(self.rectangle))
        scene.play(Write(self.labels[0]))
        self.show_side_percentages(scene, LEFT, self.values[0][1], fill_opacity=.5)
        scene.play(Write(self.labels[1]))
        self.show_side_percentages(scene, RIGHT, self.values[1][1], fill_opacity=.3)
