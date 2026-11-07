"""
levels/level_07.py - Introduce moving hazards and challenging platform sequences.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_PLATFORM_MOVING, COLOR_SPIKE

class Level07(BaseLevel):
    def __init__(self):
        super().__init__(7)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(400, 480, 160, 30, COLOR_PLATFORM_MOVING, is_moving=True))
        self.platforms.add(Platform(800, 360, 160, 30, COLOR_PLATFORM_MOVING, is_moving=True))
        self.hazards.add(Platform(600, 620, 150, 30, COLOR_SPIKE))

        self.collectibles.add(Collectible(850, 300, "gem"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)