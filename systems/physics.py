"""
systems/physics.py - Physics and movement calculation utilities.
"""

from settings import GRAVITY, TERMINAL_VELOCITY

def apply_gravity(velocity_y: float) -> float:
    new_vy = velocity_y + GRAVITY
    return min(new_vy, TERMINAL_VELOCITY)