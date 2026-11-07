"""
levels/level_10.py - Final challenging level with a boss encounter.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.boss import Boss
from entities.collectible import Collectible
from settings import COLOR_PLATFORM

class Level10(BaseLevel):
    def __init__(self):
        super().__init__(10)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(300, 480, 200, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(700, 380, 200, 30, COLOR_PLATFORM))

        # Boss instance
        self.boss = Boss(1500, 550)

        self.collectibles.add(Collectible(1500, 480, "gem"))

        self.exit_rect = pygame.Rect(2800, 550, 50, 100)