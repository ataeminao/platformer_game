"""
levels/level_03.py - Introduce moving platforms and more challenging jumps.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_PLATFORM_MOVING

class Level03(BaseLevel):
    def __init__(self):
        super().__init__(3)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(400, 500, 180, 30, COLOR_PLATFORM))
        # Moving platform
        self.platforms.add(Platform(700, 400, 180, 30, COLOR_PLATFORM_MOVING, is_moving=True))
        self.platforms.add(Platform(1100, 300, 180, 30, COLOR_PLATFORM))

        self.collectibles.add(Collectible(780, 340, "gem"))
        self.collectibles.add(Collectible(1180, 240, "coin"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)