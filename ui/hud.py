"""
ui/hud.py - Top heads-up display rendering game stats.
"""

import pygame
from settings import COLOR_WHITE, COLOR_HUD_BG

class HUD:
    def __init__(self):
        try:
            self.font = pygame.font.SysFont("Arial", 22, bold=True)
        except Exception:
            self.font = pygame.font.Font(None, 24)

    def draw(self, surface: pygame.Surface, game_state):
        # HUD background banner
        hud_surface = pygame.Surface((1200, 50), pygame.SRCALPHA)
        hud_surface.fill(COLOR_HUD_BG)
        surface.blit(hud_surface, (0, 0))

        # Stats text
        score_text = self.font.render(f"SCORE: {game_state.score}", True, COLOR_WHITE)
        lives_text = self.font.render(f"LIVES: {game_state.lives}", True, COLOR_WHITE)
        health_text = self.font.render(f"HEALTH: {game_state.health}%", True, COLOR_WHITE)
        level_text = self.font.render(f"LEVEL: {game_state.current_level}/10", True, COLOR_WHITE)

        surface.blit(score_text, (20, 12))
        surface.blit(lives_text, (220, 12))
        surface.blit(health_text, (380, 12))
        surface.blit(level_text, (580, 12))

        # Health bar
        pygame.draw.rect(surface, (100, 100, 100), (480, 15, 80, 20), border_radius=4)
        health_width = int(80 * (game_state.health / 100.0))
        pygame.draw.rect(surface, (80, 220, 100), (480, 15, health_width, 20), border_radius=4)