from manim import Tex, DR, UL


class LaserTitle(Tex):

    def __init__(self, *tex_strings, **kwargs):
        super().__init__(*tex_strings, **kwargs)
        t = self.copy().set_opacity(.3).shift(.03 * DR).set_z_index(self.z_index - 1)
        self.add(t)
        t = self.copy().set_opacity(.3).shift(.03 * UL).set_z_index(self.z_index - 1)
        self.add(t)
