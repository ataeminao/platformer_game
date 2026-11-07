"""
levels/level_06.py - Introduce faster enemies and disappearing platforms.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.enemy import Enemy
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_PLATFORM_DISAPPEARING

class Level06(BaseLevel):
    def __init__(self):
        super().__init__(6)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(400, 500, 180, 30, COLOR_PLATFORM_DISAPPEARING, is_disappearing=True))
        self.platforms.add(Platform(700, 400, 180, 30, COLOR_PLATFORM_DISAPPEARING, is_disappearing=True))

        self.enemies.add(Enemy(500, 610, "patrol", 150))
        self.collectibles.add(Collectible(750, 340, "coin"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)