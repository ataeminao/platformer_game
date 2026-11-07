"""
levels/level_08.py - Combine previous mechanics with more difficult enemy encounters.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.enemy import Enemy
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_PLATFORM_MOVING

class Level08(BaseLevel):
    def __init__(self):
        super().__init__(8)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(400, 500, 200, 30, COLOR_PLATFORM_MOVING, is_moving=True))
        self.platforms.add(Platform(800, 380, 200, 30, COLOR_PLATFORM))

        self.enemies.add(Enemy(500, 610, "chaser"))
        self.enemies.add(Enemy(900, 320, "flyer"))

        self.collectibles.add(Collectible(850, 320, "gem"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)