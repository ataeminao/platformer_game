"""
levels/level_09.py - Advanced platforming challenges and demanding obstacle combinations.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.enemy import Enemy
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_PLATFORM_DISAPPEARING, COLOR_SPIKE

class Level09(BaseLevel):
    def __init__(self):
        super().__init__(9)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 500, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(700, 550, 150, 30, COLOR_PLATFORM_DISAPPEARING, is_disappearing=True))
        self.platforms.add(Platform(1000, 420, 150, 30, COLOR_PLATFORM_DISAPPEARING, is_disappearing=True))
        self.hazards.add(Platform(600, 620, 350, 30, COLOR_SPIKE))

        self.enemies.add(Enemy(1050, 360, "chaser"))
        self.collectibles.add(Collectible(1050, 360, "powerup"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)