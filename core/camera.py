"""
core/camera.py - Smooth 2D camera with target tracking and screen boundaries.
"""

import pygame

class Camera:
    def __init__(self, width: int, height: int):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.shake_timer = 0.0
        self.shake_intensity = 0.0

    def apply(self, entity: pygame.Rect) -> pygame.Rect:
        shake_x = 0
        shake_y = 0
        if self.shake_timer > 0:
            import random
            shake_x = random.randint(-int(self.shake_intensity), int(self.shake_intensity))
            shake_y = random.randint(-int(self.shake_intensity), int(self.shake_intensity))
        return entity.move(self.camera.topleft).move(shake_x, shake_y)

    def apply_point(self, pos: tuple) -> tuple:
        return (pos[0] + self.camera.x, pos[1] + self.camera.y)

    def update(self, target_rect: pygame.Rect, level_width: int, level_height: int):
        # Center camera on target
        x = -target_rect.centerx + int(1200 / 2)
        y = -target_rect.centery + int(750 / 2)

        # Limit camera to level bounds
        x = min(0, x)  # Stop at left edge
        x = max(-(level_width - 1200), x)  # Stop at right edge
        y = min(0, y)  # Stop at top edge
        y = max(-(level_height - 750), y)  # Stop at bottom edge

        self.camera = pygame.Rect(x, y, self.width, self.height)

        if self.shake_timer > 0:
            self.shake_timer -= 1/60.0

    def shake(self, intensity: float = 5.0, duration: float = 0.3):
        self.shake_intensity = intensity
        self.shake_timer = duration