
"""
Calculate the degree change of a point's position in a circular path.

Author: Maksim Nudga
"""

from math import pi

CIRCLE = 360


def get_degree(radius: float, time: float, accel: float, start_sp: float):
    """
    Change in the pos of a point relative to the starting point.

    Args:
        radius (float): The radius of the circular path.
        time (float): The time elapsed.
        accel (float): The acceleration.
        start_sp (float): The initial speed.

    Returns:
        float: The degree change in position.
    """
    distance = start_sp * time + (accel * (time ** 2) / 2)
    circle = 2 * pi * radius
    return round(((distance % circle) / circle * CIRCLE), 3)
