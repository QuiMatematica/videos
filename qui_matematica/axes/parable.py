import math

from manim import Axes


def parable_from_coefficients(axes: Axes, a_coefficient, b_coefficient=0, c_coefficient=0, **kwargs):
    x_min = axes.x_range[0]
    x_max = axes.x_range[1]
    y_min = axes.y_range[0]
    y_max = axes.y_range[1]
    x_min_parable = (-b_coefficient - math.sqrt(b_coefficient ** 2 - 4 * a_coefficient * (c_coefficient - y_max))) / \
                    (2 * a_coefficient)
    if x_min_parable < x_min:
        x_min_parable = x_min
    x_max_parable = (-b_coefficient + math.sqrt(b_coefficient ** 2 - 4 * a_coefficient * (c_coefficient - y_max))) / \
                    (2 * a_coefficient)
    if x_max_parable > x_max:
        x_max_parable = x_max

    return axes.plot(lambda x: a_coefficient * x ** 2 + b_coefficient * x + c_coefficient,
                     x_range=[x_min_parable, x_max_parable], **kwargs)
