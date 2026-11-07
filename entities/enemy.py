"""
entities/enemy.py - Multiple enemy types (Patrol, Chaser, Flyer, Stationary).
"""

import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, enemy_type: str = "patrol", patrol_distance: int = 150):
        super().__init__()
        self.enemy_type = enemy_type
        self.width = 40
        self.height = 40
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.start_x = x
        self.start_y = y
        self.patrol_distance = patrol_distance
        self.direction = 1
        self.speed = 2.0
        self.timer = 0.0
        self.health = 1

        self.render_graphics()

    def update(self, player_rect=None):
        self.timer += 0.05
        if self.enemy_type == "patrol":
            self.rect.x += int(self.speed * self.direction)
            if abs(self.rect.x - self.start_x) > self.patrol_distance:
                self.direction *= -1
        elif self.enemy_type == "chaser" and player_rect:
            dist = player_rect.centerx - self.rect.centerx
            if abs(dist) < 350:
                self.rect.x += 2 if dist > 0 else -2
        elif self.enemy_type == "flyer":
            self.rect.y = self.start_y + int(math.sin(self.timer * 3) * 50)
            self.rect.x += int(1.5 * self.direction)
            if abs(self.rect.x - self.start_x) > 200:
                self.direction *= -1

    def render_graphics(self):
        self.image.fill((0, 0, 0, 0))
        if self.enemy_type == "patrol":
            pygame.draw.rect(self.image, (220, 60, 60), (0, 10, self.width, self.height - 10), border_radius=8)
            pygame.draw.circle(self.image, (255, 255, 255), (12, 20), 4)
            pygame.draw.circle(self.image, (255, 255, 255), (28, 20), 4)
        elif self.enemy_type == "chaser":
            pygame.draw.rect(self.image, (200, 40, 180), (5, 5, self.width - 10, self.height - 5), border_radius=12)
            pygame.draw.circle(self.image, (255, 255, 0), (14, 18), 5)
            pygame.draw.circle(self.image, (255, 255, 0), (26, 18), 5)
        elif self.enemy_type == "flyer":
            pygame.draw.ellipse(self.image, (100, 220, 100), (0, 10, self.width, 24))
            pygame.draw.circle(self.image, (255, 255, 255), (20, 22), 6)
        elif self.enemy_type == "stationary":
            pygame.draw.polygon(self.image, (240, 140, 40), [(20, 0), (40, 40), (0, 40)])