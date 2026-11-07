"""
levels/level_05.py - Introduce multiple enemy types and more complex platform arrangements.
"""

import pygame
from levels.base_level import BaseLevel, Platform
from entities.enemy import Enemy
from entities.collectible import Collectible
from settings import COLOR_PLATFORM

class Level05(BaseLevel):
    def __init__(self):
        super().__init__(5)
        self.setup_level()

    def setup_level(self):
        self.platforms.add(Platform(0, 650, 3000, 100, COLOR_PLATFORM))
        self.platforms.add(Platform(350, 520, 200, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(650, 400, 200, 30, COLOR_PLATFORM))
        self.platforms.add(Platform(950, 280, 200, 30, COLOR_PLATFORM))

        self.enemies.add(Enemy(400, 610, "patrol", 100))
        self.enemies.add(Enemy(700, 360, "chaser"))
        self.enemies.add(Enemy(1000, 200, "flyer"))

        self.collectibles.add(Collectible(720, 340, "gem"))
        self.collectibles.add(Collectible(1020, 220, "powerup"))

        self.exit_rect = pygame.Rect(2700, 550, 50, 100)