"""
ui/victory_screen.py - Final victory screen displayed after completing all 10 levels.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE, COLOR_BUTTON, COLOR_BUTTON_HOVER

class VictoryScreen:
    def __init__(self):
        try:
            self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
            self.font = pygame.font.SysFont("Arial", 28, bold=True)
        except Exception:
            self.title_font = pygame.font.Font(None, 50)
            self.font = pygame.font.Font(None, 32)

        self.menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 500, 300, 50)

    def draw(self, surface: pygame.Surface, total_score: int):
        surface.fill((15, 35, 25))
        title = self.title_font.render("VICTORY! ALL LEVELS COMPLETED", True, (80, 240, 150))
        score_text = self.font.render(f"Final Score: {total_score}", True, COLOR_WHITE)

        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        surface.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(surface, COLOR_BUTTON_HOVER if self.menu_button.collidepoint(mouse_pos) else COLOR_BUTTON, self.menu_button, border_radius=8)
        t_surface = self.font.render("MAIN MENU", True, COLOR_WHITE)
        surface.blit(t_surface, (self.menu_button.centerx - t_surface.get_width() // 2, self.menu_button.centery - t_surface.get_height() // 2))

    def handle_event(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.menu_button.collidepoint(event.pos):
                return "menu"
        return None