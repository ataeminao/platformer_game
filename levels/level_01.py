"""
levels/level_01.py - Beginner tutorial level introducing movement, jumping, platforms, and collectibles.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_SPIKE

class Level01(BaseLevel):
    def __init__(self):
        super().__init__(1)
        self.setup_level()

    def setup_level(self):
        # Ground
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        # Introductory platforms
        self.platforms.add(Platform(400, 520, 200, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(700, 420, 200, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(1000, 320, 200, 30, COLOR_PLATFORM))
        
        # Collectibles
        self.collectibles.add(Collectible(480, 460, "coin"))
        self.collectibles.add(Collectible(780, 360, "coin"))
        self.collectibles.add(Collectible(1080, 260, "gem"))

        # Exit
        self.exit_rect = pygame.Rect(2700, 550, 50, 100)