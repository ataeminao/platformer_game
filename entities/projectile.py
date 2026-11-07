"""
entities/projectile.py - Projectile entities for enemies and boss.
"""

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, velocity_x: float, velocity_y: float):
        super().__init__()
        self.width = 16
        self.height = 16
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.render_graphics()

    def update(self):
        self.rect.x += int(self.velocity_x)
        self.rect.y += int(self.velocity_y)

    def render_graphics(self):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (255, 120, 40), (8, 8), 8)