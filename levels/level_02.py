"""
levels/level_02.py - Introduce basic enemies and simple obstacles.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.enemy import Enemy
from entities.collectible import Collectible
from settings import COLOR_PLATFORM

class Level02(BaseLevel):
    def __init__(self):
        super().__init__(2)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(400, 500, 250, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(800, 400, 250, 30, COLOR_PLATFORM))

        self.enemies.add(Enemy(500, 610, "patrol", 100))
        self.enemies.add(Enemy(900, 360, "patrol", 120))

        self.collectibles.add(Collectible(520, 440, "coin"))
        self.collectibles.add(Collectible(920, 340, "gem"))
        self.collectibles.add(Collectible(1200, 600, "heart"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)