from manim import *


class Video(MovingCameraScene):

    def construct(self):
        shape = Line()
        # shape = Rectangle(fill_opacity=1, fill_color=WHITE)
        self.play(Burn(shape))
        self.wait()


class Burn(DrawBorderThenFill):

    def get_outline(self) -> Mobject:
        temp = self.mobject
        self.mobject = Rectangle(fill_opacity=1, fill_color=WHITE)
        outline = super().get_outline()
        self.mobject = temp
        return outline

    def interpolate_submobject(
        self,
        submobject: Mobject,
        starting_submobject: Mobject,
        outline,
        alpha: float,
    ) -> None:  # Fixme: not matching the parent class? What is outline doing here?
        print("\nBurn.interpolate_submobject: submobject = ", submobject,
              "; starting_submobject = ", starting_submobject,
              "; outline = ", outline,
              "; alpha = ", alpha)
        return super().interpolate_submobject(submobject, starting_submobject, outline, alpha)
