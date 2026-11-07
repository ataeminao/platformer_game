"""
levels/level_04.py - Introduce spikes, pits, and environmental hazards.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.collectible import Collectible
from settings import COLOR_PLATFORM, COLOR_SPIKE

class Level04(BaseLevel):
    def __init__(self):
        super().__init__(4)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 600, 100, COLOR_PLATFORM))
        # Pit gap 600 to 900
        self.platforms.add(Platform(900, 650, 2100, 100, COLOR_PLATFORM))
        
        # Spikes in pit / platforms
        self.hazards.add(Platform(700, 620, 100, 30, COLOR_SPIKE))
        self.platforms.add(Platform(450, 480, 200, 30, COLOR_PLATFORM))

        self.collectibles.add(Collectible(520, 420, "coin"))
        self.collectibles.add(Collectible(950, 600, "gem"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)