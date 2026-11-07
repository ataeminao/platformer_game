"""
levels/base_level.py - Abstract base class for all levels.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, color, is_moving=False, is_disappearing=False):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.is_moving = is_moving
        self.is_disappearing = is_disappearing
        self.disappear_timer = 0.0
        self.is_active = True
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.start_x = x
        self.start_y = y
        self.move_timer = 0.0

    def update(self):
        if self.is_moving:
            self.move_timer += 0.05
            import math
            self.rect.x = self.start_x + int(math.sin(self.move_timer) * 100)
        if self.is_disappearing and self.disappear_timer > 0:
            self.disappear_timer -= 1/60.0
            if self.disappear_timer <= 0:
                self.is_active = False

    def trigger_disappear(self):
        if self.is_disappearing and self.disappear_timer == 0:
            self.disappear_timer = 1.0  # Disappears after 1 second


class BaseLevel:
    def __init__(self, level_num: int):
        self.level_num = level_num
        self.width = 3000
        self.height = 750
        
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.hazards = pygame.sprite.Group()
        
        self.player_spawn = (100, 500)
        self.exit_rect = pygame.Rect(2800, 500, 50, 100)
        self.boss = None

    def setup_level(self):
        pass

    def update(self, player_rect):
        self.platforms.update()
        self.enemies.update(player_rect)
        self.collectibles.update()
        self.projectiles.update()
        if self.boss:
            self.boss.update(player_rect, self.projectiles)