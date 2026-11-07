"""
entities/collectible.py - Collectible items (coins, gems, health pickups, power-ups).
"""

import pygame
import math
from settings import COLOR_COIN, COLOR_GEM, COLOR_HEART, COLOR_POWERUP

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, item_type: str = "coin"):
        super().__init__()
        self.item_type = item_type
        self.width = 28
        self.height = 28
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.start_y = float(y)
        self.timer = x * 0.1  # Offset float animation

        self.render_graphics()

    def update(self):
        self.timer += 0.1
        # Floating hover effect
        self.rect.y = int(self.start_y + math.sin(self.timer) * 6)

    def render_graphics(self):
        self.image.fill((0, 0, 0, 0))
        center = (self.width // 2, self.height // 2)
        if self.item_type == "coin":
            pygame.draw.circle(self.image, COLOR_COIN, center, 12)
            pygame.draw.circle(self.image, (255, 240, 100), center, 8)
        elif self.item_type == "gem":
            pygame.draw.polygon(self.image, COLOR_GEM, [(14, 2), (26, 14), (14, 26), (2, 14)])
        elif self.item_type == "heart":
            pygame.draw.circle(self.image, COLOR_HEART, (9, 10), 8)
            pygame.draw.circle(self.image, COLOR_HEART, (19, 10), 8)
            pygame.draw.polygon(self.image, COLOR_HEART, [(2, 12), (26, 12), (14, 26)])
        elif self.item_type == "powerup":
            pygame.draw.rect(self.image, COLOR_POWERUP, (4, 4, 20, 20), border_radius=5)