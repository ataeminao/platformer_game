"""
entities/boss.py - Level 10 boss enemy with multiple attack phases and patterns.
"""

import pygame
import math

class Boss(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 90
        self.height = 90
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.max_health = 100
        self.health = 100
        self.speed = 3.0
        self.direction = 1
        self.start_x = x
        self.timer = 0.0
        self.phase = 1
        self.attack_cooldown = 0.0

        self.render_graphics()

    def update(self, player_rect, projectiles_group):
        self.timer += 0.05
        self.attack_cooldown -= 1/60.0

        # Phase transition
        if self.health <= 50:
            self.phase = 2
            self.speed = 4.5

        # Movement pattern
        self.rect.x += int(self.speed * self.direction)
        if abs(self.rect.x - self.start_x) > 300:
            self.direction *= -1

        # Hover motion
        self.rect.y += int(math.sin(self.timer * 4) * 2)

        # Attacks
        if self.attack_cooldown <= 0:
            self.attack_cooldown = 2.0 if self.phase == 1 else 1.2
            from entities.projectile import Projectile
            # Spawn projectile towards player
            proj = Projectile(self.rect.centerx, self.rect.centery, -6 if self.rect.centerx > player_rect.centerx else 6, 0)
            projectiles_group.add(proj)

        self.render_graphics()

    def render_graphics(self):
        self.image.fill((0, 0, 0, 0))
        color = (180, 40, 220) if self.phase == 1 else (240, 40, 40)
        pygame.draw.rect(self.image, color, (0, 10, self.width, self.height - 10), border_radius=18)
        # Boss eye core
        pygame.draw.circle(self.image, (255, 255, 0), (self.width // 2, self.height // 2), 16)
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 2, self.height // 2), 6)